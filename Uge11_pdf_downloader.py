# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 09:42:58 2024

@author: KOM
"""


# Import libraries
import requests
from bs4 import BeautifulSoup
import os
import pandas as pd

os.chdir("C:/Users/KOM/Desktop/Opgaver/Uge11") #Define folder path
 
# test url
# url = "https://www.geeksforgeeks.org/how-to-extract-pdf-tables-in-python/"
# url = "http://cdn12.a1.net/m/resources/media/pdf/A1-Umwelterkl-rung-2016-2017.pdf"

# Test with only 3 links
# url = pd.read_excel("GRI_2017_2020_3_linjer.xlsx", usecols=['Pdf_URL'])

#Pandas with URLs
url = pd.read_excel("GRI_2017_2020_few.xlsx", usecols=['Pdf_URL'])
url = url.dropna() 
    
#%%



for i, link in enumerate(url['Pdf_URL'], start=1):
    try:
        # Make a GET request to the URL
        response = requests.get(link)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            
            #Change PDF file download directory
            os.chdir("C:/Users/KOM/Desktop/Opgaver/Uge11/PDF")
            
            # Write the content of the response to a PDF file
            with open(f'pdf{i}.pdf', 'wb') as f:
                f.write(response.content)
            print(f"PDF file {i} downloaded successfully.")
        
        
        # If Pdf_URL download fails, try downloading from Report Html Address
        else:
            report_url = url.at[i-1, 'Report Html Address']  # Get the corresponding Report Html Address
            response = requests.get(report_url)
            if response.status_code == 200:
                os.chdir("C:/Users/KOM/Desktop/Opgaver/Uge11/PDF")
                with open(f'pdf{i}.pdf', 'wb') as f:
                    f.write(response.content)
                print(f"PDF file {i} downloaded successfully from Report Html Address.")
            else:
                print(f"Failed to download PDF file {i}. Status code:", response.status_code)
    
    except Exception as e:
        print(f"An error occurred while downloading PDF file {i}: {e}")
        
        