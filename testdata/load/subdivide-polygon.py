import arcpy

arcpy.env.workspace = r"C:/data/project.gdb"
arcpy.SubdividePolygon_management(
    "studyarea", "subdivisions", "NUMBER_OF_EQUAL_PARTS", 10, "", "", 0, 
    "STRIPS")