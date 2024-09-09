'''****************************************************************************
       Name: Update Antenna Positions
Description: Updates antenna positions based on elevations from a surface.
****************************************************************************'''
# Import system modules
import arcpy

in_fc = arcpy.GetParameterAsText(1) # pt features representing antenna locations
surface = arcpy.GetParameterAsText(2) # surface used to modify feature Z values


try:
    if arcpy.Describe(surface).dataType in ('Raster', 'RasterLayer'):
        method = 'BILINEAR'
    else:
        method = 'CONFLATE_ZMAX'
    arcpy.ddd.UpdateFeatureZ(in_fc, surface, method)

except arcpy.ExecuteError:
    print(arcpy.GetMessages())