# P0 gate — preregistration frozen; software lock incomplete

- **Frozen source plan:** `00_config/frozen_work_plan_v2.txt`
- **SHA-256:** `0ab133f9b828207e50dbff1ab2b14f599bed170b39122c0d046a4a898e9480bd`
- **Registry:** 32 bulk, 12 single-cell, 2 spatial, and 1 intervention entry; counts match the plan tables.
- **Accession validation:** 47 of 47 GEO/ArrayExpress accessions resolved in `accession_validation.tsv`.
- **Locked cohort:** GSE113619 was checked by HTTP headers only. No metadata or data contents were read.
- **Git freeze:** original commit `c942919` was published as `p0-plan-v2-20261101`. The expanded config and contrast table are being recorded as a follow-up setup revision.
- **R environment:** R 4.5.1. `renv.lock` pins renv 1.3.1; `package_plan.csv` lists all study packages, but their versions are not yet resolved/pinned.

The dataset registry and preregistered contrasts/thresholds are recorded. P0 remains **incomplete** until all analysis-package versions are pinned in renv. Do not begin P2 before that lock is completed and the owner approves the P0 gate. P1 acquisition is underway under the owner's direct request to complete steps 1 and 2.
