{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "6529cbfb",
   "metadata": {},
   "outputs": [],
   "source": [
    "from selenium import webdriver as wb\n",
    "from selenium.webdriver.common.keys import Keys\n",
    "from selenium.webdriver.common.by import By\n",
    "import time"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "705c2cee",
   "metadata": {},
   "outputs": [],
   "source": [
    "#1. 브라우저를 실행 > 유튜브채널 사이트로!\n",
    "driver = wb.Chrome()\n",
    "driver.get(\"https://www.youtube.com/watch?v=GEsG_rlYils\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "c58f6e77",
   "metadata": {},
   "outputs": [],
   "source": [
    "#2. 댓글정보를 수집\n",
    "review = driver.find_elements(By.ID,\"content-text\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "7f55fa8a",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "너네 허위 제보 뭐냐~~~~!!!!\n",
      "아니 둘이 케미가 돌았어 ㅋㅋㅋ 풀영상 저 상태로 4시간 넘게 케미 쭉 유지되는데 이걸 어떻게 존버를 안하냐고 ㅋㅋㅋㅋㅋㅋ\n",
      "ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ아니 어떻게 이렇게 엮였는데 어색한 분위기 하나도 없이 티키타카가 잘되냐ㅋㅋㅋㅋㅋㅋ둘이 진짜 잘 맞네\n",
      "조합이 진짜 개 재밌넼ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ 계속 웃으면서 봄\n",
      "결국 이날 공포게임 안하고 미룸ㅋㅋㅋ 한번더 같이 합방해야돼 ㅋㅋㅋㅋㅋㅋ\n",
      "민교등장할때마다 꿀잼이네ㅋㅋㅋㅋ\n",
      "오늘도 또 쉬냐고 드립칠줄알았는데\n",
      "잘참았네ㅋㅋㅋ\n",
      "데이트하는거 다봤지만 조용히해준다ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ\n",
      "편집자님 센스에 감탄이 절로나오네요\n",
      "이건 ㄹㅇ 풀영상 봐야 감정이입 개잘된다\n",
      "꼭 봐라잉 ㅋㅋ\n",
      "임선비 방송 본지 2년이 되어가는데\n",
      "매번 눈팅하면서 와, 임선비 나랑 생각하는게 행동하는게 비슷하다 \n",
      "진지할땐 진지하게 장난일땐 장난스럽게 \n",
      "하는게 비슷하다했는데 MBTI가 나랑 같았네ㅋㅋㅋㅋ 잇프제 소름ㅋㅋㅋㅋ\n",
      "일부러 다음약속 잡을려고 뽀뽀플레이타임 다음으로 미루는거봐라ㅌㅋㅋㅋㅋ\n",
      "싫은 척 하면서 속으론 즐기고있을 선비누나...\n",
      "\n",
      "꾸티뉴도 허락했다 교 선 비 존 버\n",
      "둘이 케미 지리네 진짜 ㅋㅋㅋㅋㅋㅋㅋ\n",
      "케미의 끝판왕..교선비..볼수록 흐뭇해지고 행복해져요ㅎㅎ 교선비존버!!\n",
      "싸우다 정드는데 ㅋㅋ\n",
      "친남매처럼 서로 위해주는 모습 참 보기 좋네요~\n",
      "이 조합이 달달해질 수가 있네 ㅋㅋㅋㅋㅋ\n",
      "처음으로 풀영상 다봤다ㅋㅋㅋㅋㅋ 단 한 순간도 버릴게 없을 정도로 개꿀잼임ㅋㅋㅋㅋ\n",
      "\n",
      "근데.....말입니다\n",
      ".\n",
      "임선비가 심장 뛰는거 우리집에서도 느껴짐\n",
      "선민교 케미가 미쳐서 더 그런것 같네요 ㅋㅋㅋㅋ 오늘도 역시 믿고 보는 티키타카 이에요 !! (최고)\n",
      "\n",
      "p.s. 그 와중에 선비님 MBTI가 ISFJ였군요!! 괜히 같으니까 신기하네요 ㅋㅋㅋ 평소에 고민이나 생각이 많으실수도 있겠네요.\n",
      "썸네일 민교 하트 ㅁㅊㅋㅋㅋㅋㅋㅋㅋ\n",
      "임선비 이번 영상 짱웃기네 둘이 케미 왜케 좋아요??\n"
     ]
    }
   ],
   "source": [
    "for i in review:\n",
    "    print(i.text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "efcf01d4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "20"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(review)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "244fe9b6",
   "metadata": {},
   "source": [
    "### 스크롤 내리는 방법\n",
    "- 키보드의 END키를 활용!\n",
    "- 전체 페이지를 움직이기 때문에 body태그를 접근\n",
    "- body 태그에게 키보드의 END값을 전달 > body.send_keys(Keys.END)\n",
    "- [주의점]\n",
    "    - 반복 작업시 while문은 사용금지 > body는 계속 존재 > 무한루프\n",
    "    - for문을 활용해서 많은 양의 반복을 통해 진행 추천!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "bad9d210",
   "metadata": {},
   "outputs": [],
   "source": [
    "for i in range(100):\n",
    "    body = driver.find_element(By.TAG_NAME,\"body\")\n",
    "    body.send_keys(Keys.END)\n",
    "    time.sleep(0.5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1dcdcc4b",
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
