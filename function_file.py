def coord(response):
    #response must be in json format
    a = response
    x, y = a['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['boundedBy']['Envelope'][
        'lowerCorner'].split()
    xx, yy = a['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['boundedBy']['Envelope'][
        'upperCorner'].split()
    if float(x) >= float(xx):
        finx = float(x) - float(xx)
    else:
        finx = float(xx) - float(x)

    if float(y) >= float(yy):
        finy = float(y) - float(yy)
    else:
        finy = float(yy) - float(y)

    return (finx, finy)