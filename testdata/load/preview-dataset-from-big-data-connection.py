# Name: PreviewDatasetFromBigDataConnection.py
# Description: Preview a dataset from a MFC.

# Requirements: ArcGIS Pro Advanced License

# Import system modules
import arcpy

# Set local variables
dataset = r"c:\Projects\MyProjectFolder\my_BigDataConnection.mfc\airplane_tracksDataset"
csvOutput = r"c:\Projects\MyProjectFolder\Preview_airplane_tracks.csv"

# Preview MFC Dataset
arcpy.gapro.PreviewDatasetFromBDC(dataset, csvOutput)