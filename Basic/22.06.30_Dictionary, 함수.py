{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "9dfe6957",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'name': 'MG', 'age': 26, 'phone': '010-1234-5678'}\n",
      "<class 'dict'>\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "{'name': 'MG', 'age': 26}"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dic1 = {\"name\" : \"MG\", \"age\" : 26, \"phone\" : '010-1234-5678'}\n",
    "print(dic1)\n",
    "print(type(dic1))\n",
    "dic1['name']\n",
    "del dic1['phone']\n",
    "dic1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "bb4bf3ff",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'name': 'MG', 'age': 26, 'birth': '06/10'}"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dic1['birth'] = '06/10'\n",
    "dic1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "320f3253",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'노래제목': '참고사항', '가수': '이무진', '날짜': '2022.06.23'}\n"
     ]
    }
   ],
   "source": [
    "dic_test = {\"노래제목\" : \"참고사항\"}\n",
    "dic_test[\"가수\"] = \"이무진\"\n",
    "dic_test[\"날짜\"] = \"2022.06.23\"\n",
    "print(dic_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "ea1b89e9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'MG'"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dic1.get('name') # get은 값이 없어도 error가 안남 None 값을 돌려줌"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "2b703c2c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "dict_keys(['name', 'age', 'birth'])\n",
      "['MG', 26, '06/10']\n"
     ]
    }
   ],
   "source": [
    "print(dic1.keys())\n",
    "print(list(dic1.values()))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "5d2d190d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "name\n",
      "age\n",
      "birth\n"
     ]
    }
   ],
   "source": [
    "for key in dic1.keys():\n",
    "    print(key)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "0a594de8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "MG\n",
      "26\n",
      "06/10\n"
     ]
    }
   ],
   "source": [
    "for value in dic1.values():\n",
    "    print(value)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "93918a51",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "name \t MG\n",
      "age \t 26\n",
      "birth \t 06/10\n"
     ]
    }
   ],
   "source": [
    "for key, value in dic1.items(): # dic.items() key값 과 value값을 둘다 담아올수잇음\n",
    "    print(key,\"\\t\",value)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "c11764c5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "False\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "print('name' in dic1) # key in dic 은 key 값에 한해서만 가능\n",
    "print('gender' in dic1)\n",
    "print('age' in dic1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "8c3f98bd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{}"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dic1.clear()\n",
    "dic1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "92ebd217",
   "metadata": {},
   "outputs": [],
   "source": [
    "def number_sum(num1,num2):\n",
    "    result = num1 + num2\n",
    "    return result"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "d7a0d6f0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "13"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "number_sum(3,10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "2b10920e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "첫 번째 정수 입력 >> 10\n",
      "두 번째 정수 입력 >> 3\n",
      "7\n"
     ]
    }
   ],
   "source": [
    "def number_minus(num1,num2):\n",
    "    result = num1 - num2\n",
    "    return result\n",
    "num1 = int(input(\"첫 번째 정수 입력 >> \"))\n",
    "num2 = int(input(\"두 번째 정수 입력 >> \"))\n",
    "result = number_minus(num1,num2)\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d94fb736",
   "metadata": {},
   "outputs": [],
   "source": [
    "def number_minus(num1, num2) :\n",
    "    result = 0\n",
    "    if num1 > num2 :\n",
    "        result = num1 - num2\n",
    "    else :\n",
    "        result = num2 - num1\n",
    "    return result\n",
    "\n",
    "num1 = int(input(\"첫 번째 정수 입력 >> \"))\n",
    "num2 = int(input(\"두 번째 정수 입력 >> \"))\n",
    "result = number_minus(num1, num2)\n",
    "result"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "70fc1a46",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "문자열 입력 >> ㅋ을모두지워주세욬ㅋㅋㅋㅋ\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'을모두지워주세욬'"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def s_replace(s):    \n",
    "    result = s.replace('ㅋ','')\n",
    "    return result\n",
    "s = input('문자열 입력 >> ')\n",
    "s = s_replace(s)\n",
    "s                "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "d6f2ef91",
   "metadata": {},
   "outputs": [],
   "source": [
    "def cal(n1,n2,op):\n",
    "    \"\"\"덧셈과 뺄셈을 계산하는 함수입니다.\"\"\"\n",
    "    if op == '+':\n",
    "        result = n1+n2\n",
    "    if n1 > n2 :\n",
    "        if op == '-':\n",
    "            result = n1-n2\n",
    "    else:\n",
    "        result = n2-n1\n",
    "    return result"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "e5619eb0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "첫 번째 정수 입력 >> 7\n",
      "두 번째 정수 입력 >> 8\n",
      "연산자 입력 (+,-)-\n",
      "1\n"
     ]
    }
   ],
   "source": [
    "num1 = int(input(\"첫 번째 정수 입력 >> \"))\n",
    "num2 = int(input(\"두 번째 정수 입력 >> \"))\n",
    "op = input(\"연산자 입력 (+,-)\")\n",
    "result = cal(num1,num2,op)\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "edfe6926",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "오늘 하루 정말 좋았습니다^^화이팅!\n"
     ]
    }
   ],
   "source": [
    "print(\"오늘 하루 정말 좋았습니다\",\"화이팅!\" ,sep = \"^^\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "a652106b",
   "metadata": {},
   "outputs": [],
   "source": [
    "def divisor(num):\n",
    "    for i in range(1,num+1):\n",
    "        if num % i == 0:\n",
    "            print(i, end = \" \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "id": "85d2203e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 2 4 5 10 20 25 50 100 "
     ]
    }
   ],
   "source": [
    "divisor(100)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0fa0e60c",
   "metadata": {},
   "outputs": [],
   "source": [
    "def add(*args):  # * 가변 매개변수 : 여러개 값을 받더라도 동작할수잇음\n",
    "    print(args)  # 전달된 모든 인수는 튜플형태"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "id": "ab377203",
   "metadata": {},
   "outputs": [],
   "source": [
    "def add(*args):\n",
    "    print(sum(args))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "eba60241",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6\n"
     ]
    }
   ],
   "source": [
    "add(1,2,3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "id": "3065edf7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "55\n"
     ]
    }
   ],
   "source": [
    "add(1,2,3,4,5,6,7,8,9,10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "a3d74b63",
   "metadata": {},
   "outputs": [],
   "source": [
    "review_naver = ['윌 스미스가 하드캐리 ㅋㅋㅋㅋㅋㅋㅋㅋ',\n",
    "               '쟈스민 너무 멋지고 팬 엄청나게 생길듯ㅋㅋ',\n",
    "               '기대보다 더욱 재밌는 영화였다^^']\n",
    "review_google = ['색감도 노래도 너무 화려하고 재밌었어요 ㅋㅋㅋ',\n",
    "                '오늘부터 디즈니 팬입니닼ㅋㅋ',\n",
    "                '디즈니의 새로운 해석도 놀랍고, 윌스미스도 신의한수!']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "e189cf02",
   "metadata": {},
   "outputs": [],
   "source": [
    "def jegugi(string):\n",
    "    for i in string:\n",
    "        print(i.replace(\"ㅋ\",\"\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "468960b7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "윌 스미스가 하드캐리 \n",
      "쟈스민 너무 멋지고 팬 엄청나게 생길듯\n",
      "기대보다 더욱 재밌는 영화였다^^\n",
      "색감도 노래도 너무 화려하고 재밌었어요 \n",
      "오늘부터 디즈니 팬입니닼\n",
      "디즈니의 새로운 해석도 놀랍고, 윌스미스도 신의한수!\n"
     ]
    }
   ],
   "source": [
    "jegugi(review_naver)\n",
    "jegugi(review_google)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fb7b57e1",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "aeb24e5c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e1518bf7",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4c970572",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6417fcf6",
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
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
