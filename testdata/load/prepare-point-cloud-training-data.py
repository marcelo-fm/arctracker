import arcpy
arcpy.env.workspace = 'C:/data'
arcpy.ddd.PreparePointCloudTrainingData('training_source.lasd', '35 Meters', 'vegetation_training.pctd', 
                                        validation_point_cloud='validation_source.lasd', 
                                        class_codes_of_interest=[14, 15], block_point_limit=12000,
                                        reference_height='Ground_Elevation.tif', 
                                        excluded_class_codes=[2, 6, 8, 9, 20])