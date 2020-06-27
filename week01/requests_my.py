# 爬取猫眼电影的前 10 个电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中。
import requests
from bs4 import BeautifulSoup as bs
import lxml.etree

def get_url_name(myurl):

    Cookie = '__mta=250051257.1580314299857.1593156458332.1593156531738.5; _lxsdk_cuid=16ff21289f735-03875eb00e827c-b383f66-1fa400-16ff21289f8c8; mojo-uuid=aa021156229dd56b3fe74b697a57c0c5; uuid_n_v=v1; uuid=66E7C8D0B77E11EAA94453F28D7995DF8A3DFC401EE847229699DD2F31AC2F41; _csrf=b18850e018e324427c128c7e96114de26767b62acbb8f88ed287921a89344525; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593156409; _lxsdk=66E7C8D0B77E11EAA94453F28D7995DF8A3DFC401EE847229699DD2F31AC2F41; mojo-session-id={"id":"07a52fa29f32521b2ea9a7243d07fcbb","time":1593181807859}; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593182708; mojo-trace-id=18; __mta=250051257.1580314299857.1593156531738.1593182708378.6; _lxsdk_s=172f1092000-75d-0c5-add%7C%7C29'
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'

    header = {
        'Cookie': Cookie,
        'user-agent': user_agent
    }

# https://maoyan.com/films?showType=3
# https://maoyan.com/films?showType=3&offset=0
# https://maoyan.com/films?showType=3&offset=30
# https://maoyan.com/films?showType=3&offset=60
# myurl = 'https://maoyan.com/films?showType=3'

    response = requests.get(myurl,headers=header)
    bs_info = bs(response.text,'html.parser')

# https://maoyan.com/films/1250952
    for tags in bs_info.find_all('div', attrs = {'class': 'movie-item'}):
        # print(tags)
        for atag in tags.find_all('a',):
            # 获取电影链接
            print('https://maoyan.com' + atag.get('href'))

urls = tuple(f'https://maoyan.com/films?showType=3&offset={(page-1) * 30}' for page in range(1,3))

print(urls)

from time import sleep

sleep(5)

for page in urls:
    get_url_name(page)
    sleep(5)


# print(response)
# print(f'返回码是:{response.status_code}')


