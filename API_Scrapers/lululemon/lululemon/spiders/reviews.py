# import scrapy
# import json
# import re
# from lululemon import


# class LuluSpider(scrapy.Spider):
#      name = 'review'
#      allowed_domains = ['https://api.bazaarvoice.com']
#      start_urls = ["https://api.bazaarvoice.com/data/batch.json?passkey=caOGkxt5ZGxRUy0oZU3zbSlV36IBwxAijWghipc2FSoQY&apiversion=5.5&displaycode=7834-en_us&resource.q0=reviews&filter.q0=isratingsonly%3Aeq%3Afalse&filter.q0=productid%3Aeq%3AAlign_Crop_21_Diamond_Dye&filter.q0=contentlocale%3Aeq%3Aen_US&sort.q0=rating%3Adesc&stats.q0=reviews&filteredstats.q0=reviews&include.q0=authors%2Cproducts%2Ccomments&filter_reviews.q0=contentlocale%3Aeq%3Aen_US&filter_reviewcomments.q0=contentlocale%3Aeq%3Aen_US&filter_comments.q0=contentlocale%3Aeq%3Aen_US&limit.q0=8&offset.q0=0&limit_comments.q0=3&callback=bv_351_52133"]

#     def parse_reviews(self, response, lulu):
#          key = prods.get("bazaar-voice-id")
#          url = f'https://api.bazaarvoice.com/data/batch.json?passkey=caOGkxt5ZGxRUy0oZU3zbSlV36IBwxAijWghipc2FSoQY&apiversion=5.5&displaycode=7834-en_us&resource.q0=reviews&filter.q0=isratingsonly%3Aeq%3Afalse&filter.q0=productid%3Aeq%3A{key}&filter.q0=contentlocale%3Aeq%3Aen_US&sort.q0=rating%3Adesc&stats.q0=reviews&filteredstats.q0=reviews&include.q0=authors%2Cproducts%2Ccomments&filter_reviews.q0=contentlocale%3Aeq%3Aen_US&filter_reviewcomments.q0=contentlocale%3Aeq%3Aen_US&filter_comments.q0=contentlocale%3Aeq%3Aen_US&limit.q0=8&offset.q0=0&limit_comments.q0=3&callback=bv_351_52133'
#          r = json.loads(response.body)
#          for a in r:
#              review = a.get("BatchedResults").get("q0").get("TotalResults")
#              rating = a.get("BatchedResults").get("q0").get("Includes").get("Authors").get(
#                 "ec867jnavdpz5dowqd4dk1ob2").get("ReviewStatistics").get("AverageOverallRating")
