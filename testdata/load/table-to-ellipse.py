# Import system modules
import arcpy

# Set local variables
input_table = r'c:\workspace\SGS\eltop.gdb\elret'
output_ellipse = r'c:\workspace\SGS\eltop.gdb\Eplyln_001'

# Run Table To Ellipse
arcpy.management.TableToEllipse(input_table, output_ellipse, 'lond', 'latd', 
                                'mjerr', 'mnerr', 'KILOMETERS', 'orient', 
                                'DEGREES', 'LinkID')