import arcpy

# Access data locally
arcpy.env.baDataSource = "LOCAL;;USA_ESRI_2023"

# Access data online
arcpy.env.baDataSource = "ONLINE;US;"