import scrapy

class DeputadosSpider(scrapy.Spider):
    name = 'deputados'

    def start_requests(self):
        urls = ['https://www.camara.leg.br/deputados/quem-sao/resultado?search=&partido=&uf=&legislatura=56&sexo=M&pagina='+str(i) for i in range(1, 22)]
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_pages)

    def parse_pages(self, response):
        for tag in response.xpath('//h3[@class="lista-resultados__cabecalho"]/a/@href'):
            yield scrapy.Request(url=tag.get(), callback=self.parse_deputados)

    def parse_deputados(self, response):
        tag = response.xpath('//h2[@id="nomedeputado"]//text()')
        yield {'nome': tag.get()}
