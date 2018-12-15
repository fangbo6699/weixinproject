# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from weixinproject.items import WeixinprojectItem
class WeixinappSpider(CrawlSpider):
    name = 'weixinapp'
    allowed_domains = ['wxapp-union.com']
    start_urls = ['http://www.wxapp-union.com/portal.php?mod=list&catid=2&page=1']

    rules = (
        Rule(LinkExtractor(allow=r'.+mod=list&catid=2&page=\d'),follow=True),
        Rule(LinkExtractor(allow=r'.+article.+\.html'),callback='parse_item',follow=False)
    )

    def parse_item(self, response):
        # i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        # return i
        title=response.xpath("//div[@class='bm vw']//h1/text()").get()
        print(title)
        authors=response.xpath("//p[@class='authors']")
        author=authors.xpath("./a/text()").get()
        time=authors.xpath("./span/text()").get()
        content=response.xpath("//td[@id='article_content']//text()").getall()
        content="".join(content).strip()
        print(author)
        print(time)
        print(content)
        print("#"*50)
        item=WeixinprojectItem(title=title,author=author,time=time,content=content)
        yield item


