'''****************************************************************************
Name: Near 3D Example
Description: This script demonstrates how to use
             the Near 3D tool to identify the nearest z-aware features
             that satisfy the results from a queried feature.
****************************************************************************'''
# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = 'C:/data'
# Set Local Variables
inFC = 'homes.shp'
nearFC = 'radiotowers.shp'
# See the 'Building an SQL expression' topic for more information
# Query the field 'MATERIAL' for the string 'Reinforced Concrete'
SQL_Expression = "'"'MATERIAL'"' = 'Reinforced Concrete'"
#Execute Make Feature Layer
arcpy.management.MakeFeatureLayer(nearFC, 'Near Layer', SQL_Expression)
result = arcpy.management.GetCount('Near Layer')
if int(result.getOutput(0)) == 0:
    arcpy.AddMessage('{0} has no features that satisfy the query: {1}'\
         .format(nearFC, SQL_Expression))
else:
    #Execute Near3D
    arcpy.ddd.Near3D(inFC, 'nearLayer', '', 'LOCATION', 'ANGLE')