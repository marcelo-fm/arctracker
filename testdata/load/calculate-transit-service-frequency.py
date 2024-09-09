import datetime

arcpy.transit.CalculateTransitServiceFrequency(
    r"C:\Data\TransitData.gdb\Transit",
    "AREAS",
    r"C:\Data\Output.gdb\TransitSystemCoverage",
    [[True, datetime.datetime(2021, 6, 30, 7, 0, 0), 120, "ARRIVALS", "June30AM"]],
    "",
    None,
    "https://www.arcgis.com/",
    "Walking Time",
    10,
    "MINUTES",
    "100 Meters"
)