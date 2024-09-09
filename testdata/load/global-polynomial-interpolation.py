# Name: GlobalPolynomialInterpolation_Example_02.py
# Description: Global Polynomial interpolation fits a smooth surface that is
#              defined by a mathematical function (a polynomial) to the input 
#              sample points. The Global Polynomial surface changes gradually 
#              and captures coarse-scale pattern in the data.  Global Polynomial
#              interpolation is like taking a piece of paper and fitting it 
#              between the raised points (raised to the height of value).
# Requirements: Geostatistical Analyst Extension

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/gapyexamples/data"

# Set local variables
inPointFeatures = "ca_ozone_pts.shp"
zField = "ozone"
outLayer = "outGPI"
outRaster = "C:/gapyexamples/output/gpiout"
cellSize = 2000.0
power = 2

# Execute GlobalPolynomialInterpolation
arcpy.GlobalPolynomialInterpolation_ga(inPointFeatures, zField, outLayer, 
                                       outRaster, cellSize, power)