import datetime

arcpy.na.MakeLastMileDeliveryAnalysisLayer(
    r"C:\Data\SanFrancisco.gdb\Transportation\Streets_ND",
    "Package Delivery",
    "Trucking Time",
    time_units="Hours",
    earliest_route_start_date=datetime.date(2023, 11, 28),
    earliest_route_start_time=datetime.time(7, 30, 0),
    route_start_flexibility=1.5,
    line_shape="NO_LINES"
)