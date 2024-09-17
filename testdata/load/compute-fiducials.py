import arcpy

in_mosaic_dataset = "c:\\test\\ortho.gdb\\ortho_md"
out_fiducial_table = "c:\\test\\ortho.gdb\\fiducial_table"
where_clause = ""
fiducial_template = "c:\\test\\fiducilatemplate.csv"
film_coordinate_system = "NO_CHANGE"


arcpy.ComputeFiducials_management(in_mosaic_dataset, out_fiducial_table,
where_clause,fiducial_template, film_coordinate_system)