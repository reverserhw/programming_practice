#-*- coding: utf-8 -*-
'''
Coded by. ReverserHW
Dcinside Dead By Daylight Minor Gallery Monitoring Tools

'''
from bs4 import BeautifulSoup
import requests
import time
import ctypes
import os

def Warning_MsgBox():
	return ctypes.windll.user32.MessageBoxA(0, "I found filter article!", "Monitoring", 0)

filter_word = [u'keyword1', u'keyword2', u'keyword3']

while True:
	url = "http://gall.dcinside.com/mgallery/board/lists/?id=dbd"
	req_headers = {
	"Host": "gall.dcinside.com",
	"Referer": "http://gall.dcinside.com/mgallery/board/lists/?id=dbd",
	"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36"
	}
	try:
		req = requests.get(url, headers=req_headers)
	except req.exceptions.ConnectionError:
		time.sleep(3)
		continue
	soup = BeautifulSoup(req.content, "html.parser")
	
	notice = soup.find_all(class_="t_notice")
	subject = soup.find_all(class_="t_subject")

	for i in range(0, 45):
		for search in filter_word:
			if search in subject[i].get_text():
				print "Article Number : "+notice[i].get_text()
				print "Subject Name : "+subject[i].get_text()
				print "---------------------------------------------"
				#Warning_MsgBox()
				break;
	time.sleep(3)
	os.system("cls")
