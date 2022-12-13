{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "e1ad3923",
   "metadata": {},
   "source": [
    "# OOP (Object Oriented Programming)\n",
    "- 객체 지향 프로그래밍\n",
    "- 객체를 만들기 위한 설계도 : Class\n",
    "- 설계도로부터 만들어지는 개념 : Object\n",
    "- 설계도로부터 실체화된(구현화된) : Instance"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "a3e4a3af",
   "metadata": {},
   "outputs": [],
   "source": [
    "class 집:\n",
    "    # class 내부 요소 : 멤버(member)\n",
    "    # 멤버 변수 => 필드,특성,속성\n",
    "    화장실 = 2\n",
    "    방 = 4\n",
    "    층 = 2\n",
    "    다락방 = True\n",
    "    # 멤버 함수 => 메소드,함수,기능\n",
    "    def 정보(self):\n",
    "        print(f'화장실 : {self.화장실}개')\n",
    "        print(f'방 : {self.방}개')\n",
    "        print(f'층 : {self.층}층')\n",
    "        print(f'다락방 : {self.다락방}')\n",
    "    # java => 컴파일언어, python => 인터프리터 언어 (한줄한줄씩 로드)\n",
    "    # self. => 클래스내부를 가리킴\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "071b3aaa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "화장실 : 1개\n",
      "방 : 5개\n",
      "층 : 2층\n",
      "다락방 : True\n",
      "----------------\n",
      "화장실 : 2개\n",
      "방 : 4개\n",
      "층 : 2층\n",
      "다락방 : True\n"
     ]
    }
   ],
   "source": [
    "명기집 = 집()\n",
    "명기집.화장실=1\n",
    "명기집.방 = 5\n",
    "명기집.정보()\n",
    "\n",
    "print('----------------')\n",
    "\n",
    "부모님집 = 집()\n",
    "부모님집.정보()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "id": "74eb8a1f",
   "metadata": {},
   "outputs": [],
   "source": [
    "class 고양이 :\n",
    "    # 접근 제한자(Access Modifier) __(언더바 두개 외부,자식 막아짐)\n",
    "    # 정보은닉, 캡슐화              _(언더바 한개 외부막아짐, 자식은 상속가능)\n",
    "    \n",
    "    \n",
    "    # 좋아하는 사료, 무늬, 털색깔\n",
    "    이름,좋아하는사료, 무늬, 털색깔 = None,None,None,None\n",
    "    \n",
    "    # 울음소리, 먹이를 먹다\n",
    "    def 울다(self):\n",
    "        print(\"크르렁\")\n",
    "    def 먹이를먹다(self):\n",
    "        print(\"와쿠와구\")\n",
    "    def 정보(self):\n",
    "        print(f'이름 : {self.이름}\\n좋아하는사료 : {self.좋아하는사료}\\n무늬 : {self.무늬}\\n털색깔 : {self.털색깔}\\n')\n",
    "    def __init__(self,이름,좋아하는사료,무늬,털색깔):\n",
    "        self.이름 = 이름\n",
    "        self.좋아하는사료 = 좋아하는사료\n",
    "        self.무늬 = 무늬\n",
    "        self.털색깔 = 털색깔\n",
    "# 생성자(constructor)\n",
    "# 객체가 생성될 때 자동으로 호출"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "7172a16a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "이름 : 니달리\n",
      "좋아하는사료 : 뼈다귀\n",
      "무늬 : 없음\n",
      "털색깔 : 흰색\n",
      "\n",
      "와쿠와구\n",
      "크르렁\n"
     ]
    }
   ],
   "source": [
    "렝가 = 고양이('렝가','뼈다귀','없음','흰색')\n",
    "렝가.이름 = '니달리'\n",
    "렝가.정보()\n",
    "렝가.먹이를먹다()\n",
    "렝가.울다()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "69ec759d",
   "metadata": {},
   "source": [
    "# 추상화(Abstraction)\n",
    "- 객체의 공통적인 특징을 추출하는 작업\n",
    "- 단, 너무 세부적인 정보 배제\n",
    "\n",
    "# 상속 (Inheritance)\n",
    "- 부모클래스의 멤버 (변수,함수)를 물려 받아\n",
    "- 자식클래스를 정의\n",
    "\n",
    "# 캡슐화(Encapsulation)\n",
    "- 개발자가 원하는 변수, 함수만 접근할 수 있도록\n",
    "- 정보를 제한\n",
    "\n",
    "# 다형성(Polymophism)\n",
    "- 다양한 형태를 나타낼 수 있는 능력"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "181578c0",
   "metadata": {},
   "outputs": [],
   "source": [
    "class 샴고양이(고양이):\n",
    "    털색깔 = \"투톤\"\n",
    "    \n",
    "    def __init__(self,이름,좋아하는사료,무늬):\n",
    "        self.이름 = 이름\n",
    "        self.좋아하는사료 = 좋아하는사료\n",
    "        self.무늬 = 무늬"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "65008588",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "이름 : 샤오미\n",
      "좋아하는사료 : 츄르\n",
      "무늬 : 없음\n",
      "털색깔 : 투톤\n",
      "\n"
     ]
    }
   ],
   "source": [
    "샤오미 = 샴고양이(\"샤오미\",\"츄르\",\"없음\")\n",
    "샤오미.정보()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "492204b7",
   "metadata": {},
   "outputs": [],
   "source": [
    "class 계산기:\n",
    "    \n",
    "    def add(self,num1,num2):\n",
    "        return num1+num2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "id": "db23b7ee",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'35'"
      ]
     },
     "execution_count": 76,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "계산기1 = 계산기()\n",
    "계산기1.add(3,6)\n",
    "계산기1.add('3','5')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b30dcb3b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e57bd152",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "df7313c1",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6ea703c1",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "da6c92a9",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0e9d0600",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f0f82430",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "af2a4a7b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "14684431",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "13f6008a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f9938ecf",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "049b45bf",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ad345d4d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4733737a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1464bfd6",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0b964155",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "62673b44",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "249e15fc",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "785ee7f4",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7358ceda",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2cbfa981",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "773a776d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "21216203",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7ac377d3",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9e07850c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fcb0e5e9",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1fe993eb",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "87612340",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5608a102",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5eef1442",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5f148d1e",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4a975841",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c6f942a0",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cbfabe57",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3ba3cdf1",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fa2638e7",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "12f7ff9c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f646ef1c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "21e4a997",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "61233c5c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ac2fa6f2",
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
