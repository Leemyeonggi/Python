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
    "    <tr><td style=\"border: 1px solid black; width:600px; height:40px; text-align: center;\"><font size=4 color=blue><b>[3차시] 학습목표</b></font></td></tr>       \n",
    "    <tr><td style=\"border: 1px solid black; text-align: left;\"><font size=3>○ 카메라나 동영상으로부터 비디오 프레임 캡처하기<br>\n",
    "○ CCTV 만들기 - 동영상 녹화하기<br>\n",
    "○ 동영상에서 한 프레임을 이미지 파일로 저장하기<br>\n",
    "○ 저장한 이미지들을 동영상으로 만들기<br>\n",
    "○ 유튜브 영상 연동하기<br>\n",
    "        </font></td></tr>   \n",
    "</table>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "gLauf9_UarFp"
   },
   "source": [
    "# 동영상을 읽고 출력하기\n",
    "\n",
    "## 카메라나 동영상으로부터 비디오 프레임 캡처하기\n",
    "\n",
    "- <font color=red>cap = cv2.VideoCapture(0)</font>\n",
    "  - 0번 카메라로부터 비디오 캡처\n",
    "  - 0 대신에 파일명을 입력하면 동영상으로부터 캡처  cv2.VideoCapture(“images/video.mp4”)\n",
    "  - IP가 부여된 웹캠인 경우 IP와 카메라 번호를 입력  cap = cv2.VideoCapture(\"rtsp:127.0.0.1/0\")\n",
    "  \n",
    "  \n",
    "- <font color=red>w = cap.set(3, 480)</font> : 비디오의 가로(3) 크기 설정하기\n",
    "- <font color=red>h = cap.set(4, 320)</font> : 비디오의 세로(4) 크기 설정하기\n",
    "\n",
    "\n",
    "- <font color=red>ret, frame = cap.read()</font> \n",
    "  - 카메라로부터 비디오 파일을 읽고 프레임(frame) 이미지와 읽기성공여부(ret)를 반환 (True/False)\n",
    "\n",
    "\n",
    "- <font color=red>key = cv2.waitKey(33)</font>\n",
    "  - 0.033초동안 키 입력을 대기 (30프레임인 경우)\n",
    "  - key 값은 아스키 코드로 반환\n",
    "  \n",
    "  \n",
    "- <font color=red>cap.release()</font>\n",
    "  - 비디오 객체를 종료하고 메모리를 해제\n",
    "  \n",
    "\n",
    "- 아스키 코드\n",
    "<img src=\"./lecture_image/03_ascii.png\" width=70%>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- 아스키 코드  \n",
    "0: 30  \n",
    "A: 41  \n",
    "a: 61  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 55
    },
    "executionInfo": {
     "elapsed": 585,
     "status": "ok",
     "timestamp": 1601964088660,
     "user": {
      "displayName": "강성관",
      "photoUrl": "",
      "userId": "00571094306841577419"
     },
     "user_tz": -540
    },
    "id": "Gdu9-Y9LarFn",
    "outputId": "dc8915da-3df0-4d1f-d9fe-4e472c1c0911",
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "# 실습\n",
    "import cv2\n",
    "\n",
    "try:\n",
    "    cap = cv2.VideoCapture(\"./image/video.mp4\")\n",
    "    print(\"비디오 캡쳐 성공\")\n",
    "    # 캡쳐한 비디오로부터 프레임이미지를 읽는다.\n",
    "    while True:\n",
    "        # ret(성공여부T/F),frame:읽은 이미지 반환 \n",
    "        ret, frame = cap.read()    \n",
    "\n",
    "        if not ret: #이미지를 읽지 못했다면\n",
    "            cap.release() #비디오 객체 메모리에서 해제\n",
    "            cv2.destroyAllWindows() #창닫기\n",
    "            break\n",
    "\n",
    "        cv2.imshow(\"video\", frame)\n",
    "\n",
    "        key=cv2.waitKey(3)  # 이 숫자 줄이면 빨리감 33은 1000/33 해서 1초에 30프레임 나오게 하는 것 숫자 줄이면 1초에 더많은 프레임 돌림\n",
    "\n",
    "        if key ==49 : #숫자1을 누르면\n",
    "            cap.release() #비디오 객체 메모리에서 해제\n",
    "            cv2.destroyAllWindows() #창닫기\n",
    "            break\n",
    "except:\n",
    "    print(\"비디오 캡쳐 실패\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<table border=1 width=100%>\n",
    "    <tr><td style=\"border: 1px solid black; width:600px; text-align: left;\"><font size=4 color=red><b>실습문제</b></font><br><br>\n",
    "        <font size=4>○ 동영상 파일을 읽고 출력해보자.</font></td></tr>       \n",
    "    <tr><td style=\"border: 1px solid black; text-align: left;\">\n",
    "        <img src=\"./lecture_image/03_movie.png\" width=50%></td></tr>   \n",
    "</table>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 위젯을 이용하여 동영상 출력하기"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import ipywidgets as widget\n",
    "from IPython.display import display\n",
    "import cv2\n",
    "\n",
    "img_widget = widget.Image(format=\".jpeg\", width=480, height=480)\n",
    "display(img_widget)\n",
    "\n",
    "cap = cv2.VideoCapture(\"./image/video.mp4\")\n",
    "\n",
    "while True: \n",
    "    ret, frame = cap.read()    \n",
    "    if not ret:\n",
    "        cap.release #비디오 격리해제 안하면 다시 재생 안됨\n",
    "        break\n",
    "        \n",
    "    try:\n",
    "        cv2.waitKey(33)\n",
    "        _, en_img = cv2.imencode(\".jpeg\", frame)\n",
    "    except KeyboardInterrupt :\n",
    "        cap.release()\n",
    "        break\n",
    "\n",
    "    img_widget.value = en_img.tobytes() #바이트 단위로 바꿔서 전송해주기 위함\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "c_T9xGKy7YGH"
   },
   "source": [
    "## CCTV 만들기 - 동영상 녹화하기\n",
    "\n",
    "- <font color=red>codec = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')</font> : 비디오 타입을 DIVX로 설정\n",
    "\n",
    "<img src=\"./lecture_image/03_codec.png\" width=70%>\n",
    "\n",
    "\n",
    "- <font color=red>out = cv2.VideoWriter('cctv01.avi', codec, fps, (w, h))</font>  \n",
    "  - cctv01.avi 파일에 설정한 코덱, 프레임, 크기로 저장하도록 설정\n",
    "  \n",
    "  \n",
    "- <font color=red>out.write(frame)</font>  : 이미지 프레임을 파일에 쓰기\n",
    "\n",
    "\n",
    "- <font color=red>out.release() </font> : 파일 객체 해제하기"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2\n",
    "\n",
    "# 0번은 카메라 번호\n",
    "# 카메라로부터 영상을 획득\n",
    "cap = cv2.VideoCapture(0)\n",
    "\n",
    "img_widget = widget.Image(format=\".jpeg\", width=480, height=480)\n",
    "display(img_widget)\n",
    "\n",
    "\n",
    "\n",
    "while True: \n",
    "    ret, frame = cap.read()    \n",
    "    if not ret:\n",
    "        cap.release() #비디오 격리해제 안하면 다시 재생 안됨\n",
    "        out.release()\n",
    "        break\n",
    "        \n",
    "    \n",
    "    try:\n",
    "        cv2.waitKey(33)\n",
    "        _, en_img = cv2.imencode(\".jpeg\", frame)\n",
    "    except KeyboardInterrupt :\n",
    "        cap.release()\n",
    "        break\n",
    "    \n",
    "    img_widget.value = en_img.tobytes() #바이트 단위로 바꿔서 전송해주기 위함\n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2\n",
    "\n",
    "# 0번은 카메라 번호\n",
    "cap = cv2.VideoCapture(0)\n",
    "\n",
    "# 녹화설정\n",
    "fps=30.0 #초당 프레임 수 frame per second\n",
    "w = int(cap.get(3)) # 3은 가로크기를 가져온다\n",
    "h = int(cap.get(4)) # 4는 세로크기를 가져온다\n",
    "\n",
    "# * : 가변 매개변수 설정 (여러개 매개변수 쓸 때 아스타리스크)\n",
    "codec = cv2.VideoWriter_fourcc(*'DIVX') # avi타입으로 저장\n",
    "out = cv2.VideoWriter(\"./image/cctv01.avi\", codec, fps, (w,h))\n",
    "\n",
    "record = False #처음에는 녹화하지 않음\n",
    "\n",
    "while True: \n",
    "    ret, frame = cap.read()    \n",
    "    \n",
    "    if not ret:\n",
    "        out.release()\n",
    "        cap.release() #비디오 격리해제 안하면 다시 재생 안됨\n",
    "        cv2.destroyAllWindows()\n",
    "        break\n",
    "        \n",
    "    key=cv2.waitKey(33)\n",
    "    cv2.imshow(\"web_cam\", frame)\n",
    "    \n",
    "    #녹화하기\n",
    "    if record:\n",
    "        out.write(frame)\n",
    "            \n",
    "    if key == 49: #숫자 1을 누르면 (조건을 다양하게 줄 수 있다)\n",
    "        record = True\n",
    "        print('녹화시작')\n",
    "        \n",
    "    if key == 50: #숫자 2를 누르면\n",
    "        record = False\n",
    "        print('녹화종료')\n",
    "        \n",
    "    if key ==51 : #숫자3을 누르면\n",
    "        print('종료')\n",
    "        cap.release() #비디오 객체 메모리에서 해제\n",
    "        cv2.destroyAllWindows() #창닫기\n",
    "        break\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "ARYE0iZR7YGL"
   },
   "source": [
    "# 동영상에서 한 프레임을 이미지 파일로 저장하기\n",
    "\n",
    "- <font color=red>cv2.imwrite(“파일명.확장자”, 프레임이미지, 옵션)</font>\n",
    "  - params=[cv2.IMWRITE_PNG_COMPRESSION, 0]) : 압축 하지 않는 PNG, 세 번째 파라미터는 압축률로 0~9까지 설정 가능 (0은 압축 없음)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "### import cv2\n",
    "\n",
    "# 카메라로부터 영상을 획득\n",
    "cap = cv2.VideoCapture(0)\n",
    "seq=0\n",
    "\n",
    "\n",
    "while True :\n",
    "    ret, frame = cap.read()\n",
    "    if not ret :\n",
    "        print(\"종료\")\n",
    "        cap.release()\n",
    "        cv2.destroyAllWindows()\n",
    "        break\n",
    "        \n",
    "    key = cv2.waitKey(33)\n",
    "    cv2.imshow(\"cctv\", frame)\n",
    "\n",
    "    #숫자 1을 누르면 프레임이미지를 파일(PNG)로 저장\n",
    "    if key == 49: \n",
    "        seq +=1\n",
    "        print(f'./image/img{seq}.png 파일을 저장하였습니다.')\n",
    "        #파일을 압축하지 않고 png파일로 저장하겠다.\n",
    "        cv2.imwrite(f'./image/img{seq}.png', frame,\n",
    "                   params=[cv2.IMWRITE_PNG_COMPRESSION, 0])\n",
    "        \n",
    "    if key ==51 : #숫자3을 누르면\n",
    "        print('종료')\n",
    "        cap.release() #비디오 객체 메모리에서 해제\n",
    "        cv2.destroyAllWindows() #창닫기\n",
    "        break"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "Q2YlE60vAEtW"
   },
   "source": [
    "## 저장한 이미지들을 동영상으로 만들기"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "FUw1ewhLAEX_"
   },
   "outputs": [],
   "source": [
    "import cv2\n",
    "#동영상 설정\n",
    "fps = 5\n",
    "w = 640\n",
    "h = 480\n",
    "codec = cv2.VideoWriter_fourcc(*'DIVX')\n",
    "out = cv2.VideoWriter('./image/img.avi', codec, fps, (w,h))\n",
    "\n",
    "#이미지를 한장씩 읽어와서 동영상을 만들기\n",
    "for i in range(1,11):\n",
    "    img = cv2.imread(f'./image/img{i}.png', cv2.IMREAD_COLOR)\n",
    "    out.write(img)\n",
    "out.release()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 유튜브 영상 연동하기\n",
    "\n",
    "## pafy로 유튜브 영상 연동하기\n",
    "\n",
    "- pafy : youtube의 메타 데이터를 수집/검색하거나 다운로드 할 수 있는 Python 라이브러리\n",
    "- yt-dlp : 현재 업데이트가 되지 않는 youtube-dl을 업그레이드한 버전, 유튜브로부터 영상을 다운로드 (영상만 다운로드 – 음성 제외)"
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
      "Collecting pafy\n",
      "  Downloading pafy-0.5.5-py2.py3-none-any.whl (35 kB)\n",
      "Installing collected packages: pafy\n",
      "Successfully installed pafy-0.5.5\n",
      "Collecting youtube-dl\n",
      "  Downloading youtube_dl-2021.12.17-py2.py3-none-any.whl (1.9 MB)\n",
      "Installing collected packages: youtube-dl\n",
      "Successfully installed youtube-dl-2021.12.17\n",
      "Collecting yt-dlp\n",
      "  Downloading yt_dlp-2022.9.1-py2.py3-none-any.whl (2.7 MB)\n",
      "Collecting websockets\n",
      "  Downloading websockets-10.3-cp39-cp39-win_amd64.whl (98 kB)\n",
      "Collecting pycryptodomex\n",
      "  Downloading pycryptodomex-3.15.0-cp35-abi3-win_amd64.whl (1.9 MB)\n",
      "Collecting brotli\n",
      "  Downloading Brotli-1.0.9-cp39-cp39-win_amd64.whl (383 kB)\n",
      "Collecting mutagen\n",
      "  Downloading mutagen-1.45.1-py3-none-any.whl (218 kB)\n",
      "Requirement already satisfied: certifi in c:\\users\\ai\\anaconda3\\lib\\site-packages (from yt-dlp) (2021.10.8)\n",
      "Installing collected packages: websockets, pycryptodomex, mutagen, brotli, yt-dlp\n",
      "Successfully installed brotli-1.0.9 mutagen-1.45.1 pycryptodomex-3.15.0 websockets-10.3 yt-dlp-2022.9.1\n"
     ]
    }
   ],
   "source": [
    "# Youtube의 메타 데이터를 수집/검색하거나 다운로드 할 수 있는 Python 라이브러리 (음성x 영상만 가지고 옴)\n",
    "!pip install pafy\n",
    "# 유튜브로부터 영상만을 다운로드 \n",
    "!pip install youtube-dl\n",
    "# 유튜브로부터 영상만을 다운로드 (youtube-dl 라이브러리 업그레이드 버전)\n",
    "!pip install yt-dlp"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- <font color=red>video = pafy.new(\"유튜브 주소\")</font> : YouTube 주소로 영상 정보 가져오기\n",
    "\n",
    "- <font color=red>best = video.getbest(preftype=\"mp4\")</font> : YouTube 실제 주소 가져오기"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "ename": "KeyError",
     "evalue": "'dislike_count'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
      "Input \u001b[1;32mIn [2]\u001b[0m, in \u001b[0;36m<cell line: 2>\u001b[1;34m()\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mpafy\u001b[39;00m\n\u001b[1;32m----> 2\u001b[0m video \u001b[38;5;241m=\u001b[39m \u001b[43mpafy\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mnew\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43mhttps://www.youtube.com/watch?v=M2_TMY1hZ7g\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m)\u001b[49m\n\u001b[0;32m      4\u001b[0m \u001b[38;5;66;03m#유튜브영상정보 출력\u001b[39;00m\n\u001b[0;32m      5\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124mf\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m제목 : \u001b[39m\u001b[38;5;132;01m{\u001b[39;00mvideo\u001b[38;5;241m.\u001b[39mtitle\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m'\u001b[39m)\n",
      "File \u001b[1;32m~\\Anaconda3\\lib\\site-packages\\pafy\\pafy.py:124\u001b[0m, in \u001b[0;36mnew\u001b[1;34m(url, basic, gdata, size, callback, ydl_opts)\u001b[0m\n\u001b[0;32m    121\u001b[0m     \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[0;32m    122\u001b[0m        \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mbackend_youtube_dl\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m YtdlPafy \u001b[38;5;28;01mas\u001b[39;00m Pafy\n\u001b[1;32m--> 124\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43mPafy\u001b[49m\u001b[43m(\u001b[49m\u001b[43murl\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mbasic\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mgdata\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43msize\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mcallback\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mydl_opts\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mydl_opts\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[1;32m~\\Anaconda3\\lib\\site-packages\\pafy\\backend_youtube_dl.py:31\u001b[0m, in \u001b[0;36mYtdlPafy.__init__\u001b[1;34m(self, *args, **kwargs)\u001b[0m\n\u001b[0;32m     29\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m ydl_opts:\n\u001b[0;32m     30\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_ydl_opts\u001b[38;5;241m.\u001b[39mupdate(ydl_opts)\n\u001b[1;32m---> 31\u001b[0m \u001b[38;5;28msuper\u001b[39m(YtdlPafy, \u001b[38;5;28mself\u001b[39m)\u001b[38;5;241m.\u001b[39m\u001b[38;5;21m__init__\u001b[39m(\u001b[38;5;241m*\u001b[39margs, \u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39mkwargs)\n",
      "File \u001b[1;32m~\\Anaconda3\\lib\\site-packages\\pafy\\backend_shared.py:97\u001b[0m, in \u001b[0;36mBasePafy.__init__\u001b[1;34m(self, video_url, basic, gdata, size, callback, ydl_opts)\u001b[0m\n\u001b[0;32m     94\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mexpiry \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;01mNone\u001b[39;00m\n\u001b[0;32m     96\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m basic:\n\u001b[1;32m---> 97\u001b[0m     \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_fetch_basic\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m     99\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m gdata:\n\u001b[0;32m    100\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_fetch_gdata()\n",
      "File \u001b[1;32m~\\Anaconda3\\lib\\site-packages\\pafy\\backend_youtube_dl.py:54\u001b[0m, in \u001b[0;36mYtdlPafy._fetch_basic\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m     52\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_viewcount \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_ydl_info[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mview_count\u001b[39m\u001b[38;5;124m'\u001b[39m]\n\u001b[0;32m     53\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_likes \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_ydl_info[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mlike_count\u001b[39m\u001b[38;5;124m'\u001b[39m]\n\u001b[1;32m---> 54\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_dislikes \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_ydl_info\u001b[49m\u001b[43m[\u001b[49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43mdislike_count\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m]\u001b[49m\n\u001b[0;32m     55\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_username \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_ydl_info[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124muploader_id\u001b[39m\u001b[38;5;124m'\u001b[39m]\n\u001b[0;32m     56\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_category \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_ydl_info[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mcategories\u001b[39m\u001b[38;5;124m'\u001b[39m][\u001b[38;5;241m0\u001b[39m] \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_ydl_info[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mcategories\u001b[39m\u001b[38;5;124m'\u001b[39m] \u001b[38;5;28;01melse\u001b[39;00m \u001b[38;5;124m'\u001b[39m\u001b[38;5;124m'\u001b[39m\n",
      "\u001b[1;31mKeyError\u001b[0m: 'dislike_count'"
     ]
    }
   ],
   "source": [
    "import pafy\n",
    "video = pafy.new('https://www.youtube.com/watch?v=M2_TMY1hZ7g')\n",
    "\n",
    "#유튜브영상정보 출력\n",
    "print(f'제목 : {video.title}')\n",
    "print(f'평점 : {video.rating}')\n",
    "print(f'조회수 : {video.viewcount}')\n",
    "print(f'좋아요 : {video.likes}')\n",
    "print(f'싫어요 : {video.dislikes}')\n",
    "codec = video.getbest(preftype='mp4')\n",
    "print(f'영상크기 : {codec.resolution}')\n",
    "video.expiry\n",
    "\n",
    "print(f'실제파일링크 : {codec.url}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# import cv2\n",
    "\n",
    "cap = cv2.VideoCapture(codec.url)\n",
    "\n",
    "while True :\n",
    "    ret, frame = cap.read()\n",
    "    \n",
    "    if not ret :\n",
    "        print(\"종료\")\n",
    "        cap.release()\n",
    "        cv2.destroyAllWindows()\n",
    "        break\n",
    "        \n",
    "    key = cv2.waitKey(33)\n",
    "    cv2.imshow(\"cctv\", frame)\n",
    "    \n",
    "    if key == 49 :\n",
    "        print(\"종료\")\n",
    "        cap.release()\n",
    "        cv2.destroyAllWindows()\n",
    "        break"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- 코드 수행시에 KeyError: 'dislike_count'가 뜨는 경우\n",
    "  - pafy 설치폴더 (anaconda3설치폴더\\envs\\OpenCV\\Lib\\site-packages\\pafy)로 이동해서 backend_youtube_dl.py 파일을 열어서 53, 54라인을\n",
    "    - self._likes = self._ydl_info['like_count']\n",
    "    - self._dislikes = self._ydl_info['dislike_count']\n",
    "  - 다음 코드로 변경    \n",
    "    - self._likes = self._ydl_info.get('like_count',0)\n",
    "    - self._dislikes = self._ydl_info.get('dislike_count',0)\n",
    "    \n",
    "  - 주피터노트북을 닫고 재실행  \n",
    "  \n",
    "  - get함수를 써서 없으면 0을 반환하도록 하면 됨"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## yt-dlp로 유튜브 영상 다운로드하기"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (4003308493.py, line 13)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Input \u001b[1;32mIn [4]\u001b[1;36m\u001b[0m\n\u001b[1;33m    download_list = cv2.resize(download_list, (1920, 1280))\u001b[0m\n\u001b[1;37m                  ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "import yt_dlp  #음성은 안됨\n",
    "import cv2\n",
    "\n",
    "# 다운받을 영상 리스트\n",
    "download_list = [\"https://www.youtube.com/watch?v=M2_TMY1hZ7g\"]\n",
    "\n",
    "# 저장 폴더\n",
    "save_dir = './image/'\n",
    "\n",
    "#다운로드 옵션\n",
    "yt_opts = {\n",
    "    #다운받을 영상의 파일명과 확장자 명을 정하는 것\n",
    "    'outtmpl' : f\"./image/%(title)s.%(ext)s\",\n",
    "    #최상의 품질의 영상을 다운로드 하겠다는 것\n",
    "    \"format\" : \"bestvideo/best\"\n",
    "}\n",
    "\n",
    "#다운로드\n",
    "with yt_dlp.YoutubeDL(yt_opts) as yt:   #with 파일을 저장할 때 with을 쓰면 알아서 파일을 닫아주는 역할을 함\n",
    "    yt.download(download_list)\n",
    "print(\"종료\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## pytube로 유튜브 영상 다운로드\n",
    "  \n",
    "  - 영상과 음성을 모두 다운로드"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting git+https://github.com/nficano/pytube.git\n",
      "  Cloning https://github.com/nficano/pytube.git to c:\\users\\ai\\appdata\\local\\temp\\pip-req-build-rtm9qlci\n",
      "  Resolved https://github.com/nficano/pytube.git to commit 2e307d8d615ef30aa837fe2275954146dab07ca6\n",
      "  Preparing metadata (setup.py): started\n",
      "  Preparing metadata (setup.py): finished with status 'done'\n",
      "Building wheels for collected packages: pytube\n",
      "  Building wheel for pytube (setup.py): started\n",
      "  Building wheel for pytube (setup.py): finished with status 'done'\n",
      "  Created wheel for pytube: filename=pytube-12.1.0-py3-none-any.whl size=56929 sha256=2344baf5be39567df8593bf70ee68addbe79d908f337f482ab83ef05a4c523f0\n",
      "  Stored in directory: C:\\Users\\AI\\AppData\\Local\\Temp\\pip-ephem-wheel-cache-0l6y7wam\\wheels\\f1\\b5\\78\\12b4d0c5846b07ac841f094923d3b270c10c0a522dad8c2951\n",
      "Successfully built pytube\n",
      "Installing collected packages: pytube\n",
      "Successfully installed pytube-12.1.0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "  Running command git clone --filter=blob:none --quiet https://github.com/nficano/pytube.git 'C:\\Users\\AI\\AppData\\Local\\Temp\\pip-req-build-rtm9qlci'\n"
     ]
    }
   ],
   "source": [
    "# 아나콘다 프롬프트 창에서 실행\n",
    "!pip install --upgrade \"git+https://github.com/nficano/pytube.git\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "제목 : 착한데 질리는 남자\n",
      "조회수 : 1830988\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'C:\\\\Users\\\\AI\\\\오픈CV\\\\./image/착한데 질리는 남자.mp4'"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import os\n",
    "import pytube\n",
    "from pytube.cli import on_progress\n",
    "\n",
    "url = 'https://www.youtube.com/watch?v=Uh2uQ7fTQuI'\n",
    "\n",
    "#유튜브로부터 영상을 가져온다.\n",
    "yt = pytube.YouTube(url)\n",
    "\n",
    "#영상정보출력\n",
    "print(f'제목 : {yt.title}')\n",
    "print(f'조회수 : {yt.views}')\n",
    "\n",
    "#다운받을 폴더\n",
    "save_dir = \"./image/\"\n",
    "\n",
    "#다운로드\n",
    "#progressive : 순차적으로 다운로드\n",
    "#file_extension : 파일 확장자\n",
    "#order_by(\"resolution\") : 해상도로 검색\n",
    "#desc() : 내림차순\n",
    "#first() : 첫번째 파일\n",
    "yt.streams.filter(progressive=True, file_extension=\"mp4\")\\\n",
    "                .order_by('resolution')\\\n",
    "                .desc().first().download(save_dir)\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<table border=1 width=100%>\n",
    "    <tr><td style=\"border: 1px solid black; width:600px; text-align: left;\"><font size=4 color=red><b>실습문제</b></font><br><br>\n",
    "        <font size=4>○ 다른 유튜브 영상을 읽고 출력해보자.</font></td></tr>       \n",
    "    <tr><td style=\"border: 1px solid black; text-align: left;\">\n",
    "        <img src=\"./lecture_image/03_youtube.png\" width=50%></td></tr>   \n",
    "</table>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<table border=1 width=100%>\n",
    "    <tr><td style=\"border: 1px solid black; width:600px; text-align: left;\"><font size=4 color=red><b>실습문제</b></font><br><br>\n",
    "        <font size=4>○ 다른 유튜브 영상을 저장해보자.</font></td></tr>   \n",
    "</table>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<table border=1 width=100%>\n",
    "    <tr><td style=\"border: 1px solid black; width:600px; height:40px; text-align: center;\"><font size=4 color=blue><b>[3차시] 학습요약</b></font></td></tr>       \n",
    "    <tr><td style=\"border: 1px solid black; text-align: left;\"><font size=3>\n",
    "        \n",
    "○ <font color=red>cv2.VideoCapture()</font> : 비디오 캡처 (카메라, 동영상, 유튜브 등)<br>\n",
    "○ <font color=red>ret, frame = cap.read()</font> : 비디오로부터 프레임 이미지를 읽어서 반환<br>\n",
    "○ <font color=red>cv2.VideoWriter_fourcc ()</font> : 녹화 파일을 설정하는 함수<br>\n",
    "○ <font color=red>out.write()</font> : 영상을 저장<br>\n",
    "○ <font color=red>cv2.imwrite()</font> : 이미지를 저장<br>\n",
    "\n",
    "        \n",
    "○ 일반적인 동영상은 1초에 30장의 프레임이미지로 구성<br>\n",
    "○ pafy : 유투브 메타 데이터를 가져오는 라이브러리<br>\n",
    "○ yt-dlp : 유투브 영상을 다운로드하는 라이브러리 (음성 제외)<br>\n",
    "○ pytube : 유투브 영상을 다운로드하는 라이브러리 (음성 포함)\n",
    "         \n",
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
    "width": "165px"
   },
   "toc_section_display": true,
   "toc_window_display": true
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
