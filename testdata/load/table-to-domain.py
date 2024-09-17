# Name: TableToDomain.py
# Description: Update an attribute domain to constrain valid pipe material values

# Import system modules
import arcpy
 
# Set the workspace (to avoid having to type in the full path to the data every time)
arcpy.env.workspace = "C:/data"

#Set local parameters
domTable = "diameter.dbf"
codeField = "code"
descField = "descript"
dWorkspace = "Montgomery.gdb"
domName = "diameters"
domDesc = "Valid pipe diameters"

# Process: Create a domain from an existing table
arcpy.TableToDomain_management(domTable, codeField, descField, dWorkspace, domName, domDesc)