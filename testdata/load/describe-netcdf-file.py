# Name: DescribeNetCDFFile.py  
# Description: Describe a NetCDF dataset.  

# Import system modules 
import arcpy 
 
# Set environment settings  
arcpy.env.workspace = "C:/data" 

# Set a variable 
in_netCDF_file = r"C:\example\airtemp.nc" 
out_file = r"C:\example\summary.md" 

# Run DescribeNetCDFFile 
arcpy.md.DescribeNetCDFFile(in_netCDF_file, out_file)