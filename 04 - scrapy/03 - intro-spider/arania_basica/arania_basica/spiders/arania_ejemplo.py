import scrapy 

class IntroSpider(scrapy.Spider):
    name = "introduccion_spider"
    urls = ['http://books.toscrape.com/catalogue/category/books/travel_2/index.html']

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url)

    def parse(self, response):
        etiqueta_contenedora = response.css(
            'article.product_pod'
        )
        titulos = etiqueta_contenedora.css(
            'h3 >a::text'
        ).extract()
        dinero = etiqueta_contenedora.css(
            'div.product_price > p.price_color::text'
            ).extract()
        
        stock = etiqueta_contenedora.css(
            'div.product_price > p.availability::text'
            ).extract()

        """
        stock = etiqueta_contenedora.css(
            'div.product_price > p.availability::attr(class)'
            ).extract()
        """

        starts = response.css(
            'article.product_pod>p::attr(class)'
            ).extract()

        imagen = etiqueta_contenedora.css(
            'div.image_container>a>img::attr(src)'
            ).extract()

        print("titulos",titulos)

        print("dinero",dinero)

        print("stock",stock)

        print("starts",starts)

        print("imagen",imagen)


