class Town:
    self.scores = []

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

'''
 filter = CostFilter('cost', 0.5)
 score = filter.score(450000, 600000)
 # score is 2.25
'''
class CostFilter:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def score(cost, maxavgprice):
        if (cost > maxavgprice):
            return 0
        return self.weight*(cost/100000)

class CommuteFilter:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def score(workZip, homeZip):
        distance = 1 # get distance in miles from locations
        return self.weight*distance

class SchoolFilter:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def score(school):
        rating = 1 # lookup school rating
        return self.weight*rating