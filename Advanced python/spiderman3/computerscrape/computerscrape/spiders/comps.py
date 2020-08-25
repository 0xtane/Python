import scrapy


#//div[@class='owl-item active']

#class for our spider which inherits from scrapy.spider
class ComputerScraper(scrapy.Spider):
    name='computers'

    start_urls = ['https://www.osta.ee/kategooria/arvutid']

    def parse(self, response):
        for listing in response.xpath("//div[@class='owl-item active']"):
            yield {
                'Title*': listing.xpath(".//p[@class='offer-thumb_title']/@title").get(), 
                'Price*': listing.xpath(".//span[@class='discount-price']/text()").get(), 
                'Picture href*': listing.xpath(".//a/img/@data-original").get()
            }

        for listing in response.xpath("//li[@class='col-md-4 mb-30  ']"):
            yield {
                'Title': listing.xpath(".//figure/div/div/p/@title").get(), 
                'Price': listing.xpath(".//footer/div/div/span[contains(@class, 'price-cp')]/text()").get(), 
                'Picture href': listing.xpath(".//figure/figure/a/img[@class='lazy']/@data-original").get()
            }

        

        next_page = response.xpath("//a[@class='icon next page-link']/@href").get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(url=next_page,callback=self.parse)