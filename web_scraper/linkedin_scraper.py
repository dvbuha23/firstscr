```python
from scrapy.crawler import CrawlerProcess
from web_scraper.spiders.linkedin_spider import LinkedInSpider
from web_scraper.pipelines import JsonWriterPipeline
from web_scraper.items import LinkedInItem
from web_scraper.settings import Settings
from web_scraper.middlewares import LinkedInSpiderMiddleware

def main():
    process = CrawlerProcess(settings={
        "FEEDS": {
            "web_scraper/output.json": {"format": "json"},
        },
        "ITEM_PIPELINES": {'web_scraper.pipelines.JsonWriterPipeline': 1},
        "DOWNLOADER_MIDDLEWARES": {'web_scraper.middlewares.LinkedInSpiderMiddleware': 543},
    })

    process.crawl(LinkedInSpider)
    process.start() 

if __name__ == "__main__":
    main()
```