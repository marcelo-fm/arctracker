# Name: SpatialJoin_Example2.py
# Description: Join attributes of cities to states based on spatial relationships.

# Import system modules
import arcpy
import os

# Set local variables
workspace = r"C:\gpqa\mytools\spatialjoin\usa.gdb"
outWorkspace = r"C:\gpqa\mytools\spatialjoin\output.gdb"
 
# Want to join USA cities to states and calculate the mean city population
# for each state
targetFeatures = os.path.join(workspace, "states")
joinFeatures = os.path.join(workspace, "cities")
 
# Output will be the target features, states, with a mean city population field (mcp)
outfc = os.path.join(outWorkspace, "states_mcp2")
 
# Create a new fieldmappings and add the two input feature classes.
fieldmappings = arcpy.FieldMappings()
fieldmappings.addTable(targetFeatures)
fieldmappings.addTable(joinFeatures)
 
# First get the POP1990 fieldmap. POP1990 is a field in the cities feature class.
# The output will have the states with the attributes of the cities. Setting the
# field's merge rule to mean will aggregate the values for all of the cities for
# each state into an average value. The field is also renamed to be more appropriate
# for the output.
pop1990FieldIndex = fieldmappings.findFieldMapIndex("POP1990")
fieldmap = fieldmappings.getFieldMap(pop1990FieldIndex)
 
# Get the output field's properties as a field object
field = fieldmap.outputField
 
# Rename the field and pass the updated field object back into the field map
field.name = "mean_city_pop"
field.aliasName = "mean_city_pop"
fieldmap.outputField = field
 
# Set the merge rule to mean and then replace the old fieldmap in the mappings object
# with the updated one
fieldmap.mergeRule = "mean"
fieldmappings.replaceFieldMap(pop1990FieldIndex, fieldmap)
 
# Delete fields that are no longer applicable, such as city CITY_NAME and CITY_FIPS
# as only the first value will be used by default
x = fieldmappings.findFieldMapIndex("CITY_NAME")
fieldmappings.removeFieldMap(x)
y = fieldmappings.findFieldMapIndex("CITY_FIPS")
fieldmappings.removeFieldMap(y)
 
#Run the Spatial Join tool, using the defaults for the join operation and join type
arcpy.analysis.SpatialJoin(targetFeatures, joinFeatures, outfc, "#", "#", fieldmappings)