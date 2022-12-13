{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a5729fb6",
   "metadata": {},
   "outputs": [],
   "source": [
    "from selenium import webdriver as wb\n",
    "from selenium.webdriver.common.by import By\n",
    "import time"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "ca5400a2",
   "metadata": {},
   "outputs": [],
   "source": [
    "driver = wb.Chrome()\n",
    "driver.get(\"http://corners.gmarket.co.kr/Bestsellers\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "ac11072d",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 1. 첫번째 상품 클릭\n",
    "img = driver.find_elements(By.CLASS_NAME,\"lazy\")\n",
    "img[0].click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "520d8af8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "진짜진짜 촉촉한 올리브 토너 2개 + 로션 1개/+사은품\n",
      "10,500원\n"
     ]
    }
   ],
   "source": [
    "# 상품명, 상품가격정보를 수집\n",
    "title = driver.find_element(By.CLASS_NAME,\"itemtit\")\n",
    "price = driver.find_element(By.CLASS_NAME,\"price_real\")\n",
    "print(title.text)\n",
    "print(price.text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "32066dbb",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 페이지 뒤로가기\n",
    "driver.back()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "701f573b",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 상품 10개를 수집!\n",
    "title_list = []\n",
    "price_list = []\n",
    "\n",
    "for i in range(10):\n",
    "    img = driver.find_elements(By.CLASS_NAME,\"lazy\")\n",
    "    img[i].click()\n",
    "    # 중간중간 코드에 쉬는 시간을 부여\n",
    "    # 서버에게 부담을 주지 않기 위해서\n",
    "    # 화면에 전환이 있었을 때 (클라이언트와 서버가 통신할때)\n",
    "    # time.sleep() = 무조건 정해진 시간만큼 멈춤\n",
    "    time.sleep(2)\n",
    "    # implicitly_wait(10) = 최대 10초\n",
    "    # html 파일을 다 받아오면 그 중간에 멈추고 뒤코드를 실행\n",
    "    driver.implicitly_wait(10)\n",
    "    \n",
    "    title = driver.find_element(By.CLASS_NAME,\"itemtit\")\n",
    "    title_list.append(title.text)\n",
    "    price = driver.find_element(By.CLASS_NAME,\"price_real\")\n",
    "    price_list.append(price.text)\n",
    "    time.sleep(2)\n",
    "    driver.back()\n",
    "    time.sleep(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "fc3c4742",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['진짜진짜 촉촉한 올리브 토너 2개 + 로션 1개/+사은품',\n",
       " '완도 전복 쿠폰가 26340 초복 선물용 횟감용 14-16미 1KG 더큰 전복 국내산',\n",
       " '제스프리 제스프리 썬골드키위 특대과 3.2kg(23~25과 개당 130g~140g내외)+스푼3개',\n",
       " '몽베스트 1L 24병 /생수전문배송',\n",
       " '소문난오부자 재래도시락김5g 72봉 최근생산',\n",
       " '소울키친 빅마마 이혜정의 시크릿코인 205개',\n",
       " '올반 볶음밥 3종 10봉(새우4+김치4+우삼겹2)',\n",
       " '(무료반품) 2+1 균일가 덧신면양말 남성여성발목중목',\n",
       " '(추가할인+사은품) 책과함께 떠나는 북캉스 추천도서 188종 선택/무료배송',\n",
       " '진안 늘푸른 구운계란 60알']"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "title_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "07829220",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['10,500원',\n",
       " '30,000원',\n",
       " '27,740원',\n",
       " '11,880원',\n",
       " '18,900원',\n",
       " '55,640원',\n",
       " '15,700원',\n",
       " '7,900원',\n",
       " '3,900원',\n",
       " '14,900원']"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "price_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fd40fb1b",
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
