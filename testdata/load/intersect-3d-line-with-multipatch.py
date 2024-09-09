'''****************************************************************************
Name: Intersect3DLineWithMultiPatch Example
Description: This script demonstrates how to
             use the Intersect3DLine tool.
****************************************************************************'''
# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = 'C:/data'

# Set Local Variables
inLineFC = 'sample.gdb/lines_3d'
inMP = 'sample.gdb/test_MP'

# Ensure a unique name is produced for output files
outPoint = arcpy.CreateUniqueName('OutPt_3DIntersect', 'sample.gdb')
outLine = arcpy.CreateUniqueName('OutLine_3DIntersect', 'sample.gdb')

# Execute Intersect 3D Line with Multipatch
arcpy.Intersect3DLineWithMultiPatch_3d(inLineFC, inMP, 'IDS_ONLY',
                                       outPoint, outLine)