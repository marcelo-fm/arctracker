'''****************************************************************************
Name: SurfaceAspect Example
Description: This script demonstrates how to use the
             SurfaceAspect and SurfaceSlope tools to generate a polygon
             that contains the intersection of both
****************************************************************************'''

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data"

# List all TINs in workspace
listTINs = arcpy.ListDatasets("","TIN")

# Determine whether the list contains any TINs
if len(listTINs) > 0:
    for dataset in listTINs:
        print(dataset)
        # Set Local Variables
        aspect = arcpy.CreateUniqueName("Aspect.shp")
        slope = arcpy.CreateUniqueName("Slope.shp")
        outFC = dataset + "_Aspect_Slope.shp"
        #Execute SurfaceAspect
        arcpy.ddd.SurfaceAspect(dataset, aspect)
        #Execute SurfaceSlope
        arcpy.ddd.SurfaceSlope(dataset, slope)
        #Execute SurfaceSlope
        print("Starting Intersect")
        arcpy.analysis.Intersect(aspect + " #;" + slope + " #", outFC, "ALL")
        print("Completed intersect for " + dataset)
else:
    print("There are no TINs in the " + env.workspace + " directory.")