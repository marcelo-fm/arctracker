import arcpy
arcpy.management.InterpolateFromPointCloud('c:/data/LASFolder',
                                           'c:/data/dsm.crf', '10',
                                           'IDW', 'GAUSS5x5', 'DTM')