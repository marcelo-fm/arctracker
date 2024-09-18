import arcpy

# Set the outputZFlag environment to Enabled
arcpy.env.outputZFlag = "Enabled"

# AddTraceLocations
arcpy.un.AddTraceLocations(r"http://landbase.mydomain.com/server/rest/services/NapervilleElectric/FeatureServer/9", 
                           r"C:\Project\MyUNProject.gdb\TraceLocations",
                           "DO_NOT_LOAD_SELECTED_FEATURES",
                           "KEEP_LOCATIONS",
                           "'Circuit Breaker' {DDB0765D-860A-4054-908D-9360E1A32F74} '(3/Load)' #";"'ElecDist Line' {67C0534B-A80D-4E5F-8926-5FB5F887A5F2} # 0.25","TRAVERSABILITY_BARRIER")