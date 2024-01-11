import json
from Model.zone import Zone

class ZoneProvider:
    def __init__(self, file_name):
        self.file_name = "zones.json"

    def get_zones_and_stations(self):
        try:
            f = open(self.file_name)
            data = json.load(f)

        except:
            print("error opening file or loading json")

        try:
            zones = []
            zone_list = data["zones"]
            for zone in zone_list:
                zone_model = Zone(zone)
                if zone_model != None:
                    zones.append(zone_model)
            return zone_list        
        except:
            print("error parsing json data")      

        f.close()      
