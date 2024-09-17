# Import system modules
import arcpy

arcpy.env.workspace = "C:/OrientedImageryExample"

# Set local variables
gdbName = "CreateOI.gdb"
oiName = "myFirstOI"
dataset = "C:/OrientedImageryExample/CreateOI.gdb/dataset"
spatialRef = arcpy.Describe(dataset).spatialReference
elvSource = "DEM"
demService = "https://elevation.arcgis.com/arcgis/rest/services/WorldElevation/Terrain/ImageServer/"

# Run Create Oriented Imagery Dataset 
arcpy.oi.CreateOrientedImageryDataset(
    gdbName, oiName, spatialRef, elevation_source=elvSource, dem=demService
)