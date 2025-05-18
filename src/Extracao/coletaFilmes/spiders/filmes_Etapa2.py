import scrapy
import pandas as pd

class FilmesSpider(scrapy.Spider):
    name = "filmes_etapa2"
    allowed_domains = ["filmow.com"]

    def start_requests(self):
        
        arquivo_xlsx = 'C:\\Users\\pedro\\OneDrive\\Área de Trabalho\\Python-projetos\\ETL_Filmow\\arquivoFilmes\\filmes.xlsx'
        df = pd.read_excel(arquivo_xlsx)
        
        for url in df['Link']:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # extrair as informações detalhadas de cada filme
        yield {
            'Nome': response.css('h2.movie-original-title::text').get(),
            'Diretor': response.css('div.directors span[itemprop="name"] strong::text').get(),
            'Nota': response.css('div.movie-rating-average span.average::text').get(),
            'Gênero': response.css('div.btn-tags-list a[itemprop="genre"]::text').getall()
        }