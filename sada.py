from google.auth import credentials
import gspread
from gspread.models import Worksheet
import requests
from bs4 import BeautifulSoup as soup

gc = gspread.service_account(filename='credentials.json')
sh = gc.open_by_key('1KY0WAxVEhyzxlAlslkLlTEH-5inK62fHJGYdijtuX2E')
Worksheet = sh.sheet1

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
r = requests.get('https://www.bigbasket.com/custompage/sysgenpd/?type=pc&slug=potato-onion-tomato-Carrot-Coccinia-Cabbage-Cucumber-Beetroot-Lemon ',headers=header)
bsobj = soup(r.content,'html.parser')
#print(bsobj.prettify())
import json
comp = json.loads(r.text)
#print(comp)
comp = comp['tab_info']

#print(comp[0])
a =[]
for i in comp[0]['product_info']['products']:
    a.append(i)
#print(a)
name = []
mrp = []
sp = []
img = []
p_brand1=[]
p_type1=[]
weight = []
rating_info1=[]

for j in a:
  name.append(j['p_desc'])
  mrp.append(j['mrp'])
  sp.append(j['sp'])
  img.append(j['p_img_url'])
  p_brand1.append(j['p_brand'])
  weight.append(j['w'])
  rating_info1.append(j['rating_info'])
  p_type1.append(j['p_type'])

print(len(name))
print(len(mrp))
print(len(sp))
print(len(img))
print(len(p_brand1))
print(len(p_type1))
print(len(weight))
print(len(rating_info1))

length = len(name)
for i in range(length):
     list1 = []
     list1.append(name[i])
     list1.append(mrp[i])
     list1.append(sp[i])
     list1.append(img[i])
     list1.append(weight[i])
     list1.append(p_type1[i])


     print(list1)
     Worksheet.append_row(list1)
     del list1[0:]