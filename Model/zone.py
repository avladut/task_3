from Model.station import Station


class Zone:
    def __init__(self, dict):
        try:
            self.name = dict["zone_name"]
            self.order = dict["order"]
            
            stations_from_dictionary = []
            for stationName in dict["stations"]:
                newStation = Station(stationName)
                stations_from_dictionary.append(newStation)
            self.stations = stations_from_dictionary
        except Exception as err:
            print(f'something went wrong initialising a Zone with args: {dict} and error: {err}')
        
