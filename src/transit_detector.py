from lightcurve_fetcher import fetch_lightcurve
from transitleastsquares import transitleastsquares

#TIC_IDS = ["25155310", "278564876", "150428135", "388857263", "413248763", "438128814", "256428741"]
TIC_IDS = ["25155310"]

for id in TIC_IDS:
    time, flux, flux_err = fetch_lightcurve(id)

    model = transitleastsquares(time, flux, flux_err)
    results = model.power(period_min=1, period_max=15.0)

    if results["SDE"] > 9.0:
        print(f"Candidate planet for TIC {id} | Period: {results["period"]} days, SDE: {results["SDE"]}")
    else:
        print(f"No candidate planet for TIC {id}")