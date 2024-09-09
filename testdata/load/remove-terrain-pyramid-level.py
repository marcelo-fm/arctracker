'''****************************************************************************
Name: RemoveTerrainPyramidLevel Example
Description: This script demonstrates how to add new 
             points to a terrain with the DeleteTerrainPoints tool, then use 
             the ChangeTerrainReferenceScale and RemoveTerrainPyramidLevel to
             to adjust the pyramids for reducing the amount of data stored for 
             providing an optimized display performance.
****************************************************************************'''
# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data"

# Set Local Variables
inTerrain = "sample.gdb/featuredataset/terrain"
targetPts = "mass_pts_embed"
AOI = "1379938.43267328 235633.08128634 1382756.00752135 237681.848838107"

# Execute DeleteTerrainPoints
arcpy.ddd.DeleteTerrainPoints(inTerrain, targetPts, AOI)
arcpy.AddMessage("Changing the terrain reference scale...")

# Execute ChangeTerrainReferenceScale
arcpy.ddd.ChangeTerrainReferenceScale(inTerrain, 500, 1000)

# Execute RemoveTerrainPyramidLevel
arcpy.ddd.RemoveTerrainPyramidLevel(inTerrain, 4)