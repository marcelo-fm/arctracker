# Import system modules
import os 
import arcpy

# Set environment settings
arcpy.env.workspace = 'C:/arcgis/ArcTutor/BuildingaGeodatabase/Layers' 

# Loop through the workspace, find all the layer files (.lyr) and create a consolidated folder for each 
# layer file found using the same name as the original layer file.
for lyr in arcpy.ListFiles('*.lyr'):
    print('Consolidating {}'.format(lyr))
    arcpy.management.ConsolidateLayer(lyr, os.path.splitext(lyr)[0], 'PRESERVE', 'CONVERT_ARCSDE')