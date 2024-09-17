# Name: DisableArchiving_Example.py
# Description: Disable archiving on a dataset

# Import system modules
import arcpy

# Set local variables
in_dataset = "C:/Data/connections/intense.sde/intense.carbine.bike_routes"

# Run program
desc = arcpy.Describe(in_dataset)
if desc.isArchived == True:
  arcpy.DisableArchiving_management(in_dataset)
  print('Successfully disabled archiving on: {0}'.format(in_dataset))
else:
  print('Archiving has already been disabled.')