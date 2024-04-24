# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 14:30:41 2024

@author: KOM
"""
#PDF Downloader Readme

##Oversigt
Dette Python-script er designet til at downloade PDF-filer fra en liste over URL'er, der er angivet i en Excel-fil. Det håndterer også tilfælde, hvor direkte PDF-downloads mislykkes, ved at forsøge at downloade fra alternative kilder angivet i den samme Excel-fil. Derudover opdaterer det metadata i en anden Excel-fil for at spore status for hver PDF-download.

#Forudsætninger

- Python 3.9.18 installeret på dit system
- Krævede Python-biblioteker: requests, pandas, os og threading
- Load Requirements.txt i den python prompt (pip install -r Requirements.txt (dette sørger for at installere alt i .txt filen) )

#Brug
- Klone eller download scriptfilerne til din lokale pc.
- Sørg for, at de påkrævede Excel-filer (i dette tilfælde: GRI_2017_2020 (1).xlsx og Metadata2006_2016.xlsx) er i samme mappe som scriptet.
- Åbn scriptet i Python eller kør det via kommandolinjen.

#Konfiguration
------------------- Mappesystem:-----------------

- Opdatér stierne i scriptet i overensstemmelse med din opsætning.
   - eksempel: os.chdir("C:/Users/KOM/Desktop/Opgaver/Uge11")
   - pdf'erne lage jeg i en mappe for sig - os.chdir("C:/Users/KOM/Desktop/Opgaver/Uge11/PDF")
- os.chdir() bruges til at angive mappen til Excel-filer.
- os.chdir() inden for download_pdf()-funktionen bruges til at angive mappen til de downloadede PDF-filer.

------------------- Navne på Excel-filer:-----------------

- Sørg for, at navnene på Excel-filerne matcher dem, der er angivet i scriptet (GRI_2017_2020 (1).xlsx og Metadata2006_2016.xlsx).
- Ændr filnavnene om nødvendigt.

#Scripteksekvering
- Scriptet udfører download_pdf()-funktionen for hver URL i Excel-filen og bruger multithreading for at downloade af flere omgange samtidigt.
- PDF-filer downloades og gemmes i den angivne mappe.
- Metadata vedrørende downloadstatus opdateres i Excel-filen.
- Ved fuldførelse gemmes det opdaterede metadata til en ny Excel-fil (Metadata2006_2016_new.xlsx).

#Fejlhåndtering
- Scriptet inkluderer fejlhåndtering for at håndtere undtagelser under PDF-downloadprocessen.
- Det logger eventuelle fejl, der opstår under downloadprocessen, og opdaterer metadataen i overensstemmelse hermed.

#LAST MINUTE TILFØJELSE
- i filen Uge11_pdf_downloader_multithreading_file_reg.py er der tilføjet to linjer. 
# if not os.path.isfile(f"C:/Users/KOM/Desktop/Opgaver/Uge11/PDF/{BRnum}.pdf"):
# else:
#     print(f"File {BRnum}.pdf has already been downloaded")
- Her bliver der tjekket om filerne allerede er downloadet, hvis ja, så bliver pågældende filer sprunget over
- Her skal stierne også opdateres i scriptet i overensstemmelse med din opsætning.