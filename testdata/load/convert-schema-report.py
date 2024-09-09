# Name: ConvertSchemaReport_Example.py
# Description: ConvertSchemaReport of a file geodatabase

# Import the system modules
import arcpy

# Set local variables
out_location=r"C:\location\folder"

arcpy.management.ConvertSchemaReport(schema_report=r"C:\folder\TEST.xlsx", out_location,
                                     name="NEW", formats=["JSON", "XLSX", "HTML", "PDF", "XML"])