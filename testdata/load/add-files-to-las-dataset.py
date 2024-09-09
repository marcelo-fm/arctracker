'''*********************************************************************
Name: Modify Files in LAS Dataset& Calculate Stats for LASD
Description: Adds files & surface constraints to a LAS dataset, then
             calculates statistics and generates report.
*********************************************************************'''
# Import system modules
import arcpy

try:
    # Script variables
    arcpy.env.workspace = 'C:/data'
    lasd = 'sample.lasd'
    oldLas = ['2006', '2007/file2.las']
    newLas = ['2007_updates_1', '2007_updates_2']
    oldSurfaceConstraints = ['boundary.shp', 'streams.shp']
    newSurfaceConstraints = [['sample.gdb/boundary', '<None>',
                              'Soft_Clip']
                             ['sample.gdb/streams', 'Shape.Z',
                              'Hard_Line']]
    arcpy.management.RemoveFilesFromLasDataset(lasd, oldLas,
                                               oldSurfaceConstraints)
    arcpy.management.AddFilesToLasDataset(lasd, newLas, 'RECURSION',
                                          newSurfaceConstraints)
    arcpy.management.LasDatasetStatistics(lasd, "UPDATED_FILES",
                                          "lasd_stats.txt",
                                          "LAS_FILE", "DECIMAL_POINT",
                                          "SPACE", "LAS_summary.txt")
except arcpy.ExecuteError:
    print(arcpy.GetMessages())
except Exception as err:
    print(err.args[0])