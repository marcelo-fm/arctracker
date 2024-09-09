import arcpy
arcpy.conversion.ConvertLas('2014_survey.zlas', '2014_unclassified_collection', 
                            '1.4', 7, 'NO_COMPRESSION',
                            ['REMOVE_VLR', 'REMOVE_EXTRA_BYTES', 'REARRANGE_POINTS'], 
                            '2014_unclassified_collection/2014_Survey_Collection.lasd')