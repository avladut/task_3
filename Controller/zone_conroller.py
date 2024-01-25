import json
import numpy as np
from Model.zone import Zone
from Model.station import Station
import itertools

class ZoneController:
    def __init__(self, file_path):
        self.file_path = file_path
        # this should be somewhere else and async
        # for longer files it will get the mai thread stuck
        self.zones_and_stations = self.get_zones_and_stations()

    def get_zones_and_stations(self):
        try:
            with open(self.file_path) as f:
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
            return zones        
        except Exception as err2:
            print(err2)

    def get_formatted_stations(self):
        longest_row_count = self.get_longest_station_row()
        station_names = []
        for i in range(0, len(self.zones_and_stations)):
            stations_column = []

            stations_sorted = sorted(self.zones_and_stations[i].stations, key=lambda x: x.name)
            for j in range(0, longest_row_count):
                if j < len(self.zones_and_stations[i].stations):
                    stations_column.append(stations_sorted[j].name)
                else:
                    stations_column.append(" ")
            station_names.append(stations_column)

        # because symply py UI table requires a sinister format, the matrix needs transposing
        transposed_names = np.transpose(station_names)    

        # change from numpy list to normal list as required by table
        return transposed_names.tolist()           


    
    def get_zone_names(self):
        zone_names = []
        for zone in self.zones_and_stations:
            zone_names.append(zone.name)
        return zone_names    

    def get_longest_station_row(self):
        longest_stations_row = 0
        for zone in self.zones_and_stations:
            if len(zone.stations) > longest_stations_row:
                longest_stations_row = len(zone.stations)
        return longest_stations_row         





