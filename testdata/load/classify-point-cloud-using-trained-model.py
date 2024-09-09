import arcpy
arcpy.env.workspace = 'C:/data/'
arcpy.ddd.ClassifyPointCloudUsingTrainedModel('2018_survey.lasd', 'electrical_infrastructure_classification.emd', 
                                              [14, 15], 'EDIT_SELECTED', [0,1])