import arcpy

result = arcpy.management.CheckGeometry('c:/data/data.gdb/badgeometryfc')
if result[1] == 'true':
    # Geometry problems found, print the tool messages.
    print(result.getMessages())

else:
    # No problems found
    print("No problems Found")