import pandas as pd
import json
import os.path

class Lector:
    def __init__(self, path: str):
        self.path = path

    def _comprueba_extension(self, extension):
        file_extension = os.path.splitext(self.path)[1]
        if file_extension != extension:
            raise Exception("Extension incorrecta")
        
        else:
            return True

    def lee_archivo(self):
        pass

    @staticmethod
    def convierte_dict_a_csv(data: dict):
        x = pd.DataFrame.from_dict(data)
        return x


class LectorCSV(Lector):
    
    def lee_archivo(self, datetime_columns=[]):
        x = None
        if super()._comprueba_extension(".csv"):
            x = pd.read_csv(self.path)
        return x


class LectorJSON(Lector):

    def lee_archivo(self):
        x = None
        if super()._comprueba_extension(".json"):

            with open(self.path, 'r', encoding= "utf-8") as file:
                x = json.load(file)
        return x


class LectorTXT(Lector):
 
    def lee_archivo(self):
        if super()._comprueba_extension(".txt"):
            with open(self.path, 'r', encoding="utf-8") as file:
                cabecera = file.readline().strip().split(", ")
                data = []
                for linea in file:
                    valores = linea.strip().split(", ")
                    registro = {cabecera[i]: valores[i] for i in range(len(cabecera))}
                    data.append(registro)
            return data
 
        




