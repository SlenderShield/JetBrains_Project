## Self.
# import os
# import sys
# import requests
# from collections import deque
# from bs4 import BeautifulSoup
# from colorama import Fore,Style
# args = sys.argv
# # if not os.path.exists(args[1]):
# # 	os.mkdir(args[1])
# os.makedirs(args[1],exist_ok=True)  # same as above lines
# info = deque()
# ip = ''
# website = []
# while True:
# 	ip = input()
# 	if ip == 'exit':
# 		exit()
# 	if '.' in ip: website.append(ip[:-4])
# 	else:
# 		if ip not in website:
# 			print('invalid')
# 			continue
# 	if ip == 'back':
# 		print(info.pop())
# 	else:
# 		if ip in website:
# 			for i in range(len(we)):
# 				x = info.pop()
# 				print(x.text)
# 		else:
# 			with open(f'{args[1]}/{ip[:-4]}', 'w') as blog:
# 				if 'https://' in ip:
# 					web = requests.get(ip)
# 					soup = BeautifulSoup(web.content, 'html.parser')
# 				else:
# 					ip = 'https://' + ip
# 					web = requests.get(ip)
# 					soup = BeautifulSoup(web.content, 'html.parser')
# 				we = []
# 				lst = ['p','h1','h2','h3','h4','h5','h6','a','ul','ol','li']
# 				for i in lst:
# 					we += soup.find_all(i)
# 				for i in range(len(we)):
# 					blog.write(we[i].text)
# 					info.append(we[i])
# 					print(we[i].text)
#

## Copied
import sys
import os
from collections import deque
import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style


def save_to_file(filename, contents):
    with open(filename, "w") as f:
        f.write(contents)


args = sys.argv
save_dir = args[1]
os.makedirs(save_dir,exist_ok=True)
stack = deque()

while True:
    url = input()
    if url == "exit":
        break
    elif url == "back":
        if len(stack) > 1:
            temp = stack.pop()
            print(stack.pop())
            stack.append(temp)
    elif "." not in url:
        print("URL error")
    else:
        filename = save_dir + "/" + url.split('.')[0]
        if not url.startswith("https://"):
            url = "https://" + url
        data = requests.get(url)
        if data:
            soup_data = BeautifulSoup(data.content, "html.parser")
            tags = soup_data.find_all(["p", "a", "ul", "ol", "li", "h1",
                                       "h2", "h3", "h4", "h5", "h6"])
            contents = ""
            for tag in tags:

                if str(tag).startswith("<a "):
                    contents = contents + Fore.BLUE + " ".join(tag.text.split()) + "\n"
                contents = contents + Style.RESET_ALL + " ".join(tag.text.split()) + "\n"
            print(contents)
            save_to_file(filename, contents)
            stack.append(contents)
        else:
            print("URL access error")