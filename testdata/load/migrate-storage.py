# Name: MigrateStorage_Example.py
# Description: Migrates the input dataset to the ST_Geometry geometry storage type. 

# Import arcpy module
import arcpy

# Local variables:
inputDataset = "f:\\Connections\\Oracle on khyber.sde\\MAP.SBMigrate"

# Process: Migrate Storage
arcpy.management.MigrateStorage(inputDataset, "ST_GEOMETRY")