# Import system modules
import arcpy
import getpass

# Provide tool parameters
in_table = "MyData"
out_SASDS = "casuser.MySASData"
replace_output = "OVERWRITE"
field_domains = "USE_DOMAIN"
connection = "USE_CAS"
hosturl = https://XXX.vdp.sas.com/XXX-XXXXX-default-http/ 
port = 100
username = "CAS_user"

# Provide password securely
password = getpass.getpass()

try:
    # Set the workspace and run the tool.
    arcpy.env.workspace = r"C:\\TableToSAS\\MyData.gdb"
    arcpy.conversion.TableToSAS(in_table, out_SASDS, replace_output, 
                                field_domains, connection, hosturl, port, 
                                username, password)
except arcpy.ExecuteError:
    # If an error occurred when running the tool, print the error message.
    print(arcpy.GetMessages())