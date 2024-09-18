import arcpy
extent = arcpy.Extent(7497466.20831177, 441293.021878974, 7502009.67757057, 444095.976178293)
arcpy.parcel.GenerateParcelFabricLinks('L0Parcel_Fabric', 'C:\Data\Database.gdb\OutLinks', 'C:\Data\Database.gdb\OutAnchor2', 
'7/29/2020 3:50:13 PM', '', '', arcpy.env.extent)