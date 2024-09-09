"""*********************************************************************
Name: Model Shadows For GeoVRML Models
Description: Creates a model of the shadows cast by GeoVRML models
             imported to a multipatch feature class for a range of dates
             and times. A range of times from the start time and end
             time can also be specified by setting the EnforceTimes
             Boolean to True. This sample is designed to be used in a
             script tool.
*********************************************************************"""

# Import system modules
import arcpy
from datetime import datetime, time, timedelta

# *************************  Script Variables  **************************
inFiles = arcpy.GetParameterAsText(0)  # list of input features
spatialRef = arcpy.GetParameterAsText(1)  # list of GeoVRML files
outFC = arcpy.GetParameterAsText(2)  # multipatch from 3D files
inTimeZone = arcpy.GetParameterAsText(3)  # time zone
startDate = arcpy.GetParameter(4)  # starting date as datetime
endDate = arcpy.GetParameter(5)  # ending date as datetime
dayInterval = arcpy.GetParameter(6)  # day interval as long (0-365)
minInterval = arcpy.GetParameter(7)  # minute interval as long (0-60)
enforceTime = arcpy.GetParameter(8)  # minute interval as Boolean
outShadows = arcpy.GetParameterAsText(9)  # output shadow models
outIntersection = arcpy.GetParameterAsText(10)  # shadow & bldg intersection


# Function to find all possible date/time intervals for shadow modelling
def time_list():
    dt_result = [startDate]
    if dayInterval:
        if endDate:  # Defines behavior when end date is supplied
            while startDate < endDate:
                startDate += timedelta(days=dayInterval)
                dt_result.append(startDate)
            dt_result.append(endDate)
        else:  # Behavior when end date is not given
            daymonthyear = datetime.date(startDate)
            while startDate <= datetime(daymonthyear.year, 12, 31, 23, 59):
                startDate += timedelta(days=dayInterval)
                dt_result.append(startDate)
    return dt_result


importFC = arcpy.CreateUniqueName("geovrml_import", "in_memory")

# Import GeoVRML files to in-memory feature
arcpy.ddd.Import3DFiles(
    inFiles, importFC, "ONE_FILE_ONE_FEATURE", spatialRef, "Z_IS_UP", "wrl"
)

# Ensure that building models are closed
arcpy.ddd.EncloseMultiPatch(importFC, outFC, 0.05)

# Discard in-memory feature
arcpy.management.Delete(importFC)
dt_result = time_list()
for dt in dt_result:
    if dt == dt_result[0]:
        shadows = outShadows
    else:
        shadows = arcpy.CreateUniqueName("shadow", "in_memory")
    arcpy.ddd.SunShadowVolume(
        outFC, dt, shadows, "ADJUST_FOR_DST", inTimeZone, "", minInterval, "MINUTES"
    )
    if dt is not dt_result[0]:
        arcpy.management.Append(shadows, outShadows)
        arcpy.management.Delete(shadows)
arcpy.ddd.Intersect3D(outFC, outIntersection, outShadows, "SOLID")
