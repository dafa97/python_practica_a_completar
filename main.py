import sys
sys.path.append("..")
import os
import pandas as pd
from entities.aeropuerto import Aeropuerto
from entities.lector import LectorTXT, LectorCSV, LectorJSON


def preprocess_data(df_list):
    df_ = pd.concat(df_list)
    df_["fecha_llegada"] = df_["fecha_llegada"].apply(lambda x: x.replace('T', ' '))
    df_["fecha_llegada"] = pd.to_datetime(df_["fecha_llegada"])
    return df_




if __name__ == '__main__':
    path_1 = os.path.abspath('./data/vuelos_1.txt')
    path_2 = os.path.abspath('./data/vuelos_2.csv')
    path_3 = os.path.abspath('./data/vuelos_3.json')

    lector_1 = LectorTXT(path_1)
    lector_2 = LectorCSV(path_2)
    lector_3 = LectorJSON(path_3)

    d = lector_1.lee_archivo()
    df1 = lector_1.convierte_dict_a_csv(d)
    
    
    df2 = lector_2.lee_archivo()
    
    d= lector_3.lee_archivo()
    df3 = lector_3.convierte_dict_a_csv(d)
    
    df_list = [df1,df2,df3]
    df = preprocess_data(df_list)


    aeropuerto = Aeropuerto(df, 4, 60, 100)
    aeropuerto.asigna_slots()





