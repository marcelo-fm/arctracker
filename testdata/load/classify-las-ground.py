'''****************************************************************************
Name:        Classify Ground & Vegetation in Forest Environment
Description: Classify points representing vegetation with LAS class code values
             of 3, 4, and 5. The code is designed for use as a script tool.
****************************************************************************'''
# Import system modules
import arcpy

# Set Local Variables
inLas = arcpy.GetParameterAsText(0)
recursion = arcpy.GetParameterAsText(1)
lasd = arcpy.GetParameterAsText(2)

try:
    arcpy.CheckOutExtension('3D')
    # Execute CreateLasDataset
    arcpy.management.CreateLasDataset(inLas, lasd, folder_recursion=recursion)
    # Make an initial pass of ground classifier
    arcpy.ddd.ClassifyLasGround(lasd, method="Conservative")
    # Make a secondary pass to capture ridges
    arcpy.ddd.ClassifyLasGround(lasd, method="Aggressive", 
                                reuse_ground="REUSE_GROUND")
    # Classify vegetation
    arcpy.ddd.ClassifyLasByHeight(lasd, ground_source='GROUND', 
                                  height_classification=[[3, 5], 
                                                         [4, 17], 
                                                         [5, 120]], 
                                  noise='HIGH_NOISE', compute_stats="COMPUTE_STATS")
    arcpy.CheckInExtension('3D')

except arcpy.ExecuteError:
    print(arcpy.GetMessages())