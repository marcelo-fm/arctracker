# Name: CalculateField.py
# Description: Calculate the mean of the 3 most recent speed measurements in hurricane tracks

# Import system modules
import arcpy

arcpy.env.workspace = "C:/data/Weather.gdb"

# Set local variables
inFeatures = "Hurricanes"
fieldName = "MeanSpeed3"
out = "HurricaneTracks_Mean"
calcExpression = "Date($feature.DateAsString)"

# Run Calculate Field
arcpy.gapro.CalculateField(inFeatures, out, "NEW_FIELD", fieldName, "", "Date", 
                           calcExpression)