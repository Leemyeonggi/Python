{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "74f0c029",
   "metadata": {},
   "outputs": [],
   "source": [
    "from selenium import webdriver as wb\n",
    "from selenium.webdriver.common.keys import Keys\n",
    "from selenium.webdriver.common.by import By\n",
    "import time"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "d94319dc",
   "metadata": {},
   "outputs": [],
   "source": [
    "driver = wb.Chrome()\n",
    "driver.get(\"https://map.kakao.com/\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "9544a2b3",
   "metadata": {},
   "outputs": [],
   "source": [
    "#1 검색창에 광주맛집 검색\n",
    "# 지도설정 레이어를 클릭!\n",
    "layer = driver.find_element(By.ID,\"dimmedLayer\")\n",
    "layer.click()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c9bbcaad",
   "metadata": {},
   "source": [
    "### id나 클래스에(선택자에) . , # 기호가 들어가 있는 경우\n",
    "\n",
    "- 컴퓨터가 해석할 때 #(아이디), .(클래스)로 인식하기 때문에\n",
    "- 문자로 인식 시키기 위해서 \\# or \\. 사용!\n",
    "- 문자로 \".\", \"#\" 으로 인식한다!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "5ec003a9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<selenium.webdriver.remote.webelement.WebElement (session=\"539ac2dcd333c918154332cb9011a5ab\", element=\"5381a465-965e-4b75-bbbf-6a278e68cd2a\")>"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 검색창 찾기\n",
    "search = driver.find_element(By.CSS_SELECTOR,\"#search\\.keyword\\.query\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5e741981",
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
