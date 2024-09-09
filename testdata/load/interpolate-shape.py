'''*********************************************************************
Name: InterpolateShape Example
Description: This script demonstrates how to use InterpolateShape
             on all 2D features in a target workspace.
*********************************************************************'''
# Import system modules
import arcpy

# Set local variables
inWorkspace = arcpy.GetParameterAsText(0)
surface = arcpy.GetParameterAsText(1)

try:
    # Set default workspace
    arcpy.env.workspace = inWorkspace
    # Create list of feature classes in target workspace
    fcList = arcpy.ListFeatureClasses()
    if fcList:
        for fc in fcList:
            desc = arcpy.Describe(fc)
            # Find 2D features
            if not desc.hasZ:
                # Set Local Variables
                outFC = "{0}_3D.shp".format(desc.basename)
                method = "BILINEAR"
                # Execute InterpolateShape
                arcpy.ddd.InterpolateShape(surface, fc, outFC, 
                                           10, 1, method, True)
            else:
                print("{0} is not a 2D feature.".format(fc))
    else:
        print("No feature classes were found in {0}.".format(env.workspace))
    
except arcpy.ExecuteError:
    print(arcpy.GetMessages())
    
except Exception as err:
    print(err)