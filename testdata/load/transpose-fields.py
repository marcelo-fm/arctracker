# Name: TransposeFields_Ex_02.py
# Description: Tranpose field names from column headers to values in one column
# Requirements: None

# Import system modules
import arcpy
from arcpy import env

# set workspace
arcpy.env.workspace = "C:/Data/TemporalData.gdb"

# Set local variables
inTable = "Input"
# Specify fields to transpose
fieldsToTranspose = "Field1 newField1;Field2 newField2;Field3 newField3"
# Set a variable to store output feature class or table
outTable = "Output_Time"
# Set a variable to store time field name
transposedFieldName = "Transposed_Field"
# Set a variable to store value field name
valueFieldName = "Value"
# Specify attribute fields to be included in the output
attrFields = "Shape;Type"

# Execute TransposeTimeFields
arcpy.TransposeFields_management(inTable, fieldsToTranspose, outTable, transposedFieldName, valueFieldName, attrFields)