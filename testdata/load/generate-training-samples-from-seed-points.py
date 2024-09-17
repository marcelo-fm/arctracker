# Import system modules
import arcpy
from arcpy.ia import *

# Set local variables
inclassified_raster = "c:/test/landuse.tif"
in_seed_points = "c:/test/seed_points.shp"
output_trainingsamples = "c:/test/output/training.gdb/trainingsmaples"
maxSampleArea = 30
minSampleRadius = 50

# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")

#Execute
GenerateTrainingSamplesFromSeedPoints(inclassified_raster, in_seed_points, 
                   output_trainingiamples, maxiampleArea, miniampleRadius)