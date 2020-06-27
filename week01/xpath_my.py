import requests
import lxml.etree
import pandas as pd

Cookie = '__mta=250051257.1580314299857.1593187382396.1593187389354.7; _lxsdk_cuid=16ff21289f735-03875eb00e827c-b383f66-1fa400-16ff21289f8c8; mojo-uuid=aa021156229dd56b3fe74b697a57c0c5; uuid_n_v=v1; uuid=66E7C8D0B77E11EAA94453F28D7995DF8A3DFC401EE847229699DD2F31AC2F41; _csrf=b18850e018e324427c128c7e96114de26767b62acbb8f88ed287921a89344525; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593156409; _lxsdk=66E7C8D0B77E11EAA94453F28D7995DF8A3DFC401EE847229699DD2F31AC2F41; __mta=250051257.1580314299857.1593156531738.1593182721100.6; mojo-session-id={"id":"65a98409c1a802f458e3f36632778236","time":1593187381886}; mojo-trace-id=2; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593187389; _lxsdk_s=172f15dcf4c-275-6be-848%7C%7C5'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'

header = {
    'Cookie': Cookie,
    'user-agent': user_agent
}

url = 'https://maoyan.com/films/1250952'

response = requests.get(url,headers=header)

# xml化处理
selector = lxml.etree.HTML(response.text)

# 电影名称
film_name = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/h1/text()')
print(f'电影名称: {film_name}')

# 电影类型
film_type = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[1]//text()')
print(f'电影类型: {film_type}')
# /html/body/div[3]/div/div[2]/div[1]/ul/li[1]/a[1]
# /html/body/div[3]/div/div[2]/div[1]/ul/li[1]/a[2]
# /html/body/div[3]/div/div[2]/div[1]/ul/li[1]/a[3]
# 上映日期
plan_date = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[3]/text()')
print(f'上映日期: {plan_date}')

mylist = [film_name, film_type, plan_date]

movie1 = pd.DataFrame(data = mylist)

movie1.to_csv('./movie1.csv', encoding='utf8', index=False, header=False)

# print(response)
# print(f'返回码是:{response.status_code}')