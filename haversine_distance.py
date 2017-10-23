def haversine_distance(point1, point2, radius):
    """
    Calculates great-circle distance between two points on a sphere given their longtitudes and latitudes.
    https://en.wikipedia.org/wiki/Haversine_formula
    :param point1: tuple(latitude, longtitude) in degrees
    :param point2: tuple(latitude, longtitude) in degrees
    :param radius: radius in units
    :return: distance between two points in radius units
    Sample call:
    point1 = (37.8136, 144.9631)
    point2 = (33.8650, 151.2094)
    haversine_distance(point1, point2, 6371)
    """
    import math
    point1 = tuple(math.radians(deg) for deg in point1)
    point2 = tuple(math.radians(deg) for deg in point2)

    delta_latitude = point1[0] - point2[0]
    delta_longtitude = point1[1] - point2[1]

    a = math.sin(delta_latitude/2)**2 + math.cos(point1[0])*math.cos(point2[0])*math.sin(delta_longtitude/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c

    return d