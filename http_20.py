import requests
import subprocess 



re = requests.get(f'http://*.put_url?',params={'key[please]':'1'})
print(re.text + re.url)


#make curl request with subprocess
print("curl command :" + "curl " + re.url)
subprocess.call(f'curl {re.url}', shell=True)



#curl 'http://*.put_url?key%5Bplease%5D=1'