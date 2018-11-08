class tweetData:
    def __init__(self, time, text, language, time_zone, location, coordinates, place, followers, screenName, name, source):
        self.time = time
        self.text = text
        self.language = language
        self.time_zone = time_zone
        self.location = location
        self.coordinates = coordinates
        self.place = place
        self.followers = followers
        self.screenName = screenName
        self.name = name
        self.source = source
        
    def toString(self):
        return str(self.time) + "," + self.place + "," + self.coordinates