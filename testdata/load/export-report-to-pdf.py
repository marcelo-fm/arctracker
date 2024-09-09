# ExportReporttoPDFAPI.py
# Simple example of exporting a report using Python

# Import system variables
import arcpy

# Identify all parcel reports in a project
aprx = arcpy.mp.ArcGISProject("C:/data/parcels/Parcels.aprx")
report = aprx.listReports("Parcels Report")[0]

# Export the report with a definition query
arcpy.ExportReportToPDF_management(report.name, "C:/data/parcels/ParcelsPDF.pdf", 
                                   ' "LotSize" > 325 ')