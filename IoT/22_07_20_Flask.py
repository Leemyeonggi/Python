{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "5a67825a",
   "metadata": {},
   "source": [
    "# Server란?\n",
    "- flask Server\n",
    "### 웹 마이크로 프레임워크"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a5f0fb1d",
   "metadata": {},
   "outputs": [],
   "source": [
    "# render_template\n",
    "# 현재 실행되고 있는 파이썬 파일과 같은 경로에 있는\n",
    "# template 폴더 내 html문서를 불러온다"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "8d4721e5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "\u001b[31m   WARNING: This is a development server. Do not use it in a production deployment.\u001b[0m\n",
      "\u001b[2m   Use a production WSGI server instead.\u001b[0m\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://192.168.31.171:5048/ (Press CTRL+C to quit)\n",
      "192.168.31.171 - - [20/Jul/2022 16:42:07] \"GET / HTTP/1.1\" 200 -\n",
      "192.168.31.171 - - [20/Jul/2022 16:42:10] \"POST /cal HTTP/1.1\" 200 -\n",
      "192.168.31.171 - - [20/Jul/2022 16:43:44] \"POST /cal HTTP/1.1\" 200 -\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask, render_template, request\n",
    " \n",
    "app = Flask(__name__)\n",
    "\n",
    "@app.route('/')\n",
    "def index():\n",
    "    return render_template('main.html')\n",
    "\n",
    "@app.route('/cal',methods = ['GET','POST']) # 주소 ? : 쿼리스트림\n",
    "def cal():\n",
    "    if request.method == 'GET':\n",
    "        num1 = request.args['num1']\n",
    "        num2 = request.args['num2']\n",
    "        result = int(num1) + int(num2)\n",
    "        return str(result)\n",
    "    elif request.method == 'POST':\n",
    "        num1 = request.form['num1']\n",
    "        num2 = request.form['num2']\n",
    "        result = int(num1) + int(num2)\n",
    "        return str(result)\n",
    "    return '계산 완료'\n",
    "\n",
    "if __name__ == '__main__' :\n",
    "    app.run(host='192.168.31.171', port='5048')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "0e014c83",
   "metadata": {},
   "outputs": [],
   "source": [
    "movie = {\"boxOfficeResult\":{\"boxofficeType\":\"일별 박스오피스\",\"showRange\":\"20220610~20220610\",\"dailyBoxOfficeList\":[{\"rnum\":\"1\",\"rank\":\"1\",\"rankInten\":\"0\",\"rankOldAndNew\":\"OLD\",\"movieCd\":\"20204548\",\"movieNm\":\"범죄도시 2\",\"openDt\":\"2022-05-18\",\"salesAmt\":\"1509984970\",\"salesShare\":\"45.3\",\"salesInten\":\"412579450\",\"salesChange\":\"37.6\",\"salesAcc\":\"101563644940\",\"audiCnt\":\"146311\",\"audiInten\":\"34454\",\"audiChange\":\"30.8\",\"audiAcc\":\"9833051\",\"scrnCnt\":\"1409\",\"showCnt\":\"6391\"},{\"rnum\":\"2\",\"rank\":\"2\",\"rankInten\":\"0\",\"rankOldAndNew\":\"OLD\",\"movieCd\":\"20206257\",\"movieNm\":\"브로커\",\"openDt\":\"2022-06-08\",\"salesAmt\":\"1134820170\",\"salesShare\":\"34.1\",\"salesInten\":\"143809170\",\"salesChange\":\"14.5\",\"salesAcc\":\"3580762850\",\"audiCnt\":\"112525\",\"audiInten\":\"6896\",\"audiChange\":\"6.5\",\"audiAcc\":\"370503\",\"scrnCnt\":\"1546\",\"showCnt\":\"6849\"},{\"rnum\":\"3\",\"rank\":\"3\",\"rankInten\":\"0\",\"rankOldAndNew\":\"OLD\",\"movieCd\":\"20206061\",\"movieNm\":\"쥬라기 월드: 도미니언\",\"openDt\":\"2022-06-01\",\"salesAmt\":\"545108960\",\"salesShare\":\"16.4\",\"salesInten\":\"180806510\",\"salesChange\":\"49.6\",\"salesAcc\":\"24241220550\",\"audiCnt\":\"51914\",\"audiInten\":\"15402\",\"audiChange\":\"42.2\",\"audiAcc\":\"2354578\",\"scrnCnt\":\"948\",\"showCnt\":\"3306\"},{\"rnum\":\"4\",\"rank\":\"4\",\"rankInten\":\"0\",\"rankOldAndNew\":\"OLD\",\"movieCd\":\"20224634\",\"movieNm\":\"그대가 조국\",\"openDt\":\"2022-05-25\",\"salesAmt\":\"35908360\",\"salesShare\":\"1.1\",\"salesInten\":\"11688800\",\"salesChange\":\"48.3\",\"salesAcc\":\"2852620610\",\"audiCnt\":\"3451\",\"audiInten\":\"835\",\"audiChange\":\"31.9\",\"audiAcc\":\"306583\",\"scrnCnt\":\"79\",\"showCnt\":\"100\"},{\"rnum\":\"5\",\"rank\":\"5\",\"rankInten\":\"0\",\"rankOldAndNew\":\"OLD\",\"movieCd\":\"20135304\",\"movieNm\":\"극장판 포켓몬스터DP: 기라티나와 하늘의 꽃다발 쉐이미\",\"openDt\":\"2022-06-01\",\"salesAmt\":\"23425900\",\"salesShare\":\"0.7\",\"salesInten\":\"8548760\",\"salesChange\":\"57.5\",\"salesAcc\":\"3761286650\",\"audiCnt\":\"2664\",\"audiInten\":\"858\",\"audiChange\":\"47.5\",\"audiAcc\":\"402252\",\"scrnCnt\":\"235\",\"showCnt\":\"297\"},{\"rnum\":\"6\",\"rank\":\"6\",\"rankInten\":\"0\",\"rankOldAndNew\":\"OLD\",\"movieCd\":\"20212855\",\"movieNm\":\"닥터 스트레인지: 대혼돈의 멀티버스\",\"openDt\":\"2022-05-04\",\"salesAmt\":\"20302220\",\"salesShare\":\"0.6\",\"salesInten\":\"6287020\",\"salesChange\":\"44.9\",\"salesAcc\":\"62442681020\",\"audiCnt\":\"1894\",\"audiInten\":\"522\",\"audiChange\":\"38\",\"audiAcc\":\"5864931\",\"scrnCnt\":\"63\",\"showCnt\":\"106\"},{\"rnum\":\"7\",\"rank\":\"7\",\"rankInten\":\"5\",\"rankOldAndNew\":\"OLD\",\"movieCd\":\"20224468\",\"movieNm\":\"애프터 양\",\"openDt\":\"2022-06-01\",\"salesAmt\":\"13696100\",\"salesShare\":\"0.4\",\"salesInten\":\"8048500\",\"salesChange\":\"142.5\",\"salesAcc\":\"196123390\",\"audiCnt\":\"1850\",\"audiInten\":\"1262\",\"audiChange\":\"214.6\",\"audiAcc\":\"19663\",\"scrnCnt\":\"51\",\"showCnt\":\"72\"},{\"rnum\":\"8\",\"rank\":\"8\",\"rankInten\":\"0\",\"rankOldAndNew\":\"NEW\",\"movieCd\":\"20218904\",\"movieNm\":\"코다\",\"openDt\":\"2021-08-31\",\"salesAmt\":\"5136000\",\"salesShare\":\"0.2\",\"salesInten\":\"5136000\",\"salesChange\":\"100\",\"salesAcc\":\"680104599\",\"audiCnt\":\"610\",\"audiInten\":\"610\",\"audiChange\":\"100\",\"audiAcc\":\"74880\",\"scrnCnt\":\"5\",\"showCnt\":\"5\"},{\"rnum\":\"9\",\"rank\":\"9\",\"rankInten\":\"17\",\"rankOldAndNew\":\"OLD\",\"movieCd\":\"20196906\",\"movieNm\":\"스텔라\",\"openDt\":\"2022-04-06\",\"salesAmt\":\"3109000\",\"salesShare\":\"0.1\",\"salesInten\":\"1492000\",\"salesChange\":\"92.3\",\"salesAcc\":\"860750300\",\"audiCnt\":\"587\",\"audiInten\":\"356\",\"audiChange\":\"154.1\",\"audiAcc\":\"95349\",\"scrnCnt\":\"2\",\"showCnt\":\"3\"},{\"rnum\":\"10\",\"rank\":\"10\",\"rankInten\":\"6\",\"rankOldAndNew\":\"OLD\",\"movieCd\":\"20218527\",\"movieNm\":\"이공삼칠\",\"openDt\":\"2022-06-08\",\"salesAmt\":\"5347500\",\"salesShare\":\"0.2\",\"salesInten\":\"536580\",\"salesChange\":\"11.2\",\"salesAcc\":\"26367520\",\"audiCnt\":\"509\",\"audiInten\":\"38\",\"audiChange\":\"8.1\",\"audiAcc\":\"3089\",\"scrnCnt\":\"84\",\"showCnt\":\"114\"}]}}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "27ca72f5",
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'boxofficeType': '일별 박스오피스',\n",
       " 'showRange': '20220610~20220610',\n",
       " 'dailyBoxOfficeList': [{'rnum': '1',\n",
       "   'rank': '1',\n",
       "   'rankInten': '0',\n",
       "   'rankOldAndNew': 'OLD',\n",
       "   'movieCd': '20204548',\n",
       "   'movieNm': '범죄도시 2',\n",
       "   'openDt': '2022-05-18',\n",
       "   'salesAmt': '1509984970',\n",
       "   'salesShare': '45.3',\n",
       "   'salesInten': '412579450',\n",
       "   'salesChange': '37.6',\n",
       "   'salesAcc': '101563644940',\n",
       "   'audiCnt': '146311',\n",
       "   'audiInten': '34454',\n",
       "   'audiChange': '30.8',\n",
       "   'audiAcc': '9833051',\n",
       "   'scrnCnt': '1409',\n",
       "   'showCnt': '6391'},\n",
       "  {'rnum': '2',\n",
       "   'rank': '2',\n",
       "   'rankInten': '0',\n",
       "   'rankOldAndNew': 'OLD',\n",
       "   'movieCd': '20206257',\n",
       "   'movieNm': '브로커',\n",
       "   'openDt': '2022-06-08',\n",
       "   'salesAmt': '1134820170',\n",
       "   'salesShare': '34.1',\n",
       "   'salesInten': '143809170',\n",
       "   'salesChange': '14.5',\n",
       "   'salesAcc': '3580762850',\n",
       "   'audiCnt': '112525',\n",
       "   'audiInten': '6896',\n",
       "   'audiChange': '6.5',\n",
       "   'audiAcc': '370503',\n",
       "   'scrnCnt': '1546',\n",
       "   'showCnt': '6849'},\n",
       "  {'rnum': '3',\n",
       "   'rank': '3',\n",
       "   'rankInten': '0',\n",
       "   'rankOldAndNew': 'OLD',\n",
       "   'movieCd': '20206061',\n",
       "   'movieNm': '쥬라기 월드: 도미니언',\n",
       "   'openDt': '2022-06-01',\n",
       "   'salesAmt': '545108960',\n",
       "   'salesShare': '16.4',\n",
       "   'salesInten': '180806510',\n",
       "   'salesChange': '49.6',\n",
       "   'salesAcc': '24241220550',\n",
       "   'audiCnt': '51914',\n",
       "   'audiInten': '15402',\n",
       "   'audiChange': '42.2',\n",
       "   'audiAcc': '2354578',\n",
       "   'scrnCnt': '948',\n",
       "   'showCnt': '3306'},\n",
       "  {'rnum': '4',\n",
       "   'rank': '4',\n",
       "   'rankInten': '0',\n",
       "   'rankOldAndNew': 'OLD',\n",
       "   'movieCd': '20224634',\n",
       "   'movieNm': '그대가 조국',\n",
       "   'openDt': '2022-05-25',\n",
       "   'salesAmt': '35908360',\n",
       "   'salesShare': '1.1',\n",
       "   'salesInten': '11688800',\n",
       "   'salesChange': '48.3',\n",
       "   'salesAcc': '2852620610',\n",
       "   'audiCnt': '3451',\n",
       "   'audiInten': '835',\n",
       "   'audiChange': '31.9',\n",
       "   'audiAcc': '306583',\n",
       "   'scrnCnt': '79',\n",
       "   'showCnt': '100'},\n",
       "  {'rnum': '5',\n",
       "   'rank': '5',\n",
       "   'rankInten': '0',\n",
       "   'rankOldAndNew': 'OLD',\n",
       "   'movieCd': '20135304',\n",
       "   'movieNm': '극장판 포켓몬스터DP: 기라티나와 하늘의 꽃다발 쉐이미',\n",
       "   'openDt': '2022-06-01',\n",
       "   'salesAmt': '23425900',\n",
       "   'salesShare': '0.7',\n",
       "   'salesInten': '8548760',\n",
       "   'salesChange': '57.5',\n",
       "   'salesAcc': '3761286650',\n",
       "   'audiCnt': '2664',\n",
       "   'audiInten': '858',\n",
       "   'audiChange': '47.5',\n",
       "   'audiAcc': '402252',\n",
       "   'scrnCnt': '235',\n",
       "   'showCnt': '297'},\n",
       "  {'rnum': '6',\n",
       "   'rank': '6',\n",
       "   'rankInten': '0',\n",
       "   'rankOldAndNew': 'OLD',\n",
       "   'movieCd': '20212855',\n",
       "   'movieNm': '닥터 스트레인지: 대혼돈의 멀티버스',\n",
       "   'openDt': '2022-05-04',\n",
       "   'salesAmt': '20302220',\n",
       "   'salesShare': '0.6',\n",
       "   'salesInten': '6287020',\n",
       "   'salesChange': '44.9',\n",
       "   'salesAcc': '62442681020',\n",
       "   'audiCnt': '1894',\n",
       "   'audiInten': '522',\n",
       "   'audiChange': '38',\n",
       "   'audiAcc': '5864931',\n",
       "   'scrnCnt': '63',\n",
       "   'showCnt': '106'},\n",
       "  {'rnum': '7',\n",
       "   'rank': '7',\n",
       "   'rankInten': '5',\n",
       "   'rankOldAndNew': 'OLD',\n",
       "   'movieCd': '20224468',\n",
       "   'movieNm': '애프터 양',\n",
       "   'openDt': '2022-06-01',\n",
       "   'salesAmt': '13696100',\n",
       "   'salesShare': '0.4',\n",
       "   'salesInten': '8048500',\n",
       "   'salesChange': '142.5',\n",
       "   'salesAcc': '196123390',\n",
       "   'audiCnt': '1850',\n",
       "   'audiInten': '1262',\n",
       "   'audiChange': '214.6',\n",
       "   'audiAcc': '19663',\n",
       "   'scrnCnt': '51',\n",
       "   'showCnt': '72'},\n",
       "  {'rnum': '8',\n",
       "   'rank': '8',\n",
       "   'rankInten': '0',\n",
       "   'rankOldAndNew': 'NEW',\n",
       "   'movieCd': '20218904',\n",
       "   'movieNm': '코다',\n",
       "   'openDt': '2021-08-31',\n",
       "   'salesAmt': '5136000',\n",
       "   'salesShare': '0.2',\n",
       "   'salesInten': '5136000',\n",
       "   'salesChange': '100',\n",
       "   'salesAcc': '680104599',\n",
       "   'audiCnt': '610',\n",
       "   'audiInten': '610',\n",
       "   'audiChange': '100',\n",
       "   'audiAcc': '74880',\n",
       "   'scrnCnt': '5',\n",
       "   'showCnt': '5'},\n",
       "  {'rnum': '9',\n",
       "   'rank': '9',\n",
       "   'rankInten': '17',\n",
       "   'rankOldAndNew': 'OLD',\n",
       "   'movieCd': '20196906',\n",
       "   'movieNm': '스텔라',\n",
       "   'openDt': '2022-04-06',\n",
       "   'salesAmt': '3109000',\n",
       "   'salesShare': '0.1',\n",
       "   'salesInten': '1492000',\n",
       "   'salesChange': '92.3',\n",
       "   'salesAcc': '860750300',\n",
       "   'audiCnt': '587',\n",
       "   'audiInten': '356',\n",
       "   'audiChange': '154.1',\n",
       "   'audiAcc': '95349',\n",
       "   'scrnCnt': '2',\n",
       "   'showCnt': '3'},\n",
       "  {'rnum': '10',\n",
       "   'rank': '10',\n",
       "   'rankInten': '6',\n",
       "   'rankOldAndNew': 'OLD',\n",
       "   'movieCd': '20218527',\n",
       "   'movieNm': '이공삼칠',\n",
       "   'openDt': '2022-06-08',\n",
       "   'salesAmt': '5347500',\n",
       "   'salesShare': '0.2',\n",
       "   'salesInten': '536580',\n",
       "   'salesChange': '11.2',\n",
       "   'salesAcc': '26367520',\n",
       "   'audiCnt': '509',\n",
       "   'audiInten': '38',\n",
       "   'audiChange': '8.1',\n",
       "   'audiAcc': '3089',\n",
       "   'scrnCnt': '84',\n",
       "   'showCnt': '114'}]}"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "result1 = movie['boxOfficeResult']\n",
    "result1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "112829d0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "322315"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "result2 = result1['dailyBoxOfficeList']\n",
    "result2[0]['audiCnt']\n",
    "aud_sum = 0\n",
    "for i in range(len(result2)):\n",
    "    aud_sum += int(result2[i]['audiCnt'])\n",
    "aud_sum"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9d89c463",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ce6ea281",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "08703a16",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "434a89e8",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "eaddec43",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "56697a0f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "92940684",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "534c3093",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "09a7527b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fe5b41cc",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a662b04c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fd75ebeb",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b0cbe55a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e9443f3d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a1c73555",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3e9f9027",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2d877bd4",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a10f7cb2",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cb87e4ab",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5d5c6cf6",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "366197b3",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5db3ef43",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "016e4e77",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bbbbdfb1",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "74a6f2d9",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a0972308",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5b92d601",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "57bf8b32",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5547a461",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e36e4859",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a9dce3c3",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5918775f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "29226b28",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6b1d8436",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f9c36dfb",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8a7871bb",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2ffd40e3",
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
