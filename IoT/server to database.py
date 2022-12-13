{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "81603eba",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'pymysql'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "Input \u001b[1;32mIn [2]\u001b[0m, in \u001b[0;36m<cell line: 1>\u001b[1;34m()\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mpymysql\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mps\u001b[39;00m\n\u001b[0;32m      2\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mpandas\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mpd\u001b[39;00m\n\u001b[0;32m      3\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mdatetime\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m datetime\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'pymysql'"
     ]
    }
   ],
   "source": [
    "import pymysql as ps\n",
    "import pandas as pd\n",
    "from datetime import datetime\n",
    "\n",
    "def con():\n",
    "    conn = ps.connect(host='localhost', user='root', passwd='12345', db='aqu4men')\n",
    "    return conn\n",
    "\n",
    "def insert_db(table, calumns, values): #calumns, values\n",
    "    conn = con()\n",
    "    curs = conn.cursor()\n",
    "    sql = f\"insert into {table} {calumns} values {values};\"\n",
    "    curs.execute(sql)\n",
    "    conn.commit()\n",
    "    curs.close()\n",
    "    conn.close()\n",
    "    return sql\n",
    "\n",
    "def select_db(calumn,table, where):\n",
    "    conn = con()\n",
    "    curs = conn.cursor()\n",
    "    sql = f\"selet {calumn} from {table} where {where} \"\n",
    "    curs.execute(sql)\n",
    "    result = curs.fetchall()\n",
    "    print(result)\n",
    "    curs.close()\n",
    "    conn.close()\n",
    "    return sql"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "8bc99591",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1650ml\n"
     ]
    }
   ],
   "source": [
    "#목표섭취량 계산 공식\n",
    "conn = con()\n",
    "curs = conn.cursor()\n",
    "id = 1\n",
    "sql = f'select user_weight from t_user where {int(id)} = user_id'\n",
    "curs.execute(sql)\n",
    "result = curs.fetchall()  #튜플형태로 반환\n",
    "current_objective = result[0][0]*33\n",
    "print(f'{current_objective}'+'ml')\n",
    "curs.close()\n",
    "conn.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "aac33c98",
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "200ml\n"
     ]
    }
   ],
   "source": [
    "#현재섭취량(1) 계산 공식 (이전 무게 - 현재 무게)\n",
    "conn = con()\n",
    "curs = conn.cursor()\n",
    "id = 1\n",
    "sql = f'select weight, wv_time from t_coasters where {int(id)} = user_id order by wv_time desc limit 2'\n",
    "curs.execute(sql)\n",
    "result = curs.fetchall()\n",
    "coasters=result[1][0]-result[0][0]\n",
    "print(f'{coasters}'+'ml')\n",
    "curs.close()\n",
    "conn.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "02267daf",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    x1   y1   x2   y2   x3   y3   x4   y4   x5   y5  ...  y26  x27  y27  x28  \\\n",
      "0  200  100  200  100  200  100  200  100  200  100  ...  100  200  100  200   \n",
      "\n",
      "   y28  x29  y29  x30  y30  t  \n",
      "0  100  200  100  200  100  3  \n",
      "\n",
      "[1 rows x 61 columns]\n"
     ]
    }
   ],
   "source": [
    "#현재 섭취량(2) 계산 공식 \n",
    "conn = con()\n",
    "curs = conn.cursor()\n",
    "id = 1\n",
    "sql = f'select x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10,x11,y11,x12,y12,x13,y13,x14,y14,x15,y15,x16,y16,x17,y17,x18,y18,x19,y19,x20,y20,\\\n",
    "x21,y21,x22,y22,x23,y23,x24,y24,x25,y25,x26,y26,x27,y27,x28,y28,x29,y29,x30,y30,t from t_cupholder where {int(id)} = user_id order by av_time desc limit 1;'\n",
    "curs.execute(sql)\n",
    "result = curs.fetchall()\n",
    "df = pd.DataFrame(result, columns=['x1','y1','x2','y2','x3','y3','x4','y4','x5','y5',\n",
    "                                   'x6','y6','x7','y7','x8','y8','x9','y9','x10','y10',\n",
    "                                   'x11','y11','x12','y12','x13','y13','x14','y14','x15','y15',\n",
    "                                   'x16','y16','x17','y17','x18','y18','x19','y19','x20','y20',\n",
    "                                   'x21','y21','x22','y22','x23','y23','x24','y24','x25','y25',\n",
    "                                   'x26','y26','x27','y27','x28','y28','x29','y29','x30','y30','t'])\n",
    "\n",
    "#여기에 머신러닝\n",
    "\n",
    "# sql2 = f'insert into t_cupholder (label) values ({pre})'\n",
    "print(df)\n",
    "\n",
    "cupholder=0\n",
    "\n",
    "curs.close()\n",
    "conn.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "dc22fef4",
   "metadata": {},
   "outputs": [],
   "source": [
    "#남은 섭취량\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "32cdf3ac",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "((datetime.datetime(2022, 8, 20, 21, 51, 50),),)\n",
      "2022-08-20 23:21:50.993084\n"
     ]
    }
   ],
   "source": [
    "#알림 계산 공식 (현재시각 - [무게or각도변화시각])\n",
    "conn = con()\n",
    "curs = conn.cursor()\n",
    "id = 1\n",
    "sql = f'select wv_time from t_coasters where {int(id)} = user_id order by wv_time desc limit 1'\n",
    "curs.execute(sql)\n",
    "result = curs.fetchall()\n",
    "sql2 = f'select av_time from t_cupholder where {int(id)} = user_id order by av_time desc limit 1'\n",
    "curs.execute(sql2)\n",
    "result2 = curs.fetchall()\n",
    "if result>result2 :\n",
    "    result=result\n",
    "else:\n",
    "    result=result2\n",
    "print(result)\n",
    "curs.close()\n",
    "conn.close()\n",
    "# Q. 데이터 타입을 모르겠음 (어떻게 조회하고 현재시각과 비교해야할지 모르겠음)\n",
    "print(datetime.now())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "e83e7b99",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (4245623013.py, line 22)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Input \u001b[1;32mIn [6]\u001b[1;36m\u001b[0m\n\u001b[1;33m    select_db =\u001b[0m\n\u001b[1;37m                ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "#달성 계산 공식 (current_objective -(coasters+cupholder) <= 0)\n",
    "id = 1\n",
    "\n",
    "#첫째 날\n",
    "if (current_objective - (coasters+cupholder)) <= 0:\n",
    "    table = \"t_achievement\"\n",
    "    calumns = '(a_time, user_id, 1st_achievement)'\n",
    "    values = f\"(now(), {int(id)}, 'T')\"\n",
    "    insert_db(table, calumns, values)\n",
    "\n",
    "#둘째 날    \n",
    "if (current_objective - (coasters+cupholder)) <= 0:\n",
    "    table = \"t_achievement\"\n",
    "    calumns = '(a_time, user_id, 1st_achievement, 2nd_achievement)'\n",
    "    values = f\"(now(), {int(id)}, 'T', 'T')\"\n",
    "    insert_db(table, calumns, values)    \n",
    "    \n",
    "#셋째 날\n",
    "if 0 <= 0:\n",
    "    table = \"t_achievement\"\n",
    "    calumns = '(a_time, user_id, 1st_achievement, 2nd_achievement, reward, nft_index)'\n",
    "    values = f\"(now(), {int(id)}, 'T', 'T', 'T', )\"\n",
    "    insert_db(table, calumns, values)    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "2407afc8",
   "metadata": {},
   "outputs": [
    {
     "ename": "IndentationError",
     "evalue": "expected an indented block (1493939005.py, line 28)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Input \u001b[1;32mIn [1]\u001b[1;36m\u001b[0m\n\u001b[1;33m    @app.route('/collection/<int:id>', methods=['GET', 'POST'])\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mIndentationError\u001b[0m\u001b[1;31m:\u001b[0m expected an indented block\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask, request, redirect, jsonify\n",
    "from flask_cors import CORS, cross_origin\n",
    "\n",
    "app = Flask(__name__)\n",
    "cors = CORS(app)\n",
    "app.config[\"CORS_HEADERS\"] = 'Content-Type'\n",
    "\n",
    "\n",
    "\n",
    "#메인 페이지\n",
    "@app.route('/main/<int:id>',methods=['GET', 'POST'])\n",
    "def main():\n",
    "    return 'main'\n",
    "\n",
    "#대쉬보드 페이지\n",
    "@app.route('/dashboard/<int:id>', methods=['GET', 'POST'])\n",
    "def dashboard(id):           \n",
    "#     title = ''\n",
    "#     body= ''\n",
    "#     for topic in topics:\n",
    "#         if id == topic['id']:\n",
    "#             title = topic['title']\n",
    "#             body = topic['body']\n",
    "#             break\n",
    "#     return template(getContetns(), f'<h2>{title}</h2>{body}')\n",
    "\n",
    "#컬렉션 페이지\n",
    "@app.route('/collection/<int:id>', methods=['GET', 'POST'])\n",
    "def collection(id):\n",
    "    return 'collection'\n",
    "\n",
    "\n",
    "\n",
    "#설정 페이지\n",
    "@app.route('/setting/<int:id>', methods=['GET', 'POST'])\n",
    "def setting():\n",
    "    return 'setting'\n",
    "\n",
    "\n",
    "\n",
    "#목표 섭취량\n",
    "def cur_object(id):\n",
    "    calumns\n",
    "    table\n",
    "    object = select()\n",
    "\n",
    "# #현재섭취량\n",
    "# @app.route('/current intake')\n",
    "# def \n",
    "\n",
    "\n",
    "# #남은 섭취량\n",
    "\n",
    "\n",
    "# #알림\n",
    "# @app.route('/alret')\n",
    "# def\n",
    "\n",
    "\n",
    "# #달성\n",
    "# @app.route('/achivement')\n",
    "# def\n",
    "\n",
    "\n",
    "# #보상획득\n",
    "# @app.route('/reward')\n",
    "# def\n",
    "\n",
    "\n",
    "@app.route('/insert/loadcell', methods=['GET'])\n",
    "def insert_loadcell():\n",
    "    read = \"can not read\"\n",
    "    if request.method == 'GET':\n",
    "        request.get_json()\n",
    "        read = request.args['loadcell']\n",
    "        print('sensing data : ',read)\n",
    "        \n",
    "        table = 'coasters'\n",
    "        print('table :',table)\n",
    "        calumns= '(product_id, user_id, wv_time, weight)'\n",
    "        print('calumns :',calumns)\n",
    "        values = f'(\"productID\", \"1\", now(), {int(read)})'\n",
    "        print('values :',values)\n",
    "        sql=insert_db(table, calumns, values)\n",
    "        print(sql)\n",
    "        return \"value of loadcell is %s\" %read \n",
    "    else:\n",
    "        return read\n",
    "    \n",
    "\n",
    "@app.route('/insert/mpu', methods=['GET'])\n",
    "def insert_mpu():\n",
    "    read = \"can not read\"\n",
    "    if request.method == 'GET':\n",
    "        request.get_json()\n",
    "        x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10 = request.args['x1'],request.args['y1'],request.args['x2'],\\\n",
    "request.args['y2'],request.args['x3'],request.args['y3'],request.args['x4'],request.args['y4'],request.args['x5'],\\\n",
    "request.args['y5'],request.args['x6'],request.args['y6'],request.args['x7'],request.args['y7'],request.args['x8'],\\\n",
    "request.args['y8'],request.args['x9'],request.args['y9'],request.args['x10'],request.args['y10']\n",
    "        x11,y11,x12,y12,x13,y13,x14,y14,x15,y15,x16,y16,x17,y17,x18,y18,x19,y19,x20,y20 = request.args['x11'],request.args['y11'],\\\n",
    "request.args['x12'],request.args['y12'],request.args['x13'],request.args['y13'],request.args['x14'],request.args['y14'],\\\n",
    "request.args['x15'],request.args['y15'],request.args['x16'],request.args['y16'],request.args['x17'],request.args['y17'],\\\n",
    "request.args['x18'],request.args['y18'],request.args['x19'],request.args['y19'],request.args['x20'],request.args['y20']\n",
    "        x21,y21,x22,y22,x23,y23,x24,y24,x25,y25,x26,y26,x27,y27,x28,y28,x29,y29,x30,y30 = request.args['x21'],request.args['y21'],\\\n",
    "request.args['x22'],request.args['y22'],request.args['x23'],request.args['y23'],request.args['x24'],request.args['y24'],\\\n",
    "request.args['x25'],request.args['y25'],request.args['x26'],request.args['y26'],request.args['x27'],request.args['y27'],\\\n",
    "request.args['x28'],request.args['y28'],request.args['x29'],request.args['y29'],request.args['x30'],request.args['y30']\n",
    "#         T,Label = request.args['T'],request.args['Label']\n",
    "        t=3\n",
    "        label=150\n",
    "        table = 't_cupholder'\n",
    "        print('table :',table)\n",
    "        calumns= '(product_id, user_id, av_time, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8, x9, y9, x10, y10, X11,\\\n",
    "y11, x12, y12, x13, y13, x14, y14, x15, y15, x16, y16, x17, y17, x18, y18, x19, y19, x20, y20, x21, y21, x22, y22, x23, y23,\\\n",
    "x24, y24, x25, y25, x26, y26, x27, y27, x28, y28, x29, y29, x30, y30, t, label)'\n",
    "        print('calumns :',calumns)\n",
    "        values = f'(\"productID\", \"1\", now(), {int(x1)}, {int(y1)}, {int(x2)}, {int(y2)}, {int(x3)}, {int(y3)}, {int(x4)}, {int(y4)},\\\n",
    "{int(x5)}, {int(y5)}, {int(x6)}, {int(y6)}, {int(x7)}, {int(y7)}, {int(x8)}, {int(y8)}, {int(x9)}, {int(y9)}, {int(x10)},\\\n",
    "{int(y10)}, {int(x11)}, {int(y11)}, {int(x12)}, {int(y12)}, {int(x13)}, {int(y13)}, {int(x14)}, {int(y14)}, {int(x15)},\\\n",
    "{int(y15)}, {int(x16)}, {int(y16)}, {int(x17)}, {int(y17)}, {int(x18)}, {int(y18)}, {int(x19)}, {int(y19)}, {int(x20)},\\\n",
    "{int(y20)}, {int(x21)}, {int(y21)}, {int(x22)}, {int(y22)}, {int(x23)}, {int(y23)}, {int(x24)}, {int(y24)}, {int(x25)},\\\n",
    "{int(y25)}, {int(x26)}, {int(y26)}, {int(x27)}, {int(y27)}, {int(x28)}, {int(y28)}, {int(x29)}, {int(y29)}, {int(x30)},\\\n",
    "{int(y30)}, {t}, {label})'\n",
    "        print('values :',values)\n",
    "        sql=insert_db(table, calumns, values)\n",
    "        print(sql)\n",
    "        return \"value of MPU6050 is done\"\n",
    "    \n",
    "    else:\n",
    "        return read\n",
    "\n",
    "@app.route('/react/test')\n",
    "def react_test():\n",
    "    return '{\"name\":\"1hour\", \"userMean\":\"4000\", \"ActiveUser\" : \"2400\"}'\n",
    "\n",
    "\n",
    "@app.route('/select')\n",
    "def select():\n",
    "    result = select_db()\n",
    "    print(result)\n",
    "    return 'you got the values'\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run(host='192.168.30.178', port=5020)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cdc50d6e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# from flask_cors import CORS, cross_origin\n",
    "# from flask import Flask, request, redirect, jsonify\n",
    "# app = Flask(__name__)\n",
    "# cors = CORS(app)\n",
    "# app.config[\"CORS_HEADERS\"] = 'Content-Type'\n",
    "\n",
    "# @app.route('/select')\n",
    "# def main():\n",
    "#     return '{\"user\":\"main222\"}'\n",
    "\n",
    "# if __name__ == '__main__':\n",
    "#     app.run(host='192.168.30.178', port=5020)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1b80ac92",
   "metadata": {},
   "source": [
    "http://192.168.30.178:5020/insert/mpu?x1=200&y1=100&x2=200&y2=100&x3=200&y3=100&x4=200&y4=100&x5=200&y5=100&x6=200&y6=100&x7=200&y7=100&x8=200&y8=100&x9=200&y9=100&x10=200&y10=100&x11=200&y11=100&x12=200&y12=100&x13=200&y13=100&x14=200&y14=100&x15=200&y15=100&x16=200&y16=100&x17=200&y17=100&x18=200&y18=100&x19=200&y19=100&x20=200&y20=100&x21=200&y21=100&x22=200&y22=100&x23=200&y23=100&x24=200&y24=100&x25=200&y25=100&x26=200&y26=100&x27=200&y27=100&x28=200&y28=100&x29=200&y29=100&x30=200&y30=100"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8fd4ee8c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b8a0fa2b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3053450f",
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
