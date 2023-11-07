'''
Robots.txt
User-agent: *
Disallow: /api/
Disallow: /post/
Disallow: /edit/
Disallow: /account/
Disallow: /chat/
Disallow: /profile/
Disallow: /payments/
Disallow: /nf/
Disallow: /items$
#Base Filters
Disallow: */*?*filter=*price_
Disallow: */*?*filter=*condition_
#Cars Filters
Disallow: */*?*filter=*cartype_
Disallow: */*?*filter=*mileage_
Disallow: */*?*filter=*transmission_
Disallow: */*?*filter=*year_

# Generated on 2023-07-25T10:40:38.725Z
'''
import scrapy


class MotorSpider(scrapy.Spider):
    name = 'motor'
    start_urls = ['https://www.olx.co.id/jakarta-selatan_g4000030/motor-bekas_c200']

    def parse(self, response):
        for motor in response.css('div.fTZT3'):
            try:
                yield{
                    'harga':motor.css('span._2Ks63::text').getall(),
                    'tahun':motor.css('span.YBbhy::text').getall(),
                    'merk': motor.css('span._2poNJ::text').getall(),
                }
            except:
                yield{
                    'harga':'tidak ditemukan',
                    'tahun':'tidak ditemukan',
                    'merk': 'tidak ditemukan',
                }
        nextBarang = response.xpath('//*[@id="main_content"]/div/div/section/div/div/div[5]/div[2]/div/div[2]/ul/li[22]/div/button')
        if nextBarang is not None:
            yield response.follow(nextBarang, callback=self.parse)
    
# cara mendapatkan link API 
# inspect kemudian network
# cari ketik api
#salin kemudian paste di column pencarian
#atur page=1 dan size=
