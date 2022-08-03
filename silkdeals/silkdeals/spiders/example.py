import scrapy
from scrapy_selenium import SeleniumRequest


class ExampleSpider(scrapy.Spider):
    name = 'example'

    def start_requests(self):
        yield SeleniumRequest(
            url='https://duckduckgo.com',
            # wait_time=3,
            screenshot=True,
            callback=self.parse
        )

    def parse_result(self, response):
        with open('image.png', 'wb') as image_file:
            image_file.write(response.meta['screenshot'])
