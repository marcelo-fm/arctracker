'''****************************************************************************
Name: Buffer 3D Example
Description: This script demonstrates an application of
             the Buffer 3D and Inside 3D tools.
****************************************************************************'''
# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = 'C:/data'

# Set Local Variables
inFC = 'lineFC.shp'
bufferOut = 'buffer3d.shp'

# Execute Buffer 3D
arcpy.Buffer3D_3d(inFC, bufferOut, '15 Meters', 'Round', '30', '1 Meters')
arcpy.Inside3D_3d(bufferOut, 'survey_pts.shp', 'inside_analysis.dbf')