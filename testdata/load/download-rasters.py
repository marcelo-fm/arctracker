##Download Rasters from image services URL
##Maintain the original sensor data folder structure

import arcpy
arcpy.env.workspace = r"\\myworkstation\Workspace\downloadras"
    
arcpy.DownloadRasters_management(
     "http://serv1/arcgis/services/Ext/MD_LS_pan/ImageServer?",
     "downloadFolder", "AcquisitionDate = date '1999-08-18 00:00:00'",
     "", "", "", "", "", "MAINTAIN_FOLDER")