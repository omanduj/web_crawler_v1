import scrapy

class amazonSpider(scrapy.Spider):
    name = "reddit"
    start_urls = ["https://www.reddit.com/r/cscareerquestions/new/"]

    def parse(self, response):
        for post in response.css('div._1poyrkZ7g36PawDueRza-J'):

            try:
                yield {
                    'post_name': post.css('h3._eYtD2XCVieq6emjKBH3m::text').get(),
                    'text': post.css('p._1qeIAgB0cPwnLhDF9XSiJM::text').get(),
                    'link': post.css('a.SQnoC3ObvgnGjWt90zD9Z').attrib['href'],
                    'comments': post.css('span.FHCV02u6Cp2zYL0fhQPsO::text').get()
                }
            except:
                yield {
                    'post_name': scrapy.exceptions.DropItem,
                    'text': scrapy.exceptions.DropItem,
                    'link': scrapy.exceptions.DropItem,
                    'comments': scrapy.exceptions.DropItem
                    }





# ________

    #
    # def parse(self, response):
    #     post = response.css('div.blog-post')
    #     name = post.css('h2.post-title')
    #     title_of_post = name.css('a::text').get()
    #
    #     tag = post.css('span.post-tag::text').get()[1:-1]
    #
    #     try :
    #         yield {
    #         'tag': tag,
    #         'article_names': title_of_post
    #
    #         }
    #     except:
    #         "Error"
        # title = post.css('h3._eYtD2XCVieq6emjKBH3m::text').get()
        # text = post.css('p._1qeIAgB0cPwnLhDF9XSiJM::text').get()
        # link = post.css('a.SQnoC3ObvgnGjWt90zD9Z').attrib['href']
        # comments = post.css('span.FHCV02u6Cp2zYL0fhQPsO::text').get()
