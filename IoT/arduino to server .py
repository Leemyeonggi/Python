{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f5c26788",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, request, redirect, jsonify\n",
    "#request모듈은 접근주소, url, path정보를 알아낼 수 있다.\n",
    "#redirect모듈은 브라우저에게 어디로 이동할지 명령하는 것"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "839d742a",
   "metadata": {
    "scrolled": true
   },
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
      " * Running on http://localhost:5000/ (Press CTRL+C to quit)\n"
     ]
    }
   ],
   "source": [
    "app = Flask(__name__)\n",
    "\n",
    "@app.route('/', methods=['GET', 'POST'])\n",
    "def main():\n",
    "    return 'main'\n",
    "\n",
    "@app.route('/loadcell', methods=['GET', 'POST'])\n",
    "def loadcell():\n",
    "    read = \"can not read\"\n",
    "    if request.method == 'GET':\n",
    "        request.get_json()\n",
    "        read = request.args['loadcell']\n",
    "        print(read)\n",
    "        return \"value of loadcell is %s\" %read \n",
    "    else:\n",
    "        return read\n",
    "    \n",
    "@app.route('/mpu', methods=['GET', 'POST'])\n",
    "def mpu():\n",
    "    read = \"can not read\"\n",
    "    if request.method == 'GET':\n",
    "        request.get_json()\n",
    "        X = request.args['X']\n",
    "        Y = request.args['Y']\n",
    "        T = request.args['T']\n",
    "        R = request.args['R']\n",
    "        print(X,Y,T,R)\n",
    "        return \"value of MPU6050 is %s\" %X+' '+Y+' '+T+' '+R\n",
    "\n",
    "@app.route('/layout', methods=['GET', 'POST'])\n",
    "def layout():\n",
    "    return 'layout'\n",
    "\n",
    "@app.route('/chart', methods=['GET', 'POST'])\n",
    "def chart():\n",
    "    return 'chart'\n",
    "\n",
    "@app.route('/adormment', methods=['GET', 'POST'])\n",
    "def adormment():\n",
    "    return 'adormment'\n",
    "\n",
    "@app.route('/setting', methods=['GET', 'POST'])\n",
    "def setting():\n",
    "    return 'setting'\n",
    "\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run(host='172.30.1.51', port=5020)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "296b5169",
   "metadata": {},
   "source": [
    "- request.args : URL query string 에 있는 key/value 쌍을 가져온다.\n",
    "- request.form : 주로 HTML form의 post 요청 데이터를 다룰 때 사용한다.(또는 Json 형식이 아닌 JavaScipt 요청도 가능하다.)\n",
    "- request.files : body 내에 존재하는 파일을 다룸. HTML은 무조건 enctype=multipart/form-data을 사용해야 하며 그렇지 않으면 업로드가 되지 않음.\n",
    "- request.values : args, form 둘다 사용가능 , 그러나 key가 겹치는 경우 args가 우선시 된다.\n",
    "- request.json : 파싱된 JSON 데이터. 요청에 application/json 콘텐츠 유형이 있거나\n",
    "- request.get_json(force=True)을 사용하여 콘텐츠 유형을 무시해야 합니다.\n",
    "- request.form['name'] : key가 존재하는 것을 안다면 indexing을 통해 접근(없는 key를 요청하면 오류남)\n",
    "- request.form.get('name') : key가 존재하지 않을 수도 있는 경우엔 get을 사용하자(key가 없으면 None값을 return)\n",
    "- request.form.getlist('name') : key가 여러번 전송되고, 값 목록이 필요한 경우에 사용한다.(get은 첫번째 값만 반환합니다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "50de96e0",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4ad8fe03",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8ba5ec40",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ea96148f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "aba0ca52",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a3b4c2a2",
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
