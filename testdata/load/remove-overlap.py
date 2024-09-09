import arcpy
arcpy.ba.RemoveOverlap("Ring_Trade_Areas", r"C:\Temp\MyProject.gdb\Ring_Trade_Areas_RemoveOverlap", "THIESSEN", "DEFINE_TRADE_AREA", "RING", None, STORE_ID)