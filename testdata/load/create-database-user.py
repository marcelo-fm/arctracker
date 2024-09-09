"""
Name: create_database_user.py
Description: Provide connection information to a database user.
Type create_database_user.py -h or create_database_user.py --help for usage
"""

# Import system modules
import arcpy
import os
import optparse
import sys


# Define usage and version
parser = optparse.OptionParser(usage = "usage: %prog [Options]", version="%prog 1.0 for 10.1 release")

#Define help and options
parser.add_option ("--DBMS", dest="Database_type", type="choice", choices=['SQLSERVER', 'ORACLE', 'POSTGRESQL', ''], default="", help="Type of enterprise DBMS:  SQLSERVER, ORACLE, or POSTGRESQL.")                   
parser.add_option ("-i", dest="Instance", type="string", default="", help="DBMS instance name")
parser.add_option ("-D", dest="Database", type="string", default="none", help="Database name:  Not required for Oracle")
parser.add_option ("--auth", dest="Account_authentication", type ="choice", choices=['DATABASE_AUTH', 'OPERATING_SYSTEM_AUTH'], default='DATABASE_AUTH', help="Authentication type options (case-sensitive):  DATABASE_AUTH, OPERATING_SYSTEM_AUTH.  Default=DATABASE_AUTH")
parser.add_option ("-U", dest="Dbms_admin", type="string", default="", help="DBMS administrator user")
parser.add_option ("-P", dest="Dbms_admin_pwd", type="string", default="", help="DBMS administrator password")
parser.add_option ("--utype", dest="user_type", type ="choice", choices=['DATABASE_USER', 'OPERATING_SYSTEM_USER'], default='DATABASE_USER', help="Authentication type options (case-sensitive):  DATABASE_USER, OPERATING_SYSTEM_USER.  Default=DATABASE_USER")
parser.add_option ("-u", dest="dbuser", type="string", default="", help="database user name")
parser.add_option ("-p", dest="dbuser_pwd", type="string", default="", help="database user password")
parser.add_option ("-r", dest="role", type="string", default="", help="role to be granted to the user")
parser.add_option ("-t", dest="Tablespace", type="string", default="", help="Tablespace name")
# Check if value entered for option
try:
	(options, args) = parser.parse_args()

	#Check if no system arguments (options) entered
	if len(sys.argv) == 1:
		print "%s: error: %s\n" % (sys.argv[0], "No command options given")
		parser.print_help()
		sys.exit(3)

	#Usage parameters for spatial database connection
	database_type = options.Database_type.upper()
	instance = options.Instance
	database = options.Database.lower()	
	account_authentication = options.Account_authentication.upper()
	dbms_admin = options.Dbms_admin
	dbms_admin_pwd = options.Dbms_admin_pwd
	dbuser = options.dbuser
	dbuser_pwd = options.dbuser_pwd	
	tablespace = options.Tablespace
	user_type = options.user_type
	role = options.role

	
	if (database_type == "SQLSERVER"):
		database_type = "SQL_SERVER"
	
	if( database_type ==""):	
		print(" \n%s: error: \n%s\n" % (sys.argv[0], "DBMS type (--DBMS) must be specified."))
		parser.print_help()
		sys.exit(3)		
	
	if(database_type == "SQL_SERVER"):
		if( account_authentication == "DATABASE_AUTH" and dbms_admin == ""):
			print("\n%s: error: %s\n" % (sys.argv[0], "DBMS administrator must be specified with database authentication"))
			sys.exit(3)
		if( account_authentication == "OPERATING_SYSTEM_AUTH" and dbms_admin != ""):
			print("\nWarning: %s\n" % ("Ignoring DBMS administrator specified when using operating system authentication..."))
	else:		
		if( dbuser.lower() == ""):
			print("\n%s: error: %s\n" % (sys.argv[0], "Database user must be specified."))
			sys.exit(3)		
		if( dbms_admin == ""):
			print("\n%s: error: %s\n" % (sys.argv[0], "DBMS administrator must be specified!"))
			sys.exit(3)

	if ( user_type == "DATABASE_USER" and (dbuser =="" or dbuser_pwd =="")):
		print(" \n%s: error: \n%s\n" % (sys.argv[0], "To create database authenticated user, user name and password must be specified!"))
		parser.print_help()
		sys.exit(3)	

	# Get the current product license
	product_license=arcpy.ProductInfo()
	
	# Checks required license level
	if product_license.upper() == "ARCVIEW" or product_license.upper() == 'ENGINE':
		print("\n" + product_license + " license found!" + "  Creating a user in an enterprise geodatabase or database requires an ArcGIS Desktop Standard or Advanced, ArcGIS Engine with the Geodatabase Update extension, or ArcGIS Server license.")
		sys.exit("Re-authorize ArcGIS before creating a database user.")
	else:
		print("\n" + product_license + " license available!  Continuing to create...")
		arcpy.AddMessage("+++++++++")

	# Local variables
	instance_temp = instance.replace("\\","_")
	instance_temp = instance_temp.replace("/","_")
	instance_temp = instance_temp.replace(":","_")
	Conn_File_NameT = instance_temp + "_" + database + "_" + dbms_admin   

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

	try:
		print("\nCreating Database Connection File...\n")
		# Process: Create Database Connection File...
		# Usage:  out_file_location, out_file_name, DBMS_TYPE, instnace, database, account_authentication, username, password, save_username_password(must be true)
		#arcpy.CreateDatabaseConnection_management(temp , Connection_File_Name, database_type, instance, database, account_authentication, dbms_admin, dbms_admin_pwd, "TRUE")
		arcpy.CreateDatabaseConnection_management(out_folder_path=temp, out_name=Connection_File_Name, database_platform=database_type, instance=instance, database=database, account_authentication=account_authentication, username=dbms_admin, password=dbms_admin_pwd, save_user_pass="TRUE")
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

		print("Creating database user...\n")
		arcpy.CreateDatabaseUser_management(input_workspace=Connection_File_Name_full_path, user_authentication_type=user_type, user_name=dbuser, user_password=dbuser_pwd, role=role, tablespace_name=tablespace)
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
		arcpy.AddMessage("+++++++++\n")
	except:
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
			
#Check if no value entered for option	
except SystemExit as e:
	if e.code == 2:
		parser.usage = ""
		print("\n")
		parser.print_help()   
		parser.exit(2)