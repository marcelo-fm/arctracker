# Name: RemoveDatasetFromBDC.py
# Description: Remove specified datasets from one or more multifile feature connection files.

# Requirements: ArcGIS Pro Advanced License

# Import system modules
import arcpy

# Set local variables
datasets = [r"c:\Projects\MyProjectFolder\my_BigDataConnection.mfc\Dataset1", 
            r"c:\Projects\MyProjectFolder\my_BigDataConnection.mfc\Dataset2"]

# Run Remove Dataset From Multifile Feature Connection
arcpy.gapro.RemoveDatasetFromBDC(datasets)