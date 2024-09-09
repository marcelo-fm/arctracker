import arcpy

arcpy.management.AddRuleToRelationshipClass(
    "C:\\MyProject\\sdeConn.sde\\progdb.user1.ParcelsToBuildings", "Residential", 
    0, 1, "House", 1, 3)