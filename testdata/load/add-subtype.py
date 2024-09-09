# Name: ManageSubtypes.py
# Purpose: Create a subtype definition

# Import system modules
import arcpy
 
# Set the workspace (to avoid having to type in the full path to the data every time)
arcpy.env.workspace =  "C:/data/Montgomery.gdb"
    
# Set local parameters
inFeatures = "water/fittings"
 
# Process: Set Subtype Field...
arcpy.SetSubtypeField_management(inFeatures, "TYPECODE")

# Process: Add Subtypes...
# Store all the suptype values in a dictionary with the subtype code as the 
# "key" and the subtype description as the "value" (stypeDict[code])
stypeDict = {"0": "Unknown", "1": "Bend", "2": "Cap", "3": "Cross", 
             "4": "Coupling", "5": "Expansion joint", "6": "Offset", 
             "7": "Plug", "8": "Reducer", "9": "Saddle", "10": "Sleeve", 
             "11": "Tap", "12": "Tee", "13": "Weld", "14": "Riser"} 
    
# use a for loop to cycle through the dictionary
for code in stypeDict:
    arcpy.AddSubtype_management(inFeatures, code, stypeDict[code])     
			
# Process: Set Default Subtype...
arcpy.SetDefaultSubtype_management(inFeatures, "4")