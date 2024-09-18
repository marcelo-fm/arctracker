import arcpy
arcpy.management.DeleteAttributeRule(
    "C:\\MyProject\\MyDatabase.sde\\pro.USER1.campusData", "Rule A;Rule B", 
    "CALCULATION")