import scrapy 
import numpy as np

class IntroSpider(scrapy.Spider):
    name = "spider_fybeca"
    urls = ['https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=639&s=0&pp=25']

    def getPrice(self, data_bind):
        return float(data_bind.split('(')[1].split(')')[0])

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url)

    def parse(self, response):
        etiqueta_contenedora = response.css(
            'div.side'
        )
        precios_sin_afiliacion = etiqueta_contenedora.css(
            'div.price::attr(data-bind)'
        ).extract()

        precios_con_afiliacion = etiqueta_contenedora.css(
            'div.price-member>div::attr(data-bind)'
        ).extract()
        
        precios_sin_afiliacion_limpios = list(map(self.getPrice,precios_sin_afiliacion))

        precios_con_afiliacion_limpios = list(map(self.getPrice,precios_con_afiliacion))

        print("MAYOR PRECIO SIN AFILIACION")
        print(max(precios_sin_afiliacion_limpios))

        print("MENOR PRECIO SIN AFILIACION")
        print(min(precios_sin_afiliacion_limpios))

        print("MAYOR PRECIO CON AFILIACION")
        print(max(precios_con_afiliacion_limpios))

        print("MENOR PRECIO CON AFILIACION")
        print(min(precios_con_afiliacion_limpios))

        print("AHORRO")
        print(list(np.array(precios_sin_afiliacion_limpios) - np.array(precios_con_afiliacion_limpios)))

        print("AHORRO TOTAL")
        print(np.sum(list(np.array(precios_sin_afiliacion_limpios) - np.array(precios_con_afiliacion_limpios))))


