# Description: 
#   Goes through the table generated by the Check Geometry tool and does 
#   the following
#   1) backs-up all features which will be 'fixed' to a "_bad_geom" feature class
#   2) runs repairGeometry on all feature classes listed in the table 

import arcpy
import os
 
# Table that was produced by Check Geometry tool
table = r"c:\temp\data.gdb\cg_sample1"
 
# Create local variables
fcs = []
 
# Loop through the table and get the list of fcs
for row in arcpy.da.SearchCursor(table, ("CLASS")):
    # Get the class (feature class) from the cursor
    if not row[0] in fcs:
        fcs.append(row[0])
 
# Now loop through the fcs list, backup the bad geometries into fc + "_bad_geom"
# then repair the fc
print("> Processing {0} feature classes".format(len(fcs)))
for fc in fcs:
    print("Processing " + fc)
    lyr = 'temporary_layer'
    if arcpy.Exists(lyr):
        arcpy.Delete_management(lyr)
    
    tv = "cg_table_view"
    if arcpy.Exists(tv):
        arcpy.Delete_management(tv)

    arcpy.MakeTableView_management(table, tv, ("\"CLASS\" = '%s'" % fc))
    arcpy.MakeFeatureLayer_management(fc, lyr)
    arcpy.AddJoin_management(lyr, arcpy.Describe(lyr).OIDFieldName, tv, "FEATURE_ID")
    arcpy.CopyFeatures_management(lyr, fc + "_bad_geom")
    arcpy.RemoveJoin_management(lyr, os.path.basename(table))
    arcpy.RepairGeometry_management(lyr)