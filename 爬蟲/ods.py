import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib
import re

headers = {	
'User-Agen' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36(KHTML,like Gecko)Chrome/59.0.3071.115 Safari/537.36'
}


form_data = {
"__VIEWSTATE": "OnyV8/Xd10fkic/c/4FX47RcEguciLijFUdLRlP+5DEVj7nj6aDQTpGDBp/wwgU4Z+Ztnf6fJAVD4ZrcW27WlJHfX4TgtHK+xxJaRhY8ULG7CG0qc6Up35bJGFc=",
"__VIEWSTATEGENERATOR": "CA0B0334",
"Foi$cph_content$ddlTypeID": "0",
"Foi$cph_content$ddl_page": "100",
"Foi$cph_content$ddl_ResultKind": "0",

"Foi$cph_content$ddlVerticals": "0",
"Foi$cph_content$dll_BCase": "評",

"Foi$cph_content$btn_submit": "送出查詢",
"Foi$cph_content$ddlOrderBy": "1",
"Foi$cph_content$hSort": "1",
"Foi$cph_content$HFrecCurrentPage": "1",
"Foi$cph_content$HFRecordCount": "100",
"Foi$cph_content$HFrecPageCount": "1"
}


res = requests.post('https://ods.foi.org.tw', headers=headers, data = form_data)
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text, 'html.parser')
images = soup.select('a[href^=download.aspx?article=]')

images1 = '\n'.join(map(str, images))
r = re.compile(".*aspx")
newlist = list(filter(r.match, images1)) # Read Note
print(newlist)

images = pd.DataFrame(images)
images1 = images.to_string()

images1


list = []

'''for i,x in enumerate(images):
    title_for_url = urllib.parse.quote_plus(x.encode('utf-8')) #利用urllib轉換正確的URL
    imdb_search_link = "https://ods.foi.org.tw/{}".format(title_for_url)
    list.append(imdb_search_link)
    #print("開始轉換IMDB電影網搜尋網址，第",i+1,"部，電影名稱： ", x) #檢視錯誤用'''


print(list)

'''for image in images:
	print(image['href'])
	filename = image['href']
	img = urlopen(image['href'])
	with open('./download/' + str(filename), 'wb') as f:
		f.write(img.read())'''









