from Model.station import Station


class Zone:
    def __init__(self, dict):
        try:
            self.name = dict["zone_name"]
            self.order = dict["order"]
            self.stations = []
            for stationName in dict["stations"]:
                self.stations.append[Station(stationName)]
        except:
            print("something went wrong initialising a Zone with args: " + dict)    
        
