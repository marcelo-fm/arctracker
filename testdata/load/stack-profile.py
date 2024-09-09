'''**********************************************************************
Name: Save Profiles to Graph Files
Description: Creates profile graphs of multipatch and surface features,
             which are then saved as graph files.
**********************************************************************'''
# Import system modules
import arcpy

# Set Local Variables
profileLine = arcpy.GetParameterAsText(0)
profileTargets = arcpy.GetParameterAsText(1) # input las files
profileTable = arcpy.CreateUniqueName('profile_table', 'in_memory')
graphName = "Sample Graph"
outGraph = arcpy.GetParameterAsText(2) # output graph file

# Execute StackProfile
arcpy.ddd.StackProfile(profileLine, profileTargets, profileTable, graphName)

# Execute SaveGraph
arcpy.management.SaveGraph(graphName, outGraph)