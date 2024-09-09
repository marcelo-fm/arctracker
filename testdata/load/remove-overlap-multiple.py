import arcpy
arcpy.analysis.RemoveOverlapMultiple("Ring_Trade_Areas", r"C:\Temp\MyProject.gdb\Ring_Trade_Areas_RemoveOverlapMultiple", "THIESSEN", "ALL")