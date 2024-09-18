# Import system modules and check out ArcGIS Image Analyst extension license
import arcpy
arcpy.CheckOutExtension("ImageAnalyst")
from arcpy.ia import *

# Set local variables
in_radar = r"C:\Data\SAR\S1\S S1B_IW_SLC__1SDV_20181014T014103_20181014T014130_013142_018486_1753.SAFE\manifest.safe\IW1"
orbit_type = "SENTINEL_PRECISE" 
username = "esaUsername"
password = "esaPassword"
cloud_storage = r"C:\connection_files\eodata.acs" 

# Execute 
arcpy.ia.DownloadOrbitFile(in_radar, orbit_type, username, password, cloud_storage)