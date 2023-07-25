```python
import scrapy

class LinkedInItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    title = scrapy.Field()
    company = scrapy.Field()
    location = scrapy.Field()
    url = scrapy.Field()
    connections = scrapy.Field()
    experiences = scrapy.Field()
    educations = scrapy.Field()
    skills = scrapy.Field()
    recommendations = scrapy.Field()
    accomplishments = scrapy.Field()
```