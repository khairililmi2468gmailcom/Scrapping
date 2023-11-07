import scrapy
from scrapy.crawler import CrawlerProcess

class OlxSpider(scrapy.Spider):
    name = 'olx_spider'
    start_urls = ['https://www.olx.co.id/jakarta-selatan_g4000030/motor-bekas_c200']

    def parse(self, response):
        for li in response.css('ul.list li'):
            yield {
                'title': li.css('div.listing-item__main a.link::text').get(),
                'link': li.css('div.listing-item__main a.link::attr(href)').get(),
                'price': li.css('div.price strong::text').get(),
                'year': li.css('div.info div.additional_data div.additional_info div.date span::text').get(),
                'brand': li.css('div.info div.additional_data div.additional_info div.seller_location span::text').get(),
            }

        # pagination
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

process = CrawlerProcess()
process.crawl(OlxSpider)
process.start()