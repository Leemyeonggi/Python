{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "39c44fcc",
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
   "execution_count": 39,
   "id": "fe628701",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 1. 크롬브라우저를 실행\n",
    "# 1.1 한솥메뉴사이트로 이동\n",
    "driver = wb.Chrome()\n",
    "driver.get(\"https://www.hsd.co.kr/menu/menu_list\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "61598d99",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 상품명, 상품가격정보를 수집(글자만 출력)\n",
    "title = driver.find_elements(By.CLASS_NAME,\"h.fz_03\")\n",
    "price = driver.find_elements(By.CLASS_NAME,\"item-price\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "ca8b1729",
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['오븐구이 오리도시락', '열무 감초고추장 비빔밥', '열무 두부강된장 비빔밥', '핫 치즈 닭갈비 덮밥', '오리지널 치즈 닭갈비 덮밥', '1993 왕돈까스 도시락', '한입 족발 도시락', '매화(순살 고등어 간장구이)', '진달래', '개나리(순살 고등어 간장구이)', '돈까스도련님고기고기', '탕수육도련님고기고기', '새치 고기고기', '돈치 고기고기', '숯불직화구이', '소불고기', '메가치킨제육', '칠리 찹쌀탕수육도련님', '동백', '치킨제육', '돈까스도련님', '제육볶음', '돈치스팸 도시락', '제육 김치찌개 정식', '제육 김치 부대찌개 정식', '돈치스팸 김치 부대찌개 정식', '빅치킨마요 김치 부대찌개 정식', '치킨마요 김치 부대찌개 정식', '빅치킨마요 김치찌개 정식', '치킨마요 김치찌개 정식', '메가스팸마요', '스팸마요', '메가치킨마요', '왕치킨마요', '빅치킨마요', '치킨마요', '참치마요', '돈치마요', '돈까스 카레', '스팸 김치볶음밥', '김치볶음밥', '스팸철판볶음밥', '소불고기 철판볶음밥', '나시고랭', '묵은지 김치찌개', '김치 부대찌개', '숯불직화구이 덮밥', '마파두부 덮밥', '왕카레돈까스덮밥', '새우돈까스 덮밥', '돈까스 덮밥', '소불고기 감초고추장 비빔밥', '시골제육 두부강된장 비빔밥', '참치야채 감초고추장', '튼튼도시락', '토네이도 소세지 파스타', '트리플 치즈 파스타', '토마토 미트 파스타', '메가스팸마요', '스팸마요', '메가치킨마요', '왕치킨마요', '빅치킨마요', '치킨마요', '참치마요', '돈치마요', '돈까스 카레', '스팸 김치볶음밥', '김치볶음밥', '스팸철판볶음밥', '소불고기 철판볶음밥', '나시고랭', '묵은지 김치찌개', '김치 부대찌개', '숯불직화구이 덮밥', '마파두부 덮밥', '왕카레돈까스덮밥', '새우돈까스 덮밥', '돈까스 덮밥', '소불고기 감초고추장 비빔밥', '시골제육 두부강된장 비빔밥', '참치야채 감초고추장', '튼튼도시락', '토네이도 소세지 파스타', '트리플 치즈 파스타', '토마토 미트 파스타', '반찬 계란말이', '반찬 묵은지김치찌개', '반찬 카레', '반찬 순살 고등어데리야끼', '반찬 김치 부대찌개', '반찬 치킨', '반찬 고기고기', '반찬 돈까스 도련님', '반찬 제육볶음', '반찬 토네이도 소세지', '반찬 반달돈까스', '뉴 감자고로케', '미니 찹쌀핫도그', '미니 찹쌀탕수육', '케이준후라이', '고메이 크림 고로케', '후라이드 순살(소)_스리라차마요소스', '후라이드 순살(중)', '후라이드 순살(소)_양념치킨소스', '후라이드 순살(소)_케이준소스', '오리지널 닭강정(중)', '오리지널 닭강정(소)', '무생채', '열무김치', '오징어젓갈', '오이지무침', '한솥 두부강된장소스', '한솥 감초볶음고추장소스', '볶음김치', '김치', '무말랭이 무침', '한솥밥', '현미밥', '리얼 티라미수 찰떡', '리얼꿀 미니호떡']\n",
      "['6,900', '4,500', '4,900', '5,900', '5,900', '9,300', '8,500', '10,000', '7,500', '8,000', '6,000', '5,800', '6,700', '5,800', '6,500', '5,400', '7,000', '4,200', '5,800', '4,700', '4,500', '4,200', '4,900', '8,200', '8,500', '8,500', '7,500', '6,900', '7,000', '6,500', '5,600', '3,700', '5,800', '4,800', '4,100', '3,500', '3,200', '3,800', '4,500', '4,700', '3,900', '4,500', '4,700', '6,000', '4,500', '5,800', '5,900', '5,000', '5,900', '4,100', '4,000', '5,200', '5,000', '3,300', '5,000', '5,500', '5,500', '4,500', '5,600', '3,700', '5,800', '4,800', '4,100', '3,500', '3,200', '3,800', '4,500', '4,700', '3,900', '4,500', '4,700', '6,000', '4,500', '5,800', '5,900', '5,000', '5,900', '4,100', '4,000', '5,200', '5,000', '3,300', '5,000', '5,500', '5,500', '4,500', '2,500', '4,000', '2,800', '3,600', '4,500', '3,600', '3,400', '3,800', '3,200', '2,600', '2,800', '2,700', '2,500', '2,200', '1,700', '3,500', '4,000', '7,500', '4,000', '4,000', '8,000', '3,400', '400', '500', '400', '700', '1,800', '500', '400', '300', '300', '1,000', '1,700', '1,500', '2,200']\n"
     ]
    }
   ],
   "source": [
    "title_list = []\n",
    "price_list = []\n",
    "\n",
    "for i in range(len(title)):\n",
    "    title_list.append(title[i].text)\n",
    "    price_list.append(price[i].text)\n",
    "print(title_list)\n",
    "print(price_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "f2fe948d",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "b8e71e09",
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>메뉴이름</th>\n",
       "      <th>가격</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>오븐구이 오리도시락</td>\n",
       "      <td>6,900</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>열무 감초고추장 비빔밥</td>\n",
       "      <td>4,500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>열무 두부강된장 비빔밥</td>\n",
       "      <td>4,900</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>핫 치즈 닭갈비 덮밥</td>\n",
       "      <td>5,900</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>오리지널 치즈 닭갈비 덮밥</td>\n",
       "      <td>5,900</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>116</th>\n",
       "      <td>무말랭이 무침</td>\n",
       "      <td>300</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>117</th>\n",
       "      <td>한솥밥</td>\n",
       "      <td>1,000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>118</th>\n",
       "      <td>현미밥</td>\n",
       "      <td>1,700</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>119</th>\n",
       "      <td>리얼 티라미수 찰떡</td>\n",
       "      <td>1,500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>120</th>\n",
       "      <td>리얼꿀 미니호떡</td>\n",
       "      <td>2,200</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>121 rows × 2 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "               메뉴이름     가격\n",
       "0        오븐구이 오리도시락  6,900\n",
       "1      열무 감초고추장 비빔밥  4,500\n",
       "2      열무 두부강된장 비빔밥  4,900\n",
       "3       핫 치즈 닭갈비 덮밥  5,900\n",
       "4    오리지널 치즈 닭갈비 덮밥  5,900\n",
       "..              ...    ...\n",
       "116         무말랭이 무침    300\n",
       "117             한솥밥  1,000\n",
       "118             현미밥  1,700\n",
       "119      리얼 티라미수 찰떡  1,500\n",
       "120        리얼꿀 미니호떡  2,200\n",
       "\n",
       "[121 rows x 2 columns]"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dic = {\"메뉴이름\":title_list,\"가격\":price_list}\n",
    "pd.DataFrame(dic)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "55f08cdf",
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6,900\n",
      "4,500\n",
      "4,900\n",
      "5,900\n",
      "5,900\n",
      "9,300\n",
      "8,500\n",
      "10,000\n",
      "7,500\n",
      "8,000\n",
      "6,000\n",
      "5,800\n",
      "6,700\n",
      "5,800\n",
      "6,500\n",
      "5,400\n",
      "7,000\n",
      "4,200\n",
      "5,800\n",
      "4,700\n",
      "4,500\n",
      "4,200\n",
      "4,900\n",
      "8,200\n",
      "8,500\n",
      "8,500\n",
      "7,500\n",
      "6,900\n",
      "7,000\n",
      "6,500\n",
      "5,600\n",
      "3,700\n",
      "5,800\n",
      "4,800\n",
      "4,100\n",
      "3,500\n",
      "3,200\n",
      "3,800\n",
      "4,500\n",
      "4,700\n",
      "3,900\n",
      "4,500\n",
      "4,700\n",
      "6,000\n",
      "4,500\n",
      "5,800\n",
      "5,900\n",
      "5,000\n",
      "5,900\n",
      "4,100\n",
      "4,000\n",
      "5,200\n",
      "5,000\n",
      "3,300\n",
      "5,000\n",
      "5,500\n",
      "5,500\n",
      "4,500\n",
      "5,600\n",
      "3,700\n",
      "5,800\n",
      "4,800\n",
      "4,100\n",
      "3,500\n",
      "3,200\n",
      "3,800\n",
      "4,500\n",
      "4,700\n",
      "3,900\n",
      "4,500\n",
      "4,700\n",
      "6,000\n",
      "4,500\n",
      "5,800\n",
      "5,900\n",
      "5,000\n",
      "5,900\n",
      "4,100\n",
      "4,000\n",
      "5,200\n",
      "5,000\n",
      "3,300\n",
      "5,000\n",
      "5,500\n",
      "5,500\n",
      "4,500\n",
      "2,500\n",
      "4,000\n",
      "2,800\n",
      "3,600\n",
      "4,500\n",
      "3,600\n",
      "3,400\n",
      "3,800\n",
      "3,200\n",
      "2,600\n",
      "2,800\n",
      "2,700\n",
      "2,500\n",
      "2,200\n",
      "1,700\n",
      "3,500\n",
      "4,000\n",
      "7,500\n",
      "4,000\n",
      "4,000\n",
      "8,000\n",
      "3,400\n",
      "400\n",
      "500\n",
      "400\n",
      "700\n",
      "1,800\n",
      "500\n",
      "400\n",
      "300\n",
      "300\n",
      "1,000\n",
      "1,700\n",
      "1,500\n",
      "2,200\n"
     ]
    }
   ],
   "source": [
    "# By.CSS_SELECTOR : 선택자를 직접 명시할 때 사용\n",
    "# 주의점! 아이디는 #, 클래스는 . , 키워드를 항상 명시해야 한다!\n",
    "price = driver.find_elements(By.CSS_SELECTOR,\".item-price > strong\")\n",
    "for i in price:\n",
    "    print(i.text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "2df9b1f4",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 더보기 버튼을 끝까지 누르는 로직\n",
    "btn = driver.find_element(By.CSS_SELECTOR,\"#btn_more > span > a\")\n",
    "btn.click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "afb7cf33",
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "ename": "ElementNotInteractableException",
     "evalue": "Message: element not interactable\n  (Session info: chrome=103.0.5060.114)\nStacktrace:\nBacktrace:\n\tOrdinal0 [0x004A6463+2188387]\n\tOrdinal0 [0x0043E461+1762401]\n\tOrdinal0 [0x00353C40+801856]\n\tOrdinal0 [0x00382873+993395]\n\tOrdinal0 [0x00378613+951827]\n\tOrdinal0 [0x0039C7DC+1099740]\n\tOrdinal0 [0x00377FF4+950260]\n\tOrdinal0 [0x0039C9F4+1100276]\n\tOrdinal0 [0x003ACC22+1166370]\n\tOrdinal0 [0x0039C5F6+1099254]\n\tOrdinal0 [0x00376BE0+945120]\n\tOrdinal0 [0x00377AD6+948950]\n\tGetHandleVerifier [0x007471F2+2712546]\n\tGetHandleVerifier [0x0073886D+2652765]\n\tGetHandleVerifier [0x0053002A+520730]\n\tGetHandleVerifier [0x0052EE06+516086]\n\tOrdinal0 [0x0044468B+1787531]\n\tOrdinal0 [0x00448E88+1805960]\n\tOrdinal0 [0x00448F75+1806197]\n\tOrdinal0 [0x00451DF1+1842673]\n\tBaseThreadInitThunk [0x764B6739+25]\n\tRtlGetFullPathName_UEx [0x779A8FEF+1215]\n\tRtlGetFullPathName_UEx [0x779A8FBD+1165]\n",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mElementNotInteractableException\u001b[0m           Traceback (most recent call last)",
      "Input \u001b[1;32mIn [42]\u001b[0m, in \u001b[0;36m<cell line: 4>\u001b[1;34m()\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[38;5;28;01mwhile\u001b[39;00m \u001b[38;5;28;01mTrue\u001b[39;00m:\n\u001b[0;32m      4\u001b[0m     btn \u001b[38;5;241m=\u001b[39m driver\u001b[38;5;241m.\u001b[39mfind_element(By\u001b[38;5;241m.\u001b[39mCSS_SELECTOR,\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m#btn_more > span > a\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[1;32m----> 5\u001b[0m     \u001b[43mbtn\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mclick\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m      6\u001b[0m     time\u001b[38;5;241m.\u001b[39msleep(\u001b[38;5;241m1\u001b[39m)\n",
      "File \u001b[1;32m~\\Anaconda3\\lib\\site-packages\\selenium\\webdriver\\remote\\webelement.py:88\u001b[0m, in \u001b[0;36mWebElement.click\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m     86\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mclick\u001b[39m(\u001b[38;5;28mself\u001b[39m) \u001b[38;5;241m-\u001b[39m\u001b[38;5;241m>\u001b[39m \u001b[38;5;28;01mNone\u001b[39;00m:\n\u001b[0;32m     87\u001b[0m     \u001b[38;5;124;03m\"\"\"Clicks the element.\"\"\"\u001b[39;00m\n\u001b[1;32m---> 88\u001b[0m     \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_execute\u001b[49m\u001b[43m(\u001b[49m\u001b[43mCommand\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mCLICK_ELEMENT\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[1;32m~\\Anaconda3\\lib\\site-packages\\selenium\\webdriver\\remote\\webelement.py:396\u001b[0m, in \u001b[0;36mWebElement._execute\u001b[1;34m(self, command, params)\u001b[0m\n\u001b[0;32m    394\u001b[0m     params \u001b[38;5;241m=\u001b[39m {}\n\u001b[0;32m    395\u001b[0m params[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m'\u001b[39m] \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_id\n\u001b[1;32m--> 396\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_parent\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mexecute\u001b[49m\u001b[43m(\u001b[49m\u001b[43mcommand\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mparams\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[1;32m~\\Anaconda3\\lib\\site-packages\\selenium\\webdriver\\remote\\webdriver.py:435\u001b[0m, in \u001b[0;36mWebDriver.execute\u001b[1;34m(self, driver_command, params)\u001b[0m\n\u001b[0;32m    433\u001b[0m response \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mcommand_executor\u001b[38;5;241m.\u001b[39mexecute(driver_command, params)\n\u001b[0;32m    434\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m response:\n\u001b[1;32m--> 435\u001b[0m     \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43merror_handler\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mcheck_response\u001b[49m\u001b[43m(\u001b[49m\u001b[43mresponse\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m    436\u001b[0m     response[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mvalue\u001b[39m\u001b[38;5;124m'\u001b[39m] \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_unwrap_value(\n\u001b[0;32m    437\u001b[0m         response\u001b[38;5;241m.\u001b[39mget(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mvalue\u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;28;01mNone\u001b[39;00m))\n\u001b[0;32m    438\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m response\n",
      "File \u001b[1;32m~\\Anaconda3\\lib\\site-packages\\selenium\\webdriver\\remote\\errorhandler.py:247\u001b[0m, in \u001b[0;36mErrorHandler.check_response\u001b[1;34m(self, response)\u001b[0m\n\u001b[0;32m    245\u001b[0m         alert_text \u001b[38;5;241m=\u001b[39m value[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124malert\u001b[39m\u001b[38;5;124m'\u001b[39m]\u001b[38;5;241m.\u001b[39mget(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m'\u001b[39m)\n\u001b[0;32m    246\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m exception_class(message, screen, stacktrace, alert_text)  \u001b[38;5;66;03m# type: ignore[call-arg]  # mypy is not smart enough here\u001b[39;00m\n\u001b[1;32m--> 247\u001b[0m \u001b[38;5;28;01mraise\u001b[39;00m exception_class(message, screen, stacktrace)\n",
      "\u001b[1;31mElementNotInteractableException\u001b[0m: Message: element not interactable\n  (Session info: chrome=103.0.5060.114)\nStacktrace:\nBacktrace:\n\tOrdinal0 [0x004A6463+2188387]\n\tOrdinal0 [0x0043E461+1762401]\n\tOrdinal0 [0x00353C40+801856]\n\tOrdinal0 [0x00382873+993395]\n\tOrdinal0 [0x00378613+951827]\n\tOrdinal0 [0x0039C7DC+1099740]\n\tOrdinal0 [0x00377FF4+950260]\n\tOrdinal0 [0x0039C9F4+1100276]\n\tOrdinal0 [0x003ACC22+1166370]\n\tOrdinal0 [0x0039C5F6+1099254]\n\tOrdinal0 [0x00376BE0+945120]\n\tOrdinal0 [0x00377AD6+948950]\n\tGetHandleVerifier [0x007471F2+2712546]\n\tGetHandleVerifier [0x0073886D+2652765]\n\tGetHandleVerifier [0x0053002A+520730]\n\tGetHandleVerifier [0x0052EE06+516086]\n\tOrdinal0 [0x0044468B+1787531]\n\tOrdinal0 [0x00448E88+1805960]\n\tOrdinal0 [0x00448F75+1806197]\n\tOrdinal0 [0x00451DF1+1842673]\n\tBaseThreadInitThunk [0x764B6739+25]\n\tRtlGetFullPathName_UEx [0x779A8FEF+1215]\n\tRtlGetFullPathName_UEx [0x779A8FBD+1165]\n"
     ]
    }
   ],
   "source": [
    "# 더보기를 반복해서 끝까지 실행!\n",
    "# 반복의 횟수가 다 다르기 때문에, while문을 활용!\n",
    "while True:\n",
    "    btn = driver.find_element(By.CSS_SELECTOR,\"#btn_more > span > a\")\n",
    "    btn.click()\n",
    "    time.sleep(1)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9d5ece3c",
   "metadata": {},
   "source": [
    "# 예외처리\n",
    "- 오류가 나기전까지 실행하다 오류가 났을때는 다른 코드를 실행!\n",
    "- try = 오류 나기 전까지 코드\n",
    "- except = 오류가 났을 때 코드"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "d061c097",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "더보기 완료!\n"
     ]
    }
   ],
   "source": [
    "try : \n",
    "    # 오류 나기 전\n",
    "    while True:\n",
    "        btn = driver.find_element(By.CSS_SELECTOR,\"#btn_more > span > a\")\n",
    "        btn.click()\n",
    "        time.sleep(1)\n",
    "except :\n",
    "    # 오류 난 후\n",
    "    print(\"더보기 완료!\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bfd5514d",
   "metadata": {},
   "source": [
    "# 한셀에 완벽한 크롤링 코드 짜기"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c9120ce7",
   "metadata": {},
   "outputs": [],
   "source": [
    "#1. 크롬창 실행 후 > 한솥메뉴사이트 요청\n",
    "driver = wb.Chrome()\n",
    "driver.get(\"https://www.hsd.co.kr/menu/menu_list\")\n",
    "#2. 더보기를 끝가지 누르는 로직\n",
    "try :\n",
    "    while True :\n",
    "        btn = driver.find_element(By.CSS_SELECTOR,\"#btn_more > span > a\")\n",
    "        btn.click()\n",
    "        time.sleep(1)\n",
    "except :\n",
    "    print(\"더보기 완료~\")\n",
    "#3. 가격,메뉴명을 수집\n",
    "title = driver.find_elements(By.CLASS_NAME,\"h.fz_03\")\n",
    "price = driver.find_elements(By.CSS_SELECTOR,\".item-price > strong\")\n",
    "#4. 순수한 텍스트 정보만 추출 => 비어있는 리스트에 텍스트만 담기\n",
    "titleList = []\n",
    "priceList = []\n",
    "for i in range(len(title)) :\n",
    "    titleList.append(title[i].text)\n",
    "    priceList.append(price[i].text)\n",
    "#5. 데이터프레임 제작 => 판다스\n",
    "dic = {\"상품명\":titleList, \"가격\" : priceList}\n",
    "df = pd.DataFrame(dic)\n",
    "#6. 한글이 깨지지 않고 csv파일을 제작\n",
    "df.to_csv(\"한솥.csv\", encoding=\"euc-kr\")\n",
    "#7. 크롬창을 종료!\n",
    "driver.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "76f66082",
   "metadata": {},
   "outputs": [],
   "source": [
    "#1. 크롬창 실행 후 > 한솥메뉴사이트 요청\n",
    "#2. 더보기를 끝까지 누르는 로직\n",
    "#3. 가격, 메뉴명을 수집\n",
    "#4. 순수한 텍스트 정보만 추출 => 비어있는 리스트에 텍스트만 담기\n",
    "#5. 데이터프레임 제작 => 판다스\n",
    "#6. 한글이 깨지지 않고 csv파일을 제작\n",
    "#7. 크롬창을 종료!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "5c3e6303",
   "metadata": {},
   "outputs": [],
   "source": [
    "driver = wb.Chrome()\n",
    "driver.get(\"https://www.hsd.co.kr/menu/menu_list\")\n",
    "time.sleep(1)\n",
    "try :\n",
    "    btn = driver.find_element(By.CSS_SELECTOR,\"#btn_more > span > a\")\n",
    "    btn.click()\n",
    "    time.sleep(1)\n",
    "except :\n",
    "    title_list = []\n",
    "    price_list = []\n",
    "    title = driver.find_elements(By.CLASS_NAME,\"h.fz_03\")\n",
    "    price = driver.find_elements(By.CSS_SELECTOR,\"div.item-text > div > strong\")\n",
    "    for i in range(len(title_list)):\n",
    "        title_list.append(title[i].text)\n",
    "        price_list.append(price[i].text)\n",
    "        \n",
    "dic = {'메뉴이름':title_list,'가격':price_list}\n",
    "hansot = pd.DataFrame(dic)\n",
    "hansot.to_csv(\"한솥.csv\",encoding='euc-kr')\n",
    "driver.close()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f23f968d",
   "metadata": {},
   "source": [
    "# 선택자 한번에 복사해오는 방법\n",
    "- F12개발자 도구에서 원하는 요소 찾기\n",
    "- 마우스 우클릭 > copy > copy selector\n",
    "- [주의점]\n",
    "- copy selector를 사용시 무조건 선택한 하나만 가지고옴\n",
    "- 복수개를 요청할때는 선택자의 수정이 필요함\n",
    "- ex) li:nth-child(3) > a 는 하나만 요청 / 복수개로 변경시에는 li > a 로 수정!"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "254e408b",
   "metadata": {},
   "source": [
    "# ActionChains\n",
    "- ActionChains 사용법\n",
    "    - 1. 내가 액션을 줄 모든 요소들을 수집\n",
    "    - 2. ActionChains(\"브라우저\") 호출\n",
    "    - 3. ActionChains(\"브라우저\").기능(요소명).기능(요소명).perform()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "5dab33e7",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 이벤트를 묶어서 실행하는 라이브러리\n",
    "from selenium.webdriver import ActionChains"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "8a5dd510",
   "metadata": {},
   "outputs": [],
   "source": [
    "driver = wb.Chrome()\n",
    "driver.get(\"https://www.hsd.co.kr/\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "bd214cbf",
   "metadata": {},
   "outputs": [],
   "source": [
    "#1. 메뉴탭에 마우스를 올리기!\n",
    "#2. 올린 상태에서 전체 메뉴를 클릭\n",
    "menu = driver.find_element(By.CSS_SELECTOR,\"#gnb > div.gnb_menu > ul > li:nth-child(3) > p > a\")\n",
    "allList = driver.find_element(By.CSS_SELECTOR,\"#gnb > div.gnb_menu > ul > li:nth-child(3) > div > ul > li:nth-child(1) > a\")\n",
    "ActionChains(driver).move_to_element(menu).click(allList).perform()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "015ebbf9",
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
