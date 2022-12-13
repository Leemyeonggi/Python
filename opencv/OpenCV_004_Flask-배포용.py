{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<img src=\"./lecture_image/00_title.png\">"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<table border=1 width=100%>\n",
    "    <tr><td style=\"border: 1px solid black; width:600px; height:40px; text-align: center;\"><font size=4 color=blue><b>[4차시] 학습목표</b></font></td></tr>       \n",
    "    <tr><td style=\"border: 1px solid black; text-align: left;\"><font size=3>\n",
    "        \n",
    "○ 기본적인 Flask 사용법 학습하기<br>\n",
    "○ 웹 화면에 카메라 영상 출력하기<br>\n",
    "○ 웹 출력 영상을 Gray 이미지로 출력하기\n",
    "        \n",
    "</font></td></tr>   \n",
    "</table>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- 파이썬은 기본적으로 동기방식으로 작동한다.\n",
    "- 플라스크도 동기방식으로 작동한다.\n",
    "- 순서대로 실행되는 구조라는 뜻이다."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Flask 설치 및 서버 실행하기\n",
    "\n",
    "- 플라스크(Flask)는 파이썬으로 작성된 마이크로 웹 프레임워크의 하나\n",
    "  - 특별한 도구나 라이브러리가 필요 없음\n",
    "  \n",
    "##  flask 설치하기"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Flask 설치\n",
    "!pip install flask"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## flask 서버 실행하기\n",
    "\n",
    "- <font color=red>app = Flask(__name__)</font> : Flask 객체를 app 변수에 할당\n",
    "- <font color=red>@app.route(\"/\")</font> : Flask에게 어떤 URL이 해당 함수를 실행하는지 알려줌\n",
    "- <font color=red>app.run(host='127.0.0.1', port=5000)</font> \n",
    "  - 서버 IP, 포트 등을 설정하고 서버를 실행\n",
    "  - 브라우저에서 IP와 포트로 서버 접속\n",
    "   \n",
    "<img src=\"./lecture_image/04_flask01.png\" width=50%> "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "# 실습"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### URL를 함수로 연결하기\n",
    "\n",
    "- <font color=red>@app.route(\"/hello\")</font>\n",
    "  - URL에  함수명을 설정\n",
    "  - 브라우저에서 IP와 포트로 서버 접속하고 URL로 함수명을 넘김\n",
    "  \n",
    "  <img src=\"./lecture_image/04_flask02.png\" width=50%> "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 실습"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### URL을 변수로 사용하기\n",
    "\n",
    "- @app.route(\"/hello/<value>\") \n",
    "  - URL에  value 값을 설정\n",
    "  - 브라우저에서 IP와 포트로 서버 접속하고 URL로 100을 넘김\n",
    "    \n",
    "  <img src=\"./lecture_image/04_flask03.png\" width=50%>     "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 실습"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### html 문서를 반환하기\n",
    "\n",
    "- <font color=red>render_template(\"hello.html\")</font>\n",
    "  - hello.html 문서를 반환\n",
    "\n",
    "- hello.html 파일을 작성하고 templates 폴더를 생성하고 저장\n",
    "- 브라우저에서 IP와 포트로 서버 접속\n",
    "\n",
    "  <img src=\"./lecture_image/04_flask04.png\" width=50%>  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 실습"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 실습"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 이미지가 포함된 문서 반환하기\n",
    "\n",
    "- static 폴더 : 자원을 담아 놓는 폴더\n",
    "- static 폴더에 이미지 폴더를 만들고 출력할 이미지를 저장"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 실습"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 실습"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 데이터 스트리밍 구현\n",
    "\n",
    "## 구현 방법\n",
    "\n",
    "- <font color=red>Response(stream_with_context(test()))</font>\n",
    "  - 텍스트 스트리밍 함수 test()를 실행\n",
    "  \n",
    "  <img src=\"./lecture_image/04_flask05.png\" width=50%>  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def test():\n",
    "    yield \"Hello\"  #yieldsms return과 비슷한 함수\n",
    "    yield \"World\"\n",
    "    yield \"^^\"  #return 은 반환하고 돌아가는데 yield는 return하고 나가지 않고 함수 안에 머뭄\n",
    "                 #함수를 실행하다 중간 결과 값을 받고 싶을 때 유용하다.\n",
    "    \n",
    "for i in test():\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import time\n",
    "\n",
    "def return_abc():\n",
    "    temp = []\n",
    "    \n",
    "    #ABC 문장을 1초마다 1그자씩 읽어서 리스트를 저장 \n",
    "    for ch in \"ABC\":\n",
    "        time.sleep(1)\n",
    "        temp.append(ch)\n",
    "    return temp  #데이터가 다 저장된 뒤 마지막 결과물 반환\n",
    "\n",
    "for i in return_abc():\n",
    "    print(i)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def yield_abc():\n",
    "    temp = []\n",
    "    \n",
    "    #ABC 문장을 1초마다 1그자씩 읽어서 리스트를 저장 \n",
    "    for ch in \"ABC\":\n",
    "        time.sleep(1)\n",
    "        temp.append(ch)\n",
    "        yield ch  #데이터가 다 저장된 뒤 마지막 결과물 반환\n",
    "    \n",
    "for i in yield_abc():\n",
    "    print(i)    "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- yield() 함수 배우기\n",
    "\n",
    "  \n",
    "  <img src=\"./lecture_image/04_yield.png\" width=70%>  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 실습"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 실습"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 웹 브라우저에 카메라 영상 출력하기\n",
    "\n",
    "- <font color=red>ret, buffer = cv2.imencode('.jpg', frame)</font> : frame 이미지를 jpg로 인코딩\n",
    "\n",
    "- <font color=red>frame = buffer.tobytes()</font> : 전송을 위해 인코딩된 이미지를 byte 형식으로 변환\n",
    "\n",
    "\n",
    "- <font color=red>yield (b'--frame\\r\\n' b'Content-Type: image/jpeg\\r\\n\\r\\n' + frame + b'\\r\\n') </font>\n",
    "\n",
    "  - b : byte 형식임을 의미\n",
    "  - --frame : 프레임을 표시\n",
    "  - Content-Type: image/jpeg : 문서가 jpg 이미지임을 표시"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- index.html를 작성하고 templates 폴더에 저장\n",
    "  - video_feed : 실행할 함수명"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "%%writefile ./templates/index.html\n",
    "<html>\n",
    "<body>\n",
    "<div class=\"container\">\n",
    "    <div class=\"row\">\n",
    "        <div class=\"col-lg-8 offset-lg-2\">\n",
    "            <h3 class=\"mt-5\">Live Streaming</h3>\n",
    "            <img src =\"{{ url_for('video_feed')}}\" width=\"50%\">\n",
    "        </div>\n",
    "    </div>\n",
    "</div>\n",
    "</body>\n",
    "</html>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- <font color=red>Response(get_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')</font>\n",
    "\n",
    "  - get_frames() : 호출할 함수명\n",
    "  - mimetype : 클라이언트에게 전송된 문서의 타입을 알려주기 위한 파라미터 (type/subtype)\n",
    "  - multipart : 복합문서 타입 (파일, 영상 등)을 의미\n",
    "  - x-mixed-replace : x (추가적인 확장 형식), mixed (복합문서), repalce (subtype을 다음 메시지로 대체)\n",
    "  - boundary : 복합문서 내의 각 문서들을 구분하는 분리자 (동영상이므로 frame으로 구분)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "import cv2\n",
    "cap = cv2.VideoCapture(0)\n",
    "# 이미지를 읽어서 한프레임씩 바로 전송하는 스트리밍 함수\n",
    "def get_frames() :\n",
    "    while True :\n",
    "        ret, frame = cap.read()\n",
    "        # 현재 프레임이미지를 읽지 못했다면 다음 프레임이미지를 읽는다\n",
    "        if not ret :\n",
    "            continue\n",
    "        else :\n",
    "            ret1, buffer = cv2.imencode(\".jpg\", frame)\n",
    "            # 전송하기 위해 바이트로 변환\n",
    "            frame = buffer.tobytes()\n",
    "            # 전송\n",
    "            yield (b'--frame\\r\\n' b'Content-Type: image/jpeg\\r\\n\\r\\n' + frame + b'\\r\\n')\n",
    "from flask import Flask, render_template, Response\n",
    "app = Flask(__name__)\n",
    "# 초기화면\n",
    "@app.route(\"/\")\n",
    "def index() :\n",
    "    return render_template(\"index.html\")\n",
    "@app.route(\"/video_feed\")\n",
    "def video_feed() :\n",
    "    return Response(get_frames(),\n",
    "                   mimetype='multipart/x-mixed-replace; boundary=frame')\n",
    "if __name__ == \"__main__\" :\n",
    "    app.run(host=\"192.168.70.44\", port=9000)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 웹 출력 영상을 Gray 이미지로 출력하기"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "%%writefile ./templates/index2.html\n",
    "<html>\n",
    "<body>\n",
    "<div class=\"container\">\n",
    "    <div class=\"row\">\n",
    "        <div class=\"col-lg-8 offset-lg-2\">\n",
    "            <h3 class=\"mt-5\">Live Streaming</h3>\n",
    "            <img src =\"{{ url_for('video_feed1')}}\" width=\"50%\">\n",
    "            <img src =\"{{ url_for('video_feed2')}}\" width=\"50%\">\n",
    "        </div>\n",
    "    </div>\n",
    "</div>\n",
    "</body>\n",
    "</html>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
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
     "ename": "OSError",
     "evalue": "[WinError 10049] 요청한 주소는 해당 컨텍스트에서 유효하지 않습니다",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mOSError\u001b[0m                                   Traceback (most recent call last)",
      "Input \u001b[1;32mIn [1]\u001b[0m, in \u001b[0;36m<cell line: 46>\u001b[1;34m()\u001b[0m\n\u001b[0;32m     44\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m Response(get_frames2(),\n\u001b[0;32m     45\u001b[0m                    mimetype\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mmultipart/x-mixed-replace; boundary=frame\u001b[39m\u001b[38;5;124m'\u001b[39m)\n\u001b[0;32m     46\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;18m__name__\u001b[39m \u001b[38;5;241m==\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m__main__\u001b[39m\u001b[38;5;124m\"\u001b[39m :\n\u001b[1;32m---> 47\u001b[0m     \u001b[43mapp\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mrun\u001b[49m\u001b[43m(\u001b[49m\u001b[43mhost\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43m192.168.70.44\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mport\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;241;43m9000\u001b[39;49m\u001b[43m)\u001b[49m\n",
      "File \u001b[1;32m~\\Anaconda3\\lib\\site-packages\\flask\\app.py:990\u001b[0m, in \u001b[0;36mFlask.run\u001b[1;34m(self, host, port, debug, load_dotenv, **options)\u001b[0m\n\u001b[0;32m    987\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mwerkzeug\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mserving\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m run_simple\n\u001b[0;32m    989\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[1;32m--> 990\u001b[0m     run_simple(host, port, \u001b[38;5;28mself\u001b[39m, \u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39moptions)\n\u001b[0;32m    991\u001b[0m \u001b[38;5;28;01mfinally\u001b[39;00m:\n\u001b[0;32m    992\u001b[0m     \u001b[38;5;66;03m# reset the first request information if the development server\u001b[39;00m\n\u001b[0;32m    993\u001b[0m     \u001b[38;5;66;03m# reset normally.  This makes it possible to restart the server\u001b[39;00m\n\u001b[0;32m    994\u001b[0m     \u001b[38;5;66;03m# without reloader and that stuff from an interactive shell.\u001b[39;00m\n\u001b[0;32m    995\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_got_first_request \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;01mFalse\u001b[39;00m\n",
      "File \u001b[1;32m~\\Anaconda3\\lib\\site-packages\\werkzeug\\serving.py:1017\u001b[0m, in \u001b[0;36mrun_simple\u001b[1;34m(hostname, port, application, use_reloader, use_debugger, use_evalex, extra_files, exclude_patterns, reloader_interval, reloader_type, threaded, processes, request_handler, static_files, passthrough_errors, ssl_context)\u001b[0m\n\u001b[0;32m   1009\u001b[0m     _rwr(\n\u001b[0;32m   1010\u001b[0m         inner,\n\u001b[0;32m   1011\u001b[0m         extra_files\u001b[38;5;241m=\u001b[39mextra_files,\n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m   1014\u001b[0m         reloader_type\u001b[38;5;241m=\u001b[39mreloader_type,\n\u001b[0;32m   1015\u001b[0m     )\n\u001b[0;32m   1016\u001b[0m \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[1;32m-> 1017\u001b[0m     \u001b[43minner\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[1;32m~\\Anaconda3\\lib\\site-packages\\werkzeug\\serving.py:957\u001b[0m, in \u001b[0;36mrun_simple.<locals>.inner\u001b[1;34m()\u001b[0m\n\u001b[0;32m    955\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m (\u001b[38;5;167;01mLookupError\u001b[39;00m, \u001b[38;5;167;01mValueError\u001b[39;00m):\n\u001b[0;32m    956\u001b[0m     fd \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;01mNone\u001b[39;00m\n\u001b[1;32m--> 957\u001b[0m srv \u001b[38;5;241m=\u001b[39m \u001b[43mmake_server\u001b[49m\u001b[43m(\u001b[49m\n\u001b[0;32m    958\u001b[0m \u001b[43m    \u001b[49m\u001b[43mhostname\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    959\u001b[0m \u001b[43m    \u001b[49m\u001b[43mport\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    960\u001b[0m \u001b[43m    \u001b[49m\u001b[43mapplication\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    961\u001b[0m \u001b[43m    \u001b[49m\u001b[43mthreaded\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    962\u001b[0m \u001b[43m    \u001b[49m\u001b[43mprocesses\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    963\u001b[0m \u001b[43m    \u001b[49m\u001b[43mrequest_handler\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    964\u001b[0m \u001b[43m    \u001b[49m\u001b[43mpassthrough_errors\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    965\u001b[0m \u001b[43m    \u001b[49m\u001b[43mssl_context\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    966\u001b[0m \u001b[43m    \u001b[49m\u001b[43mfd\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mfd\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    967\u001b[0m \u001b[43m\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m    968\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m fd \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n\u001b[0;32m    969\u001b[0m     log_startup(srv\u001b[38;5;241m.\u001b[39msocket)\n",
      "File \u001b[1;32m~\\Anaconda3\\lib\\site-packages\\werkzeug\\serving.py:789\u001b[0m, in \u001b[0;36mmake_server\u001b[1;34m(host, port, app, threaded, processes, request_handler, passthrough_errors, ssl_context, fd)\u001b[0m\n\u001b[0;32m    787\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mValueError\u001b[39;00m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcannot have a multithreaded and multi process server.\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m    788\u001b[0m \u001b[38;5;28;01melif\u001b[39;00m threaded:\n\u001b[1;32m--> 789\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43mThreadedWSGIServer\u001b[49m\u001b[43m(\u001b[49m\n\u001b[0;32m    790\u001b[0m \u001b[43m        \u001b[49m\u001b[43mhost\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mport\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mapp\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mrequest_handler\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mpassthrough_errors\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mssl_context\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mfd\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mfd\u001b[49m\n\u001b[0;32m    791\u001b[0m \u001b[43m    \u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m    792\u001b[0m \u001b[38;5;28;01melif\u001b[39;00m processes \u001b[38;5;241m>\u001b[39m \u001b[38;5;241m1\u001b[39m:\n\u001b[0;32m    793\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m ForkingWSGIServer(\n\u001b[0;32m    794\u001b[0m         host,\n\u001b[0;32m    795\u001b[0m         port,\n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m    801\u001b[0m         fd\u001b[38;5;241m=\u001b[39mfd,\n\u001b[0;32m    802\u001b[0m     )\n",
      "File \u001b[1;32m~\\Anaconda3\\lib\\site-packages\\werkzeug\\serving.py:693\u001b[0m, in \u001b[0;36mBaseWSGIServer.__init__\u001b[1;34m(self, host, port, app, handler, passthrough_errors, ssl_context, fd)\u001b[0m\n\u001b[0;32m    690\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m os\u001b[38;5;241m.\u001b[39mpath\u001b[38;5;241m.\u001b[39mexists(server_address):\n\u001b[0;32m    691\u001b[0m         os\u001b[38;5;241m.\u001b[39munlink(server_address)\n\u001b[1;32m--> 693\u001b[0m \u001b[38;5;28;43msuper\u001b[39;49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[38;5;21;43m__init__\u001b[39;49m\u001b[43m(\u001b[49m\u001b[43mserver_address\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mhandler\u001b[49m\u001b[43m)\u001b[49m  \u001b[38;5;66;03m# type: ignore\u001b[39;00m\n\u001b[0;32m    695\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mapp \u001b[38;5;241m=\u001b[39m app\n\u001b[0;32m    696\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mpassthrough_errors \u001b[38;5;241m=\u001b[39m passthrough_errors\n",
      "File \u001b[1;32m~\\Anaconda3\\lib\\socketserver.py:452\u001b[0m, in \u001b[0;36mTCPServer.__init__\u001b[1;34m(self, server_address, RequestHandlerClass, bind_and_activate)\u001b[0m\n\u001b[0;32m    450\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m bind_and_activate:\n\u001b[0;32m    451\u001b[0m     \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[1;32m--> 452\u001b[0m         \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mserver_bind\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m    453\u001b[0m         \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mserver_activate()\n\u001b[0;32m    454\u001b[0m     \u001b[38;5;28;01mexcept\u001b[39;00m:\n",
      "File \u001b[1;32m~\\Anaconda3\\lib\\http\\server.py:136\u001b[0m, in \u001b[0;36mHTTPServer.server_bind\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m    134\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mserver_bind\u001b[39m(\u001b[38;5;28mself\u001b[39m):\n\u001b[0;32m    135\u001b[0m     \u001b[38;5;124;03m\"\"\"Override server_bind to store the server name.\"\"\"\u001b[39;00m\n\u001b[1;32m--> 136\u001b[0m     \u001b[43msocketserver\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mTCPServer\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mserver_bind\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[43m)\u001b[49m\n\u001b[0;32m    137\u001b[0m     host, port \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mserver_address[:\u001b[38;5;241m2\u001b[39m]\n\u001b[0;32m    138\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mserver_name \u001b[38;5;241m=\u001b[39m socket\u001b[38;5;241m.\u001b[39mgetfqdn(host)\n",
      "File \u001b[1;32m~\\Anaconda3\\lib\\socketserver.py:466\u001b[0m, in \u001b[0;36mTCPServer.server_bind\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m    464\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mallow_reuse_address:\n\u001b[0;32m    465\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39msocket\u001b[38;5;241m.\u001b[39msetsockopt(socket\u001b[38;5;241m.\u001b[39mSOL_SOCKET, socket\u001b[38;5;241m.\u001b[39mSO_REUSEADDR, \u001b[38;5;241m1\u001b[39m)\n\u001b[1;32m--> 466\u001b[0m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43msocket\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mbind\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mserver_address\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m    467\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mserver_address \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39msocket\u001b[38;5;241m.\u001b[39mgetsockname()\n",
      "\u001b[1;31mOSError\u001b[0m: [WinError 10049] 요청한 주소는 해당 컨텍스트에서 유효하지 않습니다"
     ]
    }
   ],
   "source": [
    "import cv2\n",
    "cap = cv2.VideoCapture(0)\n",
    "# 이미지를 읽어서 한프레임씩 바로 전송하는 스트리밍 함수\n",
    "def get_frames() :\n",
    "    while True :\n",
    "        ret, frame = cap.read()\n",
    "        frame = cv2.cvtColor(ret, cv2.COLOR_RGB2GRAY)\n",
    "        # 현재 프레임이미지를 읽지 못했다면 다음 프레임이미지를 읽는다\n",
    "        if not ret :\n",
    "            continue\n",
    "        else :\n",
    "            ret1, buffer = cv2.imencode(\".jpg\", img_color)\n",
    "            # 전송하기 위해 바이트로 변환\n",
    "            frame = buffer.tobytes()\n",
    "            # 전송\n",
    "            yield (b'--frame\\r\\n' b'Content-Type: image/jpeg\\r\\n\\r\\n' + frame + b'\\r\\n')\n",
    "            \n",
    "def get_frames2() :\n",
    "    while True :\n",
    "        ret, frame = cap.read()\n",
    "        frame = cv2.cvtColor(ret, cv2.COLOR_RGB2GRAY)\n",
    "        # 현재 프레임이미지를 읽지 못했다면 다음 프레임이미지를 읽는다\n",
    "        if not ret :\n",
    "            continue\n",
    "        else :\n",
    "            ret1, buffer = cv2.imencode(\".jpg\", img_color)\n",
    "            # 전송하기 위해 바이트로 변환\n",
    "            frame = buffer.tobytes()\n",
    "            # 전송\n",
    "            yield (b'--frame\\r\\n' b'Content-Type: image/jpeg\\r\\n\\r\\n' + frame + b'\\r\\n')\n",
    "            \n",
    "from flask import Flask, render_template, Response\n",
    "app = Flask(__name__)\n",
    "# 초기화면\n",
    "@app.route(\"/\")\n",
    "def index() :\n",
    "    return render_template(\"index2.html\")\n",
    "@app.route(\"/video_feed1\")\n",
    "def video_feed1() :\n",
    "    return Response(get_frames(),\n",
    "                   mimetype='multipart/x-mixed-replace; boundary=frame')\n",
    "@app.route(\"/video_feed2\")\n",
    "def video_feed2() :\n",
    "    return Response(get_frames2(),\n",
    "                   mimetype='multipart/x-mixed-replace; boundary=frame')\n",
    "if __name__ == \"__main__\" :\n",
    "    app.run(host=\"192.168.70.44\", port=9000)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2\n",
    "cap = cv2.VideoCapture(0)\n",
    "# 이미지를 읽어서 한프레임씩 바로 전송하는 스트리밍 함수\n",
    "def get_frames() :\n",
    "    while True :\n",
    "        ret, frame = cap.read()\n",
    "        # 현재 프레임이미지를 읽지 못했다면 다음 프레임이미지를 읽는다\n",
    "        if not ret :\n",
    "            continue\n",
    "        else :\n",
    "            ret1, buffer = cv2.imencode(\".jpg\", frame)\n",
    "            # 전송하기 위해 바이트로 변환\n",
    "            frame = buffer.tobytes()\n",
    "            # 전송\n",
    "            yield (b'--frame\\r\\n' b'Content-Type: image/jpeg\\r\\n\\r\\n' + frame + b'\\r\\n')\n",
    "from flask import Flask, render_template, Response\n",
    "app = Flask(__name__)\n",
    "# 초기화면\n",
    "@app.route(\"/\")\n",
    "def index() :\n",
    "    return render_template(\"index.html\")\n",
    "@app.route(\"/video_feed\")\n",
    "def video_feed() :\n",
    "    return Response(get_frames(),\n",
    "                   mimetype='multipart/x-mixed-replace; boundary=frame')\n",
    "if __name__ == \"__main__\" :\n",
    "    app.run(host=\"192.168.70.44\", port=9000)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<table border=1 width=100%>\n",
    "    <tr><td style=\"border: 1px solid black; width:600px; text-align: left;\"><font size=4 color=red><b>실습문제</b></font><br><br>\n",
    "        <font size=4>\n",
    "○ 이진 이미지를 출력하는 웹 카메라 만들기<br>\n",
    "   - threshold() 함수 적용<br>\n",
    "   - OTSU 이진화 알고리즘 적용<br>\n",
    "   - 적응형 thresholding 적용</font></td></tr>       \n",
    "    <tr><td style=\"border: 1px solid black; text-align: left;\">\n",
    "        <img src=\"./lecture_image/04_flask06.png\" width=30%><img src=\"./lecture_image/04_flask07.png\" width=30%></td></tr>   \n",
    "</table>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<table border=1 width=100%>\n",
    "    <tr><td style=\"border: 1px solid black; width:600px; height:40px; text-align: center;\"><font size=4 color=blue><b>[4차시] 학습요약</b></font></td></tr>       \n",
    "    <tr><td style=\"border: 1px solid black; text-align: left;\"><font size=3>\n",
    "        \n",
    "○ <font color=red>ret, buffer = cv2.imencode()</font> : 영상 인코딩 함수<br>\n",
    "○ yield() : 반복 실행 중에 중간 과정을 반환할 때 사용<br><br>\n",
    "\n",
    "○ Flask : 파이썬으로 제작된 웹 프레임워크 (DJango의 축소 버전)<br>\n",
    "○ <font color=red>app = Flask(__name__)</font> : Flask 객체를 app 변수에 할당<br>\n",
    "○ <font color=red>@app.route(\"/\")</font> : Flask에게 어떤 URL이 해당 함수를 실행하는지 알려줌<br>\n",
    "○ <font color=red>@app.route(\"/hello\")</font> : 서버 주소에 추가적인 URL을 설정<br>\n",
    "○ <font color=red>@app.route(\"/hello/<value>\")</font> : URL에 value 값을 설정<br>\n",
    "○ <font color=red>app.run(host='127.0.0.1', port=5000)</font> : 서버 IP, 포트 등을 설정하고 서버를 실행<br><br>\n",
    "\n",
    "○ <font color=red>render_template(\"hello.html\")</font> : html 문서를 반환하기<br>\n",
    "○ <font color=red>Response(stream_with_context())</font> : 데이터 스트리밍을 반환하기\n",
    "        \n",
    "</font></td></tr>   \n",
    "</table>"
   ]
  }
 ],
 "metadata": {
  "colab": {
   "name": "DL008_01_OpenCV.ipynb",
   "provenance": []
  },
  "hide_input": false,
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
   "toc_position": {
    "height": "calc(100% - 180px)",
    "left": "10px",
    "top": "150px",
    "width": "327px"
   },
   "toc_section_display": true,
   "toc_window_display": true
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
