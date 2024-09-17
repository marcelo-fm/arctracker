import arcpy

in_mosaic_dataset = "c:\\Test\\ortho.gdb\\orthoMD"
whereClause = ""
fiducialTable = "c:\\test\\fidducial.csv"
film_coordsys = "X_DOWN_Y_RIGHT"
update_footprints = "UPDATE"

arcpy.UpdateInteriorOrientation_management(in_mosaic_dataset, whereClause,
fiducialTable, film_coordsys, update_footprints)