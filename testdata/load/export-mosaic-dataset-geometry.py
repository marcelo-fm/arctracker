#Export Mosaic Dataset Geometry


import arcpy

arcpy.env.workspace = "c:/workspace"

#Export footprint from a single record in a mosaic dataset
mdname = "exportmd_footprints.gdb/md"
out_FC = "C:/workspace/LANDSAT_footprints"
where_clause = "OBJECTID = 1"
geometry_type = "FOOTPRINT"

arcpy.ExportMosaicDatasetGeometry_management(
     mdname, out_FC, where_clause, geometry_type)