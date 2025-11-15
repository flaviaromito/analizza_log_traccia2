#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 11:56:06 2025

@author: flaviaromito
"""
import argparse
from elaborazione_log import read, write, elabora_dati

def main():
    """
    Script principale per l'analisi dei log.
    """
    #inizializza il parser per aprire gli argomenti da terminale
    parser = argparse.ArgumentParser(description='Elabora un file JSON di log per estrarre eventi diversi associati a ogni utente e il loro conteggio.')
    
    #definisce l'argomento per il file di ingresso e di uscita con un valore di default
    parser.add_argument('-i', '--input', type=str, default='test_data/test_small.json', help='Inserire percorso del file JSON di ingresso (Default: test_data/test_small.json)')
    parser.add_argument('-o', '--output', type=str, default='risultati.json', help='Inserire percorso del file JSON di uscita (Default: risultati.json)')

    pars = parser.parse_args()
    
    #asssegna il percorso del file di input e di output
    pars_in = pars.input
    pars_out = pars.output

    #legge il file
    dati_log = read(pars_in)
    
    if dati_log is not None:
        #conta gli eventi per utente
        risultato_elaborazione = elabora_dati(dati_log)
        #scrittura del risultati sul file di output
        risultato_scrittura = write(risultato_elaborazione, pars_out)
        
        if risultato_scrittura:
            print(f'Progetto completato con successo. Dati salvati in: {pars_out}')
        else:
            print("Processo interrotto per un errore di scrittura del file di output.")       
    else:
        print("Processo interrotto per un errore di lettura del file di input.")

if __name__ == "__main__":
    main()
    