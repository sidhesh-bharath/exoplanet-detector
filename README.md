# Exoplanet Detector - AstroSpaceProgram

Using the TESS(Transisting Exoplanet Survey Satellite) telescope's data to find new exoplanets using the transit method.

Uses lightkurve to obtain satellite brightness data.
Uses local parquet files to prevent repeated download of satellite data.
Uses a TLS - Transit Least Squares model to find period of exoplanets with accuracy.