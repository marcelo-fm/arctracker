# Name: GALayer3DToMDR_Example_02.py
# Description: Interpolates 3D points and exports to a multidimensional raster dataset.
# Requirements: Geostatistical Analyst Extension
# Author: Esri

# Import system modules
import arcpy

# Set local variables
in3DPoints = "C:/gapyexamples/input/my3DPoints.shp"
elevationField = "Shape.Z"
valueField = "myValueField"
outGALayer = "myGALayer"


# Check out the ArcGIS Geostatistical Analyst extension license
arcpy.CheckOutExtension("GeoStats")

# Execute Empirical Bayesian Kriging 3D
arcpy.ga.EmpiricalBayesianKriging3D(in3DPoints, elevationField, valueField, outGALayer)


# Export predictions and standard errors to multidimensional raster with tranposes.

# Set up variables
outMDRaster = r"C:\\gapydata\\outputMDRD.crf"
explicitVals = "NO_EXPLICIT_VALUES"
cell_size = 1000
min_elev = 0
max_elev = 500
elev_interval = 50
elev_list = ""
elev_units = "METERS"
out_type = "PREDICTION"
quan_value = ""
add_outputs = [["PREDICTION_STANDARD_ERROR",""]]
transpose = "BUILD_TRANSPOSE"

# Additionally output prediction standard errors.
arcpy.ga.GALayer3DToMultivariateRaster(outGALayer, outMDRaster, cell_size, explicitVals,
                                       min_elev, max_elev, elev_interval, elev_list,
                                       elev_units, out_type, quan_value, add_outputs,
                                       transpose)