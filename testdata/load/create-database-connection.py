# Name: CreateDatabaseConnection4.py
# Description: Connects to a point in time in the geodatabase in
#              PostgreSQL using database authentication.

# Import system modules
import arcpy

# Run the tool
arcpy.CreateDatabaseConnection_management("C:\\MyProject",
                                          "history.sde",
                                          "POSTGRESQL",
                                          "dbserver",
                                          "DATABASE_AUTH",
                                          "stevie",
                                          "smith",
                                          "SAVE_USERNAME",
                                          "archivedb",
                                          "#",
                                          "POINT_IN_TIME",
                                          "#",
                                          "5/19/2011 8:43:41 AM")