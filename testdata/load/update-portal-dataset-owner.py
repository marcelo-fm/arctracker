import arcpy
arcpy.UpdatePortalDatasetOwner_management(
    r"C:\MyProject\February\MyDatabase.sde\database.USER1.Electric\database.USER1.ElectricUN", 
    'gisadmin')