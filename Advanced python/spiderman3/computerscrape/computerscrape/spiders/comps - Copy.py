import scrapy


#//div[@class='owl-item active']

#class for our spider which inherits from scrapy.spider
class ComputerScraper(scrapy.Spider):
    name='computers'

    start_urls = ['https://www.osta.ee/kategooria/arvutid']

    def parse(self, response):
        for listing in response.xpath("//div[@class='owl-item active']"):
            yield {
                'Title': listing.xpath(".//div/figure/p/a/font/font/text()").extract_first(), 
                'Price': listing.xpath(".//div/figure/div[2]/span[1]/text()").extract_first(), 
                'Picture href': listing.xpath(".//div/figure/figure/a/img/@src").extract_first()
            }

        for listing in response.xpath("//li[@class='col-md-4 mb-30  ']"):
            yield {
                'Title': listing.xpath("//div/p/a/font/font/text()").extract_first(), 
                'Price': listing.xpath("//div/span[2]/font/font/text()").extract_first(), 
                'Picture href': listing.xpath("//li[@class='col-md-4 mb-30  ']/figure/figure/a/img/@src").extract_first()
            }

        

        next_page = response.xpath("//a[@class='icon next page-link']/@href").extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(url=next_page,callback=self.parse)