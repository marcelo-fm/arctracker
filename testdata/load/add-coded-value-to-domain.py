# Name: MakeDomain.py
# Description: Create an attribute domain to constrain pipe material values
 
# Import system modules
import arcpy
 
# Set the workspace (to avoid having to type in the full path to the data every time)
arcpy.env.workspace = "C:/data"
 
# Set local parameters
domName = "Material4"
gdb = "montgomery.gdb"
inFeatures = "Montgomery.gdb/Water/Distribmains"
inField = "Material"
 
# Process: Create the coded value domain
arcpy.CreateDomain_management("montgomery.gdb", domName, "Valid pipe materials", 
                              "TEXT", "CODED")

# Store all the domain values in a dictionary with the domain code as the "key" 
# and the domain description as the "value" (domDict[code])
domDict = {"CI":"Cast iron", "DI": "Ductile iron", "PVC": "PVC", \
           "ACP": "Asbestos concrete", "COP": "Copper"}
    
# Process: Add valid material types to the domain
# use a for loop to cycle through all the domain codes in the dictionary
for code in domDict:        
    arcpy.AddCodedValueToDomain_management(gdb, domName, code, domDict[code])
    
# Process: Constrain the material value of distribution mains
arcpy.AssignDomainToField_management(inFeatures, inField, domName)