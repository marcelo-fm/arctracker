# This code assumes a map named "World1" exists in the current project
import arcpy
outputFile = "c:/outputPackages/world_map.mpkx"
arcpy.management.PackageMap("World1", outputFile, "PRESERVE", "CONVERT_ARCSDE", "#", "ALL")