import scrapy
import os

class DeputadosSpider(scrapy.Spider):
    name = 'deputados'

    def start_requests(self):
        script_dir = os.path.dirname(__file__)
        rel_path_deputados = '../../deputados.txt'
        rel_path_deputadas = '../../deputadas.txt'

        with open(os.path.join(script_dir, rel_path_deputados)) as f:
            deputados = f.read().splitlines()

        with open(os.path.join(script_dir, rel_path_deputadas)) as f:
            deputadas = f.read().splitlines()
        
        for deputado in deputados:
            yield scrapy.Request(url=deputado, callback=self.parse_deputado)
        
        for deputada in deputadas:
            yield scrapy.Request(url=deputada, callback=self.parse_deputada)


    def parse_deputado(self, response):
        yield {
            'nome': self.get_nome(response),
            'genero': 'M',
            'data_nascimento': self.get_data_nascimento(response),
            'presenca_plenario': self.get_presenca_plenario(response)
        }


    def parse_deputada(self, response):
        yield {
            'nome': self.get_nome(response),
            'genero': 'F',
            'data_nascimento': self.get_data_nascimento(response),
            'presenca_plenario': self.get_presenca_plenario(response)
        }


    def get_nome(self, response):
        tag = response.xpath('//h2[@id="nomedeputado"]//text()')
        return tag.get()


    def get_data_nascimento(self, response):
        tag = response.xpath('//ul[@class="informacoes-deputado"]/li[5]/text()')
        return tag.get().strip()


    def get_presenca_plenario(self, response):
        tag = response.xpath('//dl[@class="list-table__definition-list"]/dd[1]/text()')
        return tag.get().strip().split()[0]
