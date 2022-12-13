{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "dc0c132d",
   "metadata": {},
   "source": [
    "# 재귀함수"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "637771ed",
   "metadata": {},
   "outputs": [],
   "source": [
    "def fibo(hang) :\n",
    "    if hang <= 2 :\n",
    "        return 1\n",
    "    else:\n",
    "        return fibo(hang - 2) + fibo(hang - 1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "7a1b5095",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "6765"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fibo(20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "18b90747",
   "metadata": {},
   "outputs": [],
   "source": [
    "상민 수열 정리\n",
    "\n",
    "7 8 56 448 ???\n",
    "앞선 두 항을 곱한 값\n",
    "\n",
    "상민 수열의 10번째 값을 구해주세요"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "43a74c45",
   "metadata": {},
   "outputs": [],
   "source": [
    "def 상민수열(hang):\n",
    "    if hang == 1:\n",
    "        return 7\n",
    "    elif hang == 2:\n",
    "        return 8\n",
    "    else:\n",
    "        return 상민수열(hang-2) * 상민수열(hang-1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "28009dd8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2832163999440680038848564176280658420389828886528"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "상민수열(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7be79313",
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
