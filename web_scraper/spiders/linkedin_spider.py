```python
import scrapy
from scrapy.http import Request
from web_scraper.items import LinkedInItem

class LinkedInSpider(scrapy.Spider):
    name = 'linkedin'
    allowed_domains = ['linkedin.com']
    start_urls = ['http://linkedin.com/']

    def parse(self, response):
        for profile in response.css('div.profile'):
            item = LinkedInItem()
            item['name'] = profile.css('div.name::text').get()
            item['connections'] = profile.css('div.connections::text').get()
            item['experience'] = profile.css('div.experience::text').get()
            yield item

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page_link = response.urljoin(next_page)
            yield Request(url=next_page_link, callback=self.parse)
```
