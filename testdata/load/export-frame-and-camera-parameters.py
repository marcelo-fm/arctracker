#ExportFrameAndCameraParameters

import arcpy

arcpy.rm.ExportFrameAndCameraParameters("Image Collection", 	
	r"C:\Data\FrameandCameraTable.csv", "ESRI_FRAME_AND_CAMERA_TABLE")