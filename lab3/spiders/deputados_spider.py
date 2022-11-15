import scrapy

class DeputadosSpider(scrapy.Spider):
    name = 'deputados'

    def start_requests(self):
        deputados_pages = ['https://www.camara.leg.br/deputados/quem-sao/resultado?search=&partido=&uf=&legislatura=56&sexo=M&pagina='+str(i) for i in range(1, 22)]
        deputadas_pages = ['https://www.camara.leg.br/deputados/quem-sao/resultado?search=&partido=&uf=&legislatura=56&sexo=F&pagina='+str(i) for i in range(1, 5)]
        
        for page in deputados_pages:
            yield scrapy.Request(url=page, callback=self.request_deputados)

        for page in deputadas_pages:
            yield scrapy.Request(url=page, callback=self.request_deputadas)


    def request_deputados(self, response):
        for tag in response.xpath('//h3[@class="lista-resultados__cabecalho"]/a/@href'):
            yield scrapy.Request(url=tag.get(), callback=self.parse_deputado)


    def request_deputadas(self, response):
        for tag in response.xpath('//h3[@class="lista-resultados__cabecalho"]/a/@href'):
            yield scrapy.Request(url=tag.get(), callback=self.parse_deputada)


    def get_nome(self, response):
        tag_nome = response.xpath('//h2[@id="nomedeputado"]//text()')
        return tag_nome.get()


    def parse_deputado(self, response):
        yield {
            'nome': self.get_nome(response),
            'genero': 'M'
        }


    def parse_deputada(self, response):
        yield {
            'nome': self.get_nome(response),
            'genero': 'F'
        }
