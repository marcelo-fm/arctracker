import arcpy
arcpy.ExportAttributeRules_management("C:\\MyProject\\MyDatabase.sde\\pro.USER1.GasPipes", 
                                      "C:\\MyProject\\ExpAttrRulesFrBuilding.csv")