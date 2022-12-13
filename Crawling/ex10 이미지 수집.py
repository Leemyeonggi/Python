{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "d98728a8",
   "metadata": {},
   "outputs": [],
   "source": [
    "from selenium import webdriver as wb\n",
    "from selenium.webdriver.common.keys import Keys\n",
    "from selenium.webdriver.common.by import By\n",
    "import time\n",
    "# 파일시스템을 위한 라이브러리(파일,폴더를 생성,삭제)\n",
    "import os\n",
    "# 이미지의 url값을 파일로 변형시켜주는 라이브러리\n",
    "from urllib.request import urlretrieve"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "90eee2b6",
   "metadata": {},
   "outputs": [],
   "source": [
    "#1. 크롬을 통해서 네이버 메인사이트로 이동\n",
    "driver = wb.Chrome()\n",
    "driver.get(\"http://www.naver.com\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "3ab4bdd6",
   "metadata": {},
   "outputs": [],
   "source": [
    "#2. 검색창에 원하는 검색어 입력\n",
    "#2.1 검색까지 진행\n",
    "search = driver.find_element(By.ID,\"query\")\n",
    "search.send_keys(\"이다혜\")\n",
    "search.send_keys(Keys.ENTER)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "e16cd99e",
   "metadata": {},
   "outputs": [],
   "source": [
    "#3. 이미지 탭 클릭\n",
    "tab = driver.find_element(By.CSS_SELECTOR,\"#lnb > div.lnb_group > div > ul > li:nth-child(2) > a\")\n",
    "tab.click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c29c55f4",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 스크롤 작동하는 코드(화면구성 더 많아진다~ 로딩받는 데이터 증가!)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "a69a7023",
   "metadata": {},
   "outputs": [],
   "source": [
    "#4. 이미지 태그들을 수집\n",
    "# 이유는? 이미지 태그 속에 존재하는 src만 추출하기 위해서!\n",
    "image = driver.find_elements(By.CSS_SELECTOR,\"._image._listImage\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "8c7b6981",
   "metadata": {},
   "outputs": [
    {
     "ename": "IndexError",
     "evalue": "list index out of range",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mIndexError\u001b[0m                                Traceback (most recent call last)",
      "Input \u001b[1;32mIn [36]\u001b[0m, in \u001b[0;36m<cell line: 3>\u001b[1;34m()\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[38;5;66;03m# 나 img리스트의 0번째 데이터에서 src 속성을 가져다줘!\u001b[39;00m\n\u001b[0;32m      2\u001b[0m \u001b[38;5;66;03m# 속성을 수집할 때는 get_attribute(\"속성\")\u001b[39;00m\n\u001b[1;32m----> 3\u001b[0m \u001b[43mimage\u001b[49m\u001b[43m[\u001b[49m\u001b[38;5;241;43m0\u001b[39;49m\u001b[43m]\u001b[49m\u001b[38;5;241m.\u001b[39mget_attribute(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msrc\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n",
      "\u001b[1;31mIndexError\u001b[0m: list index out of range"
     ]
    }
   ],
   "source": [
    "# 나 img리스트의 0번째 데이터에서 src 속성을 가져다줘!\n",
    "# 속성을 수집할 때는 get_attribute(\"속성\")\n",
    "image[0].get_attribute(\"src\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d46f8bd3",
   "metadata": {},
   "outputs": [],
   "source": [
    "# src만 담아줄 리스트 새로 제작\n",
    "src_list = []\n",
    "for i in image:\n",
    "    src_list.append(i.get_attribute(\"src\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8230659a",
   "metadata": {},
   "outputs": [],
   "source": [
    "src_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7cde9dd2",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 이미지를 저장!\n",
    "# 바탕화면에 이다혜 폴더를 생성\n",
    "# 바탕화면에 이다혜라는 폴더가 없다면. 바탕화면에 이다혜 폴더 만들어줘~\n",
    "if not os.path.isdir(\"C:/Users/AI/Desktop/이다혜\") :\n",
    "    os.mkdir(\"C:/Users/AI/Desktop/이다혜\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "97b9f42a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# url값을 이다혜 폴더에 저장\n",
    "cnt = 0\n",
    "for i in src_list:\n",
    "    urlretrieve(i,\"C:/Users/AI/Desktop/이다혜/\"+str(cnt)+\".jpg\")\n",
    "    cnt += 1\n",
    "    time.sleep(1)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d300047c",
   "metadata": {},
   "source": [
    "# 이미지가 중간에 깨지는 이유?\n",
    "- 이미지는 텍스트 파일보다 크기가 더 크기 때문에\n",
    "- 화면상에 스크롤을 통해서 더 많이 로딩을 받기!\n",
    "- 1. 크롬실행\n",
    "- 2. 스크롤을 충분히 진행  // 화면구성\n",
    "- 3. img태그를 수집  // 태그수집\n",
    "- 4. img태그 속 src만 추출  // 데이터가공\n",
    "- 5. 파일로 저장  // 데이터활용"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "89ad91e0",
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
