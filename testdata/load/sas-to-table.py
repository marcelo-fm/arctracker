# Import system modules
import arcpy
import getpass

# Provide tool parameters
in_SASDS = "casuser.MySASData"
out_table = "MyEsriData"
connection = "USE_CAS"
hosturl = https://XXX.vdp.sas.com/XXX-XXXXX-default-http/ 
port = 100
username = "CAS_user"

# Provide password securely
password = getpass.getpass()

try:
    # Set the workspace and run the tool.
    arcpy.env.workspace = r"C:\\SASToTable\\MyData.gdb"
    arcpy.conversion.SASToTable(in_SASDS, out_table, connection, hosturl,
                     port, username, password)

except arcpy.ExecuteError:
    # If an error occurred when running the tool, print the error message.
    print(arcpy.GetMessages())