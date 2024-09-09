# Name: TableToRelationshipClass.py
# Description: Create an attributed relationship class between parcels
#              feature class and table with owner information
# Author: ESRI

# import system modules 
import arcpy
from arcpy import env

# Set environment settings
env.workspace = "C:/data"

# Copy owners.dat to file gdb table, since both tables to be related
# must be in the same database
ownerDat = "owners.dat"
ownerTbl = "Montgomery.gdb/owners"
arcpy.CopyRows_management(ownerDat, ownerTbl)

# Create attributed relationship class between 'parcel' parcel layer
# and 'owner' table with additional parcel owner information
parcel = "Montgomery.gdb/Parcels"
relClass = "Montgomery.gdb/parcelowners_RelClass"
forLabel = "Owns"
backLabel = "Is Owned By"
attributeFields = ["OWNER_PERCENT", "DEED_DATE"]
originPK = "OBJECTID"
originFK = "owner_ID"
destinationPK = "OBJECTID"
destinationFK = "parcel_ID"
arcpy.TableToRelationshipClass_management(ownerTbl, parcel, relClass, "SIMPLE",
                                          forLabel, backLabel, "BACKWARD", "MANY_TO_MANY",
                                          ownerTbl, attributeFields, originPK, originFK,
                                          destinationPK, destinationFK)