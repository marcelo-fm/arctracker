# Name: RefreshBDC.py
# Description: Refreshes a multifile feature connection to automatically discover datasets that 
#              have been added.
#
# Requirements: ArcGIS Pro Advanced License

# Import system modules
import arcpy

# Set local variables
mfcFile = r"c:\Projects\MyProjectFolder\my_BigDataConnection.mfc"

# Run Refresh Multifile Feature Connection
arcpy.gapro.RefreshBDC(mfcFile)