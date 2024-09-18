# MakeQueryTableOLEDB.py
# Description: Create a query table from two OLE DB tables using a limited set of
#               fields and establishing an equal join.
 
# Import system modules
import arcpy
 
# Local variables...
tableList = ["c:/Connections/balrog.odc/vtest.COUNTIES",\
             "c:/Connections/balrog.odc/vtest.CODEMOG"]

fieldList = [["vtest.COUNTIES.OBJECTID", 'ObjectID'], ["vtest.COUNTIES.NAME", 'Name']\
             ["vtest.CODEMOG.Males", 'Males'], ["vtest.CODEMOG.Females", 'Females']]
whereClause = "vtest.COUNTIES.FIPS = vtest.CODEMOG.Fips" +\
              "and vtest.COUNTIES.STATE_NAME = 'California'"
keyField = "vtest.COUNTIES.OBJECTID"
lyrName = "CountyCombined"

# Make Query Table...
arcpy.management.MakeQueryTable(tableList, lyrName,"USE_KEY_FIELDS", keyField, fieldList, whereClause)

# Print the total rows
print(arcpy.management.GetCount(lyrName))
 
# Print the fields
fields = arcpy.ListFields(lyrName)
for field in fields:
    print(field.name)

# Save as a dBASE file
arcpy.management.CopyRows(lyrName, "C:/temp/calinfo.dbf")