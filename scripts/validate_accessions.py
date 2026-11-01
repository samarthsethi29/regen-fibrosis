#!/usr/bin/env python3
"""Validate registered GEO and ArrayExpress accessions without inspecting data files."""
import csv, json, subprocess, time
from pathlib import Path
from urllib.parse import urlencode

root = Path(__file__).resolve().parents[1]
rows = list(csv.DictReader((root / "00_config/dataset_registry.csv").open()))
ids = sorted({r["accession"] for r in rows})
results = []
for accession in ids:
    if accession.startswith("GSE"):
        url = "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?" + urlencode({"acc": accession, "targ": "self", "form": "text", "view": "brief"})
        if accession == "GSE113619":
            # Respect the sealed-test rule: probe headers only; do not fetch its metadata or contents.
            probe = subprocess.run(["curl", "-L", "--head", "--silent", "--show-error", "--max-time", "45", "-o", "/dev/null", "-w", "%{http_code}", url], capture_output=True, text=True)
            found = probe.returncode == 0 and probe.stdout.strip().endswith("200")
        else:
            probe = subprocess.run(["curl", "-L", "--silent", "--show-error", "--max-time", "45", url], capture_output=True, text=True)
            body = probe.stdout
            found = probe.returncode == 0 and f"!Series_geo_accession = {accession}" in body
        source = "NCBI GEO"
    elif accession.startswith("E-MTAB-"):
        url = f"https://www.ebi.ac.uk/biostudies/api/v1/studies/{accession}"
        probe = subprocess.run(["curl", "-L", "--silent", "--show-error", "--max-time", "45", url], capture_output=True, text=True)
        try:
            body_json = json.loads(probe.stdout)
            found = probe.returncode == 0 and body_json.get("accno") == accession
        except Exception:
            found = False
        source = "EMBL-EBI BioStudies"
    else:
        continue
    results.append({"accession": accession, "source": source, "resolved": found, "url": url})
    print(f"{accession}\t{'resolved' if found else 'NOT RESOLVED'}")
    time.sleep(0.35)
out = root / "00_config/accession_validation.tsv"
with out.open("w") as f:
    f.write("accession\tsource\tresolved\turl\n")
    for r in results:
        f.write(f"{r['accession']}\t{r['source']}\t{str(r['resolved']).lower()}\t{r['url']}\n")
print(f"Checked {len(results)} accessions; {sum(r['resolved'] for r in results)} resolved; wrote {out}")
