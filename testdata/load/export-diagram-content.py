import arcpy
arcpy.ExportDiagramContent_nd('elec Network', 'Basic_RMT003', 
                              'C:\temp\BasicRMT003.json', 
                              'INCLUDE_DIAGRAM_PROPERTIES', 'INCLUDE_GEOMETRIES', 
                              'INCLUDE_ATTRIBUTES', 'INCLUDE_AGGREGATIONS', 
                              'USE_CODED_VALUE_NAMES')