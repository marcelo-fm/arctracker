# Name: RemoveDomainsExample.py
# Purpose: Update an attribute domain to constrain valid pipe material values

# Import system modules
import arcpy
import os
 
# Set the workspace (to avoid having to type in the full path to the data every time)
arcpy.env.workspace = "data"
 
# set local parameters
inFeatures = "Montgomery.gdb/Water/DistribMains"
inField = "MATERIAL"
dWorkspace = "Montgomery.gdb"
domName = "Material"
codedValue =  "ACP: Asbestos concrete"
codeField = "TYPE"
descField = "DESRIPT"

# Process: Remove the constraint from the material field
arcpy.RemoveDomainFromField_management(inFeatures, inField)
 
# Edit the domain values
# Process: Remove a coded value from the domain
arcpy.DeleteCodedValueFromDomain_management(dWorkspace, domName, codedValue)

# Process: Create a table from the domain to edit it with standard editing tools
arcpy.DomainToTable_management(dWorkspace, domname, 
                               os.path.join(dWorkspace, domname), codeField, 
                               descField)
 
# Process: Delete the domain
arcpy.DeleteDomain_management(dWorkspace, domName)
 
# Edit the domain table outside of geoprocessing
# and then bring the domain back in with the TableToDomain process