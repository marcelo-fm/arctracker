# Import system modules
import arcpy
 
# Set environment settings
arcpy.env.workspace = 'C:\\data'

# Run CopyRuntimeGdbToFileGdb
arcpy.conversion.MobileGdbToFileGdb('D:\\MobileData\\replica.geodatabase', 
                                    'replica_Copy.gdb')