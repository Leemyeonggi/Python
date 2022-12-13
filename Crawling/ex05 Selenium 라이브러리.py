{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "4a91a10b",
   "metadata": {},
   "source": [
    "# Selenium 라이브러리\n",
    "- 웹 브라우저를 자동으로 제어하기 위한 라이브러리\n",
    "- 반드시 한번 설치가 필요!\n",
    "- webdriver : 브라우저의 역할\n",
    "- Keys : 컴퓨터용 키보드 역할"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "debd1c20",
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting selenium\n",
      "  Downloading selenium-4.3.0-py3-none-any.whl (981 kB)\n",
      "Collecting trio-websocket~=0.9\n",
      "  Downloading trio_websocket-0.9.2-py3-none-any.whl (16 kB)\n",
      "Requirement already satisfied: urllib3[secure,socks]~=1.26 in c:\\users\\ai\\anaconda3\\lib\\site-packages (from selenium) (1.26.9)\n",
      "Collecting trio~=0.17\n",
      "  Downloading trio-0.21.0-py3-none-any.whl (358 kB)\n",
      "Requirement already satisfied: sortedcontainers in c:\\users\\ai\\anaconda3\\lib\\site-packages (from trio~=0.17->selenium) (2.4.0)\n",
      "Requirement already satisfied: cffi>=1.14 in c:\\users\\ai\\anaconda3\\lib\\site-packages (from trio~=0.17->selenium) (1.15.0)\n",
      "Collecting outcome\n",
      "  Downloading outcome-1.2.0-py2.py3-none-any.whl (9.7 kB)\n",
      "Collecting async-generator>=1.9\n",
      "  Downloading async_generator-1.10-py3-none-any.whl (18 kB)\n",
      "Requirement already satisfied: attrs>=19.2.0 in c:\\users\\ai\\anaconda3\\lib\\site-packages (from trio~=0.17->selenium) (21.4.0)\n",
      "Requirement already satisfied: sniffio in c:\\users\\ai\\anaconda3\\lib\\site-packages (from trio~=0.17->selenium) (1.2.0)\n",
      "Requirement already satisfied: idna in c:\\users\\ai\\anaconda3\\lib\\site-packages (from trio~=0.17->selenium) (3.3)\n",
      "Requirement already satisfied: pycparser in c:\\users\\ai\\anaconda3\\lib\\site-packages (from cffi>=1.14->trio~=0.17->selenium) (2.21)\n",
      "Collecting wsproto>=0.14\n",
      "  Downloading wsproto-1.1.0-py3-none-any.whl (24 kB)\n",
      "Requirement already satisfied: PySocks!=1.5.7,<2.0,>=1.5.6 in c:\\users\\ai\\anaconda3\\lib\\site-packages (from urllib3[secure,socks]~=1.26->selenium) (1.7.1)\n",
      "Requirement already satisfied: cryptography>=1.3.4 in c:\\users\\ai\\anaconda3\\lib\\site-packages (from urllib3[secure,socks]~=1.26->selenium) (3.4.8)\n",
      "Requirement already satisfied: pyOpenSSL>=0.14 in c:\\users\\ai\\anaconda3\\lib\\site-packages (from urllib3[secure,socks]~=1.26->selenium) (21.0.0)\n",
      "Requirement already satisfied: certifi in c:\\users\\ai\\anaconda3\\lib\\site-packages (from urllib3[secure,socks]~=1.26->selenium) (2021.10.8)\n",
      "Requirement already satisfied: six>=1.5.2 in c:\\users\\ai\\anaconda3\\lib\\site-packages (from pyOpenSSL>=0.14->urllib3[secure,socks]~=1.26->selenium) (1.16.0)\n",
      "Collecting h11<1,>=0.9.0\n",
      "  Downloading h11-0.13.0-py3-none-any.whl (58 kB)\n",
      "Installing collected packages: outcome, h11, async-generator, wsproto, trio, trio-websocket, selenium\n",
      "Successfully installed async-generator-1.10 h11-0.13.0 outcome-1.2.0 selenium-4.3.0 trio-0.21.0 trio-websocket-0.9.2 wsproto-1.1.0\n"
     ]
    }
   ],
   "source": [
    "!pip install selenium"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "524f76a1",
   "metadata": {},
   "outputs": [],
   "source": [
    "# webdriver = 브라우저\n",
    "from selenium import webdriver as wb\n",
    "# Keys = 키보드\n",
    "from selenium.webdriver.common.keys import Keys\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "b5509d5b",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 크롬을 실행하기 위해서는 크롬드라이버를 설치해야함\n",
    "# 사용자가 사용하는 크롬과 같은 버전을 설치해야함\n",
    "# 브라우저가 업데이트되면 크롬드라이버도 업데이트 해야함\n",
    "# 작업중인 파일과 크롬드라이버를 같은 경로에 배치 추천"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "fb6ff1cb",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 크롬창을 시작\n",
    "# 웹드라이버야 크롬 좀 실행 시켜줘~\n",
    "# wb.Chrome(\"크롬드라이버 경로/chromedriver.exe\")\n",
    "# 같은 경로에 있다면 경로를 생략이 가능\n",
    "driver = wb.Chrome()\n",
    "driver.get(\"http://www.naver.com\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "02453283",
   "metadata": {},
   "outputs": [],
   "source": [
    "# .get(\"url\") = 페이지 정보를 요청\n",
    "driver.get(\"htttp://www.naver.com\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "e5efa069",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 검색창을 찾아오라고 명령!\n",
    "# 아이디가 query인 요소좀 찾아와줘!\n",
    "from selenium.webdriver.common.by import By\n",
    "search = driver.find_element(By.ID,\"query\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "b367d70c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# send_keys(\"전달값\") = 값을 전달하는 명령\n",
    "search.send_keys(\"광주날씨\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "e430763b",
   "metadata": {},
   "outputs": [],
   "source": [
    "# enter키 입력\n",
    "search.send_keys(Keys.ENTER)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "b4b8bee0",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 페이지 뒤로가기\n",
    "driver.back()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "63ad0393",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 화면이 바뀌면 요소를 매번 새로 탐색\n",
    "search = driver.find_element(By.ID,\"query\")\n",
    "search.send_keys(\"서울날씨\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "609eac43",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 요소를 클릭하는 메소드 click()\n",
    "btn = driver.find_element(By.ID,\"search_btn\")\n",
    "btn.click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "d614bdd8",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 창을 종료\n",
    "driver.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7c54d7ab",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  },
  "toc": {
   "base_numbering": 1,
   "nav_menu": {},
   "number_sections": true,
   "sideBar": true,
   "skip_h1_title": false,
   "title_cell": "Table of Contents",
   "title_sidebar": "Contents",
   "toc_cell": false,
   "toc_position": {},
   "toc_section_display": true,
   "toc_window_display": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
