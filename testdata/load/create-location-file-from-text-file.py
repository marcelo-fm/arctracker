# Name: CreateLocationFileFromTextFile.py
# Description: Create a custom location file for use with LocateXT. 

# Import system modules 
import arcpy 

source_file = r'C:\data\US.txt'
data_source = 'GEONAMES'
location_file = r'C:\data\US.lxtgaz'
filter_features = ['POPULATED_PLACES']
loudoun_county = r'C:\virginia.gdb\loudoun_co'

arcpy.intelligence.CreateLocationFileFromTextFile(source_file,
                                                  data_source,
                                                  location_file,
                                                  filter_features,
                                                  loudoun_county)