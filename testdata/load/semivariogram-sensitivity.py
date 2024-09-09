# Name: SemivariogramSensitivity_Example_02.py
# Description: The semivariogram parameters Nugget, Partial Sill and Range can
#   be varied to perform a sensitivity analysis.
# Requirements: Geostatistical Analyst Extension

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/gapyexamples/data"

# Set local variables
inLayer = "C:/gapyexamples/data/kriging.lyr"
inData = "C:/gapyexamples/data/ca_ozone_pts.shp OZONE"
inObs = "C:/gapyexamples/data/obs_pts.shp"
nugPercents = ""
nugCalc = ""
sillPercents = ""
sillCalc = ""
rangePercents = ""
rangeClac = ""
minrangePercent = ""
midrangeCalc = ""
outTable = "C:/gapyexamples/output/outtabSS"

# Execute SemivariogramSensitivity
arcpy.GASemivariogramSensitivity_ga(inLayer, inData, inObs, nugPercents, nugCalc,
                                    sillPercents, sillCalc, rangePercents, rangeClac,
                                    minrangePercent, midrangeCalc, outTable)