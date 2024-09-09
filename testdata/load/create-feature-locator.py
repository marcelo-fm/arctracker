# Description: Create a feature locator using data from a hosted feature service in ArcGIS Online.

# Import system modules
import arcpy

# Sign in to Portal
arcpy.SignInToPortal("https://www.arcgis.com", "<username>", "<password>")

# Set local variables
in_features = "https://services.arcgis.com/<layer_id>/arcgis/rest/services/<service_name>/FeatureServer/<layer_number>"
search_field = "*Name NAME VISIBLE NONE"
output_locator = r"C:\output\locators\service_locator"
locator_fields = "Rank <None> VISIBLE NONE;'Min X' <None> VISIBLE NONE;'Max X' <None> VISIBLE NONE;'Min Y' <None> VISIBLE NONE;'Max Y' <None> VISIBLE NONE"

arcpy.geocoding.CreateFeatureLocator(in_features, search_field, output_locator, 
                                     locator_fields)