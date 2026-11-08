import pandas as pd

def fetch_lightcurve(id):
    try:
        df = pd.read_parquet(f"data/TIC_{id}_cleaned.parquet")
        time, flux, flux_err = df['time'].values, df['flux'].values, df['flux_err'].values

        print("Lightcurve already downloaded locally.")

        return time, flux, flux_err

    except FileNotFoundError:
        print("Local parquet file not found, reverting to lightkurve.")

        import lightkurve as lk

        search_result = lk.search_lightcurve(f"TIC {id}", mission="TESS", author="SPOC")

        print(f"{len(search_result)} results found. Beginning download...")

        try:
            light_curve = search_result[0].download()
            light_curve = light_curve[light_curve.quality == 0]
        except IndexError:
            print("No lightcurves found.")
            exit()

        clean_light_curve = light_curve.remove_nans().flatten(window_length=401).remove_outliers(sigma=5)

        time, flux, flux_err = clean_light_curve.time.value, clean_light_curve.flux.value, clean_light_curve.flux_err.value    

        df = pd.DataFrame({
            "time": time,
            "flux": flux,
            "flux_err": flux_err
        })

        df.to_parquet(f"data/TIC_{id}_cleaned.parquet")
        print(f"Saved TIC {id} to local parquet file.")

        return time, flux, flux_err

if __name__ == "__main__":
    id = input("Enter TIC ID: ")

    fetch_lightcurve(id)