import arcpy
arcpy.env.workspace = 'C:/Data'
arcpy.management.ValidateSceneLayerPackage(None, 'validate_report.json',
                                           'C:/cloud_connections/AWS.acs/mySceneLayer.i3srest')