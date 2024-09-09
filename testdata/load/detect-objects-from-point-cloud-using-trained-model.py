import arcpy
arcpy.env.workspace = 'C:/data/detect_cars'
arcpy.ddd.DetectObjectsFromPointCloudUsingTrainedModel('2018_survey.lasd', 'cars.emd',
                                                       [(1, 0.7, 0.4)], 'Cars_in_Point_Cloud.shp',
                                                       10, 'study_area_boundary.shp',
                                                       'dem.tif', [2, 6, 7, 18])