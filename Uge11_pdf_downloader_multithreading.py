# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 09:13:14 2024

@author: KOM
"""

# Import libraries
import requests
import threading
import os
import pandas as pd


os.chdir("C:/Users/KOM/Desktop/Opgaver/Uge11") #Define folder path for excel-files

#Pandas with URLs and Metadata
url = pd.read_excel("GRI_2017_2020_few.xlsx") 
meta = pd.read_excel("Metadata2006_2016_few.xlsx")
#%%

#Function for download using the links in url
def download_pdf(i, link):# chunk_size=8192
    
    BRnum = url.at[i - 1, 'BRnum']#Naming each pdf after BRnum column
    
    try:
        # Make a GET request to the URL
        response = requests.get(link, timeout=10, stream=True)
        
        # Check if the request was successful (status code 200)
        if 200 <= response.status_code < 300:
        
            #Change PDF file download directory
            os.chdir("C:/Users/KOM/Desktop/Opgaver/Uge11/PDF")
            
            # Write the content of the response to a PDF file
            with open(f'{BRnum}.pdf', 'wb') as writer:
                writer.write(response.content)
            print(f"PDF file {i} downloaded successfully.")
            #Changing values in column 'pdf_downloaded' to downloaded
            meta.loc[meta['BRnum'] == BRnum, 'pdf_downloaded'] = 'Downloaded'
            
            
        # If Pdf_URL download fails, try downloading from Report Html Address
        else:
            report_url = url.at[i - 1, 'Report Html Address']
            
            response = requests.get(report_url, timeout=10, stream=True)
            
            if 200 <= response.status_code < 300:
                os.chdir("C:/Users/KOM/Desktop/Opgaver/Uge11/PDF")
                with open(f'{BRnum}.pdf', 'wb') as writer:
                    writer.write(response.content)
                print(f"PDF file {i} downloaded successfully from Report Html Address.")
                meta.loc[meta['BRnum'] == BRnum, 'pdf_downloaded'] = 'Downloaded'
                
            else:
                print(f"Failed to download PDF file {i}. Status code:", response.status_code)
                meta.loc[meta['BRnum'] == BRnum, 'pdf_downloaded'] = 'Not Downloaded'
                
                
    except Exception as e:
        print(f"An error occurred while downloading PDF file {i}: {e}")
        meta.loc[meta['BRnum'] == BRnum, 'pdf_downloaded'] = 'Not Downloaded'
        
# Multithreading loop. Looping through each iteration of links in the excel file through the target download_pdf function 
threads = []
for i, link in enumerate(url['Pdf_URL'], start=1):
    thread = threading.Thread(target=download_pdf, args=(i, link))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

#Save metadata to a new excel file    
meta.to_excel("C:/Users/KOM/Desktop/Opgaver/Uge11/Metadata2006_2016_new.xlsx", index=False)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    