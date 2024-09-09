import arcpy

# Input is a hosted table
input_table = "https://<machine_name>/server/rest/services/Hosted/<item_name>/FeatureServer/<table_number>"

# This tool works with locators on your portal
in_locator = "https://<machine_name>/server/rest/services/<locator_name>/GeocodeServer/<locator_name>"

# The easiest way to generate a field mapping is to run the tool in ArcGIS 
# Pro and right-click the green success ribbon and click "Copy Python command"
field_mapping =  "'Street or Intersection' address VISIBLE NONE;'City or Placename' <None> VISIBLE NONE;State <None> VISIBLE NONE;'ZIP Code' zip VISIBLE NONE"
output_name = "geocoding_output"

# Optional geocoding parameters. Only some are supported depending on the 
# in_locator that you use.
country = None
location_type = None
category = None

# The output is a hosted feature layer on your portal. To retrieve the
# output, go to your portal and look for a new item with the output_name that 
# you entered.
arcpy.geocoding.GeocodeLocationsFromTable(input_table, in_locator, 
                                          field_mapping, output_name, country, 
                                          location_type, category)