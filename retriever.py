def getElementsByTagName (file , tagName):
    
    tags = file.getElementsByTagName(tagName)
    value = ""
    if len(tags) > 0 : 
        tag = tags[0].firstChild
        if tag :
           value = tag.data
    
    return (value )  



def getElementAttribute (element , attr):
    
    return (element.getAttribute(attr))