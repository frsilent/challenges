"""
Scrape http://www.reddit.com/r/dailyprogrammer/wiki/challenges
and generate a neatly organized checklist for myself
"""

import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor


class ChallengeItem(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    difficulty = scrapy.Field()


class ChallengeSpider(Spider):
    name = 'reddit'
    allowed_domains = ['reddit.com']
    start_urls = ('http://www.reddit.com/r/dailyprogrammer/wiki/challenges')

    def parse(self, response):
        pass


def main():
    # http://www.reddit.com/r/dailyprogrammer/wiki/challenges
    # scrapy crawl reddit -o scraped_data.json
    pass

if __name__ == "__main__":
    main()
