# Name: CreateRelationshipClass.py
# Description: Create a relationship class between parcels feature
#              class and table with owner information
# Author: ESRI

# Import system modules 
import arcpy
from arcpy import env

# Set environment settings
env.workspace = "C:/data"

# Copy owners.dat to file gdb table, since both tables to be related
# must be in the same database
ownerDat = "owners.dat"
ownerTbl = "Montgomery.gdb/owners"
arcpy.CopyRows_management(ownerDat, ownerTbl)

# Create simple relationship class between 'parcel' parcel layer
# and 'owner' table with additional parcel owner information
parcel = "Montgomery.gdb/Parcels"
relClass = "Montgomery.gdb/parcelowners_RelClass"
forLabel = "Owns"
backLabel = "Is Owned By"
primaryKey = "PROPERTY_ID"
foreignKey = "PROPERTY_ID"
arcpy.CreateRelationshipClass_management(ownerTbl,
                                         parcel,
                                         relClass,
                                         "SIMPLE",
                                         forLabel,
                                         backLabel,
                                         "BACKWARD",
                                         "ONE_TO_MANY",
                                         "NONE",
                                         primaryKey,
                                         foreignKey)