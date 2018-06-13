#-*- coding: utf-8 -*-
'''
Coded by. ReverserHW
Dcinside Dead By Daylight Minor Gallery Monitoring Tools

'''
from bs4 import BeautifulSoup
import requests
import time
import ctypes

def Warning_MsgBox():
	return ctypes.windll.user32.MessageBoxA(0, "I found filter article!", "Monitoring", 0)

def Warning_MsgBox():
	return ctypes.windll.user32.MessageBoxA(0, "I found filter user!", "Monitoring", 0)

filter_word = [u'노무현', u'윈터솔져', u'wintersoldier', u'blackpanther', u'black', u'winter', u'솔져', u'discord', u'살구', u'살인마협회장', u'블랙팬서', u'블포핵', u'블포 핵']
while True:
	url = "http://gall.dcinside.com/mgallery/board/lists/?id=dbd"
	req_headers = {
	"Host": "gall.dcinside.com",
	"Referer": "http://gall.dcinside.com/mgallery/board/lists/?id=dbd",
	"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36"
	}
	req = requests.get(url, headers=req_headers)

	soup = BeautifulSoup(req.content, "html.parser")
	
	notice = soup.find_all(class_="t_notice")
	subject = soup.find_all(class_="t_subject")

	for i in range(0, 46):
		print "Aritcle Number : "+notice[i].get_text()
		print "Subject Name : "+subject[i].get_text()
		print "---------------------------------------------"
		for search in filter_word:
			if search in subject[i].get_text():
				Warning_MsgBox()
				break;
	time.sleep(1)
