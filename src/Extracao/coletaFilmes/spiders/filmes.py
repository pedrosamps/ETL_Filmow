import scrapy


class FilmesSpider(scrapy.Spider):
    name = "filmes"
    allowed_domains = ["filmow.com"]
    start_urls = ["https://filmow.com/usuario/pedrosamps_/filmes/ja-vi/"]
    count_page = 1
    max_page = 57

    def parse(self, response):
        filmes = response.css('.movie_list_item')

        for filme in filmes:
            yield {
                'Nome': filme.css('span.title::text').get(),
                'Nota': filme.css('div.user-rating span.tip.star-rating.star-rating-small.stars::attr(title)').get(),
                'Link': f'https://filmow.com'+ filme.css('a::attr(href)').get()
            }

        if self.count_page < self.max_page:
            next_page = response.css('a#next-page::attr(href)').get()
            if next_page:
                self.count_page += 1
                yield scrapy.Request(url=f'https://filmow.com{next_page}', callback=self.parse)

        #pass
