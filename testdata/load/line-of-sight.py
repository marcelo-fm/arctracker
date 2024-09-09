'''*********************************************************************
Name: Sight Line Visibility of Parade Path
Description: This script demonstrates how to create a sight line feature class
             from a pair of observer and target points.
*********************************************************************'''
# Import system modules
import arcpy

# Set Local Variables:
arcpy.env.workspace = 'C:/data'

# Setting up input and output variables:
obs = "observer_pts.shp"
tar = "parade_path.shp"
sightlines = "output_sightlines.shp"
height = "<None>"
join_field = "#"
sampling = 0.5
direction = "OUTPUT_THE_DIRECTION"
surface = 'elevation.tif'
bldgs = 'buildings.shp'

arcpy.ddd.ConstructSightLines(obs, tar, sightlines, height, height,
                              join_field, sampling, direction)
arcpy.ddd.LineOfSight(surface, sightlines, "Parade_LOS.shp",
                      "Obstructions.shp", in_features=bldgs)