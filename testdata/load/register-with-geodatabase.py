# RegisterWithGeodatabase.py
# Description: Example showing use of RegisterWithGeodatabase tool with a file 
#              gdb view.

# Import system modules
import arcpy

# Create a view in the geodatabase
arcpy.management.CreateDatabaseView("C:\\testdata\\mytest.gdb",
                                    "trees",
                                    "select objectid, owner, parcel from inventory where type = trees")

# Set variables
inTable = r"C:\\testdata\\mytest.gdb\\trees"

# Process: Register With Geodatabase
arcpy.management.RegisterWithGeodatabase(inTable, "objectid")