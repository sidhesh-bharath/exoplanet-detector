import pandas as pd
from lightcurve_fetcher import fetch_lightcurve
from transitleastsquares import transitleastsquares

TIC_IDS = pd.read_csv("./src/targets.csv", header=None, dtype=str, skipinitialspace=True).iloc[0].tolist()

for id in TIC_IDS:
    time, flux, flux_err = fetch_lightcurve(id)

    model = transitleastsquares(time, flux, flux_err)
    results = model.power(period_min=1, period_max=15.0)

    if results["SDE"] > 9.0:
        print(f"Candidate planet for TIC {id} | Period: {results["period"]} days, SDE: {results["SDE"]}")
    else:
        print(f"No candidate planet for TIC {id}")