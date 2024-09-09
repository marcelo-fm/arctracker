# Description: 
# Reverse Geocode customer point locations using the ArcGIS World Geocoding Service.

# Import system modules
import arcpy

# Set workspace
arcpy.env.workspace = "c:/data/Atlanta.gdb"

# Set local variables
input_features = "MyCustomers"
locator = "https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/ArcGIS World Geocoding Service"
reverse_output = "MyCustomers_Reverse_Streets"
addr_type = "ADDRESS"
feature_type = "STREET_INTERSECTION;STREET_ADDRESS"
location_type = "ROUTING_LOCATION"

# Run ReverseGeocode
arcpy.geocoding.ReverseGeocode(input_features, locator, reverse_output, 
                               addr_type, None, feature_type, location_type)