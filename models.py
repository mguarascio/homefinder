import math


class Town:
    def __init__(self, regionid, name, county, avgprice, url, latitude, longitude):
        self.regionid = regionid
        self.name = name
        self.county = county
        self.avgprice = avgprice
        self.url = url
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return repr((self.regionid, self.name, self.county, self.avgprice, self.url, self.latitude, self.longitude))


class CostFilter:
    """
    filter = CostFilter('cost', 0.5)
    score = filter.score(450000, 600000)
    # score is 2.25
    """
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def score(self, cost, maxavgprice):
        if (cost > maxavgprice):
            return 0
        return self.weight * (cost / 100000)


class CommuteFilter:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    '''
      http://www.johndcook.com/python_longitude_latitude.html
    '''
    def calcDistance(self, lat1, long1, lat2, long2):
        # Convert latitude and longitude to
        # spherical coordinates in radians.
        degrees_to_radians = math.pi / 180.0

        # phi = 90 - latitude
        phi1 = (90.0 - lat1) * degrees_to_radians
        phi2 = (90.0 - lat2) * degrees_to_radians

        # theta = longitude
        theta1 = long1*degrees_to_radians
        theta2 = long2*degrees_to_radians

        # Compute spherical distance from spherical coordinates.
            
        # For two locations in spherical coordinates 
        # (1, theta, phi) and (1, theta, phi)
        # cosine( arc length ) = 
        #    sin phi sin phi' cos(theta-theta') + cos phi cos phi'
        # distance = rho * arc length
        
        cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) + 
               math.cos(phi1)*math.cos(phi2))
        arc = math.acos( cos )

        # Remember to multiply arc by the radius of the earth 
        # in your favorite set of units to get length.
        return arc*3960

    def score(self, lat1, long1, lat2, long2):
        distance = self.calcDistance(lat1, long1, lat2, long2) # get distance in miles from locations
        return self.weight*distance

class SchoolFilter:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def score(self, school):
        rating = 1 # lookup school rating
        return self.weight*rating
