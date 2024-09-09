'''**********************************************************************
Name: LAS Point Statistics As Raster
Description: Identifies the most frequently occurring return value for
             each pulse in a given set of LAS files.
             Designed for use as a script tool.
**********************************************************************'''
# Import system modules
import arcpy

# Set Local Variables
lasD = arcpy.GetParameterAsText(0)
inLas = arcpy.GetParameterAsText(1) #input las files
sr = arcpy.GetParameter(2) #spatial reference of las dataset
statsRaster = arcpy.GetParameterAsText(3)

# Execute CreateLasDataset
arcpy.management.CreateLasDataset(inLas, lasD, 'RECURSION', '', sr)
# Execute LasPointStatsAsRaster
arcpy.management.LasPointStatsAsRaster(lasD, statsRaster,
                                       "PREDOMINANT_RETURNS_PER_PULSE",
                                       "CELLSIZE", 15)