import json
from Model.zone import Zone

class ZoneProvider:
    def __init__(self, file_name):
        self.file_name = "zones.json"

    def get_zones_and_stations(self):
        try:
            with open(r'Datasource/Storage/zones.json') as f:
                data = json.load(f) 

        except Exception as err:
            print("error opening file or loading json" + err)

        try:
            zones = []
            print (f'data is {data}')
            zone_list = data["zones"]
            for zone in zone_list:
                zone_model = Zone(zone)
                if zone_model != None:
                    zones.append(zone_model)
            return zone_list        
        except Exception as err2:
            print(err2)

             
