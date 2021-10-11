
# import pandas 
#import numpy
import os
import xml.dom.minidom
import xml.etree.ElementTree as ET
from retriever import getElementsByTagName
from retriever import getElementAttribute
import csv

csvFile = open("output/explainers/explainers.csv" , "w")  #open csv file with new dir


for file in os.listdir('explainers') :   #for loop to open all files in the explainers folder 
    
    writer = csv.writer(csvFile)
    
    xml_file = xml.dom.minidom.parse("explainers/"+file)

    title = getElementsByTagName(xml_file ,"title")
    id = getElementAttribute(xml_file.getElementsByTagName("explainer")[0],"id")
    seoMetaDescription = getElementsByTagName(xml_file ,"seo_meta_description")
    sourceId = getElementsByTagName(xml_file ,"source_id")
    developerName = getElementsByTagName(xml_file ,"developer_name")
    
    writer.writerow([file,'id',id])
    writer.writerow(['','title',title.encode('utf-8')])
    writer.writerow(['','meta description' , seoMetaDescription.encode('utf-8')])
    writer.writerow(['','sourceId' ,sourceId])
    writer.writerow(['','developer_name' , developerName])
    
csvFile.close()

 
    
