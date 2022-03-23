import requests


#make url encoding with request
#url_encode = requests.utils.quote("pretty please", safe="")

re = requests.get(f'https://ptl-278e7043-ec1f2d94.libcurl.so/pentesterlab?',params={'key[0]':'key','key[1]':'please'})
print(re.text + re.url)



#curl curl 'https://ptl-278e7043-ec1f2d94.libcurl.so/pentesterlab?key\[0\]=key&key\[1\]=please'