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