# Name: GALayer3DToNetCDF_Example_02.py
# Description: Interpolates 3D points and exports to a netCDF file.
# Requirements: Geostatistical Analyst Extension
# Author: Esri

# Import system modules
import arcpy

# Allow overwriting output
arcpy.env.overwriteOutput = True

# Set up variables
in3DPoints1 = "C:/gapydata/inputs.gdb/my3DPoints1"
in3DPoints2 = "C:/gapydata/inputs.gdb/my3DPoints2"
elevationField1 = "Shape.Z"
elevationField2 = "Shape.Z"
valueField1 = "myValueField1"
valueField2 = "myValueField2"
outGALayer1 = "myGALayer1"
outGALayer2 = "myGALayer2"


# Check out the ArcGIS Geostatistical Analyst extension license
arcpy.CheckOutExtension("GeoStats")

# Execute Empirical Bayesian Kriging 3D twice
arcpy.ga.EmpiricalBayesianKriging3D(in3DPoints1, elevationField1, valueField1, outGALayer1)
arcpy.ga.EmpiricalBayesianKriging3D(in3DPoints2, elevationField2, valueField2, outGALayer2)


# Export predictions for first model and probability that second model exceeds 10
# Export to gridded 3D points

# Set up variables
in_3d_ga_layers = outGALayer1+";"+outGALayer2
out_ncdf = "C:/gapydata/outputs/outputNetCDF1.nc"
export_locations = "3D_GRIDDED_POINTS"
x_spacing = "50 Meters"
y_spacing = "50 Meters"
elev_spacing = "5 Meters"
custom_points = ""
out_vars = "myGALayer1 PREDICTION #;myGALayer2 PROBABILITY 10"

# Run tool.
arcpy.ga.GALayer3DToNetCDF(in_3d_ga_layers, out_ncdf, export_locations,
                           x_spacing, y_spacing, elev_spacing, custom_points, out_vars)


# Export standard errors for first model and 75th quantile for second model
# Export to custom 3D points

# Set up variables
in_3d_ga_layers = outGALayer1+";"+outGALayer2
out_ncdf = "C:/gapydata/outputs/outputNetCDF2.nc"
export_locations = "CUSTOM_3D_POINTS"
x_spacing = ""
y_spacing = ""
elev_spacing = ""
custom_points = "C:/gapydata/inputs.gdb/myCustom3DPoints"
out_vars = "myGALayer1 PREDICTION_STANDARD_ERROR #;myGALayer2 QUANTILE 0.75"

# Run tool.
arcpy.ga.GALayer3DToNetCDF(in_3d_ga_layers, out_ncdf, export_locations,
                           x_spacing, y_spacing, elev_spacing, custom_points, out_vars)