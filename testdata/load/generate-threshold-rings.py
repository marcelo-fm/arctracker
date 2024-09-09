import arcpy
arcpy.ba.GenerateThresholdRingTradeArea("SF_Custs",r"C:\Project1.gdb\SF_Custs_GenerateThresholdRingTradeArea","populationtotals.totpop_cy",[50000,
100000], "MILES", "STORE_ID", Values, None)