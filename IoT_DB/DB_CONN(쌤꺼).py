{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "14023f7a",
   "metadata": {},
   "outputs": [],
   "source": [
    "ip_dic = {'192.168.0.38':'나예호', '192.168.70.160':'이명기'}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "db9f119a",
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
      " * Running on http://192.168.0.38:5021/ (Press CTRL+C to quit)\n",
      "192.168.0.38 - - [22/Sep/2022 12:28:06] \"GET / HTTP/1.1\" 200 -\n",
      "192.168.0.38 - - [22/Sep/2022 12:28:10] \"GET /sel_emp HTTP/1.1\" 200 -\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask, redirect\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "@app.route('/')\n",
    "def index():\n",
    "    return 'Hello World'\n",
    "\n",
    "@app.route('/sel_emp')\n",
    "def sel_emp():\n",
    "    dao = DAO()\n",
    "    r = dao.select()\n",
    "    result = '</br>'.join(map(str, r))\n",
    "    \n",
    "    return result\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run(host='192.168.70.94', port=5048)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b86db75c",
   "metadata": {},
   "source": [
    "#### Oracle - Python 연결 Lib 설치"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bcc85341",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "!pip install cx_Oracle"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ec0f3f80",
   "metadata": {},
   "source": [
    "#### Instant Client 설치\n",
    "- https://www.oracle.com/kr/database/technologies/instant-client/winx64-64-downloads.html"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "60be3446",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "LOCATION = r\"C:\\Users\\user\\instantclient_21_6\"\n",
    "os.environ[\"PATH\"] = LOCATION + \";\" + os.environ[\"PATH\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "14de5e11",
   "metadata": {},
   "outputs": [],
   "source": [
    "import cx_Oracle"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9e314556",
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
   "execution_count": null,
   "id": "bd3e7cb4",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 1. Connection\n",
    "db_id = 'hr'\n",
    "db_pw = 'hr'\n",
    "db_url = '127.0.0.1:1521/xe'\n",
    "conn = cx_Oracle.connect(db_id, db_pw, db_url)\n",
    "\n",
    "# 2. Cursor\n",
    "curs = conn.cursor()\n",
    "\n",
    "# 3. Execute\n",
    "sql = 'select last_name, salary from employees'\n",
    "result = curs.execute(sql)\n",
    "result.fetchall()\n",
    "\n",
    "# 4. Close\n",
    "# 연결 통로를 닫을 때는, 열었던 역순으로 닫는다\n",
    "if curs != None:\n",
    "    curs.close()\n",
    "if conn != None:\n",
    "    conn.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "c99ec443",
   "metadata": {},
   "outputs": [],
   "source": [
    "import cx_Oracle\n",
    "import pandas as pd\n",
    "class DAO:\n",
    "    \n",
    "    def select(self):\n",
    "        conn, curs = self.conn_db()\n",
    "        sql = 'select last_name, salary from employees'\n",
    "        result = curs.execute(sql)\n",
    "        r = result.fetchall()\n",
    "        if curs != None:\n",
    "            curs.close()\n",
    "        if conn != None:\n",
    "            conn.close()\n",
    "        return r\n",
    "    \n",
    "    def select_df(self):\n",
    "        conn, curs = self.conn_db()\n",
    "        sql = 'select * from member'\n",
    "        df = pd.read_sql(sql, conn)\n",
    "        conn.close()\n",
    "        return df\n",
    "    \n",
    "    def conn_db(self):\n",
    "        db_id = 'hr'\n",
    "        db_pw = 'hr'\n",
    "        db_url = '127.0.0.1:1521/xe'\n",
    "        conn = cx_Oracle.connect(db_id, db_pw, db_url)\n",
    "        curs = conn.cursor()\n",
    "        return conn, curs\n",
    "    \n",
    "    def insert(self, join_id, join_pw, join_name):\n",
    "        conn, curs = self.conn_db()\n",
    "        sql = '''insert into member(memid, id, pw, name)\n",
    "                values (mem_id_seq.nextval, :1, :2, :3)'''\n",
    "        curs.execute(sql, (join_id, join_pw, join_name))\n",
    "        conn.commit()\n",
    "        if curs != None:\n",
    "            curs.close()\n",
    "        if conn != None:\n",
    "            conn.close()\n",
    "            \n",
    "    def login(self, login_id, login_pw):\n",
    "        conn, curs = self.conn_db()\n",
    "        \n",
    "        sql = '''select count(*) from member where id = :1 and pw = :2 '''\n",
    "        result = curs.execute(sql, (login_id, login_pw))\n",
    "        cnt = result.fetchone()\n",
    "        \n",
    "        \n",
    "        if curs != None:\n",
    "            curs.close()\n",
    "        if conn != None:\n",
    "            conn.close()\n",
    "            \n",
    "        return cnt[0]\n",
    "    \n",
    "    def check(self, login_id):\n",
    "        conn, curs = self.conn_db()\n",
    "        \n",
    "        sql = '''select count(*) from member where id = :1'''\n",
    "        result = curs.execute(sql, [login_id])\n",
    "        cnt = result.fetchone()\n",
    "        \n",
    "        \n",
    "        if curs != None:\n",
    "            curs.close()\n",
    "        if conn != None:\n",
    "            conn.close()\n",
    "            \n",
    "        return cnt[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "cd364627",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dao = DAO()\n",
    "# dao.insert('yuna','9229','yuna')\n",
    "dao.check('myeonggi')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "f4651d12",
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
      " * Running on http://192.168.70.231:5048/ (Press CTRL+C to quit)\n",
      "192.168.70.231 - - [26/Sep/2022 11:08:37] \"GET / HTTP/1.1\" 200 -\n",
      "192.168.70.231 - - [26/Sep/2022 11:08:57] \"POST /join HTTP/1.1\" 302 -\n",
      "192.168.70.231 - - [26/Sep/2022 11:08:57] \"GET / HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "lee 123 123\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "192.168.70.231 - - [26/Sep/2022 11:17:55] \"POST /join HTTP/1.1\" 302 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "lmg 123 123\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask, request, redirect\n",
    "\n",
    "app = Flask(__name__)\n",
    "@app.route('/')\n",
    "def index():\n",
    "    return '<h1>Hello world</h1>'\n",
    "\n",
    "@app.route('/join', methods=['POST'])\n",
    "def join():\n",
    "    \n",
    "    if request.method == 'POST':\n",
    "        join_id = request.form['join_id']\n",
    "        join_pw = request.form['join_pw']\n",
    "        join_name = request.form['join_name']\n",
    "        print(join_id,join_pw,join_name)\n",
    "        dao = DAO()\n",
    "        try :\n",
    "            dao.insert(join_id, join_pw, join_name)\n",
    "            return redirect('/')\n",
    "        except:\n",
    "            return redirect('http://192.168.70.231:5500/index.html')\n",
    "\n",
    "@app.route('/check', methods=['POST'])\n",
    "def check_id():\n",
    "    if request.method == 'POST':\n",
    "        join_id = request.form['join_id']\n",
    "        \n",
    "        dao = DAO()\n",
    "        cnt = dao.check(join_id)\n",
    "        return cnt\n",
    "    \n",
    "@app.route('/login', methods=['GET', 'POST'])\n",
    "def login_db():\n",
    "    if request.method == 'POST' :\n",
    "        login_id = request.form['login_id']\n",
    "        login_pw = request.form['login_pw']\n",
    "        \n",
    "        print(login_id, login_pw)\n",
    "        \n",
    "        dao = DAO()\n",
    "        cnt = dao.login(login_id, login_pw)\n",
    "        print(login_id,login_pw)\n",
    "        \n",
    "        if cnt == 1:\n",
    "            url_success = 'http://lee48.dothome.co.kr/success.html'\n",
    "            return redirect(url_success)\n",
    "        else:\n",
    "            url_fail = 'http://lee48.dothome.co.kr/fail.html'\n",
    "            return redirect(url_fail)\n",
    "        \n",
    "\n",
    "if __name__ == '__main__' :\n",
    "    app.run(host='192.168.70.231', port=5048)\n",
    "    \n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "c6b61884",
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
       "      <th>MEMID</th>\n",
       "      <th>ID</th>\n",
       "      <th>PW</th>\n",
       "      <th>NAME</th>\n",
       "      <th>MONEY</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>108</td>\n",
       "      <td>yuna</td>\n",
       "      <td>9229</td>\n",
       "      <td>yuna</td>\n",
       "      <td>10000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>103</td>\n",
       "      <td>csg</td>\n",
       "      <td>1234</td>\n",
       "      <td>choiseulgi</td>\n",
       "      <td>10000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>104</td>\n",
       "      <td>dahye</td>\n",
       "      <td>1256</td>\n",
       "      <td>leedahye</td>\n",
       "      <td>10000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>105</td>\n",
       "      <td>eunbi</td>\n",
       "      <td>1236</td>\n",
       "      <td>gyeuneunbi</td>\n",
       "      <td>10000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>106</td>\n",
       "      <td>iu</td>\n",
       "      <td>1299</td>\n",
       "      <td>IU</td>\n",
       "      <td>10000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>107</td>\n",
       "      <td>soda</td>\n",
       "      <td>9999</td>\n",
       "      <td>DJsoda</td>\n",
       "      <td>10000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>102</td>\n",
       "      <td>lmg</td>\n",
       "      <td>123</td>\n",
       "      <td>leemyeonggi</td>\n",
       "      <td>10000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   MEMID     ID    PW         NAME  MONEY\n",
       "0    108   yuna  9229         yuna  10000\n",
       "1    103    csg  1234   choiseulgi  10000\n",
       "2    104  dahye  1256     leedahye  10000\n",
       "3    105  eunbi  1236   gyeuneunbi  10000\n",
       "4    106     iu  1299           IU  10000\n",
       "5    107   soda  9999       DJsoda  10000\n",
       "6    102    lmg   123  leemyeonggi  10000"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = dao.select_df() \n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2e15d819",
   "metadata": {},
   "outputs": [],
   "source": [
    "dao = DAO()\n",
    "r = dao.select()\n",
    "'</br>'.join(map(str, r))\n",
    "\n",
    "# for name, salary in r:\n",
    "#     print('name : {} / salary : {}'.format(name, salary))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f6948c90",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Python 점수를 저장하려고 함\n",
    "score = 100\n",
    "#score의 타입은????\n",
    "type(score)\n",
    "\n",
    "# 이름을 저장하려고 함\n",
    "name = '나예호'\n",
    "\n",
    "type(name)\n",
    "\n",
    "# 나예호와 Python점수를 동시에 저장\n",
    "# class를 사용!!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "80f23dbb",
   "metadata": {},
   "outputs": [],
   "source": [
    "# VO(Value Object)\n",
    "# 사용자 정의 데이터 타입\n",
    "\n",
    "# Design Pattern\n",
    "# 코드를 작성\n",
    "# Refactoring\n",
    "\n",
    "# 가장 보편적, 가장 많이 사용하는 약속된 Design\n",
    "# MVC : Model, View, Controller"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2f99fe8f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b8d9ddc0",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6305eda0",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "89b5de63",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "17d1902e",
   "metadata": {},
   "outputs": [],
   "source": [
    "num = 6\n",
    "print(num + 5)\n",
    "print(num * 5)\n",
    "print(num / 5)\n",
    "print(num % 5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "04c44733",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Scores:\n",
    "    \n",
    "    name = ''\n",
    "    score = 0\n",
    "    \n",
    "    def print_info(self):\n",
    "        print('이름 : {} / 점수: {}'.format(self.name, self.score))\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d4e6846f",
   "metadata": {},
   "outputs": [],
   "source": [
    "s1 = Scores()\n",
    "s1.name = '나예호'\n",
    "s1.score = 100\n",
    "\n",
    "s1.print_info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1e2d7375",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, request\n",
    "\n",
    "#app : Server실행, 경로를 잡아주는 객체\n",
    "app = Flask(__name__)\n",
    "\n",
    "@app.route('/')\n",
    "def index():\n",
    "    \n",
    "    ip = request.remote_addr\n",
    "    \n",
    "    if ip == '접속ㅎ':\n",
    "        return '인수씨 방가방가'\n",
    "    else:\n",
    "        return '<h1>Hello World</h1>'\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run(host='내 IP', port=5021)"
   ]
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
