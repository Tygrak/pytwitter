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
        output = "Time: {0} from {1}\n".format(str(self.time), str(self.time_zone))
        output += "Place: {0}, {1}, {2}\n".format(str(self.location), str(self.coordinates), str(self.place))
        output += "Language: {0}\n".format(str(self.language))
        output += "User: {0}, {1}, {2}\n".format(str(self.name), str(self.screenName), str(self.followers))
        output += "Text: {0}\n".format(str(self.text))
        output += "Source: {0}".format(str(self.source))
        return output