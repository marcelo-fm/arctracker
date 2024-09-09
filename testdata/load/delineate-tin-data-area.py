'''****************************************************************************
Name: Define Data Boundary of LAS File
Description: This script demonstrates how to delineate data boundaries of 
             LAS files with irregularly clustered points. It is intended for 
             use as a script tool with one input LAS file.
****************************************************************************'''
# Import system modules
import arcpy

# Set local variables
inLas = arcpy.GetParameterAsText(0)  # input LAS file
ptSpacing = arcpy.GetParameterAsText(1)  # LAS point spacing
classCode = arcpy.GetParameterAsText(2)  # List of integers
returnValue = arcpy.GetParameterAsText(3)  # List of strings
outTin = arcpy.GetParameterAsText(4)  # TIN created to delineate data area
outBoundary = arcpy.GetParameterAsText(5)  # Polygon boundary file

try:
    # Execute LASToMultipoint
    lasMP = arcpy.CreateUniqueName('lasMultipoint', 'in_memory')
    arcpy.ddd.LASToMultipoint(inLas, LasMP, ptSpacing, class_code, 
                             "ANY_RETURNS", "", sr, inFormat, zfactor)
    # Execute CreateTin
    arcpy.ddd.CreateTin(outTin, sr, "{0} Shape.Z masspoints"\
                       .format(lasMP), "Delaunay")
    # Execute CopyTin
    arcpy.ddd.CopyTin(outTin, "{0}_copy".format(outTin))
    # Execute DelineateTinDataArea
    maxEdge = ptSpacing * 4
    arcpy.ddd.DelineateTinDataArea(outTin, maxEdge, "PERIMETER_ONLY")
    # Execute TinDomain
    arcpy.ddd.TinDomain(outTin, outBoundary, "POLYGON")
        
except arcpy.ExecuteError:
    print(arcpy.GetMessages())
except Exception as err:
    print(err)