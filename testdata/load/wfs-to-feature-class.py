# Name: WFSToFeatureClass_example1.py
# Description: Create a feature class from a WFS service

# Import arcpy module
import arcpy

# Set local variables
WFS_Service = "http://sampleserver6.arcgisonline.com/arcgis/services/SampleWorldCities/MapServer/WFSServer?request=GetCapabilities&service=WFS"
WFS_FeatureType = "cities"
Out_Location = "C:/Data/Default.gdb"
Out_Name = "SampleWorldCities"

# Execute the WFSToFeatureClass tool
arcpy.conversion.WFSToFeatureClass(WFS_Service, WFS_FeatureType, Out_Location, Out_Name)