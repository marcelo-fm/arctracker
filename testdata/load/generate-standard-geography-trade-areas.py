import arcpy
arcpy.ba.StandardGeographyTA("US.ZIP5", r"C:\Temp\Output.gdb\StdGeogTradeAreas",
                             None, None, "92111,92117,92122", "USE_FIRST", None,
                             "DISSOLVE")