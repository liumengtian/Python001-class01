import scrapy
from scrapy.selector import Selector
from maoyanmovie.items import MaoyanmovieItem


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    # def parse(self, response):
    #     pass

    def start_requests(self):
        # soup = BeautifulSoup(response.text, 'html.parser')
        yield scrapy.Request(url='https://maoyan.com/films?showType=3', callback=self.parse, dont_filter=False)
        # for tags in soup.find_all('div', attrs = {'class': 'movie-item-hover'}):
        #     # print(tags)
        #     for atag in tags.find_all('a',):
        #         # 获取电影链接
        #         url = 'https://maoyan.com' + atag.get('href')
        #         yield scrapy.Request(url=url, callback=self.parse)
        

    # 解析函数
    def parse(self, response):
        # item = MaoyanmovieItem()
        movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]')
        # print(response.text)

        for movie in movies:
            # print(movie)
            item = MaoyanmovieItem()

            film_name = movie.xpath('./div[@class="movie-hover-title"][1]/@title')

            film_type = movie.xpath('./div[@class="movie-hover-title"][2]/text()')

            plan_date = movie.xpath('./div[@class="movie-hover-title movie-hover-brief"]/text()')

            # print('-----------------------------')
            # print(film_name)
            # print(film_type)
            # print(plan_date)
            # print('=============================')
            # print(film_name.extract_first().strip())
            # print(film_type.extract()[-1].strip())
            # print(plan_date.extract()[-1].strip())

            item['film_name'] = film_name.extract_first().strip()
            item['film_type'] = film_type.extract()[-1].strip()
            item['plan_date'] = plan_date.extract()[-1].strip()

            yield item



            # # 电影名称
        # film_name = selector.xpath('(//div[@class="channel-detail movie-item-title"]/@title)[%d]')
        # print(f'电影名称: {film_name}')
        #
        # # 电影类型
        # film_type = selector.xpath('(//div[@class="movie-hover-title"][2]/text())[%d]')
        # print(f'电影类型: {film_type}')
        #
        # # 上映日期
        # plan_date = selector.xpath('(//div[@class="movie-hover-title movie-hover-brief"]/text())[%d]')
        # print(f'上映日期: {plan_date}')
        #
        # item['film_name'] = film_name
        # item['film_type'] = film_type
        # item['plan_date'] = plan_date
        # yield item

