"""
Name: upgrade_gdb.py
Description: Provide connection information to an Enterprise geodatabase 
and upgrade the geodatabase
Type upgrade_gdb.py -h or upgrade_gdb.py --help for usage
"""

# Import system modules
import arcpy
import os
import optparse
import sys


# Define usage and version
parser = optparse.OptionParser(usage = "usage: %prog [Options]", version="%prog 2.0; valid for 10.1 only")

#Define help and options
parser.add_option ("--DBMS", dest="Database_type", type="choice", choices=['SQLSERVER', 'ORACLE', 'POSTGRESQL', 'DB2','INFORMIX','DB2ZOS',''], default="", help="Type of enterprise DBMS:  SQLSERVER, ORACLE, or POSTGRESQL.")
parser.add_option ("-i", dest="Instance", type="string", default="", help="DBMS instance name")
parser.add_option ("--auth", dest="account_authentication", type ="choice", choices=['DATABASE_AUTH', 'OPERATING_SYSTEM_AUTH'], default='DATABASE_AUTH', help="Authentication type options (case-sensitive):  DATABASE_AUTH, OPERATING_SYSTEM_AUTH.  Default=DATABASE_AUTH")
parser.add_option ("-u", dest="User", type="string", default="", help="Geodatabase administrator user name")
parser.add_option ("-p", dest="Password", type="string", default="", help="Geodatabase administrator password")
parser.add_option ("--upgrade", dest="Upgrade", type="choice", choices=['TRUE', 'FALSE'], default="FALSE", help="Upgrade Options (case-sensitive):  TRUE=Perform Pre-requisite check and upgrade geodatabase, FALSE=Perform Pre-requisite check only.  Default=FALSE")                   
parser.add_option ("-D", dest="Database", type="string", default="none", help="Database name:  Not required for Oracle")


# Check if value entered for option
try:
	(options, args) = parser.parse_args()

	
#Check if no system arguments (options) entered
	if len(sys.argv) == 1:
		print("%s: error: %s\n" % (sys.argv[0], "No command options given"))
		parser.print_help()
		sys.exit(3)

	#Usage parameters for spatial database connection to upgrade
	account_authentication = options.account_authentication.upper()
	username = options.User.lower() 
	password = options.Password	
	do_upgrade = options.Upgrade
	database = options.Database.lower()
	database_type = options.Database_type.upper()
	instance = options.Instance
	
	if (database_type == ""):
		print("\nDatabase type must be specified!\n")
		parser.print_help()
		sys.exit(3)
	
	if (database_type == "SQLSERVER"):
		database_type = "SQL_SERVER"
	
	# Get the current product license
	product_license=arcpy.ProductInfo()
	
	# Checks required license level to upgrade
	if product_license.upper() == "ARCVIEW" or product_license.upper() == 'ENGINE':
		print("\n" + product_license + " license found!" + "  Enterprise geodatabase upgrade requires an ArcGIS Desktop Standard or Advanced, ArcGIS Engine with the Geodatabase Update extension, or ArcGIS Server license.")
		sys.exit("Re-authorize ArcGIS before upgrading.")
	else:
		print("\n" + product_license + " license available!  Continuing to upgrade...")
		arcpy.AddMessage("+++++++++")
	
	# Local variables
	instance_temp = instance.replace("\\","_")
	instance_temp = instance_temp.replace("/","_")
	instance_temp = instance_temp.replace(":","_")
	Conn_File_NameT = instance_temp + "_" + database + "_" + username     
	
	if os.environ.get("TEMP") == None:
		temp = "c:\\temp"	
	else:
		temp = os.environ.get("TEMP")
	
	if os.environ.get("TMP") == None:
		temp = "/usr/tmp"		
	else:
		temp = os.environ.get("TMP")  
	
	Connection_File_Name = Conn_File_NameT + ".sde"
	Connection_File_Name_full_path = temp + os.sep + Conn_File_NameT + ".sde"
	
	# Check for the .sde file and delete it if present
	arcpy.env.overwriteOutput=True
	if os.path.exists(Connection_File_Name_full_path):
		os.remove(Connection_File_Name_full_path)
	
	print("\nCreating Database Connection File...\n")
	# Process: Create Database Connection File...
	# Usage:  out_file_location, out_file_name, DBMS_TYPE, instnace, database, account_authentication, username, password, save_username_password(must be true)
	arcpy.CreateDatabaseConnection_management(out_folder_path=temp, out_name=Connection_File_Name, database_platform=database_type, instance=instance, database=database, account_authentication=account_authentication, username=username, password=password, save_user_pass="TRUE")
        for i in range(arcpy.GetMessageCount()):
		if "000565" in arcpy.GetMessage(i):   #Check if database connection was successful
			arcpy.AddReturnMessage(i)
			arcpy.AddMessage("\n+++++++++")
			arcpy.AddMessage("Exiting!!")
			arcpy.AddMessage("+++++++++\n")
			sys.exit(3)            
		else:
			arcpy.AddReturnMessage(i)
			arcpy.AddMessage("+++++++++\n")
			
	# Check whether geodatabase needs upgrade
	isCurrent = arcpy.Describe(Connection_File_Name_full_path).currentRelease
	
	if isCurrent == True:
		print("The geodatabase is already at the current release and cannot be upgraded!")
		sys.exit("Upgrade did not run.")
	
	
	# Process: Upgrade geodatabase...
	try:
		if do_upgrade.lower() == "true":
			print("Upgrading Geodatabase...\n")
			arcpy.UpgradeGDB_management(input_workspace=Connection_File_Name_full_path, input_prerequisite_check="PREREQUISITE_CHECK", input_upgradegdb_check="UPGRADE")
			for i in range(arcpy.GetMessageCount()):
				arcpy.AddReturnMessage(i)
			arcpy.AddMessage("+++++++++\n")
	
		else:
			print("Running Pre-Requisite Check...\n")
			arcpy.UpgradeGDB_management(input_workspace=Connection_File_Name_full_path, input_prerequisite_check="PREREQUISITE_CHECK", input_upgradegdb_check="NO_UPGRADE")
			for i in range(arcpy.GetMessageCount()):
				arcpy.AddReturnMessage(i)
			arcpy.AddMessage("+++++++++\n")
		
	        
	except:
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
		
	if os.path.exists(Connection_File_Name_full_path):
		os.remove(Connection_File_Name_full_path)
	
#Check if no value entered for option	
except SystemExit as e:
	if e.code == 2:
		parser.usage = ""
		print("\n")
		parser.print_help()
		parser.exit(2)