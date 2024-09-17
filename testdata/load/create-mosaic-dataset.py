#Create 3-Band FGDB Mosaic Dataset

import arcpy
arcpy.env.workspace = "C:/Workspace"

gdbname = "CreateMD.gdb"
mdname = "mosaicds"
prjfile = "C:/Workspace/World_Mercator.prj"
noband = "3"
pixtype = "8_BIT_UNSIGNED"
pdef = "NONE"
wavelength = ""

arcpy.CreateMosaicDataset_management(gdbname, mdname, prjfile, noband, 
                                     pixtype, pdef, wavelength)