import scrapy


#//div[@class='owl-item active']

#class for our spider which inherits from scrapy.spider
class ComputerScraper(scrapy.Spider):
    name='computers'

    #website that we wanna scrape
    start_urls = ['https://www.osta.ee/kategooria/arvutid']


    #parser for our spider
    def parse(self, response):
        
        for listing in response.xpath("//li[@class='col-md-4 mb-30  ']"):
            yield {
                'Title': listing.xpath(".//figure/div/div/p/@title").get(), 
                'Price': listing.xpath(".//footer/div/div/span[contains(@class, 'price-cp')]/text()").get(), 
                'Picture href': listing.xpath(".//figure/figure/a/img[@class='lazy']/@data-original").get()
            }

        
        #extracts link from next page button
        next_page = response.xpath("//a[@class='icon next page-link']/@href").get()
        #if no next page ends
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(url=next_page,callback=self.parse)