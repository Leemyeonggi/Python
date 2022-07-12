{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "a11de6eb",
   "metadata": {},
   "source": [
    "# 종목명,현재가격,거래량\n",
    "## 데이터프레임 제작, csv저장"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "8b3d74d0",
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests as req\n",
    "from bs4 import BeautifulSoup as bs"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "d59b4bf6",
   "metadata": {},
   "outputs": [],
   "source": [
    "res = req.get(\"https://finance.naver.com/sise/sise_quant.naver\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "8e744c16",
   "metadata": {},
   "outputs": [],
   "source": [
    "soup = bs(res.text,\"lxml\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "737415aa",
   "metadata": {},
   "outputs": [],
   "source": [
    "title = soup.select(\"a.tltle\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "097b153f",
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "KODEX 200선물인버스2X\n",
      "KODEX 코스닥150선물인버스\n",
      "SH에너지화학\n",
      "현대약품\n",
      "KODEX 인버스\n",
      "KODEX 레버리지\n",
      "국동\n",
      "GS글로벌\n",
      "KODEX 코스닥150레버리지\n",
      "아남전자\n",
      "TIGER 차이나전기차SOLACTIVE\n",
      "일동제약\n",
      "삼성 인버스 2X WTI원유 선물 ETN\n",
      "대한전선\n",
      "TIGER 200선물인버스2X\n",
      "삼성전자\n",
      "사조동아원\n",
      "쌍방울\n",
      "삼부토건\n",
      "고려산업\n",
      "까뮤이앤씨\n",
      "DB하이텍\n",
      "대성에너지\n",
      "신한 인버스 2X 천연가스 선물 ETN\n",
      "TRUE 인버스 2X 천연가스 선물 ETN(H)\n",
      "KODEX 코스닥150\n",
      "부산주공\n",
      "후성\n",
      "삼성중공업\n",
      "KODEX 200\n",
      "NPC\n",
      "두산에너빌리티\n",
      "에이프로젠 MED\n",
      "팬오션\n",
      "KODEX WTI원유선물인버스(H)\n",
      "KBSTAR KIS단기종합채권(AA-이상)액티브\n",
      "LG디스플레이\n",
      "KEC\n",
      "일동홀딩스\n",
      "국제약품\n",
      "서울식품\n",
      "신한 인버스 2X WTI원유 선물 ETN(H)\n",
      "신일전자\n",
      "TYM\n",
      "SK하이닉스\n",
      "대한제당\n",
      "SK바이오사이언스\n",
      "대원화성\n",
      "TIGER 원유선물인버스(H)\n",
      "와이투솔루션\n",
      "대한항공\n",
      "KODEX 은행\n",
      "써니전자\n",
      "한창\n",
      "대호에이엘\n",
      "HMM\n",
      "부광약품\n",
      "KODEX 2차전지산업\n",
      "광명전기\n",
      "하나금융지주\n",
      "미래에셋증권\n",
      "일진홀딩스\n",
      "에스디바이오센서\n",
      "우리금융지주\n",
      "한신기계\n",
      "대성산업\n",
      "TIGER 2차전지테마\n",
      "한국토지신탁\n",
      "카카오뱅크\n",
      "SG세계물산\n",
      "진흥기업\n",
      "TIGER 코스닥150선물인버스\n",
      "신성이엔지\n",
      "TIGER KEDI혁신기업ESG30\n",
      "수산중공업\n",
      "동양철관\n",
      "카카오\n",
      "진원생명과학\n",
      "KODEX 미국달러선물인버스2X\n",
      "신한 인버스 2X 천연가스 선물 ETN(H)\n",
      "신송홀딩스\n",
      "대원제약\n",
      "삼성 블룸버그 인버스 2X WTI원유 선물 ETN\n",
      "한화투자증권\n",
      "대한해운\n",
      "KG스틸\n",
      "남선알미늄\n",
      "기아\n",
      "제이알글로벌리츠\n",
      "한화생명\n",
      "TIGER 인버스\n",
      "한국항공우주\n",
      "이연제약\n",
      "TIGER 미국필라델피아반도체나스닥\n",
      "신풍제약\n",
      "신한지주\n",
      "QV 인버스 레버리지 WTI원유 선물 ETN(H)\n",
      "에어부산\n",
      "모나미\n",
      "SK증권\n"
     ]
    }
   ],
   "source": [
    "for i in title:\n",
    "    print(i.text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "36a8f529",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "100"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cp = soup.select(\"td.number:nth-child(3)\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "f4c39e5a",
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3,390\n",
      "5,265\n",
      "1,050\n",
      "6,360\n",
      "5,075\n",
      "13,960\n",
      "2,090\n",
      "3,505\n",
      "7,845\n",
      "2,500\n",
      "16,595\n",
      "41,350\n",
      "120\n",
      "1,765\n",
      "3,550\n",
      "58,200\n",
      "1,520\n",
      "548\n",
      "2,180\n",
      "6,750\n",
      "2,240\n",
      "41,800\n",
      "11,400\n",
      "355\n",
      "645\n",
      "10,600\n",
      "823\n",
      "16,100\n",
      "5,360\n",
      "30,535\n",
      "9,050\n",
      "17,950\n",
      "1,605\n",
      "5,200\n",
      "4,320\n",
      "100,790\n",
      "14,550\n",
      "2,505\n",
      "31,850\n",
      "5,920\n",
      "251\n",
      "110\n",
      "2,075\n",
      "2,390\n",
      "93,000\n",
      "3,270\n",
      "146,500\n",
      "2,815\n",
      "3,005\n",
      "762\n",
      "23,500\n",
      "5,910\n",
      "2,695\n",
      "908\n",
      "2,360\n",
      "23,550\n",
      "8,920\n",
      "16,695\n",
      "2,965\n",
      "35,850\n",
      "6,140\n",
      "6,380\n",
      "48,300\n",
      "11,350\n",
      "8,820\n",
      "5,070\n",
      "16,830\n",
      "1,605\n",
      "29,900\n",
      "541\n",
      "1,615\n",
      "5,385\n",
      "1,830\n",
      "8,685\n",
      "3,000\n",
      "1,055\n",
      "69,700\n",
      "11,650\n",
      "7,125\n",
      "215\n",
      "11,850\n",
      "18,900\n",
      "17,290\n",
      "3,025\n",
      "2,325\n",
      "12,300\n",
      "2,060\n",
      "78,200\n",
      "4,370\n",
      "2,095\n",
      "5,655\n",
      "47,900\n",
      "26,050\n",
      "8,920\n",
      "25,900\n",
      "35,600\n",
      "100\n",
      "1,360\n",
      "3,635\n",
      "712\n"
     ]
    }
   ],
   "source": [
    "for i in cp:\n",
    "    print(i.text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "e77d06a9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "100"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tv = soup.select(\"td.number:nth-child(6)\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "e1c51b35",
   "metadata": {},
   "outputs": [],
   "source": [
    "title_list = []\n",
    "cp_list = []\n",
    "tv_list = []\n",
    "\n",
    "for i in range(len(title)):\n",
    "    title_list.append(title[i].text)\n",
    "    cp_list.append(cp[i].text)\n",
    "    tv_list.append(tv[i].text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "cfeec4db",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "cospi = {'종목명':title_list,\"가격정보\":cp_list,\"거래량\":tv_list}\n",
    "cospi = pd.DataFrame(cospi)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "a880edcd",
   "metadata": {},
   "outputs": [],
   "source": [
    "cospi.to_csv(\"코스피.csv\",encoding='euc-kr')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a81949a6",
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
