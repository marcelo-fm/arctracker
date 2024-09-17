#Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data/output.gdb"

# Set local variables
catalogName = "MyCatalogDataset"
outCatalogDataset = "C:/output/output.gdb/catalogds1"
zValuesPresent = "ENABLED"

# Run CreateCatalogDataset
arcpy.management.CreateCatalogDataset(outCatalogDataset, catalogName, " ",
                                      zValuesPresent)