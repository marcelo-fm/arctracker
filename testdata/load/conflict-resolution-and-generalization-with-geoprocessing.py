# Name: cartography_workflow_script.py
# Description: Process features in order to resolve graphic conflicts when
# changing scales from 25K to 50K.
#
# Tools used = Aggregate Polygons, Align Marker To Stroke Or Fill, Apply
#              Symbology From Layer, Create Overpass, Create Underpass, Calculate
#              Line Caps, Eliminate Polygon Part, Make Feature Layer, Merge
#              Divided Roads, Propagate Displacement, Resolve Building Conflicts
#              Resolve Road Conflicts, Select, Select Layer By Attribute, Set
#              Control Point At Intersect, Set Control Point By Angle, Simplify 
#              Building, Simplify Line, Simplify Polygon, Smooth Line, Smooth 
#              Polygon, Thin Road Network
# Minimum ArcGIS Pro version = 2.1
#
# The geodatabase used in this workflow is assumed to be in c:\data
# - please replace this path to your machine specific folder.


# Import system modules
import arcpy

# Start the processing
arcpy.env.workspace = "C:/data/cartography.gdb"

# The data was captured at a scale of 1:24000, and this workflow will produce
# data appropriate for a scale of 1:50000.
# Most of the geoprocessing tools in this workflow require a reference scale
arcpy.env.referenceScale = "50000"
arcpy.env.cartographicCoordinateSystem = ""

###############
# HYDROGRAPHY #
###############

# A subset of linear features (rivers/streams) will be processed
# for simplification and smoothing
# A subset of polygonal features (reservoirs/lakes) will be processed
# for simplification and smoothing

# The workspace is set to the hydrography feature dataset
arcpy.env.workspace = "C:/data/cartography.gdb/hydrography"

# Linear hydrographic features
arcpy.MakeFeatureLayer_management("streamnetwork", "streamlayer", "", "", "")

# A selection is made for features which are rivers/streams
arcpy.SelectLayerByAttribute_management("streamlayer", "NEW_SELECTION",
                                        '"FCsubtype" = 1')

# In order to reduce the complexity from the streams, vertices are removed using
# the Simplify Line tool
arcpy.SimplifyLine_cartography("streamlayer", "streams_simplified",
                               "BEND_SIMPLIFY", "100 meters", "RESOLVE_ERRORS")

# In order to reduce the amount or severity of sharp angles, Smooth Line is used
# to improve the shape of the streams
arcpy.SmoothLine_cartography("streams_simplified", "streams",
                             "BEZIER_INTERPOLATION", "#", "0", 'FLAG_ERRORS')

# Some of the processed features are intermittent rivers or streams and are
# symbolized as dashed lines. The dashes can be centered around corners to 
# improve the look of the features. The corners are identified as vertices which 
# will be flagged as control points. Symbology from an existing layer containing
# dashed line symbols is then applied. 

# A new feature layer is created from the streams data to be used as input 
# when setting control points. 
arcpy.MakeFeatureLayer_management("streams", "streamslayer", "", "", "")

# Dashed line symbology from an existing layer is applied to the new streams 
# feature layer 
arcpy.ApplySymbologyFromLayer_management("streamslayer",
                                         "C:/data/stream_symbols.lyrx")

# The dashes in the stream symbol will be placed at control points created
# anywhere an angle is less than (or equal to) 130 degrees.
arcpy.SetControlPointByAngle_cartography("streamslayer", "130")

# Polygonal hydrographic features
# A selection is made to create a new feature class for reservoirs.
arcpy.Select_analysis("openwater", "reservoirs", '"FCsubtype" = 4')

# A selection is made to create a separate feature class for processing in order
# to generate lakes.
arcpy.Select_analysis("openwater", "water_select", '"FCsubtype" <> 4')

# In order to reduce the complexity from the lakes, vertices are removed using
# the Simplify Line tool.
arcpy.SimplifyPolygon_cartography("water_select", "water_simplified", 
                                  "BEND_SIMPLIFY", "100 meters", "0",
                                  "RESOLVE_ERRORS")

# In order to reduce the amount (or severity) of sharp angles, Smooth Line is
# used to improve the shape of the lakes.
arcpy.SmoothPolygon_cartography("water_simplified", "lakes",
                                "BEZIER_INTERPOLATION", "0", "", "FLAG_ERRORS")


#############
# RAILROADS #
#############

# Set the workspace to the transportation feature dataset
arcpy.env.workspace = "C:/data/cartography.gdb/transportation"
# In order to reduce the complexity from the railroads, vertices are removed 
# using the Simplify Line tool.
arcpy.SimplifyLine_cartography("railnetwork", "rail_simplified",
                               "BEND_SIMPLIFY", "100 meters", "RESOLVE_ERRORS")

