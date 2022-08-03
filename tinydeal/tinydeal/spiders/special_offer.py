# -*- coding: utf-8 -*-
import scrapy


class SpecialOfferSpider(scrapy.Spider):
    name = "special_offer"
    allowed_domains = ["web.archive.org"]
    start_urls = [
        "https://web.archive.org/web/20190225123327/https://www.tinydeal.com/specials.html"
    ]

    # def start_requests(self):
    #    yield scrapy.Request(url="https://web.archive.org/web/20190225123327/https://www.tinydeal.com/specials.html", callback=self.parse, headers={"Add here the value you find under requests, user agents"})

    def parse(self, response):
        for product in response.xpath("//ul[@class='productlisting-ul']/div/li"):
            yield {
                "title": product.xpath(".//a[@class='p_box_title']/text()").get(),
                "url": response.urljoin(
                    product.xpath(".//a[@class='p_box_title']/@href").get()
                ),
                "dicount_price": product.xpath(
                    ".//span[@class='productSpecialPrice fl']/text()"
                ).get(),
                "og_price": product.xpath(
                    ".//span[@class='normalprice fl']/text()"
                ).get(),
            }

        next_page = response.xpath("//a[@class='nextPage']/@href").get()

        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)
