# Name: IDW3D_Example_02.py
# Description: Creates a voxel layer source file from interpolated 3D points.
# Requirements: Geostatistical Analyst Extension
# Author: Esri



# Import system modules
import arcpy

# Allow overwriting output
arcpy.env.overwriteOutput = True

# Define 3D input points and value field to be interpolated
in3DPoints = "C:/gapydata/inputs.gdb/myOxygenPoints3D"
valueField = "OxygenValue"
outNetCDF = "C:/gapydata/outputs/OxygenMeasurementsVoxel.nc"
outCVFeatureClass = "C:/gapydata/outputs/outputCrossValidationErr.shp"

# Define power of IDW and elevation inflation factor
powerValue = "2"
elevInflation = ""

# Define voxel dimensions
xSpacing = "50 Meters"
ySpacing = "50 Meters"
elevSpacing = "5 Meters"


# Define study area, minimum clipping raster layer, and maximum clipping elevation layer
studyArea = "C:/gapydata/inputs.gdb/StudyAreaPolygon"
minElevRaster = "C:/gapydata/inputs.gdb/MinElevationClippingRaster"
maxElevRaster = "C:/gapydata/inputs.gdb/MaxElevationClippingRaster"

# Define the neighborhood
radius = ""
maxNeighbors = 2
minNeighbors = 1
sectorType = "TWELVE_SECTORS"
searchNeighborhood = arcpy.SearchNeighborhoodStandard3D(radius, maxNeighbors,
                     minNeighbors, sectorType)



# Check out the ArcGIS Geostatistical Analyst extension license
arcpy.CheckOutExtension("GeoStats")

# Execute Nearest Neighbor 3D
arcpy.ga.IDW3D(in3DPoints, valueField,outNetCDF,
                           powerValue, elevInflation, outCVFeatureClass,
                           xSpacing, ySpacing, elevSpacing,
                           studyArea, minElevRaster,
                           maxElevRaster, searchNeighborhood)

# Print messages
print(arcpy.GetMessages())