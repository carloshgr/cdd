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
            'salario_bruto_par': self.get_salario_bruto_par(response),
            'quant_viagens': self.get_quant_viagens(response),
            
            'presenca_plenario': self.get_presenca_plenario(response),
            'ausencia_justificada_plenario': self.get_ausencia_justificada_plenario(response),
            'ausencia_nao_justificada_plenario': self.get_ausencia_nao_justificada_plenario(response),
            'presenca_comissoes': self.get_presenca_comissoes(response),
            'ausencia_justificada_comissoes': self.get_ausencia_justificada_comissoes(response),
            'ausencia_nao_justificada_comissoes': self.get_ausencia_nao_justificada_comissoes(response),
            
            'get_gasto_total_par': self.get_gasto_total_par(response),
            'get_gasto_janeiro_par': self.get_gasto_mes_par(response, 'JAN'),
            'get_gasto_fevereiro_par': self.get_gasto_mes_par(response, 'FEV'),
            'get_gasto_marco_par': self.get_gasto_mes_par(response, 'MAR'),
            'get_gasto_abril_par': self.get_gasto_mes_par(response, 'ABR'),
            'get_gasto_maio_par': self.get_gasto_mes_par(response, 'MAI'),
            'get_gasto_junho_par': self.get_gasto_mes_par(response, 'JUN'),
            'get_gasto_julho_par': self.get_gasto_mes_par(response, 'JUL'),
            'get_gasto_agosto_par': self.get_gasto_mes_par(response, 'AGO'),
            'get_gasto_setembro_par': self.get_gasto_mes_par(response, 'SET'),
            'get_gasto_outubro_par': self.get_gasto_mes_par(response, 'OUT'),
            'get_gasto_novembro_par': self.get_gasto_mes_par(response, 'NOV'),
            'get_gasto_dezembro_par': self.get_gasto_mes_par(response, 'DEZ'),
            
            'get_gasto_total_gab': self.get_gasto_total_gab(response),
            'get_gasto_janeiro_gab': self.get_gasto_mes_gab(response, 'JAN'),
            'get_gasto_fevereiro_gab': self.get_gasto_mes_gab(response, 'FEV'),
            'get_gasto_marco_gab': self.get_gasto_mes_gab(response, 'MAR'),
            'get_gasto_abril_gab': self.get_gasto_mes_gab(response, 'ABR'),
            'get_gasto_maio_gab': self.get_gasto_mes_gab(response, 'MAI'),
            'get_gasto_junho_gab': self.get_gasto_mes_gab(response, 'JUN'),
            'get_gasto_julho_gab': self.get_gasto_mes_gab(response, 'JUL'),
            'get_gasto_agosto_gab': self.get_gasto_mes_gab(response, 'AGO'),
            'get_gasto_setembro_gab': self.get_gasto_mes_gab(response, 'SET'),
            'get_gasto_outubro_gab': self.get_gasto_mes_gab(response, 'OUT'),
            'get_gasto_novembro_gab': self.get_gasto_mes_gab(response, 'NOV'),
            'get_gasto_dezembro_gab': self.get_gasto_mes_gab(response, 'DEZ')
        }


    def parse_deputada(self, response):
        yield {
            'nome': self.get_nome(response),
            'genero': 'F',
            'data_nascimento': self.get_data_nascimento(response),
            'salario_bruto_par': self.get_salario_bruto_par(response),
            'quant_viagens': self.get_quant_viagens(response),
            
            'presenca_plenario': self.get_presenca_plenario(response),
            'ausencia_justificada_plenario': self.get_ausencia_justificada_plenario(response),
            'ausencia_nao_justificada_plenario': self.get_ausencia_nao_justificada_plenario(response),
            'presenca_comissoes': self.get_presenca_comissoes(response),
            'ausencia_justificada_comissoes': self.get_ausencia_justificada_comissoes(response),
            'ausencia_nao_justificada_comissoes': self.get_ausencia_nao_justificada_comissoes(response),
            
            'get_gasto_total_par': self.get_gasto_total_par(response),
            'get_gasto_janeiro_par': self.get_gasto_mes_par(response, 'JAN'),
            'get_gasto_fevereiro_par': self.get_gasto_mes_par(response, 'FEV'),
            'get_gasto_marco_par': self.get_gasto_mes_par(response, 'MAR'),
            'get_gasto_abril_par': self.get_gasto_mes_par(response, 'ABR'),
            'get_gasto_maio_par': self.get_gasto_mes_par(response, 'MAI'),
            'get_gasto_junho_par': self.get_gasto_mes_par(response, 'JUN'),
            'get_gasto_julho_par': self.get_gasto_mes_par(response, 'JUL'),
            'get_gasto_agosto_par': self.get_gasto_mes_par(response, 'AGO'),
            'get_gasto_setembro_par': self.get_gasto_mes_par(response, 'SET'),
            'get_gasto_outubro_par': self.get_gasto_mes_par(response, 'OUT'),
            'get_gasto_novembro_par': self.get_gasto_mes_par(response, 'NOV'),
            'get_gasto_dezembro_par': self.get_gasto_mes_par(response, 'DEZ'),
            
            'get_gasto_total_gab': self.get_gasto_total_gab(response),
            'get_gasto_janeiro_gab': self.get_gasto_mes_gab(response, 'JAN'),
            'get_gasto_fevereiro_gab': self.get_gasto_mes_gab(response, 'FEV'),
            'get_gasto_marco_gab': self.get_gasto_mes_gab(response, 'MAR'),
            'get_gasto_abril_gab': self.get_gasto_mes_gab(response, 'ABR'),
            'get_gasto_maio_gab': self.get_gasto_mes_gab(response, 'MAI'),
            'get_gasto_junho_gab': self.get_gasto_mes_gab(response, 'JUN'),
            'get_gasto_julho_gab': self.get_gasto_mes_gab(response, 'JUL'),
            'get_gasto_agosto_gab': self.get_gasto_mes_gab(response, 'AGO'),
            'get_gasto_setembro_gab': self.get_gasto_mes_gab(response, 'SET'),
            'get_gasto_outubro_gab': self.get_gasto_mes_gab(response, 'OUT'),
            'get_gasto_novembro_gab': self.get_gasto_mes_gab(response, 'NOV'),
            'get_gasto_dezembro_gab': self.get_gasto_mes_gab(response, 'DEZ')
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


    def get_gasto_total_par(self, response):
        tag = response.xpath('//table[@id="percentualgastocotaparlamentar"]/tbody/tr/td[2]/text()')
        return tag.get().replace('.', '').replace(',', '.')


    def get_gasto_mes_par(self, response, mes):
        tag = response.xpath(f'//tr[td="{mes}"][1]/td[2]/text()')
        if tag.get() is None: return 'NaN'
        return tag.get().replace('.', '').replace(',', '.')


    def get_gasto_total_gab(self, response):
        tag = response.xpath('//table[@id="percentualgastoverbagabinete"]/tbody/tr/td[2]/text()')
        return tag.get().replace('.', '').replace(',', '.')


    def get_gasto_mes_gab(self, response, mes):
        tag = response.xpath(f'//table[@id="gastomensalverbagabinete"]/tbody/tr[td="{mes}"]/td[2]/text()')
        if tag.get() is None: return 'NaN'
        return tag.get().replace('.', '').replace(',', '.')


    def get_quant_viagens(self, response):
        tag = response.xpath('//ul[@class="recursos-beneficios-deputado-container"]/li[5]/div/span/text()')
        if tag.get() is None:
            tag = response.xpath('//ul[@class="recursos-beneficios-deputado-container"]/li[5]/div/a/text()')
        return tag.get().strip()