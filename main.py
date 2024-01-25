

from Controller.tarrif_controller import TariController
from Controller.zone_conroller import ZoneController
from View.stations_screen import StationsScreen



def main():
    print("python main function")
    zone_provider = ZoneController(file_path= "Datasource/Storage/zones.json")
    tarif_provider = TariController(file_path= "Datasource/Storage/tarifs.json")
    staton_screen = StationsScreen(zones_provider=zone_provider)
    

    zones = zone_provider.get_zones_and_stations()
    print(zones)

if __name__ == '__main__':
    main()