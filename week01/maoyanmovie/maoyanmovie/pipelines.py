# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MaoyanmoviePipeline:
    def process_item(self, item, spider):
        film_name = item['film_name']
        film_type = item['film_type']
        plan_date = item['plan_date']
        output = f'|{film_name}|\t|{film_type}|\t|{plan_date}|\n\n'
        with open('./maoyanmovie.csv', 'a+', encoding='utf-8') as article:
            article.write(output)

        return item
