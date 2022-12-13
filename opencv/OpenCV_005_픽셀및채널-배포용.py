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
    "    <tr><td style=\"border: 1px solid black; width:600px; height:40px; text-align: center;\"><font size=4 color=blue><b>[5차시] 학습목표</b></font></td></tr>       \n",
    "    <tr><td style=\"border: 1px solid black; text-align: left;\"><font size=3>\n",
    "        \n",
    "○ OpenCV를 활용한 이미지 처리 방법에 대해 학습한다.<br>\n",
    "○ 칼라/흑백/이진 이미지의 픽셀값을 출력하고 픽셀값을 변경해본다.<br>\n",
    "○ RGB 채널을 분리하고 병합해본다.\n",
    "</font></td></tr>   \n",
    "</table>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 이미지 처리 기초\n",
    "\n",
    "- 픽셀 기반 처리 : 이미지를 픽셀 단위로 처리하는 방법\n",
    "  - 이미지의 특성으로 표현하는 데 한계가 있음, 이미지 처리 속도가 느림\n",
    "- 블록 기반 처리 : 이미지를 블록 (픽셀을 그룹화한 것)  단위로 처리하는 방법\n",
    "  - 이미지의 지역적 특성을 잘 표현, 이미지 속도가  빠름  필터링\n",
    "- 주파수 기반 처리 : 이미지를  주파수 영역으로 변환하여 처리하는 방법\n",
    "  - 이미지의 전역적 특성으로 잘 표현 - FFT, DCT, WT 등\n",
    "  \n",
    "  \n",
    "- 픽셀 (pixel : picture cell)\n",
    "  - 이미지를 구성하는 최소 단위 \n",
    "  - 0-255의 값으로 구성 (검정색 0, 흰색 255)\n",
    "  \n",
    "  <img src=\"./lecture_image/05_pixel.png\">\n",
    "  \n",
    "  \n",
    "- 블럭 (block)\n",
    "  - 근방의 픽셀을 그룹핑한 것  \n",
    "  - 근방의 픽셀은 유사한 특성을 가진다는 것을 가정\n",
    "  - 일반적으로 블럭간에 중복을 시켜서 처리 – 블럭간의 Locality반영\n",
    "  \n",
    "    <img src=\"./lecture_image/05_block.png\" width=70%>\n",
    "    \n",
    "    \n",
    "- 주파수 (frequency)\n",
    "  -  주파수 (frequency) : 이미지 픽셀값들을 픽셀값의 변화분으로 변환한 것\n",
    "  - 이미지에서 주파수 : 픽셀의 변화량\n",
    "    - 고주파 성분 : 픽셀값의 변화가 큰 부분 (에지)\n",
    "    - 저주파 성분 : 픽셀값의 변화가 작은 부분\n",
    "  - 일반적인 이미지는 주로 저주파 성분으로 구성되어 있음\n",
    "  - 이미지의 중요한 특성은 주로 고주파 성분에 존재\n",
    "\n",
    "    <img src=\"./lecture_image/05_frequency.png\" width=70%>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "SVmb5bb7cJy9"
   },
   "source": [
    "## 이미지 픽셀 값 출력\n",
    "\n",
    "### 이진 이미지 픽셀 값 출력"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.image.AxesImage at 0x1c1627dd3d0>"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAOsAAADrCAYAAACICmHVAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/YYfK9AAAACXBIWXMAAAsTAAALEwEAmpwYAAADSUlEQVR4nO3ZwW3bQBBAUU2gPlwE1X8FUhG5p4f1NQfJlgI45LffO5JzGBD8IIGdtdYJOL5fey8APEesECFWiBArRIgVIsQKEedXhmfGOc8ntm3be4VDu91ue69weGutuXd9XjlnFevnnFt/bObue8hfHsXqNxgixAoRYoUIsUKEWCFCrBAhVogQK0SIFSLEChFihQixQoRYIUKsECFWiBArRIgVIsQKEWKFCLFChFghQqwQIVaIECtEiBUixAoRYoUIsUKEWCFCrBAhVogQK0SIFSLEChFihQixQoRYIUKsECFWiBArRIgVIsQKEWKFCLFChFghQqwQIVaIECtEiBUixAoRYoUIsUKEWCFCrBAhVogQK0SIFSLEChFihQixQoRYIUKsECFWiBArRIgVIsQKEWKFCLFChFghQqwQcX5leNu20/V6/apdvoWZ2XuFQ1tr7b3CoV0ul4f3fFkhQqwQIVaIECtEiBUixAoRYoUIsUKEWCFCrBAhVogQK0SIFSLEChFihQixQoRYIUKsECFWiBArRIgVIsQKEWKFCLFChFghQqwQIVaIECtEiBUixAoRYoUIsUKEWCFCrBAhVogQK0SIFSLEChFihQixQoRYIUKsECFWiBArRIgVIsQKEWKFCLFChFghQqwQIVaIECtEiBUixAoRYoUIsUKEWCFCrBAhVogQK0SIFSLEChFihQixQoRYIUKsECFWiBArRIgVIsQKEWKFiFlrPT888/zwD/XK8/yJZmbvFQ5vrXX3IfmyQoRYIUKsECFWiBArRIgVIsQKEWKFCLFChFghQqwQIVaIECtEiBUixAoRYoUIsUKEWCFCrBAhVogQK0SIFSLEChFihQixQoRYIUKsECFWiBArRIgVIsQKEWKFCLFChFghQqwQIVaIECtEiBUixAoRYoUIsUKEWCFCrBAhVogQK0SIFSLEChFihQixQoRYIUKsECFWiBArRIgVIsQKEWKFCLFChFghQqwQIVaIECtEiBUixAoRYoUIsUKEWCFCrBAhVogQK0SIFSLEChFihYjzi/N/TqfT769Y5LuYmb1XoO3t0Y1Za/3PRYB/5DcYIsQKEWKFCLFChFghQqwQIVaIECtEiBUi3gG/1ytVq1VhpQAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import cv2\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "img = cv2.imread(\"./image/checkerboard_18x18.png\",cv2.IMREAD_GRAYSCALE)\n",
    "\n",
    "plt.xticks([]), plt.yticks([])\n",
    "plt.imshow(img, cmap='gray')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- 이미지의 픽셀값은 0-255 사이 값으로 구성 (8bit 양의 정수 형태)\n",
    "- 검정색은 0, 흰색은 255"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[  0   0   0   0   0   0 255 255 255 255 255 255   0   0   0   0   0   0]\n",
      " [  0   0   0   0   0   0 255 255 255 255 255 255   0   0   0   0   0   0]\n",
      " [  0   0   0   0   0   0 255 255 255 255 255 255   0   0   0   0   0   0]\n",
      " [  0   0   0   0   0   0 255 255 255 255 255 255   0   0   0   0   0   0]\n",
      " [  0   0   0   0   0   0 255 255 255 255 255 255   0   0   0   0   0   0]\n",
      " [  0   0   0   0   0   0 255 255 255 255 255 255   0   0   0   0   0   0]\n",
      " [255 255 255 255 255 255   0   0   0   0   0   0 255 255 255 255 255 255]\n",
      " [255 255 255 255 255 255   0   0   0   0   0   0 255 255 255 255 255 255]\n",
      " [255 255 255 255 255 255   0   0   0   0   0   0 255 255 255 255 255 255]\n",
      " [255 255 255 255 255 255   0   0   0   0   0   0 255 255 255 255 255 255]\n",
      " [255 255 255 255 255 255   0   0   0   0   0   0 255 255 255 255 255 255]\n",
      " [255 255 255 255 255 255   0   0   0   0   0   0 255 255 255 255 255 255]\n",
      " [  0   0   0   0   0   0 255 255 255 255 255 255   0   0   0   0   0   0]\n",
      " [  0   0   0   0   0   0 255 255 255 255 255 255   0   0   0   0   0   0]\n",
      " [  0   0   0   0   0   0 255 255 255 255 255 255   0   0   0   0   0   0]\n",
      " [  0   0   0   0   0   0 255 255 255 255 255 255   0   0   0   0   0   0]\n",
      " [  0   0   0   0   0   0 255 255 255 255 255 255   0   0   0   0   0   0]\n",
      " [  0   0   0   0   0   0 255 255 255 255 255 255   0   0   0   0   0   0]]\n"
     ]
    }
   ],
   "source": [
    "print(img)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 그레이 이미지 픽셀 값 출력"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.image.AxesImage at 0x1c162eeaaf0>"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import cv2\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "img = cv2.imread(\"./image/checkerboard_fuzzy_18x18.jpg\",cv2.IMREAD_GRAYSCALE)\n",
    "\n",
    "plt.xticks([]), plt.yticks([])\n",
    "plt.imshow(img, cmap='gray')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[  1   0  16  21   1 133 233 252 254 253 255 229 133   0  29   2   0   0]\n",
      " [  0   2   5  19   0 136 230 255 255 247 255 228 130   0  23   1   0   0]\n",
      " [  8   6   1  28   3 139 228 252 255 248 254 226 127   1  26   4   2   2]\n",
      " [ 24  25  28  38   0 130 239 255 254 250 250 228 127   0  35  27  27  27]\n",
      " [  5   0   3   3   4 127 240 252 252 253 255 231 126   1   4   3   0   0]\n",
      " [132 128 134 121 123 161 212 226 229 226 223 204 163 125 124 128 131 131]\n",
      " [234 228 230 226 232 204 151 114 126 124 116 156 204 232 229 225 228 228]\n",
      " [254 255 255 250 255 221 102   1   0   1   0 121 224 255 255 255 255 255]\n",
      " [255 253 253 255 253 224 105   0  50  46   0 121 231 254 248 251 253 253]\n",
      " [254 249 250 255 252 221 105   0  45  49   0 127 222 255 253 255 252 252]\n",
      " [252 255 253 253 255 226 106   2   0   2   0 122 228 255 253 252 255 255]\n",
      " [235 238 231 233 233 206 140 104 107 102 108 147 205 234 237 234 231 231]\n",
      " [130 131 129 131 132 176 208 225 225 225 225 209 165 134 130 136 134 134]\n",
      " [  3   2   4   0   0 128 238 255 252 251 255 233 128   0   1   1   0   0]\n",
      " [ 20  19  32  39   8 129 237 252 252 250 254 224 129   0  38  24  20  20]\n",
      " [ 10   8   9  23   3 130 234 255 253 250 253 229 125   1  27   5  10  10]\n",
      " [  0   0   9  22   0 132 233 255 253 254 253 231 129   1  26   2   0   0]\n",
      " [  0   0   9  22   0 132 233 255 253 254 253 231 129   1  26   2   0   0]]\n"
     ]
    }
   ],
   "source": [
    "print(img)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(18, 18)\n"
     ]
    }
   ],
   "source": [
    "print(img.shape)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 칼라 이미지 픽셀 값 출력\n",
    "\n",
    "- 픽셀값 접근/변경\n",
    "   -  픽셀값은 numpy 배열 형태로 접근하고 변경\n",
    "     - img[200, 100] : 픽셀의 좌표\n",
    "     - Red, Green, Blue 순으로 출력"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.image.AxesImage at 0x1c163cf3ca0>"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import cv2\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "img = cv2.imread(\"./image/oca-cola-logo.png\",cv2.IMREAD_COLOR)\n",
    "img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)\n",
    "\n",
    "plt.xticks([]), plt.yticks([])\n",
    "plt.imshow(img)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "id": "sYbUG6QjhInH",
    "outputId": "021f7dfe-22e1-4b7a-97c7-62e574e5794b"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(700, 700, 3)\n"
     ]
    }
   ],
   "source": [
    "print(img.shape)"
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
      "[199   4  21]\n",
      "[253 253 253]\n"
     ]
    }
   ],
   "source": [
    "# 픽셀값\n",
    "# unit8 : unsigned int 8bit 양수 정수 0~255\n",
    "# array([R, G, B])\n",
    "print(img[200,100])\n",
    "print(img[400,10])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<table border=1 width=100%>\n",
    "    <tr><td style=\"border: 1px solid black; width:600px; text-align: left;\"><font size=4 color=red><b>실습문제</b></font><br><br>\n",
    "        <font size=4>\n",
    "○ 다른 이미지의 픽셀값을 출력해 보자.<br>\n",
    "   </td></tr>   \n",
    "</table>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "vCtmaISpcJzD"
   },
   "source": [
    "## 픽셀값 변경"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "id": "2gjsiaHRhInQ"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.image.AxesImage at 0x1c162881340>"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "img[200,100] = [0,0,255]\n",
    "img[201,100] = [0,0,255]\n",
    "img[200,101] = [0,0,255]\n",
    "img[201,101] = [0,0,255]\n",
    "\n",
    "plt.xticks([]), plt.yticks([])\n",
    "plt.imshow(img)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<table border=1 width=100%>\n",
    "    <tr><td style=\"border: 1px solid black; width:600px; text-align: left;\"><font size=4 color=red><b>실습문제</b></font><br><br>\n",
    "        <font size=4>\n",
    "○ 다른 이미지의 픽셀값을 변경해 보자.<br>\n",
    "   </td></tr>   \n",
    "</table>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "LjYOOULscJzS"
   },
   "source": [
    "# RGB 채널 다루기\n",
    "\n",
    "- 이미지 채널\n",
    "     - 흑백은 1개의 채널 이미지로 구성되고, 칼라는 Red, Green, Blue 3개의 채널 이미지로 구성\n",
    "\n",
    "    <img src=\"./lecture_image/05_image_channel.png\" width=50%>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## RGB 채널 분리하기\n",
    "\n",
    "- <font color=red>변수 = img[:, :, 채널번호]</font>\n",
    "\n",
    "  - img[:, :, 0] : red 채널\n",
    "  - img[:, :, 1] : green 채널\n",
    "  - img[:, :, 2] : blue 채널"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "id": "EIC_KwaLhInc"
   },
   "outputs": [],
   "source": [
    "#실습"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- 흰색이 가까울수록 픽셀 수가 많다는 것을 의미"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "5DC21U8fcJzV"
   },
   "source": [
    "## RGB 채널 합치기"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "OrZ8mjulhIng"
   },
   "source": [
    "- cv2.merge((r, g, b) : RGB 각 채널을 합침"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "id": "krGnPPhhhIne"
   },
   "outputs": [],
   "source": [
    "#실습"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "1IZ6XgEUcJzG"
   },
   "source": [
    "## 픽셀값을 RGB 채널 값을 이용해서 변경하기\n",
    "\n",
    "- <font color=red>img.itemset((x, y, 0), 0)</font>\n",
    "  - itemset((픽셀y위치, 픽셀x위치, 채널), 색상레벨)\n",
    "  - 채널 (0 : Red, 1 : Green, 2 : Blue)  \n",
    "  - 0번 채널의 (x, y) 픽셀의 값을 0으로 변경  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "id": "esFOpRMWhInT"
   },
   "outputs": [],
   "source": [
    "#실습"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<table border=1 width=100%>\n",
    "    <tr><td style=\"border: 1px solid black; width:600px; text-align: left;\"><font size=4 color=red><b>실습문제</b></font><br><br>\n",
    "        <font size=4>\n",
    "○ 다른 채널의 픽셀값을 변경해 보자.<br>\n",
    "   </td></tr>   \n",
    "</table>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "xpewff3WcJzL"
   },
   "source": [
    "# 이미지의 속성 출력\n",
    "\n",
    "- img.shape : 이미지의 크기 및 채널 \n",
    "- img.size : 이미지의 전체 픽셀 수\n",
    "- img.dtype : 데이터 타입"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "id": "gFcfIROQhInW",
    "outputId": "113bc165-e42c-4da9-fd9a-cc8ef07474d3"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(700, 700, 3)\n"
     ]
    }
   ],
   "source": [
    "print(img.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1470000\n"
     ]
    }
   ],
   "source": [
    "print(img.size)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "uint8\n"
     ]
    }
   ],
   "source": [
    "print(img.dtype)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<table border=1 width=100%>\n",
    "    <tr><td style=\"border: 1px solid black; width:600px; height:40px; text-align: center;\"><font size=4 color=blue><b>[5차시] 학습요약</b></font></td></tr>       \n",
    "    <tr><td style=\"border: 1px solid black; text-align: left;\"><font size=3>\n",
    "        \n",
    "○ 이미지 처리 방법 : 픽셀기반, 블록기반, 주파수 기반 처리<br>\n",
    "○ 이미지의 픽셀값은 0-255 사이 값으로 구성 (8bit 양의 정수 형태) - 검정색은 0, 흰색은 255<br>\n",
    "○ 픽셀값은 3차원 배열 형태로 접근 ([x축, y축, 채널])<br>\n",
    "○ <font color=red>itemset((x축, y축, 채널), 값)</font> : 해당 채널의 픽셀값을 변경<br><br>\n",
    "\n",
    "○ <font color=red>img.shape</font> : 이미지 크기<br>\n",
    "○ <font color=red>img.size</font> : 전체 픽셀 수<br>\n",
    "○ <font color=red>img.dtype</font> : 데이터 타입\n",
    "        \n",
    "</font></td></tr>   \n",
    "</table>"
   ]
  }
 ],
 "metadata": {
  "colab": {
   "collapsed_sections": [
    "LTU9kbKtcJ0a"
   ],
   "name": "DL008_02_OpenCV.ipynb",
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
    "width": "307.2px"
   },
   "toc_section_display": true,
   "toc_window_display": true
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
