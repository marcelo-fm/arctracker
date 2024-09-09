'''****************************************************************************
Name: Update Terrain
Description: This script demonstrates how to update a terrain dataset
             with new elevation measurements obtained from Lidar by
             importing LAS files to multipoint features, then appending the
             new points to another multipoint feature that participates in a
             terrain. The terrain's pyramids are modified to optimize its
             draw speed.
****************************************************************************'''
# Import system modules
import arcpy

try:
    # Set environment settings
    arcpy.env.workspace = "C:/data"

    # Set Variables
    inTerrain = "sample.gdb/featuredataset/terrain"
    currentPts = "existing_points"
    lasFiles = ['las/NE_Philly.las',
                'las/NW_Philly.las']
    newPts = 'in_memory/update_pts'
    # Define spatial reference of LAS files using factory code
    # for NAD_1983_StatePlane_Pennsylvania_South
    lasSR = arcpy.SpatialReference(2272)

    arcpy.AddMessage("Converting LAS files to multipoint features...")
    arcpy.ddd.LASToMultipoint(lasFiles, newPts, 1.5, 2, 1,
                              'INTENSITY', lasSR)

    arcpy.AddMessage("Appending LAS points to {0}..."\
                     .format(currentPts))
    arcpy.ddd.AppendTerrainPoints(inTerrain, currentPts, newPts)

    arcpy.AddMessage("Changing terrain pyramid reference scales...")
    arcpy.ddd.ChangeTerrainReferenceScale(inTerrain, 1000, 500)
    arcpy.ddd.ChangeTerrainReferenceScale(inTerrain, 2500, 2000)

    arcpy.AddMessage("Adding terrain pyramid level...")
    arcpy.ddd.AddTerrainPyramidLevel(inTerrain, "", "4 4500")

    arcpy.AddMessage("Changing pyramid resolution bounds for breaklines...")
    arcpy.ddd.ChangeTerrainResolutionBounds(inTerrain, "breaklines", 5, 4)

    arcpy.AddMessage("Building terrain...")
    arcpy.ddd.BuildTerrain(inTerrain)

    arcpy.AddMessage("Completed updates.")

except arcpy.ExecuteError:
    print(arcpy.GetMessages())
except Exception as err:
    print(err)