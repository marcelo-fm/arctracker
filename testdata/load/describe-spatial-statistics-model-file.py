# Print the properties of a spatial statistics model file
# Import modules
import arcpy

# Set the current workspace
arcpy.env.workspace = "C:/MyData"

# Run tool 
arcpy.stats.DescribeSSMFile("input_modelfile.ssm")

# Print geoprocessing messages
print(arcpy.GetMessages())