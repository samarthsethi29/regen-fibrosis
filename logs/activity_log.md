# Human Repair-Outcome Axis v2 — activity log

## 2026-10-31 — P0 setup started

- **Owner request:** clear the existing project directory, then complete plan steps 1 and 2.
- **Directory cleanup:** removed the previous project-folder contents only. The project path's Git metadata was not writable, so no changes were made outside this folder. The former files are not present in the current directory.
- **Plan source:** pasted “Human Repair-Outcome Axis — Work Plan v2”, dated Sep 27, 2026.
- **Plan snapshot:** `00_config/frozen_work_plan_v2.txt`; SHA-256: `0ab133f9b828207e50dbff1ab2b14f599bed170b39122c0d046a4a898e9480bd`.
- **Freeze timestamp:** `00_config/freeze_timestamp_utc.txt`.
- **Registry/config:** `00_config/dataset_registry.csv` and `00_config/config.yaml`; roster records 32 bulk datasets, 12 single-cell datasets, 2 spatial datasets, and 1 exploratory intervention entry. GSE113619 is marked locked.
- **Check performed:** roster counts match the plan's stated 32 bulk and 12 single-cell datasets. Registry lists its planned role and file type.
- **Accession validation:** the NCBI E-utilities batch query returned 1,744 records (the endpoint's result set is broader than the submitted GSE list and defaults to a 20-record page), so this does not establish that each listed accession resolves. Individual accession checks remain outstanding.
- **Release status:** a local timestamped snapshot and checksum exist. The plan calls for a GitHub tag or OSF release before downloads. This project folder has no writable Git metadata or configured remote, and no OSF destination is specified; therefore the required external release has not been made.
- **P0 gate:** not passed. Awaiting review/approval of the registry and an owner-selected release destination or approved local-freeze exception.
- **P1 downloads:** not started. No data have been downloaded into this reset project folder.

## 2026-11-01 — P0 registry validation and Git setup

- **Git root:** verified as `/Users/samarthsethi/projects/regen-fibrosis`; `origin` is the user's connected GitHub repository `https://github.com/samarthsethi29/regen-fibrosis.git`.
- **Data safety:** `.gitignore` excludes `01_raw/` and common large raw-data formats from Git.
- **Registry validation:** `scripts/validate_accessions.py` individually checked all 47 GEO/ArrayExpress accessions. All 47 resolved; results are in `00_config/accession_validation.tsv`.
- **Sealed test handling:** GSE113619 was checked using HTTP headers only. Its page, metadata, and data file contents were not requested or inspected.
- **Batch-query correction:** the initial NCBI batch query was not a per-accession check and is superseded by the individual validation above.
- **P0 release:** pending local commit/tag and owner approval to publish the tag.
- **P1:** not started; no data files downloaded in this project folder.

## 2026-11-01 — P1 GEO acquisition in progress

- **Plan release:** published tag `p0-plan-v2-20261101` to the connected GitHub origin. The tag points to the P0 plan snapshot, configuration, registry, individual accession checks and `.gitignore`; it does not contain raw data.
- **GEO source selection:** `scripts/p1_geo_download.py` writes `01_raw/download_manifest.csv` and `01_raw/geo_supplementary_index.csv`. Selected only raw archives/count tables and the required author metadata; excluded differential-result tables, normalized locked-test data and processed Seurat/h5ad objects where the plan specifies raw/per-sample inputs.
- **File listing:** the current raw selection is listed at about 11.18 GiB. This estimate excludes GSE312129: its only GEO archive is listed as 54 GiB, which exceeds the currently available disk space (about 41 GiB at the time checked) and conflicts with the plan's ~10 GiB single-cell estimate. It is marked pending; no data from it were downloaded.
- **Successful acquisitions recorded in manifest:** GSE209609 raw CEL tar, GSE50425 raw tar, GSE168760 raw tar, GSE124161 read-count table, GSE178411 count table, GSE162904 raw tar, GSE158766 raw tar and GSE218007 raw tar. Each is checksummed with MD5 and SHA-256 after completion. GSE209609 tar listing confirms CEL files; archive was not extracted.
- **Transfer behavior:** direct curl transfers failed or returned 403 for larger files. Resumable wget succeeded for several. Failed/partial files and retry status are recorded in the manifest; zero-byte files are not treated as acquired.
- **Locked cohort:** GSE113619 raw-count file is selected for checksum-only acquisition; no data contents have been read. Its transfer status remains whatever is recorded in the live manifest.
- **Still outstanding:** ArrayExpress raw files, plan reference resources (including STRING v12), and fallback resolution for GEO accessions without suitable supplementary raw/count files. No archive extraction, preprocessing, EDA, or modeling has been done.
- **P1 gate:** pending until all required core files are present and checksummed and owner reviews any exclusions/fallbacks.

## 2026-11-01 — P0 environment lock follow-up

- The local R installation is 4.5.1. Installed renv 1.3.1 in the project library and created `renv.lock` with the R and renv versions.
- Expanded `config.yaml` to record H1-H5, phase gates, thresholds, direction, locked-test handling and network constraints; added `contrast_definitions.csv` and `package_plan.csv`.
- **P0 limitation:** the renv lock currently pins only renv itself; exact versions of the analysis packages remain unresolved. P0 is therefore not fully compliant yet. P2 is held until package versions are pinned and the owner approves.
- The expanded setup revision is not yet committed/tagged; the original timestamped plan tag remains unchanged.
