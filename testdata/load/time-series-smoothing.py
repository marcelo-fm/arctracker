import arcpy
arcpy.env.workspace = "C:/Analysis/data.gdb"

# Smooth temperature data using adaptive method by ID Field and revise input 
arcpy.stats.TimeSeriesSmoothing("temperature_CA", "START_DATE", "VALUE", 
            "ID_FIELD", "ADAPTIVE", None, "APPEND_TO_INPUT", None, "FIPS", 
            "NOT_APPLY_SHORTER_WINDOW", "NO_POPUP")