# This code assumes a map named "World1" exists in the current project
import arcpy
arcpy.management.ConsolidateMap('World1', 'c:/projects/World', 'PRESERVE', 'CONVERT_ARCSDE')