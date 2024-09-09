import arcpy

# Input is a local table
input_table = r"C:\data\customers.csv"

# This tool works with locators on a portal
in_locator = "https://<machine_name>/server/rest/services/<service_name>/GeocodeServer/<service_name>"

# The best way to generate a field mapping is to run the tool in ArcGIS 
# Pro, right-click the green success ribbon, and click "Copy Python command"

field_mapping = "'Address or Place' Address VISIBLE NONE;Address2 <None> VISIBLE NONE;Address3 <None> VISIBLE NONE;Neighborhood <None> VISIBLE NONE;
City <None> VISIBLE NONE;County <None> VISIBLE NONE;State <None> VISIBLE NONE;ZIP ZIP VISIBLE NONE;ZIP4 <None> VISIBLE NONE;Country <None> VISIBLE NONE"
output_type = "FEATURE_CLASS"

# Output folder for the output CSV, Excel, or GDB table. If you select 
# FEATURE_CLASS output_type, a new GDB will be created in the 
# output_folder with the geocoding results
output_folder = r"C:\data\outputs"
output_name = "Geocoding_output"

# Optional geocoding parameters. Only some are supported depending on the 
# in_locator that you use.
country = None
location_type = "ROUTING_LOCATION"
category = "'Street Address'"

arcpy.geocoding.GeocodeFile(input_table, in_locator, field_mapping, output_type, 
                            output_folder, output_name, country, location_type, 
                            category)