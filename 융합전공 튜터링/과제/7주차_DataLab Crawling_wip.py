import urllib as ulib
import requests as req
from bs4 import BeautifulSoup as soup
import datetime

class WebCrawling:

    def __init__(self):
        """Get date range to generate intermediate dates."""


        self.__date_from = input("""제시된 형식에 맞게 데이터 수집을 시작할 날짜를 입력하세요.
형식: YYYY-MM-DD
입력: """)

        self.__delta_date = input("""\n데이터를 수집할 기간을 일 단위로 입력하세요.
정수 범위를 사용하고, 음수는 시작 시점보다 이전 날짜를 나타냅니다.
입력: """)

        datetime.timedelta(self.__date_from, self.__delta_date)


        self.__time = input("""원하는 시각 입력하세요.""")

        return
    

    def connect(self):
        """네이버 데이터랩에 접속."""

        self.__rq_header = {
        "User-Agent" : ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.134 Safari/537.36 Vivaldi/2.5.1525.40")
        }

        self.__url = "https://datalab.naver.com/keyword/realtimeList.naver?datetime=%sT%s&where=main" %("2019-", time)


        self.__page = req.get(self.__url, headers = self.__rq_header)
        self.__page.encoding = "utf-8"

        print("현재 접속 중인 웹페이지:", self.__page.url)

        return self.__page


    def gethtml(self):
        pass

