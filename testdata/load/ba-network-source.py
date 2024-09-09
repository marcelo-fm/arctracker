import arcpy

# Access from a local network dataset
arcpy.env.baNetworkSource = "C:\\MyData\\CustomStreetsData.gdb\\streets\\streets_ND"

# Access from the current portal URL (Online)
arcpy.env.baNetworkSource = "https://www.arcgis.com"