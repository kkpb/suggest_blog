# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re

class HatenaBlogSpider(CrawlSpider):
    name = "hatena_blog"
    start_urls = (
        'http://blog.hatena.ne.jp/-/recent',
    )

    rules = (
        Rule(LinkExtractor(allow=r'.*/recent'), follow=True),
        Rule(LinkExtractor(allow=r'.*/entry'), callback="parse_entry"),
    )

    def parse_entry(self, response):
        p = re.compile(r"<[^>]*?>")
        yield {
            'entry' : p.sub("", response.xpath('//div[@class="entry-content"]').extract_first()),
            'url' : response.url,
            'title' : p.sub("", response.xpath('/html/head/title').extract_first())
        }
