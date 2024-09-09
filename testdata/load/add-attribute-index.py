# Name: AddAttIndex.py
# Description: Create an attribute Index for specified fields

# Import system modules
import arcpy

# Set a default workspace
arcpy.env.workspace = "c:/data"

# Create an attribute index for the few fields listed in command.
arcpy.management.AddIndex("counties.shp", ["NAME", "STATE_FIPS", "CNTY_FIPS"], 
                          "#", "NON_UNIQUE", "NON_ASCENDING")
arcpy.management.AddIndex("mexico.gdb/land/lakes", ["NAME", "geocompID"], 
                          "NGIndex", "NON_UNIQUE", "NON_ASCENDING")