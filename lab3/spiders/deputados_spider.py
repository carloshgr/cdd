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
            'presenca_plenario': self.get_presenca_plenario(response),
            'ausencia_justificada_plenario': self.get_ausencia_justificada_plenario(response),
            'ausencia_nao_justificada_plenario': self.get_ausencia_nao_justificada_plenario(response),
            'presenca_comissoes': self.get_presenca_comissoes(response),
            'ausencia_justificada_comissoes': self.get_ausencia_justificada_comissoes(response),
            'ausencia_nao_justificada_comissoes': self.get_ausencia_nao_justificada_comissoes(response),
            'salario_bruto_par': self.get_salario_bruto_par(response),
            'quant_viagens': self.get_quant_viagens(response)
        }


    def parse_deputada(self, response):
        yield {
            'nome': self.get_nome(response),
            'genero': 'F',
            'data_nascimento': self.get_data_nascimento(response),
            'presenca_plenario': self.get_presenca_plenario(response),
            'ausencia_justificada_plenario': self.get_ausencia_justificada_plenario(response),
            'ausencia_nao_justificada_plenario': self.get_ausencia_nao_justificada_plenario(response),
            'presenca_comissoes': self.get_presenca_comissoes(response),
            'ausencia_justificada_comissoes': self.get_ausencia_justificada_comissoes(response),
            'ausencia_nao_justificada_comissoes': self.get_ausencia_nao_justificada_comissoes(response),
            'salario_bruto_par': self.get_salario_bruto_par(response),
            'quant_viagens': self.get_quant_viagens(response)
        }


    def get_nome(self, response):
        tag = response.xpath('//h2[@id="nomedeputado"]//text()')
        return tag.get()


    def get_data_nascimento(self, response):
        tag = response.xpath('//ul[@class="informacoes-deputado"]/li[5]/text()')
        return tag.get().strip()


    def get_presenca_plenario(self, response):
        tag = response.xpath('//ul[@class="list-table__content"]/li[1]/dl/dd[1]/text()')
        return tag.get().strip().split()[0]

    
    def get_ausencia_justificada_plenario(self, response):
        tag = response.xpath('//ul[@class="list-table__content"]/li[1]/dl/dd[2]/text()')
        return tag.get().strip().split()[0]

    
    def get_ausencia_nao_justificada_plenario(self, response):
        tag = response.xpath('//ul[@class="list-table__content"]/li[1]/dl/dd[3]/text()')
        return tag.get().strip().split()[0]


    def get_presenca_comissoes(self, response):
        tag = response.xpath('//ul[@class="list-table__content"]/li[2]/dl/dd[1]/text()')
        return tag.get().strip().split()[0]

    
    def get_ausencia_justificada_comissoes(self, response):
        tag = response.xpath('//ul[@class="list-table__content"]/li[2]/dl/dd[2]/text()')
        return tag.get().strip().split()[0]

    
    def get_ausencia_nao_justificada_comissoes(self, response):
        tag = response.xpath('//ul[@class="list-table__content"]/li[2]/dl/dd[3]/text()')
        return tag.get().strip().split()[0]


    def get_salario_bruto_par(self, response):
        tag = response.xpath('//ul[@class="recursos-beneficios-deputado-container"]/li[2]/div/a/text()')
        return tag.get().split()[1].replace('.', '').replace(',', '.')


    def get_quant_viagens(self, response):
        tag = response.xpath('//ul[@class="recursos-beneficios-deputado-container"]/li[5]/div/span/text()')
        if tag.get() is None:
            tag = response.xpath('//ul[@class="recursos-beneficios-deputado-container"]/li[5]/div/a/text()')
        return tag.get().strip()