{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "78b7b308",
   "metadata": {},
   "outputs": [],
   "source": [
    "ip_dic = {\"192.168.70.100\":'우리열',\"192.168.70.160\":\"이명기\",\"192.168.70.128\":\"근돼\",\"192.168.70.249\":\"슬구\",\"192.168.70.228\":\"윤규\"}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "bb914ec6",
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
      " * Running on http://192.168.70.160:5048/ (Press CTRL+C to quit)\n",
      "192.168.70.160 - - [22/Sep/2022 12:28:11] \"GET / HTTP/1.1\" 200 -\n",
      "192.168.70.160 - - [22/Sep/2022 12:28:19] \"GET /sel_emp HTTP/1.1\" 200 -\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask,redirect\n",
    "\n",
    "# app : Server실행, 경로를 잡아주는 객체\n",
    "app = Flask(__name__)\n",
    "\n",
    "@app.route('/')\n",
    "def index():\n",
    "      return \"ㅎㅇㅎㅇ\"\n",
    "#     url = \"https://lee48.dothome.co.kr\"\n",
    "#     return redirect(url)\n",
    "\n",
    "@app.route('/sel_emp')\n",
    "def sel_emp():    \n",
    "    dao = DAO()\n",
    "    r = dao.select()\n",
    "    result = '</br>'.join(map(str,r))\n",
    "    \n",
    "    return result\n",
    "    \n",
    "if __name__ == '__main__' :\n",
    "    app.run(host=\"192.168.70.160\", port=5048)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7cb5e782",
   "metadata": {},
   "source": [
    "## Oracle - Python 연결 Lib 설치"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3dde8569",
   "metadata": {},
   "outputs": [],
   "source": [
    "!pip install cx_oracle"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f7cc9fbd",
   "metadata": {},
   "source": [
    "## Instant Client 설치\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "95b9fa90",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "LOCATION = r\"C:\\Users\\AI\\instantclient_21_6\"\n",
    "os.environ['PATH'] = LOCATION + \":\" + os.environ['PATH']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "544e6ba0",
   "metadata": {},
   "outputs": [],
   "source": [
    "import cx_Oracle"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "165b1979",
   "metadata": {},
   "source": [
    "# DB 연결\n",
    "- 1) Connection\n",
    "- 2) Cursor\n",
    "- 3) Execute\n",
    "- 4) Close"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "abf775c2",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 1. Connection\n",
    "db_id = 'hr'\n",
    "db_pw = 'hr'\n",
    "db_url = 'localhost:1521/xe' # 127.0.0.1 # 같은인터넷망,방화벽해제 되어있을시 상대방 DB 접속가능\n",
    "conn = cx_Oracle.connect(db_id, db_pw, db_url)\n",
    "\n",
    "# 2. Cursor\n",
    "curs = conn.cursor()\n",
    "\n",
    "# 3. Execute (실행)\n",
    "sql = 'select last_name, salary from employees'\n",
    "result = curs.execute(sql)\n",
    "result.fetchall()\n",
    "\n",
    "# 4. Close\n",
    "# 연결 통로를 닫을 때는, 열었던 역순으로 닫는다\n",
    "if curs != None :\n",
    "    curs.close()\n",
    "if conn != None :\n",
    "    conn.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "cd35b98f",
   "metadata": {},
   "outputs": [],
   "source": [
    "import cx_Oracle\n",
    "import pandas as pd\n",
    "class DAO :\n",
    "    def select(self):\n",
    "        db_id = 'hr'\n",
    "        db_pw = 'hr'\n",
    "        db_url = 'localhost:1521/xe'\n",
    "        conn = cx_Oracle.connect(db_id, db_pw, db_url)\n",
    "        \n",
    "        curs = conn.cursor()\n",
    "        \n",
    "        sql = \"select last_name, salary from employees\"\n",
    "        result = curs.execute(sql)\n",
    "        r = result.fetchall() # db에서 조회 요청한 것들을 모두 긁어옴 \n",
    "        \n",
    "        if curs != None : # 커서가 안열려있다면 닫아라\n",
    "            curs.close()\n",
    "        if conn != None : # 연결이 끊기면 꺼라\n",
    "            conn.close()\n",
    "            \n",
    "        return r\n",
    "        \n",
    "    def select_df(self):\n",
    "        db_id = 'hr'\n",
    "        db_pw = 'hr'\n",
    "        db_url = 'localhost:1521/xe'\n",
    "        conn = cx_Oracle.connect(db_id, db_pw, db_url)\n",
    "        \n",
    "        sql = 'select last_name, salary from employees'\n",
    "        df = pd.read_sql(sql, conn)\n",
    "        conn.close()\n",
    "        return df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "19533bb1",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\AI\\Anaconda3\\lib\\site-packages\\pandas\\io\\sql.py:761: UserWarning: pandas only support SQLAlchemy connectable(engine/connection) ordatabase string URI or sqlite3 DBAPI2 connectionother DBAPI2 objects are not tested, please consider using SQLAlchemy\n",
      "  warnings.warn(\n"
     ]
    },
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
       "      <th>LAST_NAME</th>\n",
       "      <th>SALARY</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>King</td>\n",
       "      <td>24000.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Kochhar</td>\n",
       "      <td>17000.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>De Haan</td>\n",
       "      <td>17000.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Greenberg</td>\n",
       "      <td>12008.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>Raphaely</td>\n",
       "      <td>11000.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>45</th>\n",
       "      <td>Russell</td>\n",
       "      <td>14000.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>46</th>\n",
       "      <td>Partners</td>\n",
       "      <td>13500.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>47</th>\n",
       "      <td>Errazuriz</td>\n",
       "      <td>12000.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>48</th>\n",
       "      <td>Cambrault</td>\n",
       "      <td>11000.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>49</th>\n",
       "      <td>Zlotkey</td>\n",
       "      <td>10500.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50</th>\n",
       "      <td>Tucker</td>\n",
       "      <td>10000.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>56</th>\n",
       "      <td>King</td>\n",
       "      <td>10000.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>62</th>\n",
       "      <td>Vishney</td>\n",
       "      <td>10500.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>68</th>\n",
       "      <td>Ozer</td>\n",
       "      <td>11500.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>69</th>\n",
       "      <td>Bloom</td>\n",
       "      <td>10000.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>74</th>\n",
       "      <td>Abel</td>\n",
       "      <td>11000.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>101</th>\n",
       "      <td>Hartstein</td>\n",
       "      <td>13000.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>104</th>\n",
       "      <td>Baer</td>\n",
       "      <td>10000.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>105</th>\n",
       "      <td>Higgins</td>\n",
       "      <td>12008.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     LAST_NAME   SALARY\n",
       "0         King  24000.0\n",
       "1      Kochhar  17000.0\n",
       "2      De Haan  17000.0\n",
       "8    Greenberg  12008.0\n",
       "14    Raphaely  11000.0\n",
       "45     Russell  14000.0\n",
       "46    Partners  13500.0\n",
       "47   Errazuriz  12000.0\n",
       "48   Cambrault  11000.0\n",
       "49     Zlotkey  10500.0\n",
       "50      Tucker  10000.0\n",
       "56        King  10000.0\n",
       "62     Vishney  10500.0\n",
       "68        Ozer  11500.0\n",
       "69       Bloom  10000.0\n",
       "74        Abel  11000.0\n",
       "101  Hartstein  13000.0\n",
       "104       Baer  10000.0\n",
       "105    Higgins  12008.0"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dao = DAO()\n",
    "df = dao.select_df()\n",
    "\n",
    "df[df['SALARY']>=10000]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "b335d7f2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "name : King / salary : 24000.0\n",
      "name : Kochhar / salary : 17000.0\n",
      "name : De Haan / salary : 17000.0\n",
      "name : Hunold / salary : 9000.0\n",
      "name : Ernst / salary : 6000.0\n",
      "name : Austin / salary : 4800.0\n",
      "name : Pataballa / salary : 4800.0\n",
      "name : Lorentz / salary : 4200.0\n",
      "name : Greenberg / salary : 12008.0\n",
      "name : Faviet / salary : 9000.0\n",
      "name : Chen / salary : 8200.0\n",
      "name : Sciarra / salary : 7700.0\n",
      "name : Urman / salary : 7800.0\n",
      "name : Popp / salary : 6900.0\n",
      "name : Raphaely / salary : 11000.0\n",
      "name : Khoo / salary : 3100.0\n",
      "name : Baida / salary : 2900.0\n",
      "name : Tobias / salary : 2800.0\n",
      "name : Himuro / salary : 2600.0\n",
      "name : Colmenares / salary : 2500.0\n",
      "name : Weiss / salary : 8000.0\n",
      "name : Fripp / salary : 8200.0\n",
      "name : Kaufling / salary : 7900.0\n",
      "name : Vollman / salary : 6500.0\n",
      "name : Mourgos / salary : 5800.0\n",
      "name : Nayer / salary : 3200.0\n",
      "name : Mikkilineni / salary : 2700.0\n",
      "name : Landry / salary : 2400.0\n",
      "name : Markle / salary : 2200.0\n",
      "name : Bissot / salary : 3300.0\n",
      "name : Atkinson / salary : 2800.0\n",
      "name : Marlow / salary : 2500.0\n",
      "name : Olson / salary : 2100.0\n",
      "name : Mallin / salary : 3300.0\n",
      "name : Rogers / salary : 2900.0\n",
      "name : Gee / salary : 2400.0\n",
      "name : Philtanker / salary : 2200.0\n",
      "name : Ladwig / salary : 3600.0\n",
      "name : Stiles / salary : 3200.0\n",
      "name : Seo / salary : 2700.0\n",
      "name : Patel / salary : 2500.0\n",
      "name : Rajs / salary : 3500.0\n",
      "name : Davies / salary : 3100.0\n",
      "name : Matos / salary : 2600.0\n",
      "name : Vargas / salary : 2500.0\n",
      "name : Russell / salary : 14000.0\n",
      "name : Partners / salary : 13500.0\n",
      "name : Errazuriz / salary : 12000.0\n",
      "name : Cambrault / salary : 11000.0\n",
      "name : Zlotkey / salary : 10500.0\n",
      "name : Tucker / salary : 10000.0\n",
      "name : Bernstein / salary : 9500.0\n",
      "name : Hall / salary : 9000.0\n",
      "name : Olsen / salary : 8000.0\n",
      "name : Cambrault / salary : 7500.0\n",
      "name : Tuvault / salary : 7000.0\n",
      "name : King / salary : 10000.0\n",
      "name : Sully / salary : 9500.0\n",
      "name : McEwen / salary : 9000.0\n",
      "name : Smith / salary : 8000.0\n",
      "name : Doran / salary : 7500.0\n",
      "name : Sewall / salary : 7000.0\n",
      "name : Vishney / salary : 10500.0\n",
      "name : Greene / salary : 9500.0\n",
      "name : Marvins / salary : 7200.0\n",
      "name : Lee / salary : 6800.0\n",
      "name : Ande / salary : 6400.0\n",
      "name : Banda / salary : 6200.0\n",
      "name : Ozer / salary : 11500.0\n",
      "name : Bloom / salary : 10000.0\n",
      "name : Fox / salary : 9600.0\n",
      "name : Smith / salary : 7400.0\n",
      "name : Bates / salary : 7300.0\n",
      "name : Kumar / salary : 6100.0\n",
      "name : Abel / salary : 11000.0\n",
      "name : Hutton / salary : 8800.0\n",
      "name : Taylor / salary : 8600.0\n",
      "name : Livingston / salary : 8400.0\n",
      "name : Grant / salary : 7000.0\n",
      "name : Johnson / salary : 6200.0\n",
      "name : Taylor / salary : 3200.0\n",
      "name : Fleaur / salary : 3100.0\n",
      "name : Sullivan / salary : 2500.0\n",
      "name : Geoni / salary : 2800.0\n",
      "name : Sarchand / salary : 4200.0\n",
      "name : Bull / salary : 4100.0\n",
      "name : Dellinger / salary : 3400.0\n",
      "name : Cabrio / salary : 3000.0\n",
      "name : Chung / salary : 3800.0\n",
      "name : Dilly / salary : 3600.0\n",
      "name : Gates / salary : 2900.0\n",
      "name : Perkins / salary : 2500.0\n",
      "name : Bell / salary : 4000.0\n",
      "name : Everett / salary : 3900.0\n",
      "name : McCain / salary : 3200.0\n",
      "name : Jones / salary : 2800.0\n",
      "name : Walsh / salary : 3100.0\n",
      "name : Feeney / salary : 3000.0\n",
      "name : OConnell / salary : 2600.0\n",
      "name : Grant / salary : 2600.0\n",
      "name : Whalen / salary : 4400.0\n",
      "name : Hartstein / salary : 13000.0\n",
      "name : Fay / salary : 6000.0\n",
      "name : Mavris / salary : 6500.0\n",
      "name : Baer / salary : 10000.0\n",
      "name : Higgins / salary : 12008.0\n",
      "name : Gietz / salary : 8300.0\n"
     ]
    }
   ],
   "source": [
    "dao = DAO()\n",
    "r = dao.select()\n",
    "\n",
    "# for name, salary in r :\n",
    "#     print(f'name : {name} / salary : {salary}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "60ded498",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "str"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Python 점수를 저장하려고 함\n",
    "score = 100\n",
    "# score의 타입은??\n",
    "type(score)\n",
    "\n",
    "# 이름을 저장하려고함\n",
    "name = '이명기'\n",
    "\n",
    "type(name)\n",
    "\n",
    "# 이명기의 Python 점수를 동시에 저장\n",
    "# class를 사용!!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "689bf056",
   "metadata": {},
   "outputs": [],
   "source": [
    "# VO (Value Object)\n",
    "# 사용자 정의 데이터 타입\n",
    "\n",
    "# Design Parttern\n",
    "# 코드를 작성\n",
    "# Refactoring\n",
    "\n",
    "# 가장 보편적, 가장 많이 사용하는 약속된 Design \n",
    "# MVC : Model, View, Controller"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "16a80e30",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Scores :\n",
    "    \n",
    "    name = \"\"\n",
    "    score = 0\n",
    "    \n",
    "    def print_info(self):\n",
    "        print(f'이름 : {self.name} / 점수 : {self.score}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "68aa5254",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "이명기 100\n"
     ]
    }
   ],
   "source": [
    "s1 = Scores()\n",
    "s1.name = \"이명기\"\n",
    "s1.score = 100\n",
    "\n",
    "print(s1.name, s1.score)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "44727842",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0bcf2555",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "054c3b65",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5babf02e",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7a9a8791",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "29486551",
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
