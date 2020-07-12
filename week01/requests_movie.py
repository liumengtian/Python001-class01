# 爬取猫眼电影的前 10 个电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中。
import requests
from bs4 import BeautifulSoup as bs
import lxml.etree
import pandas as pd

Cookie = '__mta=250051257.1580314299857.1593252829611.1593350072235.13; _lxsdk_cuid=16ff21289f735-03875eb00e827c-b383f66-1fa400-16ff21289f8c8; mojo-uuid=aa021156229dd56b3fe74b697a57c0c5; uuid_n_v=v1; uuid=66E7C8D0B77E11EAA94453F28D7995DF8A3DFC401EE847229699DD2F31AC2F41; _lxsdk=66E7C8D0B77E11EAA94453F28D7995DF8A3DFC401EE847229699DD2F31AC2F41; _csrf=5f4310a5e42d8c46dba37020c44c53267bc91704e71333781c8333a479729dc3; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593156409,1593247954,1593350057; mojo-session-id={"id":"8aaf42c859ca2045bd93aec9b328cdee","time":1593355460667}; mojo-trace-id=1; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593355461; __mta=250051257.1580314299857.1593350072235.1593355465358.14; _lxsdk_s=172fb62c391-921-cca-519%7C%7C3'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'

header = {
    'Cookie': Cookie,
    'user-agent': user_agent
}

myurl = 'https://maoyan.com/films?showType=3'

response = requests.get(myurl,headers=header)
bs_info = bs(response.text,'html.parser')

# item = []

count = 0

for tags in bs_info.find_all('div', attrs = {'class': 'movie-item-hover'}):
    # print(tags)
    for atag in tags.find_all('a',):
        # 获取电影链接
        url = 'https://maoyan.com' + atag.get('href')
        print(url)


        # url = 'https://maoyan.com/films/1250952'


        response = requests.get(url,headers=header)
        # xml化处理
        selector = lxml.etree.HTML(response.text)
        print('--------------selector=============')
        print(response)
        # 电影名称
        film_name = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[1]/a/text()')
        print(f'电影名称: {film_name}')

        # 电影类型
        film_type = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[1]/a/text()')
        print(f'电影类型: {film_type}')

        # 上映日期
        plan_date = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[3]/text()')
        print(f'上映日期: {plan_date}')

        if count < 10:
            init_tuple = [(film_name, film_type, plan_date)]
            init_title = pd.DataFrame(data = init_tuple)
            init_title.to_csv('./movie.csv', encoding='utf8', index=False, header=False, mode='a')
            count += 1
        else:
            break

        # init_title = pd.DataFrame(data = init_tuple[0:9])

        # item.append(init_tuple)
    if count == 10:
        break

# item_1 = pd.DataFrame(data = item[0:9])
# item_1.to_csv('./movie.csv', encoding='utf8', index=False, header=False, mode='a')