import json
from Model.tarif import Tarif

class TariController:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_tarifs(self):
        try:
            with open(self.file_path) as f:
                data = json.load(f) 

        except Exception as err:
            print("error opening file or loading json" + err)

        try:
            tarifs = []
            print (f'data is {data}')
            tarif_list = data["tarifs"]
            for tarif in tarif_list:
                tarif_model = Tarif(tarif)
                if tarif_model != None:
                    tarifs.append(tarif_model)
            return tarifs        
        except Exception as err2:
            print(err2)