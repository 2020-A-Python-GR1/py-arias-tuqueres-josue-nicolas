import scrapy


marcas_dos_palabras = ["Great Wall",
    "Mercedes Benz",
    "King Long",
    "Saic Wuling",
    "Alfa Romero",
    "Land Rover",
    "American Motors",
    "Austin Healey"
    ]

def getMarcasModelos(titulos):
    marcas = []
    modelos = []
    for titulo in titulos:
        partes_titulo = titulo.split(" ")
        if any(item in titulo for item in marcas_dos_palabras):
            marcas.append(partes_titulo[0] + " " + partes_titulo[1])
            modelos.append(titulo.replace(partes_titulo[0] + " " + partes_titulo[1] + " ",""))
        else:
            marcas.append(partes_titulo[0])
            modelos.append(titulo.replace(partes_titulo[0] + " ",""))

    return marcas, modelos

def getUrls():
    path = r"..\..\..\data\urls.txt"
    output = open(path,'r').read()
    return output.split("\n")

class SpiderPatioTuerca(scrapy.Spider):
    name = "patiotuerca"

    path_data = r"..\..\..\data\datos_vehiculos.csv"

    urls = getUrls()
    #urls = ['https://ecuador.patiotuerca.com/usados/-/autos?orderby=published-at,desc&type_autos_moderated=moderated']

    def start_requests(self):
        headers= {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'}
        for url in self.urls:
            yield scrapy.Request(url = url, headers=headers)

    def parse(self, response):
        #TOTAL 8330
        vehiculosTitulo = response.css('div.card-info>div.module.tittle>h4::text').extract()
        numero_titulos = len(vehiculosTitulo)

        vehiculosPrecio= response.css('div.card-info>strong.price-text>span::text').extract()
        numero_Precios = len(vehiculosPrecio)

        if numero_Precios != numero_titulos:
            #with open(r"..\..\..\data\urlDescuentos.txt", "a+", encoding="utf-8") as archivo:
            #    archivo.write(str(response)[5:-1] + "\n")
            pass
        else:
            
            tipo_compra =  response.css('div.vehicle-used-item::attr(class)').extract() #CHEK
            titulos =  response.css('div.card-info>div.module.tittle>h4::text').extract() #CHEK
            anios = response.css('div.card-info>div.latam-secondary-text>span.year::text').extract() #CHECK
            kilometraje_ciudad =  response.css('div.card-info>div.latam-secondary-text::text').extract() #CHEK
            tipo_precio =  response.css('div.card-info>span.latam-secondary-text::text').extract() #CHEK
            precios = response.css('div.card-info>strong.price-text>span::text').extract() #CHEK

            # Procesamiento tipo compra
            #TIPO_COMPRA
            tipo_compra = [tipo.split(" ")[1] for tipo in tipo_compra if tipo != "row vehicle-used-item full-item banner-item-detail"]

            #Procesamiento kilometraje_ciudad 
            valores_a_eliminar = [kilometraje_ciudad[0],kilometraje_ciudad[2]]
            kilometraje_ciudad = [item.replace("\n","").strip() for item in kilometraje_ciudad if item not in valores_a_eliminar]
            kilometraje_ciudad = [item.replace("Millas","Kms.").replace("Horas","Kms.").replace(" Kms","").replace(". · ","-").replace(". ·","-Otros") for item in kilometraje_ciudad]
            
            #KILOMETRAJE
            kilometraje = [item.split("-")[0] for item in kilometraje_ciudad]
            
            #CIUDAD
            ciudad = [item.split("-")[1] for item in kilometraje_ciudad]
            
            #Procesamiento tipo_precio
            #TIPO_PRECIO
            tipo_precio = [item.replace("\n","").strip() for item in tipo_precio]

            #Porecesamiento precio
            #PRECIO
            precios = [item.replace("\n","").strip().split(" ")[1].replace(".","") for item in precios]
            
            #Procesamiento titulo
            titulos = [item.replace("\n","").strip() for item in titulos]

            #MARCAS Y MODELOS
            marcas, modelos = getMarcasModelos(titulos)

            #MARCA-MODELO-TIPOCOMPRA-ANIOS-KILOMETRAJE-CIUDAD-TIPOPRECIO-PRECIO

            for x in range(len(marcas)):
                with open(self.path_data, "a+", encoding="utf-8") as archivo:
                    archivo.write(
                        marcas[x] + "," +
                        modelos[x] + "," + 
                        tipo_compra[x] + "," +
                        anios[x] + "," +
                        kilometraje[x] + "," +
                        ciudad[x] + "," +
                        tipo_precio[x] + "," +
                        precios[x] +
                        "\n"
                    )
            

