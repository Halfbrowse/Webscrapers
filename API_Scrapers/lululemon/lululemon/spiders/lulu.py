import scrapy
import json
import re
import time


class LuluSpider(scrapy.Spider):
    name = 'lulu'
    start_urls = ['https://shop.lululemon.com/api/c/woman?page_size=100000',
                  'https://shop.lululemon.com/api/c/accessories?page_size=1000000',
                  'https://shop.lululemon.com/api/c/men?page_size=1000000']

    def parse(self, response):
        resps = json.loads(response.text)
        prods = resps.get("data").get("attributes").get(
            "main-content")[0]
        product_link = prods.get("records")[0].get(
            "pdp-url")
        yield scrapy.Request(f"https://shop.lululemon.com/api{product_link}", callback=self.parse_products, meta={'pdp-url': product_link})

    # def parse_reviews(self, response):
    #     resps = json.loads(response.body)
    #     key = resps.get("data").get("attributes").get(
    #         "product-summary")
    #     review_link = key.get("bazaar-voice-id")
    #     yield scrapy.Request(f'https://api.bazaarvoice.com/data/batch.json?passkey=caOGkxt5ZGxRUy0oZU3zbSlV36IBwxAijWghipc2FSoQY&apiversion=5.5&displaycode=7834-en_us&resource.q0=reviews&filter.q0=isratingsonly%3Aeq%3Afalse&filter.q0=productid%3Aeq%3A{review_link}&filter.q0=contentlocale%3Aeq%3Aen_US&sort.q0=rating%3Adesc&stats.q0=reviews&filteredstats.q0=reviews&include.q0=authors%2Cproducts%2Ccomments&filter_reviews.q0=contentlocale%3Aeq%3Aen_US&filter_reviewcomments.q0=contentlocale%3Aeq%3Aen_US&filter_comments.q0=contentlocale%3Aeq%3Aen_US&limit.q0=8&offset.q0=0&limit_comments.q0=3&callback=bv_351_52133')
    #     r = json.loads(response.body)
    #     review = r.get("BatchedResults").get(
    #         "q0").get("TotalResults")
    #     rating = r.get("BatchedResults").get("q0").get("Includes").get("Authors").get(
    #         "ec867jnavdpz5dowqd4dk1ob2").get("ReviewStatistics").get("AverageOverallRating")
    #     product_link = response.meta.get('pdp-url')
    #     yield scrapy.Request(f"https://shop.lululemon.com/api{product_link}", callback=self.parse_products, meta={'review': review, 'rating': rating})

    def parse_products(self, response):
        resp = json.loads(response.text)
        products = resp.get("data").get("attributes").get("child-skus")

        desc = resp.get("data").get("attributes").get(
            "whyWeMadeThis")
        names = resp.get("data").get("attributes").get("product-summary")
        cc = resp.get("data").get("attributes").get(
            "product-carousel")[0]

        for prod in products:
            size = prod.get("size")
            price = prod.get("price-details").get("list-price")
            sku = prod.get("id")
            instock = prod.get("available")
            if instock == False:
                instock = 'Not instock'
            else:
                instock = 'Available'
            descr = desc.get("text")
            icon = prod.get("sku-sku-images")
            saleprice = prod.get("price-details").get("sale-price")
            if saleprice == []:
                saleprice = "N/A"
            t = time.localtime()
            current_time = time.strftime("%H:%M:%S", t)
            product_link = response.meta.get('pdp-url')
            review = response.meta.get('review')
            rating = response.meta.get('rating')
            colorcode = cc.get("swatch-color-name")
            name = names.get("unified-id")

        yield {
            'Brand': 'Lululemon',
            'Name': name,
            'Size': size,
            'Price': price,
            'Saleprice': saleprice,
            'Icon': icon,
            'Sku': sku,
            'Product Url': product_link,
            'Description': descr,
            'Color': colorcode,
            'Time': current_time,
            'Available': instock,
            'reviews': review,
            'rating': rating


        }


# # # call categetory with page number 1000 to parse needed sections of product urls to then parse needed parameters
# # # 3 differnt funtctions one for categories one for reviews one for products
