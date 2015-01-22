# -*- coding: utf-8 -*-
from lxml import html
import requests
import sys
import urllib
from ghost import Ghost
import re, urlparse

#FUNCIONES DE ENCODEO DE WEBSITE
def urlEncodeNonAscii(b):
    return re.sub('[\x80-\xFF]', lambda c: '%%%02x' % ord(c.group(0)), b)

def iriToUri(iri):
    parts= urlparse.urlparse(iri)
    return urlparse.urlunparse(
        part.encode('idna') if parti==1 else urlEncodeNonAscii(part.encode('utf-8'))
        for parti, part in enumerate(parts)
    )
	
#OBTENGO EL LINK DEL LIBRO
#bajaebooks_u = unicode(raw_input('Copia la direccion de la web del libro que queres bajar: '))
print str(sys.argv)
print str(sys.argv[1])
bajaebooks_u = str(sys.argv[1]) #Obtengo la IRI del argumento
bajaebooks = iriToUri(bajaebooks_u)

#OBTENGO EL LINK DE DESCARGA SIN REDIRIGIR
libro = requests.get(bajaebooks)
libro_tree = html.fromstring(libro.text)
titulo = libro_tree.xpath('//*[@id="single-book"]/div/span[2]/h1')[0].text_content()
link_redirect_u = unicode(libro_tree.xpath('//*[@id="redirectLink"]')[0].attrib.get('href'))
link_redirect = iriToUri(link_redirect_u)
link_bajar=urllib.urlopen(link_redirect).geturl()

#OBTENGO EL LINK DE DESCARGA REDIRIGIDO
ghost = Ghost()
page, resources = ghost.open(link_bajar)
result, resources = ghost.evaluate("link;")

#DESCARGO EL LIBRO
page = requests.get(result)
tree = html.fromstring(page.text)
link = tree.xpath('//*[@id="ajax_container"]/div[2]/a')[0].attrib.get('href')
urllib.urlretrieve (link, titulo+".epub")