# The Merge Divided Roads tool requires symbolized features, so a feature layer
# is created using the simplified rail features, and then pre-made symbology is 
# applied from an existing feature layer.

# A feature layer is created from the simplified rail features. 
arcpy.MakeFeatureLayer_management("rail_simplified", "railwaylayer", "", "", "")

# Apply the symbology from an existing layer
arcpy.ApplySymbologyFromLayer_management("railwaylayer",
                                         "C:/data/rail_symbols.lyrx")

# The Merge Divided Roads tool will be used to generates single line railroad
# features in place of multiple divided railroad lanes.
arcpy.MergeDividedRoads_cartography("railwaylayer", "level", "25 Meters",
                                    "railways")

# Symbolized features are required when adding control points, so a new feature
# layer is created from the output of the MergeDivvidedRoads tool.
arcpy.MakeFeatureLayer_management("railways", "railwayslayer", "", "", "")

# Pre-made railway symbology from an existing layer is applied to the 
# new railway feature layer.
arcpy.ApplySymbologyFromLayer_management("railwayslayer", 
                                         "C:/data/rail_symbols.lyrx")

# The tick marks in railroad symbol (markers) will be placed at control points
# created anywhere an angle is less than (or equal to) 130 degrees.
arcpy.SetControlPointByAngle_cartography("railwayslayer", "130")


###########
# LANDUSE #
###########

# Set the workspace to the landuse feature dataset
arcpy.env.workspace = "C:/data/cartography.gdb/landuse"
# The polygons which represent landcover have holes in them where buildings are
# located. The holes need to be removed so they will not appear after buildings
# have moved. In this example, any hole which is less than 50 percent of the 
# feature's area will be removed.
arcpy.EliminatePolygonPart_management("cultural", "urban_area", "PERCENT", "0",
                                      "50", "CONTAINED_ONLY")


##############
# BOUNDARIES #
##############

# The boundary features have dashed outlines which are not in phase with each
# other on shared edges between features. To make the dashed outlines in phase
# with each other, control points are added wherever features 
# share coincident vertices.
arcpy.SetControlPointAtIntersect_cartography("C:/data/boundaries.lyrx", 
                                             "C:/data/boundaries.lyrx")


#########
# ROADS #
#########

# Set the workspace to the transportation feature dataset
arcpy.env.workspace = "C:/data/cartography.gdb/transportation"
# Linear features

# Roads which are dead ends (or cul-de-sacs) should have their Line ending
# property set to BUTT.
arcpy.CalculateLineCaps_cartography("C:/data/road_symbols.lyrx", "BUTT",
                                    "CASED_LINE_DANGLE")

# Thin Road Network identifies a subset of road segments that can be removed from
# the display to create a simplified road network that retains the connectivity 
# and general character of the input collection. Features are flagged for removal
# when their attribute value in the "invisible" field equals one. A layer
# definition query can be used to display the resulting simplified feature class.
arcpy.ThinRoadNetwork_cartography("roadnetwork", "500 meters", "invisible",
                                  "level")

# The Merge Divided Roads tool will be used to generates single line road
# features in place of multiple divided road lanes.
arcpy.MergeDividedRoads_cartography("C:/data/road_symbols.lyrx", "level",
                                    "25 meters", "roads")

# The Resolve Road Conflicts tool requires symbolized features, so a feature
# layer is created from the roads features so that pre-made
# symbology can the be applied to the new roads feature layer.
arcpy.MakeFeatureLayer_management("roads", "roadslayer", "", "", "")

# Pre-made symbology from an existing layer is applied to the roads feature 
# layer.
arcpy.ApplySymbologyFromLayer_management("roadslayer",
                                         "C:/data/road_symbols.lyrx")

# The Resolve Road Conflicts tool does not produce output road layers but instead
# alters the source feature classes of the input road layers. The Resolve Road
# Conflicts tool adjusts line features to ensure that they are graphically
# distinguishable when symbolized at output scale.
arcpy.ResolveRoadConflicts_cartography
("roadslayer", "level", "C:/data/cartography.gdb/buildings/displacement")

# The dashes in the road symbols will be placed at control points created
# anywhere an angle is less than (or equal to) 130 degrees.
arcpy.SetControlPointByAngle_cartography("roadslayer", "130")

# Create bridges
# The Create Overpass tool will create a bridge for the roads and a mask for the
# streams wherever a road goes over a steam.
arcpy.CreateOverpass_cartography("roadslayer", "streamslayer", "2 points",
                                 "1 points", "over_mask_fc", "over_mask_rc",
                                 '"BridgeCategory" = 1', "bridges",
                                 "ANGLED", "1 points")

