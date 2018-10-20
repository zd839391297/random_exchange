# This file aims to get random number
# The random numbers will be output to random.txt
# The random number was from https://www.random.org/
import numpy as np
import requests
from bs4 import BeautifulSoup


def get_num():
    url = "https://www.random.org/integers/?num=30& / min=1&max=30&col=30&base=10&format=html&rnd=new"
    code = "utf-8"
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = code
    html = r.text
    soup = BeautifulSoup(html, "html.parser")
    number = soup.find('pre')
    num = number.text
    # print(num)
    random_num = np.fromstring(num, dtype=int, sep=" ")
    random_num.shape = (1, 30)
    # print(random_num)
    return random_num


num_file = np.zeros(shape=(30, 30), dtype=np.int8)
for i in range(0, 30):
    num_file[i] = get_num()
np.savetxt("random.txt", num_file, fmt='%s', newline='\n')
# np.savetxt("random.txt",num)


# This is another kind of methods below
# from selenium import webdriver
# import io
# import sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码
# driver=webdriver.PhantomJS()
# driver=webdriver.Chrome()
# driver.get("https://www.random.org/integers/")
# print(driver.page_source)
'''
driver = webdriver.Chrome()
driver.get("https://www.random.org/integers/")
driver.find_element_by_name("num").clear()
driver.find_element_by_name("num").send_keys('3000')
driver.find_element_by_name("max").clear()
driver.find_element_by_name("max").send_keys('30')
driver.find_element_by_name("col").clear()
driver.find_element_by_name("col").send_keys('30')
driver.find_element_by_name("Get Numbers").click()
'''

# driver = webdriver.Chrome()
# driver.get("https://www.random.org/integers/?num=10000&min=1&max=30&col=30&base=10&format=html&rnd=new")
