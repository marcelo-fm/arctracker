# Name: MultipartToSinglepart_Example2.py
# Description: Break all multipart features into singlepart features,
#              and report which features were separated.

# Import system modules
import arcpy
 
# Create variables for the input and output feature classes
inFeatureClass = "c:/data/gdb.gdb/vegetation"
outFeatureClass = "c:/data/gdb.gdb/vegetation_singlepart"

try:
    # Create list of all fields in inFeatureClass
    fieldNameList = [field.name for field in arcpy.ListFields(inFeatureClass)]

    # Add a field to the input that will be used as a unique identifier
    arcpy.management.AddField(inFeatureClass, "tmpUID", "double")
 
    # Determine what the name of the Object ID is 
    OIDFieldName = arcpy.Describe(inFeatureClass).OIDFieldName
   
    # Calculate the tmpUID to the OID
    arcpy.management.CalculateField(inFeatureClass, "tmpUID",
                                    f"!{OIDFieldName}!", "PYTHON3")
 
    # Run the tool to create a new fc with only singlepart features
    arcpy.management.MultipartToSinglepart(inFeatureClass, outFeatureClass)
 
    # Check if there is a different number of features in the output
    #   than there was in the input
    inCount = int(arcpy.management.GetCount(inFeatureClass)[0])
    outCount = int(arcpy.management.GetCount(outFeatureClass)[0])
    
    if inCount != outCount:
        # If there is a difference, print the FID of the input 
        #   features that were multipart
        arcpy.analysis.Frequency(outFeatureClass,
                                 outFeatureClass + "_freq", "tmpUID")
 
        # Use a search cursor to go through the table, and print the tmpUID 
        print("Multipart features from {0}".format(inFeatureClass))
        for row in arcpy.da.SearchCursor(outFeatureClass + "_freq",
                                         ["tmpUID"], "FREQUENCY > 1"):
            print(int(row[0]))
    else:
        print("No multipart features were found")

except arcpy.ExecuteError:
    print(arcpy.GetMessages())
except Exception as err:
    print(err.args[0])