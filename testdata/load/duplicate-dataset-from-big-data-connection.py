# Name: DuplicateDatasetFromBDC.py
# Description: Creates a duplicate of a multifile feature connection dataset.
#
# Requirements: ArcGIS Pro Advanced License

# Import system modules
import arcpy

# Set local variables
bdcDataset = r"c:\Projects\MyProjectFolder\my_BigDataConnection.mfc\Taxi_Locations"
newName = "taxi_pickups"

# Run Duplicate Dataset From MFC
arcpy.gapro.DuplicateDatasetFromBDC(bdcDataset, newName)