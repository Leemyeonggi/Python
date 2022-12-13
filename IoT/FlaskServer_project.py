{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "5c4e8673",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, request, redirect, jsonify"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "7e4234d2",
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
      " * Running on http://192.168.31.126:5000/ (Press CTRL+C to quit)\n",
      "192.168.30.174 - - [18/Aug/2022 12:40:10] \"GET /mpu?X=13.82&Y=13.84&T=1 HTTP/1.1\" 400 -\n",
      "192.168.30.174 - - [18/Aug/2022 12:40:11] \"GET /mpu?X=39.75&Y=4.08&T=2 HTTP/1.1\" 400 -\n",
      "192.168.30.174 - - [18/Aug/2022 12:40:12] \"GET /mpu?X=75.36&Y=-8.74&T=3 HTTP/1.1\" 400 -\n",
      "192.168.30.174 - - [18/Aug/2022 12:40:13] \"GET /mpu?X=87.16&Y=-35.08&T=4 HTTP/1.1\" 400 -\n",
      "192.168.30.174 - - [18/Aug/2022 12:40:14] \"GET /mpu?X=92.22&Y=-25.77&T=5 HTTP/1.1\" 400 -\n",
      "192.168.30.174 - - [18/Aug/2022 12:40:23] \"GET /mpu?X=5.50&Y=-11.21&T=6 HTTP/1.1\" 400 -\n",
      "192.168.30.174 - - [18/Aug/2022 12:40:24] \"GET /mpu?X=-8.88&Y=86.59&T=7 HTTP/1.1\" 400 -\n",
      "192.168.30.174 - - [18/Aug/2022 12:40:26] \"GET /mpu?X=-1.10&Y=97.99&T=8 HTTP/1.1\" 400 -\n",
      "192.168.30.174 - - [18/Aug/2022 12:40:27] \"GET /mpu?X=6.00&Y=106.38&T=9 HTTP/1.1\" 400 -\n",
      "192.168.30.174 - - [18/Aug/2022 12:40:35] \"GET /mpu?X=24.78&Y=46.49&T=10 HTTP/1.1\" 400 -\n",
      "192.168.30.174 - - [18/Aug/2022 12:40:36] \"GET /mpu?X=30.68&Y=42.93&T=11 HTTP/1.1\" 400 -\n",
      "192.168.30.174 - - [18/Aug/2022 12:40:37] \"GET /mpu?X=37.98&Y=56.60&T=12 HTTP/1.1\" 400 -\n",
      "192.168.30.174 - - [18/Aug/2022 12:40:39] \"GET /mpu?X=48.96&Y=93.28&T=13 HTTP/1.1\" 400 -\n",
      "192.168.30.174 - - [18/Aug/2022 12:40:40] \"GET /mpu?X=56.97&Y=107.82&T=14 HTTP/1.1\" 400 -\n",
      "192.168.30.174 - - [18/Aug/2022 12:40:41] \"GET /mpu?X=69.88&Y=100.91&T=15 HTTP/1.1\" 400 -\n",
      "192.168.30.174 - - [18/Aug/2022 12:40:42] \"GET /mpu?X=75.15&Y=116.43&T=16 HTTP/1.1\" 400 -\n",
      "192.168.30.174 - - [18/Aug/2022 12:41:34] \"GET /mpu?X=14.44&Y=7.36&T=1 HTTP/1.1\" 400 -\n",
      "192.168.30.174 - - [18/Aug/2022 12:41:35] \"GET /mpu?X=7.44&Y=-41.21&T=1 HTTP/1.1\" 400 -\n",
      "192.168.30.174 - - [18/Aug/2022 12:41:36] \"GET /mpu?X=10.15&Y=-53.53&T=1 HTTP/1.1\" 400 -\n",
      "192.168.30.174 - - [18/Aug/2022 12:41:37] \"GET /mpu?X=29.62&Y=54.75&T=1 HTTP/1.1\" 400 -\n",
      "192.168.30.174 - - [18/Aug/2022 12:41:38] \"GET /mpu?X=37.61&Y=-53.49&T=1 HTTP/1.1\" 400 -\n",
      "192.168.30.174 - - [18/Aug/2022 12:41:39] \"GET /mpu?X=58.71&Y=40.22&T=1 HTTP/1.1\" 400 -\n",
      "192.168.30.174 - - [18/Aug/2022 12:41:40] \"GET /mpu?X=34.13&Y=89.07&T=1 HTTP/1.1\" 400 -\n"
     ]
    }
   ],
   "source": [
    "app = Flask(__name__)\n",
    "@app.route('/', methods=['GET', 'POST'])\n",
    "def main():\n",
    "    return 'main'\n",
    "@app.route('/loadcell', methods=['GET', 'POST'])\n",
    "def loadcell():\n",
    "    read = \"can not read\"\n",
    "    if request.method == 'GET':\n",
    "        request.get_json()\n",
    "        read = request.args['loadcell']\n",
    "        print(read)\n",
    "        return \"value of loadcell is %s\" %read\n",
    "    else:\n",
    "        return read\n",
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
    "@app.route('/layout', methods=['GET', 'POST'])\n",
    "def layout():\n",
    "    return 'layout'\n",
    "@app.route('/chart', methods=['GET', 'POST'])\n",
    "def chart():\n",
    "    return 'chart'\n",
    "@app.route('/adormment', methods=['GET', 'POST'])\n",
    "def adormment():\n",
    "    return 'adormment'\n",
    "@app.route('/setting', methods=['GET', 'POST'])\n",
    "def setting():\n",
    "    return 'setting'\n",
    "if __name__ == '__main__':\n",
    "    app.run(host='192.168.31.126', port=5000)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0acff83b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "59aa7fdc",
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
