import requests
from bs4 import BeautifulSoup

link = 'https://browser-info.ru/'
responce = requests.get(link).text

soup = BeautifulSoup(responce, 'lxml')
block = soup.find('div', id='tool_padding')

check_js = block.find('div', id = 'javascript_check')
result_js = check_js.find_all('span')[1].text
status_js = f'javascrip :{result_js}'

check_flash = block.find('div', id = 'flash_version')
result_flash = check_flash.find_all('span')[1].text
status_flash = f'flash :{result_flash}'

check_user = block.find('div', id = 'user_agent').text
status_user = f'user :{check_user}'

print(status_user)
