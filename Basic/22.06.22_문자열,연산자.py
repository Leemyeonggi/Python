{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "03deb24c",
   "metadata": {},
   "source": [
    "### 포매팅 첫번째 방법"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "a85e29dd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'오늘은 7월 8입니다.'"
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "day = 8\n",
    "s = \"오늘은 7월 %d입니다.\"%day\n",
    "s"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 128,
   "id": "b00e4459",
   "metadata": {},
   "outputs": [],
   "source": [
    "# digit = 십진수\n",
    "# %d = 정수\n",
    "# %s = 문자열\n",
    "# %c = 문자1개\n",
    "# %f = 실수"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "d30ad8b8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'오늘은 8월 8일입니다.'"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "month = 8\n",
    "day = 8\n",
    "s = \"오늘은 %d월 %d일입니다.\"%(month,day)\n",
    "s"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e1e69eef",
   "metadata": {},
   "source": [
    "### 포매팅 두번째 방법"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "33de9089",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'오늘은 6월 22일 입니다.'"
      ]
     },
     "execution_count": 69,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "month = 6\n",
    "day = 22\n",
    "s = \"오늘은 {}월 {}일 입니다.\".format(month,day)\n",
    "s"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0e04d7a1",
   "metadata": {},
   "source": [
    "### 포매팅 세번째 방법\n",
    "#### f-string 포매팅"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "aa5cfce8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'오늘은 7월 7일 입니다.'"
      ]
     },
     "execution_count": 70,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "month = 7\n",
    "day = 7\n",
    "s = f\"오늘은 {month}월 {day}일 입니다.\"\n",
    "s"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7b9bc8e3",
   "metadata": {},
   "source": [
    "x = 100\n",
    "y = 200\n",
    "sum2 = x + y\n",
    "print(f\"{x}과 {y}의 합은 {sum2}입니다.\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "81e5059f",
   "metadata": {},
   "source": [
    "### 자주 사용하는 문자열 함수"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "b7be5b55",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n"
     ]
    }
   ],
   "source": [
    "# count 함수 : 문자열에 포함된 문자 개수 세기\n",
    "s = '오늘 점심 메뉴는 탕수육입니다. 저는 탕수육을 매우 좋아해서 탕수육만 먹을겁니다'\n",
    "print(s.count('탕수육'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "08e89fa2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'오늘 점심 메뉴는 탕수육입니다.'"
      ]
     },
     "execution_count": 72,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# strip 함수 : 양쪽 공백 지우기\n",
    "s = \"   오늘 점심 메뉴는 탕수육입니다.     \"\n",
    "s.strip()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "e8106996",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'오늘 점심 메뉴는 다이어트입니다. 저는 다이어트을 매우 좋아해서 다이어트만 먹을겁니다.'"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# replace 함수 : 특정문자를 원하는 문자로 변경하기\n",
    "s = '오늘 점심 메뉴는 탕수육입니다. 저는 탕수육을 매우 좋아해서 탕수육만 먹을겁니다.'\n",
    "s.replace('탕수육','다이어트')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "9e8c206a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['오늘 점심 메뉴는 탕수육입니다', '저는 탕수육을 매우 좋아해서 탕수육만 먹을겁니다.']"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# split 함수 : 문자열을 특정 문자 기준으로 나눠주기\n",
    "s.split('. ')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "46a33310",
   "metadata": {},
   "source": [
    "### 산술 연산자"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "0687cee4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1.4285714285714286\n",
      "1\n",
      "3\n"
     ]
    }
   ],
   "source": [
    "num1  = 10\n",
    "num2 = 7\n",
    "print(num1 / num2) # 나누기\n",
    "print(num1 // num2) #몫\n",
    "print(num1 % num2) #나머지"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "id": "3720ccd0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "안녕하세요\n"
     ]
    }
   ],
   "source": [
    "str1 = \"안녕\"\n",
    "str2 = \"하세요\"\n",
    "print(str1+str2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "id": "5a52bb3d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "107\n"
     ]
    }
   ],
   "source": [
    "str1 = \"10\"\n",
    "str2 = \"7\"\n",
    "print(str1 + str2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "id": "0dbcb732",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "107\n",
      "17\n"
     ]
    }
   ],
   "source": [
    "num1 = 10\n",
    "str2 = \"7\"\n",
    "print(str(num1) +str2) # 문자열과 정수형은 더할수 없다\n",
    "print(num1 + int(str2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "id": "c3fd62dd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "더하기 결과 : 26\n",
      "빼기 결과 : 20\n",
      "곱하기 결과 : 69\n",
      "나누기 결과 : 7.666666666666667\n"
     ]
    }
   ],
   "source": [
    "num1 = 23\n",
    "num2 = 3\n",
    "print(\"더하기 결과 :\",num1 + num2)\n",
    "print(\"빼기 결과 :\",num1 - num2)\n",
    "print(\"곱하기 결과 :\",num1 * num2)\n",
    "print(\"나누기 결과 :\",num1 / num2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "df089ecb",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "정수를 입력하세요>>3\n",
      "정수를 입력하세요>>7\n",
      "더하기 결과 : 10\n",
      "빼기 결과 : -4\n",
      "곱하기 결과 : 21\n",
      "나누기 결과 : 0.42857142857142855\n"
     ]
    }
   ],
   "source": [
    "num1 = int(input(\"정수를 입력하세요>>\"))\n",
    "num2 = int(input(\"정수를 입력하세요>>\"))\n",
    "print(\"더하기 결과 :\",num1 + num2)\n",
    "print(\"빼기 결과 :\",num1 - num2)\n",
    "print(\"곱하기 결과 :\",num1 * num2)\n",
    "print(\"나누기 결과 :\",num1 / num2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "53dd983f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "python 점수 입력>> 50\n",
      "머신러닝 점수 입력>> 50\n",
      "딥러닝 점수 입력>> 50\n",
      "합계 : 150\n",
      "평균 : 50.0\n"
     ]
    }
   ],
   "source": [
    "a = int(input(\"python 점수 입력>> \"))\n",
    "b = int(input(\"머신러닝 점수 입력>> \"))\n",
    "c = int(input(\"딥러닝 점수 입력>> \"))\n",
    "\n",
    "total = a+b+c\n",
    "\n",
    "print(\"합계 : {}\".format(total))\n",
    "print(\"평균 : {}\".format((total)/3))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "id": "eb2e6278",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "시간 입력 >>1123\n",
      "0시간 18분 43초\n"
     ]
    }
   ],
   "source": [
    "time = int(input(\"시간 입력 >> \"))\n",
    "hour = time // 3600\n",
    "minute = (time%3600) // 60\n",
    "second = (time%3600) % 60\n",
    "print(f\"{hour}시간 {minute}분 {second}초\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "id": "6eae62ce",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "xxxxxxxxxx\n",
      "안녕하세요안녕하세요\n"
     ]
    }
   ],
   "source": [
    "s = 'x'\n",
    "print(s*10)\n",
    "s = '안녕하세요'\n",
    "print(s*2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "id": "93215e0f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "********** 연산하기 **********\n",
      "정수입력 >> 10\n",
      "정수입력 >> 20\n",
      "+연산자 입력 >> +\n",
      "10 + 20 = 30\n"
     ]
    }
   ],
   "source": [
    "print(\"*\"*10,\"연산하기\",\"*\"*10)\n",
    "num1 = int(input(\"정수입력 >> \"))\n",
    "num2 = int(input(\"정수입력 >> \"))\n",
    "cal = input(\"+연산자 입력 >> \")\n",
    "print(f\"{num1} {cal} {num2} =\",num1+num2)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "dce0d54e",
   "metadata": {},
   "source": [
    "### 지수 연산자"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "id": "fd90f5e6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "정수 입력 >> 2\n",
      "지수 입력 >> 3\n",
      "2의 3승은 8입니다.\n"
     ]
    }
   ],
   "source": [
    "num = int(input('정수 입력 >> '))\n",
    "power = int(input('지수 입력 >> '))\n",
    "print(f\"{num}의 {power}승은 {num**power}입니다.\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "988196cc",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "id": "dc7ed6a7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n",
      "True\n",
      "False\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "a = 3\n",
    "b = 7\n",
    "print(a > b)\n",
    "print(a <= b)\n",
    "print(a == b)\n",
    "print(a != b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 126,
   "id": "503093dc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "a:3,b:7\n",
      "True\n",
      "False\n",
      "False\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "a = random.randint(1,10)\n",
    "b = random.randint(1,10)\n",
    "print(f\"a:{a},b:{b}\")\n",
    "\n",
    "print(a < b)\n",
    "print(a >= b)\n",
    "print(a == b)\n",
    "print(a != b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 132,
   "id": "9a1bfcb1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 132,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a = 3\n",
    "b = 7\n",
    "not a < b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 131,
   "id": "406d05e8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 131,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a = 3\n",
    "b = 7\n",
    "not a == b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 134,
   "id": "1ff0eb29",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n",
      "False\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "print(3>5 and 10 == 20)\n",
    "print(3>5 and 10<20)\n",
    "print(3 < 5 and 10 < 20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 135,
   "id": "e6da05ad",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n",
      "True\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "print(3 > 5 or 10 == 20)\n",
    "print(3 > 5 or 10 < 20)\n",
    "print(3 < 5 or 10 < 20)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e8acd588",
   "metadata": {},
   "source": [
    "### 삼항 연산자"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 136,
   "id": "a7648659",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'합격!'"
      ]
     },
     "execution_count": 136,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "score = 80\n",
    "\"합격!\" if score >= 60 else \"불합격\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 137,
   "id": "045e4f10",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'불합격'"
      ]
     },
     "execution_count": 137,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "score = 50\n",
    "\"합격!\" if score >= 60 else \"불합격\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 139,
   "id": "b9b076df",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "정수입력 >> 3\n",
      "정수입력 >> 10\n",
      "b:10\n"
     ]
    }
   ],
   "source": [
    "a = int(input(\"정수입력 >> \"))\n",
    "b = int(input(\"정수입력 >> \"))\n",
    "\n",
    "print(f\"b:{b}\")if b>a else print(f\"a:{a}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 142,
   "id": "0a972bd7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "첫 번째 정수입력 >> 3\n",
      "두 번째 정수입력 >> 7\n",
      "두 수의 차 : 4\n"
     ]
    }
   ],
   "source": [
    "a = int(input(\"첫 번째 정수입력 >> \"))\n",
    "b = int(input(\"두 번째 정수입력 >> \"))\n",
    "\n",
    "print(\"두 수의 차 :\",a-b) if a>b else print(\"두 수의 차 :\",b-a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 146,
   "id": "a3e89473",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "정수 입력 >> 33\n",
      "33는(은) 홀수입니다.\n"
     ]
    }
   ],
   "source": [
    "num = int(input('정수 입력 >> '))\n",
    "print(f\"{num}는(은) 홀수입니다.\") if num%2 != 0 else print(f\"{num}는(은) 짝수입니다.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c3c35c66",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c8dacb40",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "aa885d3a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "94354cab",
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
   "toc_window_display": true
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
