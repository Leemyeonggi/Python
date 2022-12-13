{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "ed20e489",
   "metadata": {},
   "source": [
    "### 조건문 if"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "7590dd42",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "실행문장 실행\n"
     ]
    }
   ],
   "source": [
    "if True:\n",
    "    print(\"실행문장 실행\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "208dd757",
   "metadata": {},
   "outputs": [],
   "source": [
    "if False:  # 조건식이 False여서 실행안됌\n",
    "    print(\"실행문장 실행\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "55d7ab42",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "실행문장 실행\n",
      "if문 밖에 있는 실행문장\n"
     ]
    }
   ],
   "source": [
    "if True:\n",
    "    print(\"실행문장 실행\")\n",
    "print(\"if문 밖에 있는 실행문장\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "7ae5833e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "if문 밖에 있는 실행문장\n"
     ]
    }
   ],
   "source": [
    "if False:  # 들여쓰기의 중요성\n",
    "    print(\"실행문장 실행\")\n",
    "print(\"if문 밖에 있는 실행문장\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "63188256",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "택시를 탄다.\n"
     ]
    }
   ],
   "source": [
    "money = 11000\n",
    "if money >= 10000:\n",
    "    print(\"택시를 탄다.\")\n",
    "else:\n",
    "    print('버스를 탄다.')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "8fe8673f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "택시를 탄다.\n"
     ]
    }
   ],
   "source": [
    "money = 11000\n",
    "print(\"택시를 탄다.\") if money >=10000 else print(\"버스를 탄다.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "d5bfa301",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "정수 입력 >> 7\n",
      "3과 5의 배수가 아닙니다.\n"
     ]
    }
   ],
   "source": [
    "num = int(input(\"정수 입력 >> \"))\n",
    "\n",
    "if num % 15 ==0:\n",
    "    print(\"3과 5의 배수입니다.\")\n",
    "else:\n",
    "    print(\"3과 5의 배수가 아닙니다.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "2ba37367",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "주민등록번호 뒷자리 입력 >> 2835602\n",
      "당신은 여자입니다^^*\n"
     ]
    }
   ],
   "source": [
    "num = input(\"주민등록번호 뒷자리 입력 >> \")\n",
    "\n",
    "if num.startswith(\"1\"):\n",
    "    print(\"당신은 남자입니다^^7\")\n",
    "else:\n",
    "    print(\"당신은 여자입니다^^*\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "fb34737f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "주민등록번호 뒷자리 입력 >> 385620\n",
      "당신은 남자입니다^^7\n"
     ]
    }
   ],
   "source": [
    "num = input(\"주민등록번호 뒷자리 입력 >> \")\n",
    "\n",
    "if (int(num[0]))%2 != 0:\n",
    "    print(\"당신은 남자입니다^^7\")\n",
    "else:\n",
    "    print(\"당신은 여자입니다^^*\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "39ad6b31",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "이름 입력 >> 성우\n",
      "나이 입력 >> 18\n",
      "카드 소지 여부(소지, 미소지) >> 소지\n",
      "성우님은 입장료 15750원에 예약되셨습니다.\n"
     ]
    }
   ],
   "source": [
    "name = input(\"이름 입력 >> \")   # 다시풀기 더 간단하게\n",
    "age = int(input(\"나이 입력 >> \"))\n",
    "card = input(\"카드 소지 여부(소지, 미소지) >> \")\n",
    "charge = 35000\n",
    "\n",
    "if age >= 19:\n",
    "    if card == '소지':\n",
    "        print(f\"{name}님은 입장료 {int(charge*0.7)}원에 예약되셨습니다.\")\n",
    "    else:\n",
    "        print(f\"{name}님은 입장료 {charge}원에 예약되셨습니다.\")\n",
    "if age < 19:\n",
    "    charge *= 0.5\n",
    "    if card == '소지':\n",
    "        print(f\"{name}님은 입장료 {int(charge*0.9)}원에 예약되셨습니다.\")\n",
    "    else:\n",
    "        print(f\"{name}님은 입장료 {charge}원에 예약되셨습니다.\")\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "54e7c4a0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "마스크 개수 입력 >> 19\n",
      "8개들이 포장지 개수 : 2\n",
      "5개들이 포장지 개수 : 1\n"
     ]
    }
   ],
   "source": [
    "countOfMask = int(input(\"마스크 개수 입력 >> \")) # 다시 풀기 더 간단하게 줄일수있음\n",
    "pakage1 = 0\n",
    "pakage2 = 0\n",
    "\n",
    "if countOfMask % 8 != 0:\n",
    "    pakage1 = countOfMask // 8\n",
    "    if (countOfMask % 8) % 5 != 0:\n",
    "        pakage2 = (countOfMask % 8) // 5 + 1\n",
    "    else:\n",
    "        pakage2 = (countOfMask % 8) // 5\n",
    "        \n",
    "else:\n",
    "    pakage1 = countOfMask // 8 \n",
    "    \n",
    "print(\"8개들이 포장지 개수 :\",pakage1)\n",
    "print(\"5개들이 포장지 개수 :\",pakage2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3be95b72",
   "metadata": {},
   "outputs": [],
   "source": [
    "countOfMask = int(input(\"마스크 개수 입력 >> \")) # 간소화한 버젼\n",
    "\n",
    "#8개들이 포장지 개수\n",
    "eightBox = countOfMask // 8\n",
    "\n",
    "# 8개들이 포장 후에 5개들이 포장지로 포장한 다음 남은 마스크가 1개라도 있다면\n",
    "if ((counttOfMask % 8) % 5) > 0:\n",
    "    # 5개들이 포장지는 1개가 추가로 더 필요\n",
    "    fiveBox = ((countOfMask % 8)// 5) + 1\n",
    "else:\n",
    "    fiveBox = (countOfMask % 8)// 5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "660419c3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "첫 번째 정수 입력 >> 3\n",
      "두 번째 정수 입력 >> 3\n",
      "두 수가 똑같습니다.\n"
     ]
    }
   ],
   "source": [
    "num1 = int(input(\"첫 번째 정수 입력 >> \"))\n",
    "num2 = int(input(\"두 번째 정수 입력 >> \"))\n",
    "result = 0\n",
    "\n",
    "if num1 > num2:\n",
    "    print(\"첫 번째 수가 더 큽니다.\")\n",
    "elif num2 > num1:\n",
    "    print(\"두 번째 수가 더 큽니다.\")\n",
    "else:\n",
    "    print(\"두 수가 똑같습니다.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "e758b6d4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "점수 입력 >> 36\n",
      "36점은 F학점 입니다.\n"
     ]
    }
   ],
   "source": [
    "score = int(input(\"점수 입력 >> \"))\n",
    "degree = \"\"\n",
    "\n",
    "if score >= 90:\n",
    "    degree = \"A\"\n",
    "elif score >= 80:\n",
    "    degree = \"B\"\n",
    "elif score >= 70:\n",
    "    degree = \"C\"\n",
    "elif score >= 60:\n",
    "    degree = \"D\"\n",
    "else:\n",
    "    degree = \"F\"\n",
    "\n",
    "print(f\"{score}점은 {degree}학점 입니다.\")\n",
    "    \n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "e66c2eaf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "x값을 입력하세요 :12\n",
      "y값을 입력하세요 :-5\n",
      "좌표(12,-5)는 4사분면입니다.\n"
     ]
    }
   ],
   "source": [
    "x = int(input(\"x값을 입력하세요 :\"))\n",
    "y = int(input(\"y값을 입력하세요 :\"))\n",
    "quadrant = \"\"\n",
    "\n",
    "if x>0 and y>0:\n",
    "    quadrant = '1사분면'\n",
    "elif x>0 and y<0:\n",
    "    quadrant = '4사분면'\n",
    "elif x<0 and y>0:\n",
    "    quadrant = '2사분면'\n",
    "else:\n",
    "    quadrant = '3사분면'\n",
    "    \n",
    "print(f\"좌표({x},{y})는 {quadrant}입니다.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "6b646aec",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "나이 입력 >> 67\n",
      "요금은 375원 입니다.\n"
     ]
    }
   ],
   "source": [
    "age = int(input(\"나이 입력 >> \"))\n",
    "bus = 1500\n",
    "\n",
    "if age<5:\n",
    "    bus *= 0.5\n",
    "elif age < 20:\n",
    "    bus *= 0.75\n",
    "elif age >= 65:\n",
    "    bus *= 0.25\n",
    "else:\n",
    "    bus\n",
    "\n",
    "print(f\"요금은 {int(bus)}원 입니다.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "5fc852f9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "==================================================\n",
      "=================---- 자판기 ----=================\n",
      "== 1.콜라 == 2.사이다 == 3.물 ===========insert===\n",
      "==---------==---------==---------========------===\n",
      "==   600   ==   800   ==  1000  ======== 000원 ===\n",
      "=========================================------===\n",
      "==================================================\n",
      "==++++++++++++++++++++++++++++++++++++++++++++++==\n",
      "==++++++++++++++++++++++++++++++++++++++++++++++==\n",
      "==++++++++++++++++++++++++++++++++++++++++++++++==\n",
      "==++++++++++++++                  ++++++++++++++==\n",
      "==++++++++++++++      SMHRO       ++++++++++++++==\n",
      "==++++++++++++++                  ++++++++++++++==\n",
      "==================================================\n",
      "==================================================\n",
      "   ===                                      ===   \n",
      "   ===                                      ===   \n",
      "insert coin >> 3000\n",
      "메뉴 선택 >> 1\n",
      "잔돈 >> 1000원 2 500원 0 100원 4\n"
     ]
    }
   ],
   "source": [
    "insert = \"000원\"\n",
    "\n",
    "print(\"=\"*50)\n",
    "print(\"=\"*17+'-'*4,'자판기','-'*4+'='*17)\n",
    "print('='*2,'1.콜라','='*2, '2.사이다', '='*2, '3.물','='*11+'insert'+'='*3)\n",
    "print('='*2+'-'*9+'='*2+'-'*9+'='*2+'-'*9+'='*8+'-'*6+'='*3)\n",
    "print('='*2,\"  600  \",'='*2,\"  800  \",'='*2,' 1000 ','='*8,f'{insert}','='*3)\n",
    "print('='*41+'-'*6+'='*3)\n",
    "print(\"=\"*50)\n",
    "print(\"=\"*2+'+'*46+\"=\"*2)\n",
    "print(\"=\"*2+'+'*46+\"=\"*2)\n",
    "print(\"=\"*2+'+'*46+\"=\"*2)\n",
    "print(\"=\"*2+'+'*14,\"                \",\"+\"*14+\"=\"*2)\n",
    "print(\"=\"*2+'+'*14,\"     SMHRO      \",\"+\"*14+\"=\"*2)\n",
    "print(\"=\"*2+'+'*14,\"                \",\"+\"*14+\"=\"*2)\n",
    "(\"=\"*2+'+'*46+\"=\"*2)\n",
    "(\"=\"*2+'+'*46+\"=\"*2)\n",
    "print(\"=\"*50)\n",
    "print(\"=\"*50)\n",
    "print(\"  \",\"=\"*3,\"                                    \",\"=\"*3,\"  \")\n",
    "print(\"  \",\"=\"*3,\"                                    \",\"=\"*3,\"  \")\n",
    "\n",
    "coke = '1'\n",
    "cider = '2'\n",
    "water = '3'\n",
    "\n",
    "money = int(input(\"insert coin >> \"))\n",
    "choice = input(\"메뉴 선택 >> \")\n",
    "\n",
    "if choice == '1':\n",
    "    money -= 600 \n",
    "elif choice == '2':\n",
    "    money -= 800\n",
    "elif choice == '3' :\n",
    "    money -= 1000\n",
    "elif choice != '1' and choice != '2' and choice != '3':\n",
    "    print(\"잘못된 메뉴!\")\n",
    "elif money < 600:\n",
    "    print(\"잔액 부족\")\n",
    "\n",
    "change1 = money // 1000\n",
    "if (money%1000)%500 == 0:\n",
    "    change2 = (money%1000)//500\n",
    "else:\n",
    "    change2 = (money%1000)//500\n",
    "if ((money%1000)%500)%100 == 0:\n",
    "    change3 = ((money%1000)%500)//100\n",
    "else:\n",
    "    change3 = ((money%1000)%500)//100\n",
    "    \n",
    "print(f\"잔돈 >> 1000원 {change1} 500원 {change2} 100원 {change3}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "d5a4ea77",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "insert coin >> 4600\n",
      "메뉴 선택 >> 2\n",
      "잔돈 >> 천원 3개, 오백원 1개, 백원 3개\n"
     ]
    }
   ],
   "source": [
    "# 조건문을 활용한 자판기 만들기!!\n",
    "money = int(input(\"insert coin >> \"))\n",
    "num = int(input(\"메뉴 선택 >> \"))\n",
    "# 메뉴 선택하기\n",
    "if money >= 600 :\n",
    "    # 1번 메뉴 선택\n",
    "    if num == 1 :\n",
    "        money -= 600\n",
    "    elif num == 2 :\n",
    "        money -= 800\n",
    "    elif num == 3 :\n",
    "        money -= 1000\n",
    "    else :\n",
    "        print(\"잘못된 메뉴입니다!\")\n",
    "    # 잔돈 계산하기\n",
    "    cash_1000, cash_500, cash_100 = 0,0,0\n",
    "    if money >= 1000 :\n",
    "        # 천원짜리 개수\n",
    "        cash_1000 = money // 1000\n",
    "        # 오백원짜리 개수\n",
    "        cash_500 = money % 1000 // 500\n",
    "        # 백원짜리 개수\n",
    "        cash_100 = money % 1000 % 500 // 100\n",
    "    # 천원 미만 오백원 이상일 경우\n",
    "    elif money >= 500 :\n",
    "        cash_500 = money // 500\n",
    "        cash_100 = money % 500 // 100\n",
    "    # 오백원 미만일 경우\n",
    "    else :\n",
    "        chas_100 = money // 100\n",
    "    print(f\"잔돈 >> 천원 {cash_1000}개, 오백원 {cash_500}개, 백원 {cash_100}개\")\n",
    "else :\n",
    "    print(\"돈을 더 넣어주세요~~!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4eabaf1b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "57e0998f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3168deb0",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e38c9418",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f387cb9f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "df09b00e",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c5ca5f10",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5d3453cb",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "56e85175",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a26af651",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8ae6b346",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "34c66b86",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "18dcba39",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cfa50e00",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d79e04cc",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "916ffbfc",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f152fa26",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "819a3460",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "46b1ed74",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "56ff4748",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "73633aa9",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5dd866e1",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b73e03f2",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8b02d948",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a70e049f",
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
