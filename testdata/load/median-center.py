# Measure geographic distribution characteristics of coffee house locations 
# weighted by the number of employees

# Import system modules
import arcpy
 
# Local variables...
workspace = "C:/data"
input_FC = "coffee_shops.shp"
CF_output = "coffee_CENTRALFEATURE.shp"
MEAN_output = "coffee_MEANCENTER.shp"
MED_output = "coffee_MEDIANCENTER.shp"
weight_field = "NUM_EMP"
 
try:
    # Set the workspace to avoid having to type out full path names
    arcpy.env.workspace = workspace

    # Process: Central Feature...
    arcpy.stats.CentralFeature(input_FC, CF_output, "Euclidean Distance", 
                               weight_field, "#", "#")
 
    # Process: Mean Center...
    arcpy.stats.MeanCenter(input_FC, MEAN_output, weight_field)

    # Process: Median Center...
    arcpy.stats.MedianCenter(input_FC, MED_output, weight_field)
 
except:
    # If an error occurred when running the tool, print out the error message.
    print(arcpy.GetMessages())