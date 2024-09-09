import arcpy

arcpy.env.workspace = "D:/Deep_Learning_Workspace"
arcpy.ddd.TrainPointCloudObjectDetectionModel("Cars.pcotd", "D:/DL_Models", "Cars", 
    attributes=["INTENSITY", "RETURN_NUMBER", "NUMBER_OF_RETURNS", "RELATIVE_HEIGHT"],
    object_descriptions=[[31, "Cars"]], train_blocks="OBJECT_BLOCKS",
    model_selection_criteria="AVERAGE_PRECISION", max_epochs=10)