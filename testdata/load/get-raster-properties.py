import arcpy
#Get the geoprocessing result object
elevSTDResult = arcpy.GetRasterProperties_management("c:/data/elevation", "STD")
#Get the elevation standard deviation value from geoprocessing result object
elevSTD = elevSTDResult.getOutput(0)