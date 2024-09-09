import arcpy

# Set local variables
table = r"C:\Data\MyDatabase.gdb\DistributionCenters"

# Sign in to Portal
#arcpy.SignInToPortal("https://www.arcgis.com.", "MyUsername", "MyPassword")

locator = "https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/ArcGIS World Geocoding Service"

field_map = "'Single Line Input' SingleLine VISIBLE NONE;Country Country VISIBLE NONE"

geocode_result = r"C:\Data\MyDatabase.gdb\DistributionCenters_Geocoded"

arcpy.geocoding.GeocodeAddresses(table, locator, field_map, geocode_result)