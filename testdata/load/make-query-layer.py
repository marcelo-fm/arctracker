# Name: MakeQueryLayer.py
# Description: Creates an output query layer based on a where clause.
#   This example shows how to create a spatial reference object using the
#   name of a coordinate system. It also demonstrates how to use two fields
#   to generate a dynamic unique row identifier for the query layer.


# Import system modules
import arcpy

# Create the spatial reference for the output layer.
sr = arcpy.SpatialReference("WGS 1984 UTM Zone 12N")

# Run the tool
arcpy.MakeQueryLayer_management("Connections/moab.sde",
                                "Single Track",
                                "select * from moabtrails where type = 'single'",
                                "UID;name",
                                "POLYLINE",
                                "32611",
                                sr)