# Create tunnels
# The Create Overpass tool will create a tunnel for the railroads and a mask for
# the railroads wherever a railroad goes under a road.
arcpy.CreateUnderpass_cartography("roadslayer", "railwayslayer", "2 points",
                                  "1 points", "under_mask_fc", "under_mask_rc",
                                  '"RelationshipToSurface" = 3', "tunnels",
                                  "ANGLED", "1 points")


#############
# BUILDINGS #
#############

# Set the workspace to the buildings feature dataset
arcpy.env.workspace = "C:/data/cartography.gdb/buildings"
# Point features

# When the road features were adjusted by the Resolve Road Conflicts tool, the
# spatial relationship with nearby buildings was affected. A displacement feature
# class was created by that tool in order to record the change applied to the
# roads. This information can be used by the Propagate Displacement tool to apply
# the same change to the point buildings.

# The road displacement is propagated to the point buildings
arcpy.PropagateDisplacement_cartography("point_bldg", "displacement", "AUTO")

# Point buildings will be rotated against nearby linear roads
# The Align Markers To Stroke Or Fill tool can do this with symbolized features.

# A feature layer is made for point buildings
arcpy.MakeFeatureLayer_management("point_bldg", "bldglayer", "", "", "")

# Symbology is applied from an existing layer.
arcpy.ApplySymbologyFromLayer_management("bldglayer", 
                                         "C:/data/bldg_symbols.lyrx")

# The Align Marker to Stroke Or Fill tool is used to align point buildings to
# face road features within 5 points of the buildings
arcpy.AlignMarkerToStrokeOrFill_cartography("bldglayer", "roadslayer",
                                            "5 points", "PERPENDICULAR")

# Polgyonal features
# When the road features were adjusted by the Resolve Road Conflicts tool, the
# spatial relationship with nearby buildings was affected. A displacement
# feature class was created by that tool in order to record the change applied
# to the roads. This information can be used by the Propagate Displacement tool
# to apply the same change to the polygonal buildings.

# The road displacement is propagated to polygon buildings
arcpy.PropagateDisplacement_cartography("footprints", "displacement", "SOLID")

# A selection is made to create a feature class with buildings larger than
# a minimum size
# The small buildings are not appropriate at the new map scale of 1:50,000
arcpy.Select_analysis("footprints", "buildings_select", '"Shape_Area" > 100')

# There is a need to create better spacing between polygon buildings and combine
# them when they share edges or are very close together
# The Aggregate Polygons tool is used to accomplish this task
arcpy.AggregatePolygons_cartography("buildings_select", "large_buildings",
                                    "20 meters", "", "", "ORTHOGONAL")

# In order to reduce the complexity of the buildings, indentations, extensions
# and extra vertices are removed using the Simplify Building tool.
# Buildings require less visible detail at the new scale of 1:50,000.
arcpy.SimplifyBuilding_cartography("large_buildings", "area_bldg", "20 meters",
                                   "0 unknown", "CHECK_CONFLICTS")

# All buildings require further improvements to achieve better spacing between
# themselves and other nearby features. At the new scale of 1:50,000 the
# symbolized buildings may overlap other features and create a visually congested
# map. To improve the visual congestion, the Resolve Building Conflicts tool is
# used. Buildings are improved in the context of their surrounding features.
# These features are considered barriers to buildings. The Resolve Building
# Conflicts tool requires symbolized features and has several options available
# to improve the buildings. Options include: moving or resizing the buildings,
# orienting or snapping the buildings to nearby features, as well as making the
# buildings invisible. Buildings from multiple feature classes can be used as
# inputs to the tool. Barriers from multiple feature classes can be used as
# inputs to the tool. For each barrier, the option is available to specify a snap
# or orient action for the buildings when they are within a specified distance.
# For each barrier, the option is available to specify a minimum distance for
# buildings to maintain between them.

# A feature layer is made for the polygon buildings
arcpy.MakeFeatureLayer_management("area_bldg", "footprintlayer", "", "", "")

# Pre-made symbology is applied from an existing layer.
arcpy.ApplySymbologyFromLayer_management("footprintlayer",
                                         "C:/data/footprint_symbols.lyrx")

# The Resolve Building Conflicts tool is run with point and polygon buildings
# against roads, streams and railroads. The buildings will be moved away from
# streams and railroads until they reach a minimum distance. The buildings
# within a maximum distance from the roads will be rotated. Further movement
# and rotation may still be required by the tool in order to resolve any
# remaining graphic conflict.
arcpy.ResolveBuildingConflicts_cartography("footprintlayer; bldglayer", "invisible",
                                           "'roadslayer' 'true' '5 meters';'streamslayer' 'false' '5 meters';'railwayslayer' 'false' '10 meters'",
                                           "10 meters", "20 meters", "level")