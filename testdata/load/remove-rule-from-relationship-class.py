import arcpy
arcpy.management.RemoveRuleFromRelationshipClasss(
    "C:\\MyProject\\sdeConn.sde\\progdb.user1.ParcelsToBuildings", "Residential", 
    "House")