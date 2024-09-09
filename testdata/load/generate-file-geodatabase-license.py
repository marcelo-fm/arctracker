# Name: GenerateFgdbLicense.py
# Description: Use the GenerateFgdbLicense tool to generate a license file (*.sdlic) for a protected file geodatabase.

# import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data"

# Set local variables
input_licdef = "london.licdef"
export = "DENY_EXPORT"
exp_date = "2013-09-26 18:35:54"
output_sdlic = "london.sdlic"

# Process: generate the license file
arcpy.management.GenerateFgdbLicense(input_licdef, output_sdlic, export, exp_date)