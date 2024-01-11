

from Controller.zone_provider import ZoneProvider



def main():
    print("python main function")
    zone_provider = ZoneProvider(file_name= "zones.json")
    zones = zone_provider.get_zones_and_stations()
    print(zones)

if __name__ == '__main__':
    main()