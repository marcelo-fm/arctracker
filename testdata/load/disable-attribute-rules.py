import arcpy
fc = "C:\\MyProject\\MyDatabase.sde\\pro.USER1.campusData"
desc = arcpy.Describe(fc).attributeRules
for rule in desc:
    if rule.isEnabled == True and rule.type == "esriARTConstraint":
        print("Disabling rule: {}".format(rule.name))
        arcpy.DisableAttributeRules_management(fc, rule.name)