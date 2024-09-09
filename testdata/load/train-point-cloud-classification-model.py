import arcpy

arcpy.env.workspace = "D:/Deep_Learning_Workspace"
arcpy.ddd.TrainPointCloudClassificationModel(
    "Powerline_Training.pctd", "D:/DL_Models", "Powerline", 
    attributes=['INTENSITY', 'RETURN_NUMBER', 'NUMBER_OF_RETURNS'],
    target_classes=[14, 15], background_class=1,
    class_descriptions=[[1, "Background"], [14, "Wire Conductor"], [15, "Transmission Tower"]],
    model_selection_criteria="F1_SCORE", max_epochs=10)