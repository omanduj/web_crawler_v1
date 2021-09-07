import scrapy
from redditcrawler.items import RedditcrawlerItem

class amazonSpider(scrapy.Spider):
    name = "reddit"
    start_urls = ["https://www.reddit.com/r/cscareerquestions/new/"]

    def parse(self, response):
        post_individual = RedditcrawlerItem()
        for post in response.css('div._1poyrkZ7g36PawDueRza-J'):
            post_individual['post_name'] = post.css('h3._eYtD2XCVieq6emjKBH3m::text').getall()
            post_individual['text'] = post.css('p._1qeIAgB0cPwnLhDF9XSiJM::text').getall()
            post_individual['link'] = post.css('a.SQnoC3ObvgnGjWt90zD9Z').attrib['href']
            post_individual['comments'] = post.css('span.FHCV02u6Cp2zYL0fhQPsO::text').getall()
            yield post_individual

    next_page = response.css('')


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
