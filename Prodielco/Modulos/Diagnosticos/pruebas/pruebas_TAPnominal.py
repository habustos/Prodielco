import pandas as pd
#import numpy as np
import operator

"""
TAPnominal = int(input("Posición del TAP Nominal"))
#TAPnominal = 4
Voltio_TAP_nominal = 11400
Porcentaje = 0.025


class VariacionTAPnominal():
    if TAPnominal == 1:
        V_TAP_1 = Voltio_TAP_nominal
        V_TAP_2 = Voltio_TAP_nominal-(Voltio_TAP_nominal*Porcentaje)
        V_TAP_2 = round(V_TAP_2)
        V_TAP_3 = V_TAP_2-(Voltio_TAP_nominal*Porcentaje)
        V_TAP_3 = round(V_TAP_3)
        V_TAP_4 = V_TAP_3-(Voltio_TAP_nominal*Porcentaje)
        V_TAP_4 = round(V_TAP_4)
        V_TAP_5 = V_TAP_4-(Voltio_TAP_nominal*Porcentaje)
        V_TAP_5 = round(V_TAP_5)

        print(V_TAP_1)
        print(V_TAP_2)
        print(V_TAP_3)
        print(V_TAP_4)
        print(V_TAP_5)

    elif TAPnominal == 2:
        V_TAP_1 = Voltio_TAP_nominal + (Voltio_TAP_nominal * Porcentaje)
        V_TAP_1 = round(V_TAP_1)
        V_TAP_2 = Voltio_TAP_nominal
        V_TAP_3 = V_TAP_2 - (Voltio_TAP_nominal * Porcentaje)
        V_TAP_3 = round(V_TAP_3)
        V_TAP_4 = V_TAP_3 - (Voltio_TAP_nominal * Porcentaje)
        V_TAP_4 = round(V_TAP_4)
        V_TAP_5 = V_TAP_4 - (Voltio_TAP_nominal * Porcentaje)
        V_TAP_5 = round(V_TAP_5)

        print(V_TAP_1)
        print(V_TAP_2)
        print(V_TAP_3)
        print(V_TAP_4)
        print(V_TAP_5)

    elif TAPnominal == 3:
        V_TAP_1 = Voltio_TAP_nominal + (Voltio_TAP_nominal*(Porcentaje*2))
        V_TAP_1 = round(V_TAP_1)
        V_TAP_2 = Voltio_TAP_nominal + (Voltio_TAP_nominal * Porcentaje)
        V_TAP_2 = round(V_TAP_2)
        V_TAP_3 = Voltio_TAP_nominal
        V_TAP_4 = V_TAP_3 - (Voltio_TAP_nominal * Porcentaje)
        V_TAP_4 = round(V_TAP_4)
        V_TAP_5 = V_TAP_4 - (Voltio_TAP_nominal * Porcentaje)
        V_TAP_5 = round(V_TAP_5)

        print(V_TAP_1)
        print(V_TAP_2)
        print(V_TAP_3)
        print(V_TAP_4)
        print(V_TAP_5)

    elif TAPnominal == 4:
        V_TAP_1 = Voltio_TAP_nominal + (Voltio_TAP_nominal * (Porcentaje * 3))
        V_TAP_1 = round(V_TAP_1)
        V_TAP_2 = Voltio_TAP_nominal + (Voltio_TAP_nominal*(Porcentaje*2))
        V_TAP_2 = round(V_TAP_2)
        V_TAP_3 = Voltio_TAP_nominal + (Voltio_TAP_nominal * Porcentaje)
        V_TAP_3 = round(V_TAP_3)
        V_TAP_4 = Voltio_TAP_nominal
        V_TAP_5 = V_TAP_4 - (Voltio_TAP_nominal * Porcentaje)
        V_TAP_5 = round(V_TAP_5)


        print(V_TAP_1)
        print(V_TAP_2)
        print(V_TAP_3)
        print(V_TAP_4)
        print(V_TAP_5)


"""
class Resistencia_aislamiento():

    ejecucion = ["INICIAL", "FINAL", "INICIAL", "FINAL", "INICIAL", "FINAL"]
    AT_BT_T = ["AT-BT", "AT-BT", "AT-T", "AT-T", "AT-T", "BT-T"]
    segundo_15 = [0,164000,0,11700,0,67100]
    segundo_30 = [0,228000,0,12000,0,79800]
    minuto_1 = [0,311000,0,12100,0,84600]
    minuto_2 = [0,523000,0,12000,0,93000]
    minuto_3 = [0,693000,0,12200,0,90200]
    minuto_4 = [0,835000,0,12200,0,118000]
    minuto_5 = [0,964000,0,12400,0,134000]
    minuto_6 = [0,1120000,0,12500,0,157000]
    minuto_7 = [0,1230000,0,12800,0,169000]
    minuto_8 = [0,1310000,0,12900,0,182000]
    minuto_9 = [0,1400000,0,12900,0,195000]
    minuto_10 = [0,1450000,0,13100,0,213000]
    #indice_absorcion = []
    #indice_polaridad = []

    Transformador = [123]

    valores_temperatura_mohms = {"ejecucion": ejecucion,
                                 "AT_BT_T": AT_BT_T,
                                                 "segundo_15": segundo_15,
                                                 "segundo_30": segundo_30,
                                                 "minuto_1": minuto_1,
                                                 "minuto_2": minuto_2,
                                                 "minuto_3": minuto_3,
                                                 "minuto_4": minuto_4,
                                                 "minuto_5": minuto_5,
                                                 "minuto_6": minuto_6,
                                                 "minuto_7": minuto_7,
                                                 "minuto_8": minuto_8,
                                                 "minuto_9": minuto_9,
                                                 "minuto_10": minuto_10,
                                                 #"categoria_prueba": [1],
                                                 #"tipo_prueba": [1],
                                                 #"transformador": Transformador
                                                 #"indice_absorcion": [indice_absorcion],
                                                 #"indice_polaridad": [indice_polaridad],
                                 }

    df_V_temp_mohms = pd.DataFrame(valores_temperatura_mohms)
    df_V_temp_mohms["categoria_prueba_id"] = 1
    df_V_temp_mohms["tipo_prueba_id"] = 1
    df_V_Correg_20_mohms = pd.DataFrame(df_V_temp_mohms,
                                        columns=[
                                            'segundo_15',
                                            'segundo_30',
                                            'minuto_1',
                                            'minuto_2',
                                            'minuto_3',
                                            'minuto_4',
                                            'minuto_5',
                                            'minuto_6',
                                            'minuto_7',
                                            'minuto_8',
                                            'minuto_9',
                                            'minuto_10',
                                        ]
                                        )
    temperatura = 15.3
    a,b = (0.5,(20-temperatura)/10)
    df_V_Correg_20_mohms = operator.pow(a,b) * df_V_Correg_20_mohms
    df_V_Correg_20_mohms = round(df_V_Correg_20_mohms)
    df_i_absorcion = df_V_Correg_20_mohms['minuto_1']/df_V_Correg_20_mohms['segundo_30']
    df_i_absorcion= round(df_i_absorcion,1)
    df_i_polaridad = df_V_Correg_20_mohms['minuto_10']/df_V_Correg_20_mohms['minuto_1']
    df_i_polaridad = round(df_i_polaridad,1)
    df_V_Correg_20_mohms["categoria_prueba_id"] = 1
    df_V_Correg_20_mohms["tipo_prueba_id"] = 2
    df_AT_BT_T = pd.DataFrame(df_V_temp_mohms,columns=['AT_BT_T'])
    df_V_Correg_20_mohms = pd.concat([df_AT_BT_T,df_V_Correg_20_mohms,df_i_absorcion,df_i_polaridad], axis=1)
    Resistencia_aislamiento = pd.concat([df_V_temp_mohms,df_V_Correg_20_mohms],axis=0)
    print(Resistencia_aislamiento)
    Resistencia_aislamiento.columns=['ejecucion',
                                    'AT_BT_T','segundo_15','segundo_30','minuto_1','minuto_2',
                                    'minuto_3','minuto_4','minuto_5','minuto_6','minuto_7','minuto_8',
                                    'minuto_9','minuto_10','categoria_prueba_id','tipo_prueba_id',
                                    'indice_absorcion','indice_polaridad'
                                     ]
    Resistencia_aislamiento = Resistencia_aislamiento.to_csv('df_V_Correg_20_mohms.csv')


