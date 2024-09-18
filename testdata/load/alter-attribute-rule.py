import arcpy
arcpy.management.AlterAttributeRule("C:\\MyProject\\sdeConn.sde\\progdb.user1.GasPipes", 
                                    "constraintRuleOP",
                                    "Operating pressure cannot exceed 300",
                                    "999",
                                    "Invalid operating pressure value",
                                    "Pipeline;OP;ExceededValue")