#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):
    def __init__(self):
        self.lista = []
        self.diccionario = {
            "root-layout": ["width", "height", "background-color"],
            "region": ["id", "top", "botton", "left", "rigth"],
            "img": ["src", "region", "begin", "dur"],
            "audio": ["src", "begin", "dur"],
            "textstream": ["src", "region"]
        }

    def startElement(self, name, attrs):
        if name in self.diccionario:
            Mi_Dicc = {}
            for atributo in self.diccionario[name]:
                Mi_Dicc[atributo] = attrs.get(atributo, "")
            self.lista.append([name, Mi_Dicc])

    def get_tags(self):
        return self.lista

if __name__ == "__main__":
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
    lista = cHandler.get_tags()
    print(lista)
