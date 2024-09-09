import arcpy
arcpy.env.workspace = 'C:/data'
arcpy.ddd.EvaluatePointCloudUsingTrainedModel(
        ['Transmission_Power_Lines.dlpk', 'Distribution_Power_Lines.dlpk'], 
        'Classified_Power_Lines.lasd', 'D:/Evaluate_PointCNN_Models', 
        'Power_Line_Results_', 'test_boundary.shp', [[18, 14], [20, 14]])