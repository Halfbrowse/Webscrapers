from unicodedata import category
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ScraperSpider(CrawlSpider):
    name = "scraper"
    allowed_domains = ["www.yellowpages.co.za"]
    start_urls = ["http://www.yellowpages.co.za/cities"]

    rules = (
        Rule(
            LinkExtractor(
                restrict_xpaths=".//div[contains(@class, 'col-12 col-sm-6 col-md-6 col-lg-6 col-xl-4')]/a"
            ),
            callback="parse_item",
            follow=True,
        ),
    )

    def parse_item(self, response):

        category = response.xpath(
            ".//div[@class='container-fluid ']/div/h3/b[1]/text()"
        ).get()

        companies = response.xpath(".//div[contains(@class, 'idBusinessDiv ')]")
        for company in companies:
            yield {
                "Name": company.xpath(".//h5[@class='nameOverflow']/text()").get(),
                "Sub-Category": company.xpath(
                    ".//div[@class='col text-lowercase']/p/span[text()]/text()"
                ).get(),
                "Phone Number": company.xpath(
                    ".//span[@id='call_number']/a[1]/text()"
                ).get(),
                "Location": company.xpath(
                    "//p[@class='d-none yext-address']/text()"
                ).get()
                + " "
                + company.xpath("//p[@class='d-none yext-street']/text()").get()
                + " "
                + company.xpath("//p[@class='d-none yext-city']/text()").get()
                + " "
                + company.xpath("//p[@class='d-none yext-postalCode']/text()").get()
                + " "
                + company.xpath("//p[@class='d-none yext-state']/text()").get()
                + " "
                + company.xpath("//p[@class='d-none yext-country']/text()").get(),
                "Email": company.xpath(
                    ".//span[@class='d-none fullDetailId']/a[contains(@href, 'mailto:')]/text()"
                ).get(),
                "Category": category,
                "URL": response.url,
            }

            next_page = response.xpath(
                ".//ul[@class='pagination yp-object-pager-list']/li[last()]/a[1]/@href"
            ).get()

            if next_page:
                absolute_url = f"http://www.yellowpages.co.za{next_page}"
                yield scrapy.Request(url=absolute_url, callback=self.parse_item)
