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

filter_word = [u'스트리머', u'방송인', u'그 분', u'그분', u'그 스트리머', u'윈,터,솔,져', u'일베', u'일베충', u'메갈', u'쿵쾅쿵쾅', u'노무현', u'윈터솔져', u'wintersoldier', u'blackpanther', u'panther', u'winter', u'솔져', u'discord', u'살구', u'살인마협회장', u'블랙팬서', u'블포 핵', u'핵 쓰는 법', u'광고글']

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
		req = requests.get(url, headers=req_headers)
	soup = BeautifulSoup(req.content, "html.parser")
	
	notice = soup.find_all(class_="t_notice")
	subject = soup.find_all(class_="t_subject")

	for i in range(0, 46):
		for search in filter_word:
			if search in subject[i].get_text():
				print "Article Number : "+notice[i].get_text()
				print "Subject Name : "+subject[i].get_text()
				print "---------------------------------------------"
				#Warning_MsgBox()
				break;
	time.sleep(3)
	os.system("cls")
