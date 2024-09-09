# Import system modules
import arcpy

# Set environments
arcpy.env.workspace = 'C:/data'

print("Constructing Sightlines")
arcpy.ddd.ConstructSightLines("Observers.shp", "Targets.shp", "sightlines.shp", 
                              observer_height_field='Shape.Z', target_height_field='Shape.Z')

print("Calculating Intervisibility")
arcpy.ddd.Intervisibility("Sightlines.shp", obstructions=["DTM_Tin", "data.gdb/buildings"],
                          visible_field="Visibility")