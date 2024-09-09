# Description: Add polygon fields from a USA Census block group feature class in a file geodatabase to a USA locator.

import arcpy

# Set local variables:
usa_locator = r"C:\Data\USA.loc"
polygon_features = r"C:\Data\USCensus.gdb\blkgrp"
polygon_output_fields = [["BLKGRP", "BLOCKGROUP"], ["POPULATION", "POPULATION"], 
                         ["VACANT", "VACANT"], ["HSE_UNITS", "HOUSE_UNITS"]]

# Run AddPolygonFieldsToLocator
arcpy.geocoding.AddPolygonFieldsToLocator(usa_locator, polygon_features, polygon_output_fields)