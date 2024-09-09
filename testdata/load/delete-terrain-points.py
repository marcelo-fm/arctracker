'''**********************************************************************
Name: Delete Terrain Outliers
Description: Uses Locate Outliers to identify outlier points in 
             a terrain dataset, and eliminates the outliers from the 
             terrain with Delete Terrain Points.
**********************************************************************'''
# Import system modules
import arcpy

# Set Local Variables
arcpy.env.workspace = 'C:/data'
terrain = 'test.gdb/featuredataset/sample_terrain'
terrainPt = 'elevation_pts'  # name of terrain point data source
outliers = 'in_memory/outliers'

# Execute LocateOutliers
arcpy.ddd.LocateOutliers(terrain, outliers, 'APPLY_HARD_LIMIT', -10, 
                         350, 'APPLY_COMPARISON_FILTER', 1.2, 120, 
                         0.8, 8000)
# Execute Delete Terrain Points
arcpy.ddd.DeleteTerrainPoints(terrain, terrainPt, outliers)