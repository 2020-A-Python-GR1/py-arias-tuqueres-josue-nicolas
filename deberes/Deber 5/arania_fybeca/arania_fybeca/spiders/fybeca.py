import scrapy
import numpy as np
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class AraniaCrawlOnu(CrawlSpider):
    name = "crawl_fybeca" 
    precios_sin_afiliacion_limpios = []
    precios_con_afiliacion_limpios = []

    allowed_domains = [ 
        "fybeca.com"
    ]
    
    urls_iniciales = []
    segmentos_url_permitidos = []

    cat_permitidos = [
        "446", #Cabello
        "627", #Manucure y Pedicure 
        "489", #Cuidado de la piel 
        "537", #Maquillaje 
        "558", #Perfumes y Colonias 
        "562" #Lenceria 
    ]

    for x in cat_permitidos:
        urls_iniciales.append("https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=" + x + "&s=0&pp=3000")
        segmentos_url_permitidos.append('search-results.jsf\?cat=' + x + '&s=0&pp=3000')

    start_urls = tuple(urls_iniciales)
    
    regla = (
        Rule(
            LinkExtractor(
                allow_domains = allowed_domains,
                allow = segmentos_url_permitidos,
            ),
            callback="parse_page"
        ),
    )

    rules = regla

    def getPrice(self, data_bind):
        return float(data_bind.split('(')[1].split(')')[0])

    def parse_page(self, response):
        lista_titulos = response.css(
           'div.product-tile-inner > a.name::text' 
        ).extract()

        etiqueta_contenedora = response.css(
            'div.side'
        )
        precios_sin_afiliacion = etiqueta_contenedora.css(
            'div.price::attr(data-bind)'
        ).extract()

        precios_con_afiliacion = etiqueta_contenedora.css(
            'div.price-member>div::attr(data-bind)'
        ).extract()
        
        self.precios_sin_afiliacion_limpios = self.precios_sin_afiliacion_limpios + list(map(self.getPrice,precios_sin_afiliacion))

        self.precios_con_afiliacion_limpios = self.precios_con_afiliacion_limpios + list(map(self.getPrice,precios_con_afiliacion))

        for x in range(len(lista_titulos)):
            with open("DatosFybeca.txt", "a+", encoding="utf-8") as archivo:
                archivo.write(lista_titulos[x] + "\t" + str(self.precios_sin_afiliacion_limpios[x]) +"\t"+ str(self.precios_con_afiliacion_limpios[x]) +"\n")

    def close(self):
        print("MAYOR PRECIO SIN AFILIACION")
        print(max(self.precios_sin_afiliacion_limpios))

        print("MENOR PRECIO SIN AFILIACION")
        print(min(self.precios_sin_afiliacion_limpios))

        print("MAYOR PRECIO CON AFILIACION")
        print(max(self.precios_con_afiliacion_limpios))

        print("MENOR PRECIO CON AFILIACION")
        print(min(self.precios_con_afiliacion_limpios))

        #print("AHORRO")
        #print(list(np.array(self.precios_sin_afiliacion_limpios) - np.array(self.precios_con_afiliacion_limpios)))

        print("AHORRO TOTAL")
        print(np.sum(list(np.array(self.precios_sin_afiliacion_limpios) - np.array(self.precios_con_afiliacion_limpios))))
