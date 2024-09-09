# Name: CopyDatasetFromBDC.py
# Description: Copies a dataset from a MFC to a file geodatabase.

# Import system modules
import arcpy
arcpy.env.workspace = "C:/data/basin.gdb"

# Set local variables
inputDataset = "C:/data/Datasets.mfc/rivers"
output = "rivers"

# Run CopyDatasetFromBDC
arcpy.gapro.CopyDatasetFromBDC(inputDataset, output)