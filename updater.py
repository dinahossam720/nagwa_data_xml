import xml.etree.ElementTree as ET
import os

for file in os.listdir("explainers/") :
    tree = ET.parse("explainers/"+file)
    
    
    for elem in tree.findall("body/p"): # get <p> elements
        child = ET.Element("s")         # create s element
        child.text = elem.text          # copy txt   s
        elem.text = ""                  # remove txt p
        elem.append(child)              

    for elem in tree.findall("body/table/tr/td"):   # get <td> elements
        child = ET.Element("s")
        child.text = elem.text
        elem.text = ""
        elem.append(child)

    tree.write("output/updated/"+file)

    

