import arcpy

try:
    arcpy.server.StageService(r"C:\Data\World.sddraft", r"C:\Data\World.sd")
    warnings = arcpy.GetMessages(1)
    print(warnings)

except Exception as stage_exception:
    print("Sddraft not staged. Analyzer errors encountered - {}".format(str(stage_exception)))