# Name: CreateRangeDomain.py
# Purpose: Create an attribute domain to constrain valid rotation angle

# Import system modules
import arcpy
 
# Set the workspace (to avoid having to type in the full path to the data every time)
arcpy.env.workspace = "C:/data"

# Set local parameters
dWorkspace = "montgomery.gdb"
domName = "RotAngle2"
domDesc = "Valid rotation angle"
minRange = 0
maxRange = 359
inFeatures = "Montgomery.gdb/Water/fittings"
inField = "ANGLE"

# Process: Create the range domain
arcpy.CreateDomain_management(dWorkspace, domName, domDesc, "LONG", "RANGE")

# Process: Set the minimum and maximum values for the range domain
arcpy.SetValueForRangeDomain_management(dWorkspace, domname, minRange, maxRange)

# Process: Constrain the fitting rotation angle
arcpy.AssignDomainToField_management( inFeatures, inField, domName)