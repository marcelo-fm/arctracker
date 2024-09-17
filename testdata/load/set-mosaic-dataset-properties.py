#Set mosaic dataset imagery properties group

import arcpy
arcpy.env.workspace = "C:/Workspace"

arcpy.SetMosaicDatasetProperties_management(
    "mdproperties.gdb/md", "525340", "3909809", "None;JPEG", "JPEG",
    "85", "0.5", "CUBIC", "CLIP", "FOOTPRINTS_MAY_CONTAIN_NODATA",
    "NOT_CLIP", "APPLY", "Base-Top Height;Top-Top Shadow Height",
    "Base-Top Height")