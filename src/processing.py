import csv
import pandas as pd

def import_raw():
    """import_raw importe les trois datasets disponible sans traitement sous forme de dataframe pandas

    Returns
    -------
    gares : dataframe
        dataframe contenant les données gares
    TGV : dataframe

    """
    
    
    gares = pd.read_csv('data/referentiel-gares-voyageurs.csv', sep=';')
    TGV = pd.read_csv('data/tarifs-tgv-inoui-ouigo.csv', sep=';')
    TER = pd.read_csv('data/tarifs-ter-par-od.csv', sep=';')
    
    return gares, TGV, TER


def preprocess(gares_raw, TGV_raw, TER_raw):
    """preprocess _summary_

    Parameters
    ----------
    gares_raw : _type_
        _description_
    TGV_raw : _type_
        _description_
    TER_raw : _type_
        _description_

    Returns
    -------
    _type_
        _description_
    """
    gares = gares_raw[['Code UIC', 'Intitulé plateforme', 'Longitude', 'Latitude', 'Segment DRG']]
    TGV = TGV_raw[["Transporteur","Gare origine - code UIC","Gare destination - code UIC","Classe","Prix minimum"]]
    TER = TER_raw[["Origine - code UIC","Destination - code UIC", "Libellé tarif", "Prix"]]
    return gares, TGV, TER


def export_gares_TGV(gares, TGV):
    gares_TGV = gares[gares['Code UIC'].isin(TGV['Gare origine - code UIC'])]
    return gares_TGV


def get_gares():
    gares_raw, TGV_raw, TER_raw = import_raw()
    return preprocess(gares_raw, TGV_raw, TER_raw)[0]

def get_TGV():
    gares_raw, TGV_raw, TER_raw = import_raw()
    return preprocess(gares_raw, TGV_raw, TER_raw)[1]

def get_TER():
    gares_raw, TGV, TER_raw = import_raw()
    return preprocess(gares_raw, TGV, TER_raw)[2]
