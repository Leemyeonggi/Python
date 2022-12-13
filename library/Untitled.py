{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "8c3c98dc",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "b1b3dc99",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[        1,      1193,         5, 978300760],\n",
       "       [        1,       661,         3, 978302109],\n",
       "       [        1,       914,         3, 978301968],\n",
       "       ...,\n",
       "       [     6040,       562,         5, 956704746],\n",
       "       [     6040,      1096,         4, 956715648],\n",
       "       [     6040,      1097,         4, 956715569]], dtype=int64)"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data = np.loadtxt('data/ratings.dat',delimiter ='::',dtype = np.int64)\n",
    "data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "6de8435c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "배열 형태 : (1000209, 4)\n",
      "배열 차원수 : 2\n",
      "배열 전체 요소 개수 : 4000836\n"
     ]
    }
   ],
   "source": [
    "print(\"배열 형태 :\",data.shape)\n",
    "print(\"배열 차원수 :\",data.ndim)\n",
    "print(\"배열 전체 요소 개수 :\",data.size)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "f583e737",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[   1    2    3 ... 6038 6039 6040]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "6040"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "user_id = np.unique(data[:,0])\n",
    "print(user_id)\n",
    "len(user_id)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "67af70a8",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 950000000 이하 시간대 사람들 점수 평균과 980000000 이상 시간대 사람들 점수 평균 비교"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "9bcfb802",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3.612939233971303\n"
     ]
    }
   ],
   "source": [
    "user_95_ = data[data[:,3]<=960000000][:,2].mean()\n",
    "print(user_95_)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "9438a20a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3.486754048546382\n"
     ]
    }
   ],
   "source": [
    "user_98_ = data[data[:,3]>=980000000][:,2].mean()\n",
    "print(user_98_)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "6bda3e17",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([        1,         2,         3, ..., 959999923, 959999952,\n",
       "       959999966], dtype=int64)"
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "user_96 = np.unique(data[(data[:,3]<=960000000) &(data[:,3]>=950000000) ])\n",
    "user_96 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "08a686ef",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\AI\\AppData\\Local\\Temp\\ipykernel_22132\\2207748026.py:3: RuntimeWarning: Mean of empty slice.\n",
      "  user_96_ = data[data[:,3]<=i][:,2].mean()\n"
     ]
    },
    {
     "ename": "ValueError",
     "evalue": "cannot convert float NaN to integer",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "Input \u001b[1;32mIn [38]\u001b[0m, in \u001b[0;36m<cell line: 2>\u001b[1;34m()\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[38;5;28;01mfor\u001b[39;00m i \u001b[38;5;129;01min\u001b[39;00m user_96:\n\u001b[0;32m      3\u001b[0m     user_96_ \u001b[38;5;241m=\u001b[39m data[data[:,\u001b[38;5;241m3\u001b[39m]\u001b[38;5;241m<\u001b[39m\u001b[38;5;241m=\u001b[39mi][:,\u001b[38;5;241m2\u001b[39m]\u001b[38;5;241m.\u001b[39mmean()\n\u001b[1;32m----> 4\u001b[0m     user_96_mean\u001b[38;5;241m.\u001b[39mappend(\u001b[38;5;28;43mint\u001b[39;49m\u001b[43m(\u001b[49m\u001b[43muser_96_\u001b[49m\u001b[43m)\u001b[49m)\n\u001b[0;32m      5\u001b[0m user_96_mean\n",
      "\u001b[1;31mValueError\u001b[0m: cannot convert float NaN to integer"
     ]
    }
   ],
   "source": [
    "user_96_mean = []\n",
    "for i in user_96:\n",
    "    user_96_ = data[data[:,3]<=i][:,2].mean()\n",
    "    user_96_mean.append(int(user_96_))\n",
    "user_96_mean"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7298c39b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3ee11c0e",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "19032a1e",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2ed764eb",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1839ad5b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "56bcd6f7",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "617aa21b",
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
