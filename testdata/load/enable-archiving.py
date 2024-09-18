# Name: EnableArchiving_Example.py
# Description: Enable archiving on a dataset

# Import system modules
import arcpy

# Set local variables
in_dataset = 'C:/Data/connections/Redlands.sde/TEST.TOOLBOX.rdlsstreets'

# Describe the properties of the dataset to see if archiving is enabled.
desc = arcpy.Describe(in_dataset)
isArch = desc.IsArchived

# Enable Archiving if it is not already enabled.
if isArch == False:
    # Execute EnableArchiving
    arcpy.EnableArchiving_management(in_dataset)
    print("{0} has been enabled for archiving.".format(in_dataset))
elif isArch == True:
    # If IsArch = True, then archiving is already enabled
    print("{0} already has archiving enabled.".format(in_dataset))