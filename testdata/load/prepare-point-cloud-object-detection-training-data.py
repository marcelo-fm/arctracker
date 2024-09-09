import arcpy
arpy.env.workspace = r"C:\GIS_Data"
arcpy.ddd.PreparePointCloudObjectDetectionTrainingData("Training.lasd", r"Objects.fgdb\Training_FCs",
                                                       r"Objects.fgdb\Validation_FCs", "12 Meters",
                                                       "Training_Cars.pcotd", training_code_field="Car_Type",
                                                       validation_code_field="Car_Type", reference_surface="DEM.tif",
                                                       excluded_classes=[2, 7, 18])