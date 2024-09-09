# Name: AnnotateSelectedFeatures.py
# Description: Annotate features based on a selection in a map 

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:\\data\\Northumberland.gdb"

# Execute Annotate Selected Features
p = arcpy.mp.ArcGISProject("C:\\data\\Northumberland.aprx")
for m in p.listMaps():
				arcpy.AnnotateSelectedFeatures_cartography(m, 'Wells', "WellsAnno 'Class 1'", 
                                               'GENERATE_UNPLACED')