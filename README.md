# Exoplanet Detector - AstroSpaceProgram 🪐🔭📐

An automated data pipeline and algorithmic search tool built in Python to discover exoplanet transit candidates using public telemetry from NASA's **TESS (Transiting Exoplanet Survey Satellite)** mission.

---

## Features
* **Data Fetching & Caching:** Pulls lightcurves via `lightkurve` and caches them locally as compressed `.parquet` files to avoid repetitive downloads.
* **Clean Data:** Cleans telemetry, strips out instrumental noise, drops missing values and masks bad quality flags.
* **Transit Least Squares (TLS) Model:** Uses TLS instead of standard BLS algorithms to model realistic planetary transits, accounting for stellar limb darkening to find shallow signals.
* **Automated SDE Filtering:** Automatically flags high confidence candidates exceeding a 9.0 Signal Detection Efficiency (SDE) thresholds.

---

## Project Architecture
```text
exoplanet-detector/
│
├── data/ # Downloaded Models
├── src/
│   ├── lightcurve_fetcher.py
│   └── transit_detector.py
├── requirements.txt
└── README.md

---