{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "87d25bd4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "9\n",
      "17\n"
     ]
    }
   ],
   "source": [
    "list1 = [2, 5, 7, 9, 10]\n",
    "print(list1[0])\n",
    "print(list1[3])\n",
    "print(list1[2]+list1[-1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "4b59e7e9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['a', 'b', 'c']\n",
      "b\n"
     ]
    }
   ],
   "source": [
    "# 2차원 리스트\n",
    "list2 = [1,2,3,['a','b','c']]\n",
    "temp = list2[3]\n",
    "print(temp)\n",
    "print(list2[3][1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "290294e1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2]\n",
      "[0, 1]\n",
      "[3, 4]\n",
      "[3]\n"
     ]
    }
   ],
   "source": [
    "list3 = [0, 1, 2, 3, 4,]\n",
    "print(list3[1:3])\n",
    "print(list3[:2])\n",
    "print(list3[3:])\n",
    "print(list3[3:4])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "ef9255a7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, 3, 4, 5, 6]\n"
     ]
    }
   ],
   "source": [
    "list4 = [1,2,3]\n",
    "list5 = [3,4,5,6]\n",
    "print(list4 + list5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "252bf03b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0, 1, 2, 3, 4, 5]\n",
      "[0, 1, 2, 3, 4, 5, 6]\n"
     ]
    }
   ],
   "source": [
    "list5 = [0,1,2,3,4]\n",
    "list5.append(5)\n",
    "print(list5)\n",
    "list5.append(6)\n",
    "print(list5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "121af823",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['사과', '수박', '오렌지']\n"
     ]
    }
   ],
   "source": [
    "list_ = ['사과','포도',['수박','멜론'],'복숭아','딸기','오렌지']\n",
    "apple,waterMelon,orange = list_[0],list_[2][0],list_[-1]\n",
    "choice_list = []\n",
    "choice_list.append(apple)\n",
    "choice_list.append(waterMelon)\n",
    "choice_list.append(orange)\n",
    "print(choice_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "798facdf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[0, 5, 1, 2, 3, 4]"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# insert(원하는위치 인덱스 , 넣고싶은 값)\n",
    "list5 = [0,1,2,3,4,]\n",
    "list5.insert(1,5)\n",
    "list5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "e2d45ad8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[0, 5, 1, 2, 3, 6, 4]"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list5.insert(5,6)\n",
    "list5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "8981289c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[['LOVE DIVE', '아이브'], ['사랑인가봐', '멜로망스'], ['TOMBOY', '(여자)아이들'], ['That That', '싸이']]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "[['LOVE DIVE', '아이브'],\n",
       " ['사랑인가봐', '멜로망스'],\n",
       " ['TOMBOY', '(여자)아이들'],\n",
       " ['봄여름가을겨울', '빅뱅'],\n",
       " ['That That', '싸이']]"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "music_list = [['LOVE DIVE',\"아이브\"],[\"TOMBOY\",'(여자)아이들'],[\"That That\",\"싸이\"]]\n",
    "music_list.insert(1,[\"사랑인가봐\",\"멜로망스\"])\n",
    "print(music_list)\n",
    "music_list.insert(3,['봄여름가을겨울','빅뱅'])\n",
    "music_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "dcfaac7c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "인덱스 입력 >> 4\n",
      "노래 제목 >> 나의X에게\n",
      "가수명 >> 경서\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "[['LOVE DIVE', '아이브'],\n",
       " ['사랑인가봐', '멜로망스'],\n",
       " ['TOMBOY', '(여자)아이들'],\n",
       " ['봄여름가을겨울', '빅뱅'],\n",
       " ['나의X에게', '경서'],\n",
       " ['나의X에게', '경서'],\n",
       " ['That That', '싸이']]"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "index_value = int(input(\"인덱스 입력 >> \"))\n",
    "song = input(\"노래 제목 >> \")\n",
    "singer = input(\"가수명 >> \")\n",
    "\n",
    "music_list.insert(index_value,[song,singer])\n",
    "music_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "1174f290",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[0, 1, 2, 3, 4]"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list6 = [0,1,2,3,4]\n",
    "list6"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "e5bed35d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "수정 전 : 1\n",
      "수정 후 : 7\n"
     ]
    }
   ],
   "source": [
    "print(\"수정 전 :\",list6[1])\n",
    "list6[1] = 7\n",
    "print(\"수정 후 :\",list6[1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "0b6c081b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[0, 7, 7, 4]"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 리스트 값 수정\n",
    "list6[2:4] = [7]\n",
    "list6"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "3b3f5999",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, 4, 7]\n"
     ]
    }
   ],
   "source": [
    "array = [1,2,3,4,5]\n",
    "array[-1] = 7\n",
    "print(array)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "75b2d911",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, ['a', 'b', 'c'], 3, 4, 7]"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "array[1] = ['a','b','c']\n",
    "array"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "f3c7e3a2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, ['a', 'b', 'c'], 3, 'd', 'e', 'f', 'g']"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "array[3:] = ['d','e','f','g']\n",
    "array"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "79715745",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['h', 'i', 'j', ['a', 'b', 'c'], 3, 'd', 'e', 'f', 'g']"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "array[:1]= 'h','i','j'\n",
    "array"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c17c874e",
   "metadata": {},
   "source": [
    "### 리스트 값 삭제"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "4366f942",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[0, 5]"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list7 = [0,1,2,3,4,5]\n",
    "del list7[1:5]\n",
    "list7"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "dee21ca5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['a', 'c', 'd', 'e']"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list7 = ['a','b','c','d','e']\n",
    "list7.remove('b')\n",
    "list7"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "42a821c2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[9, 77, 13, 51, 100, 3]"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list8 = [9,77,13,51,100,3]\n",
    "list8"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "491c653b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[3, 9, 13, 51, 77, 100]"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 오름차순 정렬\n",
    "list8.sort()\n",
    "list8"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "6deb72ae",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[9, 77, 13, 51, 100, 3]"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list9 = [9,77,13,51,100,3]\n",
    "list9"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "42ec0196",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[3, 100, 51, 13, 77, 9]"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 내림차순 X 거꾸로 뒤집는 거임\n",
    "list9.reverse()\n",
    "list9"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "389b889e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[9, 77, 13, 51, 100, 3]"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 내림차순 첫번째 방법 정렬시킨후 거꾸로 뒤집기\n",
    "list10 = [9,77,13,51,100,3]\n",
    "list10"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "f93f980d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[3, 9, 13, 51, 77, 100]"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list10.sort()\n",
    "list10"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "08ce543f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[100, 77, 51, 13, 9, 3]"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list10.reverse()\n",
    "list10"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "da6b81e3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[100, 77, 51, 13, 9, 3]"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 내림차순 두번째 방법\n",
    "list10.sort(reverse=True)\n",
    "list10"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "9058dd84",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list11 = ['a','b','c','d','e','f']\n",
    "list11.index('f')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "dfed9603",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "d\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "['a', 'b', 'c', 'e', 'f']"
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list12 = ['a','b','c','d','e','f']\n",
    "print(list12.pop(3))\n",
    "list12"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "188f6c45",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list13 = [0,1,2]\n",
    "len(list13)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "4d43e600",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "6"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list14 = ['a','b','c','d','e','f']\n",
    "len(list14)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "0189dfd5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 64,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "str1 = \"파이썬 최고\"\n",
    "print(\"파이썬\" in str1)\n",
    "\"파이썬\" not in str1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "7b698825",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "list1 = [77,38,10]\n",
    "print(33 in list1)\n",
    "print(33 not in list1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "a76f70f4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "검색할 문자를 입력하세요 :i\n",
      "i는 2번 들어있네유!\n"
     ]
    }
   ],
   "source": [
    "s = \"Hi, My name is SeongWoo\"\n",
    "a = input(\"검색할 문자를 입력하세요 : \")\n",
    "if a in s:\n",
    "    print(f\"{a}는 {s.count(a)}번 들어있네유!\")\n",
    "else:\n",
    "    print(f\"{a}는 들어있지 않네유..\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9806b601",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6a5d6abb",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "39169880",
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
