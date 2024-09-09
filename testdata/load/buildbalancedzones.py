# Aggregate states into zones that have a target population of approximately
# 250,000 people.  Make the zones of equal area and compact. 
 
import arcpy

# Set the current workspace (to avoid having to specify the full path to
# the feature classes each time)

arcpy.env.workspace = r"c:\data\project_data.gdb"

arcpy.stats.BuildBalancedZones("states", "out_zones", "ATTRIBUTE_TARGET", 
     None, "POPULATION 250000 1", None, "TRIMMED_DELAUNAY_TRIANGULATION", 
     None, "EQUAL_AREA;COMPACTNESS", None, None, None, '', 100, 50, 0.1)