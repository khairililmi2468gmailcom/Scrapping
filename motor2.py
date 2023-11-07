import scrapy

class MotorBekasSpider(scrapy.Spider):
    name = 'motor_bekas_spider'
    start_urls = ['https://www.olx.co.id/jakarta-selatan_g4000030/motor-bekas_c200']

    def parse(self, response):
        # Mengambil semua informasi motor bekas dari setiap halaman
        for postlink in response.css('a.feed-article-title__link::attr(href)').extract():
            yield scrapy.Request(url=postlink, callback=self.parse_detail)

    def parse_detail(self, response):
        # Mengambil informasi harga, tahun, dan merk dari setiap iklan motor bekas
        harga = response.xpath('//div[@class="pricetag"]/text()').extract_first()
        tahun = response.xpath('//div[@class="attribute-text-wrapper"][2]/span[2]/text()').extract_first()
        merk = response.xpath('//div[@class="attribute-text-wrapper"][1]/span[2]/text()').extract_first()

        # Mengembalikan data yang telah di ekstrak
        yield {
            'harga': harga,
            'tahun': tahun,
            'merk': merk,
        }