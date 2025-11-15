#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 11:55:47 2025

@author: flaviaromito
"""
import json
from utilities.griglia_di_liste_RO import Tabella2D_RO

def read(path: str) -> list[list] | None:
    """
    Legge i dati da un file JSON e gestisce gli errori di file non trovato 
    o di formato errato.

    Parameters
    ----------
    path : str
        Percorso del file JSON di ingresso.

    Returns
    -------
    list[list] | None
        Restituisce le informazioni presenti nel file JSON, 
        oppure None in caso di errore di lettura.
    """
    try:
        fin = open(path)
        content = json.load(fin)
        fin.close()
        return content
    except OSError:
        print(f"Errore: File non trovato al percorso: {path}")
        return None
    except json.decoder.JSONDecodeError:
        print(f"Errore: Formato JSON non valido nel file: {path}")
        return None

def write(content: dict, path: str) -> bool:
    """
    Scrive un dizionario in un file JSON.
    
    Parameters
    ----------
    dati : dict
        Dizionario contenente i dati elaborati.
    path : str
        Percorso del file JSON di uscita.

    Returns
    -------
    bool
        True se la scrittura è andata a buon fine, False altrimenti.
    """
    try:
        f_out = open(path, 'w')
        json.dump(content, f_out, indent=3) 
        f_out.close()
        return True
    except OSError:
        print("Errore durante la scrittura del file")
        return False

def elabora_dati(lista_log: list[list]) -> dict:
    """
    Estrae la lista degli eventi diversi associati a ogni utente e il 
    loro conteggio utilizzando la classe Tabella2D_RO.

    Parameters
    ----------
    lista_log : list[list]
        Lista completa letta dal file JSON.

    Returns
    -------
    dict
        Dizionario finale.
    """
    if not lista_log:
        return {} 
    
    diz = {}
    tabella = Tabella2D_RO(lista_log)
    dim_tabella = tabella.size()
    righe = dim_tabella[0]

    for i in range(righe):
        riga = tabella.get_riga(i)
        
        id_utente = riga[1]
        evento = riga[4]

        if id_utente not in diz:
            diz[id_utente] = {'conteggio_eventi': {}, 'eventi': set()}
        
        conta = diz[id_utente]['conteggio_eventi']

        if evento in conta:
            conta[evento] += 1
        else:
            conta[evento] = 1
        
        diz[id_utente]['eventi'].add(evento)

    output_finale = {}
    for id_utente, dati_utente in diz.items():
        eventi_diversi = list(dati_utente['eventi'])
        conteggio = dati_utente['conteggio_eventi'];
        
        output_finale[id_utente] = {'eventi_diversi': eventi_diversi,'conteggio_eventi': conteggio}

    return output_finale

