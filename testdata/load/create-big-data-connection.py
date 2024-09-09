# Name: CreateBigDataConnection.py
# Description: Establishes a connection to a folder location containing one or 
#              more datasets. Datasets will be used as input to GeoAnalytics 
#              Desktop Tools.
#
# Requirements: ArcGIS Pro Advanced License

# Import system modules
import arcpy

# Set local variables
sourceFolder = r"\\FileShare\MyLargeDatasets"
outName = "my_new_MultifileFeatureConnection"
outFolder = r"c:\Projects\MyProjectFolder"
time = "TIME_NOT_VISIBLE"
geometry = "GEOMETRY_VISIBLE"

# Run Create Multifile Feature Connection
arcpy.gapro.CreateBDC(outFolder, outName, "FOLDER", sourceFolder, geometry, time)