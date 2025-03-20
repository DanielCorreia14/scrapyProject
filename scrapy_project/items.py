import scrapy

class ScrapyProjectItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    section = scrapy.Field()
    publication_date = scrapy.Field()
    api_url = scrapy.Field()
    pillar_name = scrapy.Field()
