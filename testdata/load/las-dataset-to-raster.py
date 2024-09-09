'''*********************************************************************
Name: Export Elevation Raster from Ground LAS Measurements
Description: This script demonstrates how to export
             ground measurements from LAS files to a raster using a
             LAS dataset. This sample is designed to be used as a script
             tool.
*********************************************************************'''
# Import system modules
import arcpy

try:
    # Set Local Variables
    inLas = arcpy.GetParameterAsText(0)
    recursion = arcpy.GetParameterAsText(1)
    surfCons = arcpy.GetParameterAsText(2)
    classCode = arcpy.GetParameterAsText(3)
    returnValue = arcpy.GetParameterAsText(4)
    spatialRef = arcpy.GetParameterAsText(5)
    lasD = arcpy.GetParameterAsText(6)
    outRaster = arcpy.GetParameterAsText(7)
    cellSize = arcpy.GetParameter(8)
    zFactor = arcpy.GetParameter(9)

    # Execute CreateLasDataset
    arcpy.management.CreateLasDataset(inLas, lasD, recursion, surfCons, sr)
    # Execute MakeLasDatasetLayer
    lasLyr = arcpy.CreateUniqueName('Baltimore')
    arcpy.management.MakeLasDatasetLayer(lasD, lasLyr, classCode, returnValue)
    # Execute LasDatasetToRaster
    arcpy.conversion.LasDatasetToRaster(lasLyr, outRaster, 'ELEVATION',
                              'TRIANGULATION LINEAR WINDOW_SIZE 10', 'FLOAT',
                              'CELLSIZE', cellSize, zFactor)
    print(arcpy.GetMessages())

except arcpy.ExecuteError:
    print(arcpy.GetMessages())

except Exception as err:
    print(err.args[0])

finally:
    arcpy.management.Delete(lasLyr)