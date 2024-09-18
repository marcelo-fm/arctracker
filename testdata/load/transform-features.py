import arcpy
import os

# Set environment settings
arcpy.env.overwriteOutput = True

# Function to convert link info in a text file to a line feature class
def CreateLinkFeatures(in_text_file, in_data):

    sr = arcpy.Describe(in_data).spatialReference
    features = []  # a list to hold polyline geometry objects

    f = open(in_text_file, "r")
    
    for line in f.readlines():

        # Take start/end blank spaces off
        # Separate the start and end point coordinates
        points = line.strip().split()   
        
        point1 = arcpy.Point(float(points[1]), float(points[2]))
        point2 = arcpy.Point(float(points[3]), float(points[4]))
        
        features.append(arcpy.Polyline(arcpy.Array([point1, point2]), sr))
        
    f.close()   # close the text file

    # Copy the geometry objects into a feature class named Links
    result = arcpy.management.CopyFeatures(features, in_data + "_links")

    return result[0]
    
if __name__ == "__main__":

    # Make a copy of the data because
    # TransformFeatures tool modifies the input data
    arcpy.management.CopyFeatures(r"C:\data\Tutorial.gdb\Parcels", r"C:\data\Tutorial.gdb\Parcels_copy")

    links_file = r"C:\data\TF_links.txt"
    tf_link_features = CreateLinkFeatures(links_file, r"C:\data\Tutorial.gdb\Parcels")
    
    arcpy.edit.TransformFeatures(r"C:\data\Tutorial.gdb\Parcels_copy", tf_link_features)
    print(arcpy.GetMessages())