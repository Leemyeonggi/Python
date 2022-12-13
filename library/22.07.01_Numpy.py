{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "b402d4b8",
   "metadata": {},
   "source": [
    "### Numpy 라이브러리\n",
    "- 빅데이터의 수학적 ,과학적 계산을 위해 만들어진 라이브러리\n",
    "- 반복문 없이 전체 데이터의 연산이 가능한 표준 수학 함수들을 제공\n",
    "- ※ 배열 : 같은 자료형의 값들이 연속적인 형태로 구성된 자료 구조로 대량의 데이터로 관리하고 계산하기 위해 사용!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "3b1783b9",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Numpy 라이브러리를 불러와서 np로 지칭하겠다!\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "bdcb4112",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 2, 3, 4, 5]"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list1 = [1,2,3,4,5]\n",
    "list1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "01ea1bdf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "list"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(list1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "dc05a1a3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1, 2, 3, 4, 5])"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr = np.array(list1)\n",
    "arr"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "5a6285e2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "numpy.ndarray"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(arr)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "39250934",
   "metadata": {},
   "source": [
    "### 1차원 배열"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "24f7e38b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['1', '2', '야호!'], dtype='<U11')"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr = np.array([1,2,\"야호!\"])\n",
    "arr"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "49b28a08",
   "metadata": {},
   "source": [
    "### 2차원 배열"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "3eaa2f9f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 2, 3],\n",
       "       [4, 5, 6]])"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr2 = np.array([[1,2,3],[4,5,6]])\n",
    "arr2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "4e6ad7cc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(2, 3)"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 배열의 형태 확인(행, 열)\n",
    "arr2.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "10c61c45",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "6"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 배열의 요소 전체 개수\n",
    "arr2.size"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "48e6d860",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dtype('int32')"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 배열의 데이터 타입(자료형 확인)\n",
    "arr2.dtype\n",
    "\n",
    "# 32는 bit를 뜻함(기계가 표현할 수 있는 범위) → 2^32\n",
    "# int8 → 1비트당 2개의 숫자를 표현할 수 있음 2^8 = 256개 표현 가능(-128~127)\n",
    "# int32 → -2,147,486,648 ~ 2,147,483,647"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "7f2e0575",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 배열의 차원 확인\n",
    "arr2.ndim"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "86d13871",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[[1, 2],\n",
       "        [3, 4]],\n",
       "\n",
       "       [[5, 6],\n",
       "        [7, 8]]])"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 예제\n",
    "arr3 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])\n",
    "arr3"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6dd7fa3d",
   "metadata": {},
   "source": [
    "- arr3 배열의 형태, 차원, 전체요소개수를 출력해보세요~!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "09564a19",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "배열의 형태 : (2, 2, 2)\n",
      "배열의 차원 3\n",
      "배열의 전체 요소 개수 : 8\n"
     ]
    }
   ],
   "source": [
    "print(\"배열의 형태 :\",arr3.shape)  # 2행2열의 배열이 2개 (개수,행수,열수)\n",
    "print(\"배열의 차원\",arr3.ndim)\n",
    "print(\"배열의 전체 요소 개수 :\",arr3.size)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "2605b9fe",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[[0., 0., 0., 0.],\n",
       "        [0., 0., 0., 0.],\n",
       "        [0., 0., 0., 0.]],\n",
       "\n",
       "       [[0., 0., 0., 0.],\n",
       "        [0., 0., 0., 0.],\n",
       "        [0., 0., 0., 0.]]])"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 0으로 배열 생성\n",
    "arr_zeros = np.zeros((2,3,4))\n",
    "arr_zeros"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "30a5fa56",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[[1., 1., 1.],\n",
       "        [1., 1., 1.],\n",
       "        [1., 1., 1.],\n",
       "        [1., 1., 1.]],\n",
       "\n",
       "       [[1., 1., 1.],\n",
       "        [1., 1., 1.],\n",
       "        [1., 1., 1.],\n",
       "        [1., 1., 1.]]])"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 1로 배열 생성\n",
    "arr_ones = np.ones((2,4,3))\n",
    "arr_ones"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "fa81e0bd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[[7, 7, 7, 7, 7],\n",
       "        [7, 7, 7, 7, 7],\n",
       "        [7, 7, 7, 7, 7],\n",
       "        [7, 7, 7, 7, 7],\n",
       "        [7, 7, 7, 7, 7]],\n",
       "\n",
       "       [[7, 7, 7, 7, 7],\n",
       "        [7, 7, 7, 7, 7],\n",
       "        [7, 7, 7, 7, 7],\n",
       "        [7, 7, 7, 7, 7],\n",
       "        [7, 7, 7, 7, 7]]])"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 특정값으로 배열 생성하기\n",
    "arr_full = np.full((2,5,5),7)  # 5행 5열의 배열 2개 7로 채워준다\n",
    "arr_full"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c10b91e8",
   "metadata": {},
   "source": [
    "### 다차원배열 생성에 유용한 함수\n",
    "- arange함수로 배열을 생성하고 reshape함수로 배열의 형태를 바꿔보자!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "727db4e8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17,\n",
       "       18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34,\n",
       "       35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 1부터 50까지 1씩 증가하는 값들로 리스트를 만들어주세요~!\n",
    "my_list = []\n",
    "for i in range(1,51):\n",
    "    my_list.append(i)\n",
    "print(my_list)\n",
    "\n",
    "# 만든 리스트로 배열 생성\n",
    "np.array(my_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "76d22f76",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17,\n",
       "       18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34,\n",
       "       35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 반복문을 활용하지 않고 배열 생성\n",
    "arr5 = np.arange(1,51)\n",
    "arr5"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "03559997",
   "metadata": {},
   "source": [
    "- arange 함수를 사용하여 1부터 51까지 중에서 1, 11, 21, 31, 41로 배열을 생성해보세요~!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "8c284064",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 1, 11, 21, 31, 41])"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr6 = np.arange(1,51,10)\n",
    "arr6"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "4bfc598b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17,\n",
       "       18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34,\n",
       "       35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr7 = np.arange(1,51,1)\n",
    "arr7"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "98879111",
   "metadata": {},
   "outputs": [],
   "source": [
    "# reshape : 배열의 행과 열을 변경시켜주는 명령\n",
    "arr7 = arr7.reshape(10,5)  # reshape() 안의 값들을 곱했을때와 개수가 일치해야되는게 포인트"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "0443a56c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 1,  2,  3,  4,  5],\n",
       "       [ 6,  7,  8,  9, 10],\n",
       "       [11, 12, 13, 14, 15],\n",
       "       [16, 17, 18, 19, 20],\n",
       "       [21, 22, 23, 24, 25],\n",
       "       [26, 27, 28, 29, 30],\n",
       "       [31, 32, 33, 34, 35],\n",
       "       [36, 37, 38, 39, 40],\n",
       "       [41, 42, 43, 44, 45],\n",
       "       [46, 47, 48, 49, 50]])"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr7"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "e4236edf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1.2, 2.3, 3.4])"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#실수값을 가지는 배열 생성\n",
    "arr8 = np.array([1.2,2.3,3.4])\n",
    "arr8"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "89e1cedf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1, 2, 3], dtype=int64)"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 배열의 자료형을 정수형으로 변경해서 출력!\n",
    "arr8 = np.array([1.2,2.3,3.4], dtype = np.int64)\n",
    "arr8"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "dd12f3ed",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1, 2, 3], dtype=int64)"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr9 = np.array(['1','2','3'], dtype = np.int64)\n",
    "arr9"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ec37c1da",
   "metadata": {},
   "source": [
    "### 랜덤(난수) 값 생성!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "56c639b1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0.91097015, 0.46511382, 0.98000562],\n",
       "       [0.6677111 , 0.20708609, 0.51054774]])"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 랜덤한 값으로 배열 생성하기!\n",
    "arr10 = np.random.rand(2,3)   # 6개 (2행 X 3열) 값을 랜덤으로 생성 (0 ~ 1) 사이값\n",
    "arr10"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "bc73abd8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "9"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 랜덤 정수 값 출력하기!\n",
    "np.random.randint(10)    # 0~9까지의 10개 숫자 중에서 랜덤으로 정수를 생성!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "040720b4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([2, 2, 1, 3, 3, 0, 1, 3, 1, 3])"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 랜덤값 정수형 배열 생성하기\n",
    "np.random.randint(5, size = 10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "b18ec1ed",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0, 3, 4],\n",
       "       [2, 3, 4]])"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.random.randint(5, size = (2,3))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e3534dac",
   "metadata": {},
   "source": [
    "### array 연산"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "3c1fae14",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 2],\n",
       "       [3, 4]])"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr14 = np.array([[1,2],[3,4]])\n",
    "arr14"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "b919c47c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[2, 4],\n",
       "       [6, 8]])"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr14 + arr14"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "5b019c0d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[[1, 2], [3, 4]]"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list14 = [[1,2],[3,4]]\n",
    "list14"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "6077aeb6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[[1, 2], [3, 4], [1, 2], [3, 4]]"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list14 + list14"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "fd87f83b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 1,  4],\n",
       "       [ 9, 16]])"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr14 * arr14"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "b718f173",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1., 1.],\n",
       "       [1., 1.]])"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr14 / arr14"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "0a2b3551",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0, 0],\n",
       "       [0, 0]], dtype=int32)"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr14 % arr14"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "019fd286",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 3,  6],\n",
       "       [ 9, 12]])"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr14*3"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "22f3dbdb",
   "metadata": {},
   "source": [
    "### numpy 배열의 접근은 어떻게 할까?\n",
    "- 리스트와 마찬가지로 인덱싱, 슬라이싱을 지원함!"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "92aef1ed",
   "metadata": {},
   "source": [
    "#### numpy 배열 인덱싱\n",
    "- 배열 중 하나의 인덱스값에 있는 데이터를 가져오는 것"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "0c388389",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 2, 3],\n",
       "       [4, 5, 6]])"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr16 = np.array([[1,2,3],[4,5,6]])\n",
    "arr16"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "1930737c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1, 2, 3])"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr16[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "f1542082",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr16[0][1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "5d19c2f8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr16[1][1]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8a0c9774",
   "metadata": {},
   "source": [
    "#### numpy 슬라이싱\n",
    "- 배열의 범위를 지정하여 여러개의 데이터를 가져오는 것"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "6b369c7b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr17 = np.arange(10)\n",
    "arr17"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "4dd43b3a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([3, 4, 5, 6, 7])"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr17[3:8]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "97187fe9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9],\n",
       "       [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],\n",
       "       [20, 21, 22, 23, 24, 25, 26, 27, 28, 29],\n",
       "       [30, 31, 32, 33, 34, 35, 36, 37, 38, 39],\n",
       "       [40, 41, 42, 43, 44, 45, 46, 47, 48, 49]])"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr18 = np.arange(50).reshape(5,10)\n",
    "arr18"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "cde58e54",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9],\n",
       "       [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]])"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 0번, 1번 인덱스 행의 모든 열을 출력 (arr18[행의범위,열의범위])\n",
    "arr18[0:2,]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "46349706",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 0, 10, 20, 30, 40])"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 모든 행의 0번 인덱스를 출력\n",
    "arr18[:,0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "3c21da91",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 0,  1],\n",
       "       [10, 11],\n",
       "       [20, 21],\n",
       "       [30, 31],\n",
       "       [40, 41]])"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr18[:,0:2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "d7c2b292",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 0,  1,  2,  3,  4],\n",
       "       [10, 11, 12, 13, 14],\n",
       "       [20, 21, 22, 23, 24],\n",
       "       [30, 31, 32, 33, 34]])"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr18[0:4,0:5]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "82abce43",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 0,  1,  2,  3,  4,  5],\n",
       "       [ 6,  7,  8,  9, 10, 11],\n",
       "       [12, 13, 14, 15, 16, 17]])"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr19 = np.arange(18).reshape(3,6)\n",
    "arr19"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "09b3650d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 7,  9, 11],\n",
       "       [13, 15, 17]])"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 방법 1\n",
    "arr19[1:,[1,3,5]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "d120ded7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 7,  9, 11],\n",
       "       [13, 15, 17]])"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 방법 2\n",
    "arr19[1:,1::2]    # 시작인덱스 : 끝 인덱스 : 증감량"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "7607e991",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 전치(transposition) : 배열의 행과 열을 바꿔주는 것\n",
    "arr19 = arr19.T"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "231269e9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 0,  6, 12],\n",
       "       [ 1,  7, 13],\n",
       "       [ 2,  8, 14],\n",
       "       [ 3,  9, 15],\n",
       "       [ 4, 10, 16],\n",
       "       [ 5, 11, 17]])"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr19"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "00ef4777",
   "metadata": {},
   "source": [
    "### numpy 불리언 인덱싱\n",
    "- 특정 조건에 맞으면 True, 아니면 False 값으로 배열을 만들어 조건에 맞는 값에 접근하는 방법"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "0a4e39b4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([95, 59, 97, 91, 59, 80, 58, 53])"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 50~99까지의 랜덤한 8개 값을 가지는 1차원 배열 생성\n",
    "arr20 = np.array(np.random.randint(50,100, size =8))\n",
    "arr20"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "7ad47d91",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ True, False,  True,  True, False,  True, False, False])"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# boolean(불리언) : True(참) 또는 False(거짓)으로 출력되는 자료형태\n",
    "arr20 > 60"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "17068155",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([False, False, False, False, False,  True,  True, False])"
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 짝수인 값들을 True로 출력시켜보세요~!\n",
    "arr20 % 2 == 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "f0a8dc6d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([80, 58])"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# True, False 값이 아닌 실제값을 보고 싶을 경우\n",
    "# 배열명[배열 내에서 찾고자 하는 조건]\n",
    "arr20[arr20 % 2 == 0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "id": "106039c2",
   "metadata": {},
   "outputs": [],
   "source": [
    "arr = np.array([[6,9,6,8,7],\n",
    "                  [2,3,5,4,1]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "id": "9e122b13",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[6, 0, 6, 8, 0],\n",
       "       [2, 0, 0, 4, 0]])"
      ]
     },
     "execution_count": 98,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# arr21 에서 값이 홀수면 0으로 변경하는 코드를 작성해보세요~!\n",
    "arr[arr%2==1] = 0\n",
    "arr"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "19191d75",
   "metadata": {},
   "source": [
    "### 예제) BMI지수 및 과체중 BMI값 확인"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9c843929",
   "metadata": {},
   "source": [
    "#### 1. 데이터 로드"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "d0176545",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[175.2, 180.3, 175. , 169.2, 185.2, 188. , 177.6, 178.2, 177. ,\n",
       "        179. ],\n",
       "       [ 65.6,  88. ,  79.2,  69.3,  55. ,  71.2,  73. ,  68.9,  74. ,\n",
       "         82. ]])"
      ]
     },
     "execution_count": 69,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# delimiter(구분자) : 파일에서 데이터를 구분해주는 문자 지정\n",
    "data = np.loadtxt('data/height_weight.txt', delimiter=',')\n",
    "data\n",
    "\n",
    "# 키는 cm, 몸무게는 kg"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c27acc9e",
   "metadata": {},
   "source": [
    "#### 2. 데이터의 속성 확인\n",
    "- 배열 형태\n",
    "- 배열 차원수\n",
    "- 배열 전체요소 개수"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "5df9330a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "배열 형태 : (2, 10)\n",
      "배열 차원 수 : 2\n",
      "배열 전체요소 개수 : 20\n"
     ]
    }
   ],
   "source": [
    "print('배열 형태 :',data.shape)\n",
    "print('배열 차원 수 :',data.ndim)\n",
    "print('배열 전체요소 개수 :',data.size)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ad074af5",
   "metadata": {},
   "source": [
    "#### 3. 데이터에서 키와 몸무게 데이터들을 각각 변수에 담기"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "acb1695c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "키 : [175.2 180.3 175.  169.2 185.2 188.  177.6 178.2 177.  179. ]\n",
      "몸무게 : [65.6 88.  79.2 69.3 55.  71.2 73.  68.9 74.  82. ]\n"
     ]
    }
   ],
   "source": [
    "# 키\n",
    "height = data[0]\n",
    "# 몸무게\n",
    "weight = data[1]\n",
    "print('키 :',height)\n",
    "print('몸무게 :',weight)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "41d4c176",
   "metadata": {},
   "source": [
    "https://files.slack.com/files-pri/T03M0VBV664-F03MRU7ETTR/image.png"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "id": "b7791e33",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([21.37153104, 27.07018468, 25.86122449, 24.20652885, 16.03543423,\n",
       "       20.14486193, 23.14392095, 21.69720651, 23.62028791, 25.59220998])"
      ]
     },
     "execution_count": 84,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bmi = weight*10000/(height*height)\n",
    "bmi"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f5842300",
   "metadata": {},
   "source": [
    "#### 4. BMI지수가 23이상 25이하인 사람은 몇 명일까요?\n",
    "- 불리언 인덱싱에서는 and -> &, or -> |, not -> ~를 쓴다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "id": "05415888",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([24.20652885, 23.14392095, 23.62028791])"
      ]
     },
     "execution_count": 95,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# TypeError: ufunc 'bitwise_and' not supported for the input types, and the inputs could not be safely coerced to any supported types according to the casting rule ''safe''\n",
    "# 괄호가 없기 때문에 비교할 수 없다는 에러가 뜨는 것입니당\n",
    "bmi[(bmi>=23) & (bmi<=25)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "id": "cea9bf23",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 96,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(bmi[(bmi>=23) & (bmi<=25)])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "84603059",
   "metadata": {},
   "source": [
    "#### numpy 배열 관련 유용한 함수들"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "id": "1468f43c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[4, 8, 2, 6, 9, 4, 6],\n",
       "       [4, 2, 2, 8, 2, 2, 3],\n",
       "       [9, 7, 2, 1, 3, 3, 6],\n",
       "       [6, 5, 7, 2, 6, 3, 1]])"
      ]
     },
     "execution_count": 99,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr21 = np.random.randint(1,10, size=(4,7))\n",
    "arr21"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "id": "ed6ff90e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "123\n",
      "123\n"
     ]
    }
   ],
   "source": [
    "# sum함수\n",
    "print(np.sum(arr21)) # numpy 지원 함수\n",
    "print(arr21.sum())   # python 기본 지원 함수"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "id": "827eda74",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4.392857142857143\n",
      "4.392857142857143\n"
     ]
    }
   ],
   "source": [
    "# mean함수\n",
    "print(np.mean(arr21))  # numpy 지원 함수\n",
    "print(arr21.mean())    # python 기본 지원 함수"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "id": "d4acbc0e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10])"
      ]
     },
     "execution_count": 106,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr22 = np.arange(1,11)\n",
    "arr22"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "id": "bd649fd6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5.5"
      ]
     },
     "execution_count": 107,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# median함수 (중앙값)\n",
    "np.median(arr22)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "id": "03eafe46",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1.        , 1.41421356, 1.73205081, 2.        , 2.23606798,\n",
       "       2.44948974, 2.64575131, 2.82842712, 3.        , 3.16227766])"
      ]
     },
     "execution_count": 108,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# sqrt함수 (제곱근)\n",
    "np.sqrt(arr22)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "id": "eb56e6cd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([-1,  2, -3,  4, -5])"
      ]
     },
     "execution_count": 109,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr23 = np.array([-1,2,-3,4,-5])\n",
    "arr23"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "id": "106b7ea9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1, 2, 3, 4, 5])"
      ]
     },
     "execution_count": 110,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# abs함수 (모두 양수로 변경, 절대값 출력)\n",
    "np.abs(arr23)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bd3fe9c1",
   "metadata": {},
   "source": [
    "### 예제) 영화 리뷰 평점 분석하기!"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e2f90b3a",
   "metadata": {},
   "source": [
    "#### 1. 데이터 로드"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 206,
   "id": "cb890b9c",
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
     "execution_count": 206,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "movie = np.loadtxt('data/ratings.dat',delimiter ='::',dtype=np.int64)\n",
    "movie\n",
    "# 사용자번호(user_id), 영화번호(item_id), 평점(ratings), 입력시간(time)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e515b5b4",
   "metadata": {},
   "source": [
    "#### 2. 데이터 속성 확인\n",
    "- 배열 형태\n",
    "- 배열 차원수\n",
    "- 배열 전체 요소 개수"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 113,
   "id": "3229d1d0",
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
    "print('배열 형태 :',movie.shape)\n",
    "print('배열 차원수 :',movie.ndim)\n",
    "print('배열 전체 요소 개수 :',movie.size)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b7c20be7",
   "metadata": {},
   "source": [
    "#### 3. 전체 영화의 평점 평균 구하기"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 127,
   "id": "0c0d82e9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([5, 3, 3, ..., 5, 4, 4], dtype=int64)"
      ]
     },
     "execution_count": 127,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 3번째 열에 접근하기\n",
    "ratings = movie[0:,2]   # 전체 행의 2번째 열 가져오기\n",
    "ratings"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 128,
   "id": "ea59eca7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3.581564453029317"
      ]
     },
     "execution_count": 128,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# mean함수 사용하기\n",
    "np.mean(ratings)\n",
    "\n",
    "# 전체 영화의 평점 평균"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "324e64c8",
   "metadata": {},
   "source": [
    "#### 4. 1번 사용자가 매긴 평점의 평균 구하기\n",
    "- 사용자 번호의 유일한 값(유니크 값) 확인\n",
    "- 사용자 번호의 유니크 값 개수 확인\n",
    "- 1번 사용자의 데이터에 접근(불리언 인덱싱)\n",
    "- 1번 사용자가 매긴 평점들의 평균 구하기"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 133,
   "id": "cda992e2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([   1,    2,    3, ..., 6038, 6039, 6040], dtype=int64)"
      ]
     },
     "execution_count": 133,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 평점을 매긴 사용자가 몇 명인지 알아보자!\n",
    "# unique : 유일한 값을 구해주는 명령\n",
    "user_id = np.unique(movie[:,0])\n",
    "user_id"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 134,
   "id": "eccb759c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "6040"
      ]
     },
     "execution_count": 134,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 사용자는 총 6040명\n",
    "user_id.size"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 137,
   "id": "f4abceb6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[        1,      1193,         5, 978300760],\n",
       "       [        1,       661,         3, 978302109],\n",
       "       [        1,       914,         3, 978301968],\n",
       "       [        1,      3408,         4, 978300275],\n",
       "       [        1,      2355,         5, 978824291],\n",
       "       [        1,      1197,         3, 978302268],\n",
       "       [        1,      1287,         5, 978302039],\n",
       "       [        1,      2804,         5, 978300719],\n",
       "       [        1,       594,         4, 978302268],\n",
       "       [        1,       919,         4, 978301368],\n",
       "       [        1,       595,         5, 978824268],\n",
       "       [        1,       938,         4, 978301752],\n",
       "       [        1,      2398,         4, 978302281],\n",
       "       [        1,      2918,         4, 978302124],\n",
       "       [        1,      1035,         5, 978301753],\n",
       "       [        1,      2791,         4, 978302188],\n",
       "       [        1,      2687,         3, 978824268],\n",
       "       [        1,      2018,         4, 978301777],\n",
       "       [        1,      3105,         5, 978301713],\n",
       "       [        1,      2797,         4, 978302039],\n",
       "       [        1,      2321,         3, 978302205],\n",
       "       [        1,       720,         3, 978300760],\n",
       "       [        1,      1270,         5, 978300055],\n",
       "       [        1,       527,         5, 978824195],\n",
       "       [        1,      2340,         3, 978300103],\n",
       "       [        1,        48,         5, 978824351],\n",
       "       [        1,      1097,         4, 978301953],\n",
       "       [        1,      1721,         4, 978300055],\n",
       "       [        1,      1545,         4, 978824139],\n",
       "       [        1,       745,         3, 978824268],\n",
       "       [        1,      2294,         4, 978824291],\n",
       "       [        1,      3186,         4, 978300019],\n",
       "       [        1,      1566,         4, 978824330],\n",
       "       [        1,       588,         4, 978824268],\n",
       "       [        1,      1907,         4, 978824330],\n",
       "       [        1,       783,         4, 978824291],\n",
       "       [        1,      1836,         5, 978300172],\n",
       "       [        1,      1022,         5, 978300055],\n",
       "       [        1,      2762,         4, 978302091],\n",
       "       [        1,       150,         5, 978301777],\n",
       "       [        1,         1,         5, 978824268],\n",
       "       [        1,      1961,         5, 978301590],\n",
       "       [        1,      1962,         4, 978301753],\n",
       "       [        1,      2692,         4, 978301570],\n",
       "       [        1,       260,         4, 978300760],\n",
       "       [        1,      1028,         5, 978301777],\n",
       "       [        1,      1029,         5, 978302205],\n",
       "       [        1,      1207,         4, 978300719],\n",
       "       [        1,      2028,         5, 978301619],\n",
       "       [        1,       531,         4, 978302149],\n",
       "       [        1,      3114,         4, 978302174],\n",
       "       [        1,       608,         4, 978301398],\n",
       "       [        1,      1246,         4, 978302091]], dtype=int64)"
      ]
     },
     "execution_count": 137,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 사용자의 번호가 1번인 데이터만 출력\n",
    "a = movie[ movie[:, 0]==1]\n",
    "a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 140,
   "id": "742c17d9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([5, 3, 3, 4, 5, 3, 5, 5, 4, 4, 5, 4, 4, 4, 5, 4, 3, 4, 5, 4, 3, 3,\n",
       "       5, 5, 3, 5, 4, 4, 4, 3, 4, 4, 4, 4, 4, 4, 5, 5, 4, 5, 5, 5, 4, 4,\n",
       "       4, 5, 5, 4, 5, 4, 4, 4, 4], dtype=int64)"
      ]
     },
     "execution_count": 140,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 1번 사용자가 매긴 평점들\n",
    "array = a[:,2]\n",
    "array"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 141,
   "id": "97834a68",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4.188679245283019"
      ]
     },
     "execution_count": 141,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.mean(array)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "96a1d3dc",
   "metadata": {},
   "source": [
    "- 1번 사용자는 전체 영화의 평점 평균보다 후하게 평점을 줬구나~!"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9ecffb50",
   "metadata": {},
   "source": [
    "#### 5. 각 사용자가 매긴 평점들의 평균 구하기!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 142,
   "id": "b3d2418c",
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
     "execution_count": 142,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "movie"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 143,
   "id": "1c0c3ef5",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[        1,      1193,         5, 978300760],\n",
       "       [        1,       661,         3, 978302109],\n",
       "       [        1,       914,         3, 978301968],\n",
       "       [        1,      3408,         4, 978300275],\n",
       "       [        1,      2355,         5, 978824291],\n",
       "       [        1,      1197,         3, 978302268],\n",
       "       [        1,      1287,         5, 978302039],\n",
       "       [        1,      2804,         5, 978300719],\n",
       "       [        1,       594,         4, 978302268],\n",
       "       [        1,       919,         4, 978301368],\n",
       "       [        1,       595,         5, 978824268],\n",
       "       [        1,       938,         4, 978301752],\n",
       "       [        1,      2398,         4, 978302281],\n",
       "       [        1,      2918,         4, 978302124],\n",
       "       [        1,      1035,         5, 978301753],\n",
       "       [        1,      2791,         4, 978302188],\n",
       "       [        1,      2687,         3, 978824268],\n",
       "       [        1,      2018,         4, 978301777],\n",
       "       [        1,      3105,         5, 978301713],\n",
       "       [        1,      2797,         4, 978302039],\n",
       "       [        1,      2321,         3, 978302205],\n",
       "       [        1,       720,         3, 978300760],\n",
       "       [        1,      1270,         5, 978300055],\n",
       "       [        1,       527,         5, 978824195],\n",
       "       [        1,      2340,         3, 978300103],\n",
       "       [        1,        48,         5, 978824351],\n",
       "       [        1,      1097,         4, 978301953],\n",
       "       [        1,      1721,         4, 978300055],\n",
       "       [        1,      1545,         4, 978824139],\n",
       "       [        1,       745,         3, 978824268],\n",
       "       [        1,      2294,         4, 978824291],\n",
       "       [        1,      3186,         4, 978300019],\n",
       "       [        1,      1566,         4, 978824330],\n",
       "       [        1,       588,         4, 978824268],\n",
       "       [        1,      1907,         4, 978824330],\n",
       "       [        1,       783,         4, 978824291],\n",
       "       [        1,      1836,         5, 978300172],\n",
       "       [        1,      1022,         5, 978300055],\n",
       "       [        1,      2762,         4, 978302091],\n",
       "       [        1,       150,         5, 978301777],\n",
       "       [        1,         1,         5, 978824268],\n",
       "       [        1,      1961,         5, 978301590],\n",
       "       [        1,      1962,         4, 978301753],\n",
       "       [        1,      2692,         4, 978301570],\n",
       "       [        1,       260,         4, 978300760],\n",
       "       [        1,      1028,         5, 978301777],\n",
       "       [        1,      1029,         5, 978302205],\n",
       "       [        1,      1207,         4, 978300719],\n",
       "       [        1,      2028,         5, 978301619],\n",
       "       [        1,       531,         4, 978302149],\n",
       "       [        1,      3114,         4, 978302174],\n",
       "       [        1,       608,         4, 978301398],\n",
       "       [        1,      1246,         4, 978302091]], dtype=int64)"
      ]
     },
     "execution_count": 143,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "movie[movie[:,0]==1]    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 144,
   "id": "43b6e251",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4.188679245283019"
      ]
     },
     "execution_count": 144,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "movie[movie[:,0]==1][:,2].mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 154,
   "id": "6a2f52d1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[[1, 4.188679245283019],\n",
       " [2, 3.7131782945736433],\n",
       " [3, 3.9019607843137254],\n",
       " [4, 4.190476190476191],\n",
       " [5, 3.1464646464646466],\n",
       " [6, 3.9014084507042255],\n",
       " [7, 4.32258064516129],\n",
       " [8, 3.884892086330935],\n",
       " [9, 3.7358490566037736],\n",
       " [10, 4.114713216957606],\n",
       " [11, 3.2773722627737225],\n",
       " [12, 3.8260869565217392],\n",
       " [13, 3.388888888888889],\n",
       " [14, 3.32],\n",
       " [15, 3.3233830845771144],\n",
       " [16, 3.0285714285714285],\n",
       " [17, 4.075829383886256],\n",
       " [18, 3.6491803278688524],\n",
       " [19, 3.5725490196078433],\n",
       " [20, 4.083333333333333],\n",
       " [21, 2.909090909090909],\n",
       " [22, 3.0673400673400675],\n",
       " [23, 3.3157894736842106],\n",
       " [24, 3.948529411764706],\n",
       " [25, 3.7411764705882353],\n",
       " [26, 2.96],\n",
       " [27, 4.171428571428572],\n",
       " [28, 3.7570093457943927],\n",
       " [29, 3.5833333333333335],\n",
       " [30, 3.488372093023256],\n",
       " [31, 3.73109243697479],\n",
       " [32, 3.625],\n",
       " [33, 3.498721227621483],\n",
       " [34, 3.8658536585365852],\n",
       " [35, 3.54040404040404],\n",
       " [36, 4.199430199430199],\n",
       " [37, 3.69811320754717],\n",
       " [38, 3.58],\n",
       " [39, 3.564516129032258],\n",
       " [40, 3.4479166666666665],\n",
       " [41, 3.48],\n",
       " [42, 3.74025974025974],\n",
       " [43, 4.125],\n",
       " [44, 3.6321243523316062],\n",
       " [45, 2.946127946127946],\n",
       " [46, 4.219512195121951],\n",
       " [47, 3.909090909090909],\n",
       " [48, 3.068561872909699],\n",
       " [49, 3.712962962962963],\n",
       " [50, 3.0697674418604652],\n",
       " [51, 3.825],\n",
       " [52, 3.5569620253164556],\n",
       " [53, 4.2368421052631575],\n",
       " [54, 4.025],\n",
       " [55, 4.12],\n",
       " [56, 3.970149253731343],\n",
       " [57, 2.90625],\n",
       " [58, 3.9725400457665905],\n",
       " [59, 3.4741784037558685],\n",
       " [60, 3.414285714285714],\n",
       " [61, 2.7777777777777777],\n",
       " [62, 3.566265060240964],\n",
       " [63, 3.4285714285714284],\n",
       " [64, 4.148148148148148],\n",
       " [65, 4.347107438016529],\n",
       " [66, 3.8461538461538463],\n",
       " [67, 4.296875],\n",
       " [68, 3.75],\n",
       " [69, 4.153846153846154],\n",
       " [70, 3.7037037037037037],\n",
       " [71, 3.7586206896551726],\n",
       " [72, 3.697674418604651],\n",
       " [73, 3.364705882352941],\n",
       " [74, 4.046511627906977],\n",
       " [75, 4.005714285714285],\n",
       " [76, 4.172413793103448],\n",
       " [77, 2.948717948717949],\n",
       " [78, 3.657142857142857],\n",
       " [79, 3.6451612903225805],\n",
       " [80, 3.8958333333333335],\n",
       " [81, 4.4186046511627906],\n",
       " [82, 4.016949152542373],\n",
       " [83, 3.5757575757575757],\n",
       " [84, 3.838709677419355],\n",
       " [85, 3.1025641025641026],\n",
       " [86, 4.3125],\n",
       " [87, 2.8135593220338984],\n",
       " [88, 4.147058823529412],\n",
       " [89, 3.238095238095238],\n",
       " [90, 3.511111111111111],\n",
       " [91, 4.704545454545454],\n",
       " [92, 2.7581395348837208],\n",
       " [93, 2.9727272727272727],\n",
       " [94, 3.857142857142857],\n",
       " [95, 3.595959595959596],\n",
       " [96, 3.6049382716049383],\n",
       " [97, 4.474025974025974],\n",
       " [98, 3.8],\n",
       " [99, 3.2149532710280373],\n",
       " [100, 3.026315789473684],\n",
       " [101, 4.679245283018868],\n",
       " [102, 3.128787878787879],\n",
       " [103, 4.052173913043478],\n",
       " [104, 3.347826086956522],\n",
       " [105, 4.295081967213115],\n",
       " [106, 4.0212765957446805],\n",
       " [107, 3.743801652892562],\n",
       " [108, 3.135135135135135],\n",
       " [109, 4.0],\n",
       " [110, 3.25],\n",
       " [111, 3.7282608695652173],\n",
       " [112, 4.183333333333334],\n",
       " [113, 3.5],\n",
       " [114, 3.693877551020408],\n",
       " [115, 3.8421052631578947],\n",
       " [116, 3.802325581395349],\n",
       " [117, 3.299009900990099],\n",
       " [118, 3.767857142857143],\n",
       " [119, 3.5428571428571427],\n",
       " [120, 3.619047619047619],\n",
       " [121, 4.416666666666667],\n",
       " [122, 2.9649122807017543],\n",
       " [123, 3.401315789473684],\n",
       " [124, 4.173913043478261],\n",
       " [125, 4.098591549295775],\n",
       " [126, 4.0],\n",
       " [127, 3.8448275862068964],\n",
       " [128, 4.363636363636363],\n",
       " [129, 4.025316455696203],\n",
       " [130, 4.311111111111111],\n",
       " [131, 3.3966101694915256],\n",
       " [132, 3.966292134831461],\n",
       " [133, 3.7705882352941176],\n",
       " [134, 2.7158469945355193],\n",
       " [135, 3.657142857142857],\n",
       " [136, 3.074074074074074],\n",
       " [137, 3.611940298507463],\n",
       " [138, 4.492307692307692],\n",
       " [139, 3.8816326530612244],\n",
       " [140, 3.8181818181818183],\n",
       " [141, 3.6956521739130435],\n",
       " [142, 3.3404255319148937],\n",
       " [143, 3.5441176470588234],\n",
       " [144, 3.46875],\n",
       " [145, 3.0],\n",
       " [146, 3.7699530516431925],\n",
       " [147, 3.5026737967914436],\n",
       " [148, 3.733974358974359],\n",
       " [149, 3.9408783783783785],\n",
       " [150, 4.021551724137931],\n",
       " [151, 3.653927813163482],\n",
       " [152, 4.125],\n",
       " [153, 4.076923076923077],\n",
       " [154, 3.090909090909091],\n",
       " [155, 2.96875],\n",
       " [156, 4.236486486486487],\n",
       " [157, 3.718969555035129],\n",
       " [158, 4.0],\n",
       " [159, 3.7777777777777777],\n",
       " [160, 3.5],\n",
       " [161, 4.4713804713804715],\n",
       " [162, 4.121495327102804],\n",
       " [163, 2.1828793774319064],\n",
       " [164, 4.384615384615385],\n",
       " [165, 3.981818181818182],\n",
       " [166, 3.6878048780487807],\n",
       " [167, 2.9310344827586206],\n",
       " [168, 3.8461538461538463],\n",
       " [169, 3.5670289855072466],\n",
       " [170, 3.9885057471264367],\n",
       " [171, 4.0],\n",
       " [172, 3.608695652173913],\n",
       " [173, 3.9679144385026737],\n",
       " [174, 3.649484536082474],\n",
       " [175, 3.9810725552050474],\n",
       " [176, 3.6153846153846154],\n",
       " [177, 4.113636363636363],\n",
       " [178, 3.8434782608695652],\n",
       " [179, 2.6545454545454548],\n",
       " [180, 3.694915254237288],\n",
       " [181, 3.604651162790698],\n",
       " [182, 3.8313253012048194],\n",
       " [183, 4.099009900990099],\n",
       " [184, 4.083333333333333],\n",
       " [185, 3.588235294117647],\n",
       " [186, 4.254098360655738],\n",
       " [187, 4.083932853717027],\n",
       " [188, 3.1690140845070425],\n",
       " [189, 4.0],\n",
       " [190, 3.6993464052287583],\n",
       " [191, 3.3333333333333335],\n",
       " [192, 3.0914285714285716],\n",
       " [193, 3.677685950413223],\n",
       " [194, 3.983050847457627],\n",
       " [195, 3.889294403892944],\n",
       " [196, 4.0625],\n",
       " [197, 3.909090909090909],\n",
       " [198, 3.7493403693931397],\n",
       " [199, 3.2761194029850746],\n",
       " [200, 3.423076923076923],\n",
       " [201, 3.954022988505747],\n",
       " [202, 3.2492537313432837],\n",
       " [203, 2.2913385826771653],\n",
       " [204, 3.5560538116591927],\n",
       " [205, 4.0588235294117645],\n",
       " [206, 3.066666666666667],\n",
       " [207, 3.5217391304347827],\n",
       " [208, 3.652173913043478],\n",
       " [209, 3.16],\n",
       " [210, 4.027272727272727],\n",
       " [211, 3.857142857142857],\n",
       " [212, 3.8545454545454545],\n",
       " [213, 4.2272727272727275],\n",
       " [214, 3.1626506024096384],\n",
       " [215, 4.5588235294117645],\n",
       " [216, 3.2317380352644838],\n",
       " [217, 3.7],\n",
       " [218, 3.0930232558139537],\n",
       " [219, 3.3333333333333335],\n",
       " [220, 4.215686274509804],\n",
       " [221, 3.2413793103448274],\n",
       " [222, 4.0875],\n",
       " [223, 3.44140625],\n",
       " [224, 3.4019607843137254],\n",
       " [225, 3.4330708661417324],\n",
       " [226, 3.5714285714285716],\n",
       " [227, 3.2857142857142856],\n",
       " [228, 4.0],\n",
       " [229, 3.4292452830188678],\n",
       " [230, 4.094972067039106],\n",
       " [231, 4.22680412371134],\n",
       " [232, 3.566666666666667],\n",
       " [233, 4.584905660377358],\n",
       " [234, 4.310344827586207],\n",
       " [235, 4.086363636363636],\n",
       " [236, 3.693548387096774],\n",
       " [237, 3.4036144578313254],\n",
       " [238, 3.7868217054263567],\n",
       " [239, 4.140845070422535],\n",
       " [240, 3.300699300699301],\n",
       " [241, 3.9649122807017543],\n",
       " [242, 3.2051282051282053],\n",
       " [243, 3.606060606060606],\n",
       " [244, 4.105882352941176],\n",
       " [245, 2.6714659685863875],\n",
       " [246, 4.0],\n",
       " [247, 3.935483870967742],\n",
       " [248, 4.205882352941177],\n",
       " [249, 3.9454545454545453],\n",
       " [250, 3.75],\n",
       " [251, 3.5753424657534247],\n",
       " [252, 4.016666666666667],\n",
       " [253, 3.9245283018867925],\n",
       " [254, 3.782608695652174],\n",
       " [255, 4.016393442622951],\n",
       " [256, 3.8526315789473684],\n",
       " [257, 4.452830188679245],\n",
       " [258, 3.717241379310345],\n",
       " [259, 4.0359712230215825],\n",
       " [260, 3.311688311688312],\n",
       " [261, 3.5762711864406778],\n",
       " [262, 3.330188679245283],\n",
       " [263, 3.6630434782608696],\n",
       " [264, 2.785416666666667],\n",
       " [265, 4.1938775510204085],\n",
       " [266, 4.52],\n",
       " [267, 3.3893129770992365],\n",
       " [268, 3.3946360153256707],\n",
       " [269, 3.8],\n",
       " [270, 4.198412698412699],\n",
       " [271, 3.9583333333333335],\n",
       " [272, 3.6535269709543567],\n",
       " [273, 3.727272727272727],\n",
       " [274, 4.243243243243243],\n",
       " [275, 4.247191011235955],\n",
       " [276, 3.5217391304347827],\n",
       " [277, 3.727272727272727],\n",
       " [278, 3.9646464646464645],\n",
       " [279, 2.872340425531915],\n",
       " [280, 3.94],\n",
       " [281, 3.891891891891892],\n",
       " [282, 3.5172413793103448],\n",
       " [283, 4.962962962962963],\n",
       " [284, 3.021231422505308],\n",
       " [285, 4.16546762589928],\n",
       " [286, 3.883720930232558],\n",
       " [287, 3.70873786407767],\n",
       " [288, 4.589285714285714],\n",
       " [289, 3.9054054054054053],\n",
       " [290, 3.303030303030303],\n",
       " [291, 4.137254901960785],\n",
       " [292, 3.7560975609756095],\n",
       " [293, 3.2460567823343847],\n",
       " [294, 3.489795918367347],\n",
       " [295, 3.764397905759162],\n",
       " [296, 3.597938144329897],\n",
       " [297, 4.0],\n",
       " [298, 3.925925925925926],\n",
       " [299, 4.163461538461538],\n",
       " [300, 4.180722891566265],\n",
       " [301, 3.8011204481792715],\n",
       " [302, 2.8692893401015227],\n",
       " [303, 3.861244019138756],\n",
       " [304, 3.5555555555555554],\n",
       " [305, 2.5605095541401273],\n",
       " [306, 3.937823834196891],\n",
       " [307, 4.593406593406593],\n",
       " [308, 3.385996409335727],\n",
       " [309, 4.040650406504065],\n",
       " [310, 3.4260089686098656],\n",
       " [311, 4.15],\n",
       " [312, 3.736842105263158],\n",
       " [313, 4.038461538461538],\n",
       " [314, 3.696245733788396],\n",
       " [315, 3.8636363636363638],\n",
       " [316, 4.116883116883117],\n",
       " [317, 3.8095238095238093],\n",
       " [318, 3.9523809523809526],\n",
       " [319, 3.263522884882108],\n",
       " [320, 4.238095238095238],\n",
       " [321, 3.2612612612612613],\n",
       " [322, 4.45],\n",
       " [323, 3.788135593220339],\n",
       " [324, 3.3289473684210527],\n",
       " [325, 4.046511627906977],\n",
       " [326, 3.3350923482849604],\n",
       " [327, 3.669491525423729],\n",
       " [328, 3.032258064516129],\n",
       " [329, 2.7264397905759163],\n",
       " [330, 4.0131578947368425],\n",
       " [331, 3.7654109589041096],\n",
       " [332, 4.2835820895522385],\n",
       " [333, 3.352422907488987],\n",
       " [334, 3.9508196721311477],\n",
       " [335, 2.5],\n",
       " [336, 4.308411214953271],\n",
       " [337, 3.525252525252525],\n",
       " [338, 3.665745856353591],\n",
       " [339, 4.024193548387097],\n",
       " [340, 3.5277777777777777],\n",
       " [341, 4.2],\n",
       " [342, 3.6910569105691056],\n",
       " [343, 4.047138047138047],\n",
       " [344, 2.9555555555555557],\n",
       " [345, 4.4],\n",
       " [346, 4.307420494699647],\n",
       " [347, 3.878787878787879],\n",
       " [348, 3.78],\n",
       " [349, 3.25],\n",
       " [350, 3.9375],\n",
       " [351, 3.7572815533980584],\n",
       " [352, 3.4793103448275864],\n",
       " [353, 3.9166666666666665],\n",
       " [354, 3.586206896551724],\n",
       " [355, 3.4463007159904535],\n",
       " [356, 4.380952380952381],\n",
       " [357, 3.293103448275862],\n",
       " [358, 3.8472222222222223],\n",
       " [359, 3.857142857142857],\n",
       " [360, 3.6417910447761193],\n",
       " [361, 3.5384615384615383],\n",
       " [362, 3.290909090909091],\n",
       " [363, 3.744186046511628],\n",
       " [364, 3.142857142857143],\n",
       " [365, 3.3404255319148937],\n",
       " [366, 4.06949806949807],\n",
       " [367, 4.25],\n",
       " [368, 3.78125],\n",
       " [369, 3.1954022988505746],\n",
       " [370, 3.75],\n",
       " [371, 3.5],\n",
       " [372, 4.553571428571429],\n",
       " [373, 3.5555555555555554],\n",
       " [374, 4.403846153846154],\n",
       " [375, 4.078431372549019],\n",
       " [376, 4.111111111111111],\n",
       " [377, 3.9044117647058822],\n",
       " [378, 3.5128205128205128],\n",
       " [379, 4.234375],\n",
       " [380, 3.7246376811594204],\n",
       " [381, 4.114285714285714],\n",
       " [382, 4.017857142857143],\n",
       " [383, 3.5714285714285716],\n",
       " [384, 3.590909090909091],\n",
       " [385, 3.9562043795620436],\n",
       " [386, 3.3230769230769233],\n",
       " [387, 3.676470588235294],\n",
       " [388, 3.8813559322033897],\n",
       " [389, 3.5616438356164384],\n",
       " [390, 3.6728971962616823],\n",
       " [391, 3.728395061728395],\n",
       " [392, 3.4743326488706368],\n",
       " [393, 3.581081081081081],\n",
       " [394, 3.3421052631578947],\n",
       " [395, 3.608695652173913],\n",
       " [396, 3.560693641618497],\n",
       " [397, 3.8823529411764706],\n",
       " [398, 3.8133333333333335],\n",
       " [399, 4.15625],\n",
       " [400, 3.875],\n",
       " [401, 3.871794871794872],\n",
       " [402, 3.591549295774648],\n",
       " [403, 3.8035714285714284],\n",
       " [404, 4.14],\n",
       " [405, 3.795918367346939],\n",
       " [406, 3.306122448979592],\n",
       " [407, 3.4375],\n",
       " [408, 4.352564102564102],\n",
       " [409, 3.9158249158249157],\n",
       " [410, 3.96875],\n",
       " [411, 3.280314960629921],\n",
       " [412, 4.401260504201681],\n",
       " [413, 4.404040404040404],\n",
       " [414, 3.0701754385964914],\n",
       " [415, 3.874538745387454],\n",
       " [416, 3.7580645161290325],\n",
       " [417, 4.045454545454546],\n",
       " [418, 3.549019607843137],\n",
       " [419, 3.962962962962963],\n",
       " [420, 4.359375],\n",
       " [421, 4.25],\n",
       " [422, 3.297872340425532],\n",
       " [423, 2.5],\n",
       " [424, 3.735725938009788],\n",
       " [425, 3.6613756613756614],\n",
       " [426, 3.7573221757322175],\n",
       " [427, 4.111111111111111],\n",
       " [428, 3.9],\n",
       " [429, 3.346820809248555],\n",
       " [430, 3.9682539682539684],\n",
       " [431, 3.630952380952381],\n",
       " [432, 2.9863013698630136],\n",
       " [433, 3.391304347826087],\n",
       " [434, 4.023255813953488],\n",
       " [435, 3.8333333333333335],\n",
       " [436, 3.8345864661654137],\n",
       " [437, 4.3076923076923075],\n",
       " [438, 3.528239202657807],\n",
       " [439, 3.902173913043478],\n",
       " [440, 3.586206896551724],\n",
       " [441, 3.9574468085106385],\n",
       " [442, 3.8486997635933804],\n",
       " [443, 3.823529411764706],\n",
       " [444, 4.0],\n",
       " [445, 3.3181818181818183],\n",
       " [446, 4.8431372549019605],\n",
       " [447, 4.837837837837838],\n",
       " [448, 3.4347826086956523],\n",
       " [449, 3.7222222222222223],\n",
       " [450, 4.196078431372549],\n",
       " [451, 4.511961722488039],\n",
       " [452, 4.431818181818182],\n",
       " [453, 3.66497461928934],\n",
       " [454, 3.218045112781955],\n",
       " [455, 4.2],\n",
       " [456, 3.394904458598726],\n",
       " [457, 3.7130801687763713],\n",
       " [458, 3.5348837209302326],\n",
       " [459, 3.6875],\n",
       " [460, 3.3617021276595747],\n",
       " [461, 3.224609375],\n",
       " [462, 3.536723163841808],\n",
       " [463, 3.0],\n",
       " [464, 3.6097560975609757],\n",
       " [465, 3.5405405405405403],\n",
       " [466, 4.14070351758794],\n",
       " [467, 3.2028985507246377],\n",
       " [468, 3.730769230769231],\n",
       " [469, 4.326530612244898],\n",
       " [470, 3.8088235294117645],\n",
       " [471, 3.6285714285714286],\n",
       " [472, 4.022222222222222],\n",
       " [473, 4.163265306122449],\n",
       " [474, 3.380503144654088],\n",
       " [475, 3.8299595141700404],\n",
       " [476, 3.8375870069605567],\n",
       " [477, 3.5829383886255926],\n",
       " [478, 3.869565217391304],\n",
       " [479, 3.827956989247312],\n",
       " [480, 3.411214953271028],\n",
       " [481, 3.696969696969697],\n",
       " [482, 3.2606060606060607],\n",
       " [483, 2.9310344827586206],\n",
       " [484, 3.735294117647059],\n",
       " [485, 4.044444444444444],\n",
       " [486, 4.051282051282051],\n",
       " [487, 3.34],\n",
       " [488, 3.56],\n",
       " [489, 3.3333333333333335],\n",
       " [490, 3.7662337662337664],\n",
       " [491, 3.68],\n",
       " [492, 3.9375],\n",
       " [493, 3.848101265822785],\n",
       " [494, 4.157068062827225],\n",
       " [495, 3.7954545454545454],\n",
       " [496, 4.294117647058823],\n",
       " [497, 3.5833333333333335],\n",
       " [498, 3.6511627906976742],\n",
       " [499, 3.9748743718592965],\n",
       " [500, 3.633663366336634],\n",
       " [501, 3.417910447761194],\n",
       " [502, 4.083333333333333],\n",
       " [503, 4.448275862068965],\n",
       " [504, 3.8055555555555554],\n",
       " [505, 4.217391304347826],\n",
       " [506, 3.422222222222222],\n",
       " [507, 3.9523809523809526],\n",
       " [508, 3.3221476510067114],\n",
       " [509, 3.3139695712309822],\n",
       " [510, 3.8282828282828283],\n",
       " [511, 3.740740740740741],\n",
       " [512, 3.8378378378378377],\n",
       " [513, 3.1474358974358974],\n",
       " [514, 4.2025316455696204],\n",
       " [515, 3.728395061728395],\n",
       " [516, 2.931972789115646],\n",
       " [517, 3.963855421686747],\n",
       " [518, 4.3478260869565215],\n",
       " [519, 3.3777777777777778],\n",
       " [520, 3.9363057324840764],\n",
       " [521, 4.2926829268292686],\n",
       " [522, 3.8448275862068964],\n",
       " [523, 4.06],\n",
       " [524, 3.608267716535433],\n",
       " [525, 4.025],\n",
       " [526, 3.896551724137931],\n",
       " [527, 4.08],\n",
       " [528, 3.3551724137931034],\n",
       " [529, 4.19672131147541],\n",
       " [530, 4.0],\n",
       " [531, 3.1591695501730106],\n",
       " [532, 3.86046511627907],\n",
       " [533, 3.3401015228426396],\n",
       " [534, 3.7475728155339807],\n",
       " [535, 3.5714285714285716],\n",
       " [536, 3.942857142857143],\n",
       " [537, 4.3061224489795915],\n",
       " [538, 4.458333333333333],\n",
       " [539, 3.9242424242424243],\n",
       " [540, 3.230769230769231],\n",
       " [541, 3.1894736842105265],\n",
       " [542, 3.764705882352941],\n",
       " [543, 4.078986587183309],\n",
       " [544, 3.7777777777777777],\n",
       " [545, 3.4827586206896552],\n",
       " [546, 3.231818181818182],\n",
       " [547, 3.858974358974359],\n",
       " [548, 3.093220338983051],\n",
       " [549, 3.7569444444444446],\n",
       " [550, 3.578076525336091],\n",
       " [551, 3.8201754385964914],\n",
       " [552, 3.7628865979381443],\n",
       " [553, 4.15625],\n",
       " [554, 3.511627906976744],\n",
       " [555, 3.8157894736842106],\n",
       " [556, 3.5],\n",
       " [557, 3.8793103448275863],\n",
       " [558, 3.6804123711340204],\n",
       " [559, 3.0],\n",
       " [560, 3.897810218978102],\n",
       " [561, 3.7222222222222223],\n",
       " [562, 3.7027027027027026],\n",
       " [563, 2.7023121387283235],\n",
       " [564, 4.0],\n",
       " [565, 3.44],\n",
       " [566, 2.6273408239700373],\n",
       " [567, 4.583333333333333],\n",
       " [568, 4.44],\n",
       " [569, 3.52],\n",
       " [570, 3.329113924050633],\n",
       " [571, 3.7054794520547945],\n",
       " [572, 3.05],\n",
       " [573, 3.9722222222222223],\n",
       " [574, 4.095238095238095],\n",
       " [575, 3.6564417177914113],\n",
       " [576, 3.6666666666666665],\n",
       " [577, 4.487341772151899],\n",
       " [578, 3.9642857142857144],\n",
       " [579, 3.8550724637681157],\n",
       " [580, 3.347826086956522],\n",
       " [581, 3.6666666666666665],\n",
       " [582, 4.282051282051282],\n",
       " [583, 4.040229885057471],\n",
       " [584, 4.2894736842105265],\n",
       " [585, 3.4662162162162162],\n",
       " [586, 4.485714285714286],\n",
       " [587, 3.0077922077922077],\n",
       " [588, 4.057395143487859],\n",
       " [589, 4.0],\n",
       " [590, 4.13855421686747],\n",
       " [591, 3.231404958677686],\n",
       " [592, 4.391304347826087],\n",
       " [593, 3.641509433962264],\n",
       " [594, 4.29559748427673],\n",
       " [595, 3.95],\n",
       " [596, 2.9523809523809526],\n",
       " [597, 4.473684210526316],\n",
       " [598, 3.3157894736842106],\n",
       " [599, 3.8518518518518516],\n",
       " [600, 3.652173913043478],\n",
       " [601, 3.1501340482573728],\n",
       " [602, 3.396103896103896],\n",
       " [603, 3.5238095238095237],\n",
       " [604, 3.0940766550522647],\n",
       " [605, 4.049180327868853],\n",
       " [606, 4.03030303030303],\n",
       " [607, 4.16],\n",
       " [608, 3.1882352941176473],\n",
       " [609, 4.346153846153846],\n",
       " [610, 3.484126984126984],\n",
       " [611, 3.9393939393939394],\n",
       " [612, 3.5],\n",
       " [613, 3.5849056603773586],\n",
       " [614, 3.8333333333333335],\n",
       " [615, 4.127659574468085],\n",
       " [616, 3.9545454545454546],\n",
       " [617, 4.086956521739131],\n",
       " [618, 3.0],\n",
       " [619, 3.909090909090909],\n",
       " [620, 3.3240223463687153],\n",
       " [621, 3.0416666666666665],\n",
       " [622, 3.912280701754386],\n",
       " [623, 4.226744186046512],\n",
       " [624, 3.6801075268817205],\n",
       " [625, 4.0],\n",
       " [626, 4.055555555555555],\n",
       " [627, 3.5625],\n",
       " [628, 3.9038461538461537],\n",
       " [629, 3.371308016877637],\n",
       " [630, 4.254237288135593],\n",
       " [631, 3.7948717948717947],\n",
       " [632, 3.7941176470588234],\n",
       " [633, 3.5813953488372094],\n",
       " [634, 4.014925373134329],\n",
       " [635, 4.3107344632768365],\n",
       " [636, 4.058139534883721],\n",
       " [637, 3.7559681697612732],\n",
       " [638, 4.175438596491228],\n",
       " [639, 3.705],\n",
       " [640, 4.333333333333333],\n",
       " [641, 4.008264462809917],\n",
       " [642, 4.111111111111111],\n",
       " [643, 2.7142857142857144],\n",
       " [644, 3.1203703703703702],\n",
       " [645, 4.4772727272727275],\n",
       " [646, 3.8031496062992125],\n",
       " [647, 3.103896103896104],\n",
       " [648, 3.7231638418079096],\n",
       " [649, 3.6619718309859155],\n",
       " [650, 3.8947368421052633],\n",
       " [651, 3.6129707112970713],\n",
       " [652, 2.8863636363636362],\n",
       " [653, 4.142857142857143],\n",
       " [654, 3.4324324324324325],\n",
       " [655, 2.733009708737864],\n",
       " [656, 3.8700564971751414],\n",
       " [657, 4.016949152542373],\n",
       " [658, 3.096774193548387],\n",
       " [659, 3.7],\n",
       " [660, 3.0170697012802274],\n",
       " [661, 4.647887323943662],\n",
       " [662, 3.141732283464567],\n",
       " [663, 3.580357142857143],\n",
       " [664, 4.025316455696203],\n",
       " [665, 3.5],\n",
       " [666, 3.8932038834951457],\n",
       " [667, 3.0935672514619883],\n",
       " [668, 3.5833333333333335],\n",
       " [669, 3.847255369928401],\n",
       " [670, 3.2444444444444445],\n",
       " [671, 4.2592592592592595],\n",
       " [672, 3.872340425531915],\n",
       " [673, 3.13151364764268],\n",
       " [674, 4.2784810126582276],\n",
       " [675, 3.3095238095238093],\n",
       " [676, 3.128205128205128],\n",
       " [677, 3.892682926829268],\n",
       " [678, 3.6776776776776776],\n",
       " [679, 3.926829268292683],\n",
       " [680, 3.5714285714285716],\n",
       " [681, 4.2368421052631575],\n",
       " [682, 4.733333333333333],\n",
       " [683, 3.586206896551724],\n",
       " [684, 3.8947368421052633],\n",
       " [685, 3.2357142857142858],\n",
       " [686, 3.7777777777777777],\n",
       " [687, 3.4873417721518987],\n",
       " [688, 3.75],\n",
       " [689, 3.3925925925925924],\n",
       " [690, 4.311111111111111],\n",
       " [691, 4.174757281553398],\n",
       " [692, 3.8240887480190175],\n",
       " [693, 3.8857142857142857],\n",
       " [694, 3.625],\n",
       " [695, 3.513089005235602],\n",
       " [696, 3.802992518703242],\n",
       " [697, 3.8],\n",
       " [698, 3.551851851851852],\n",
       " [699, 3.0534124629080117],\n",
       " [700, 3.875],\n",
       " [701, 3.5],\n",
       " [702, 3.3027139874739038],\n",
       " [703, 4.1],\n",
       " [704, 3.081081081081081],\n",
       " [705, 3.371212121212121],\n",
       " [706, 3.556291390728477],\n",
       " [707, 3.6153846153846154],\n",
       " [708, 3.85],\n",
       " [709, 2.8292682926829267],\n",
       " [710, 3.4271186440677965],\n",
       " [711, 4.0],\n",
       " [712, 3.475177304964539],\n",
       " [713, 3.446280991735537],\n",
       " [714, 4.1635071090047395],\n",
       " [715, 3.8877551020408165],\n",
       " [716, 4.198979591836735],\n",
       " [717, 3.1538461538461537],\n",
       " [718, 3.775147928994083],\n",
       " [719, 3.5],\n",
       " [720, 2.9098712446351933],\n",
       " [721, 3.551051051051051],\n",
       " [722, 3.909090909090909],\n",
       " [723, 3.8333333333333335],\n",
       " [724, 3.643312101910828],\n",
       " [725, 4.197530864197531],\n",
       " [726, 3.9315068493150687],\n",
       " [727, 3.6987951807228914],\n",
       " [728, 3.311377245508982],\n",
       " [729, 3.5273972602739727],\n",
       " [730, 3.7735849056603774],\n",
       " [731, 3.778816199376947],\n",
       " [732, 3.4285714285714284],\n",
       " [733, 4.05982905982906],\n",
       " [734, 3.727272727272727],\n",
       " [735, 3.590330788804071],\n",
       " [736, 3.9298245614035086],\n",
       " [737, 3.5668202764976957],\n",
       " [738, 3.303030303030303],\n",
       " [739, 4.354330708661418],\n",
       " [740, 4.243243243243243],\n",
       " [741, 3.324675324675325],\n",
       " [742, 3.9523809523809526],\n",
       " [743, 3.38255033557047],\n",
       " [744, 3.3703703703703702],\n",
       " [745, 2.64],\n",
       " [746, 2.634433962264151],\n",
       " [747, 3.59375],\n",
       " [748, 3.9753086419753085],\n",
       " [749, 3.3246187363834423],\n",
       " [750, 4.321428571428571],\n",
       " [751, 3.88],\n",
       " [752, 2.8291015625],\n",
       " [753, 3.7752293577981653],\n",
       " [754, 3.7770700636942673],\n",
       " [755, 4.111111111111111],\n",
       " [756, 3.9714285714285715],\n",
       " [757, 3.225806451612903],\n",
       " [758, 4.0],\n",
       " [759, 3.5876288659793816],\n",
       " [760, 4.265625],\n",
       " [761, 4.55],\n",
       " [762, 3.717391304347826],\n",
       " [763, 3.730769230769231],\n",
       " [764, 4.525179856115108],\n",
       " [765, 3.574626865671642],\n",
       " [766, 3.9361702127659575],\n",
       " [767, 4.023529411764706],\n",
       " [768, 4.4375],\n",
       " [769, 3.8208955223880596],\n",
       " [770, 2.935441370223979],\n",
       " [771, 3.769230769230769],\n",
       " [772, 3.479591836734694],\n",
       " [773, 3.5918367346938775],\n",
       " [774, 3.2142857142857144],\n",
       " [775, 4.0],\n",
       " [776, 3.766990291262136],\n",
       " [777, 2.5796812749003983],\n",
       " [778, 3.785276073619632],\n",
       " [779, 3.3333333333333335],\n",
       " [780, 3.45703125],\n",
       " [781, 3.1709401709401708],\n",
       " [782, 3.4347826086956523],\n",
       " [783, 3.5210084033613445],\n",
       " [784, 4.066666666666666],\n",
       " [785, 3.2358490566037736],\n",
       " [786, 4.063492063492063],\n",
       " [787, 3.58974358974359],\n",
       " [788, 3.5255102040816326],\n",
       " [789, 2.9043478260869566],\n",
       " [790, 4.3478260869565215],\n",
       " [791, 3.966463414634146],\n",
       " [792, 3.4597701149425286],\n",
       " [793, 3.486666666666667],\n",
       " [794, 3.953488372093023],\n",
       " [795, 3.442953020134228],\n",
       " [796, 2.9717391304347824],\n",
       " [797, 4.036144578313253],\n",
       " [798, 3.149847094801223],\n",
       " [799, 3.6],\n",
       " [800, 3.4849624060150375],\n",
       " [801, 3.6596491228070174],\n",
       " [802, 3.938735177865613],\n",
       " [803, 3.7115384615384617],\n",
       " [804, 3.272727272727273],\n",
       " [805, 3.835616438356164],\n",
       " [806, 4.166666666666667],\n",
       " [807, 3.9696969696969697],\n",
       " [808, 3.1236363636363635],\n",
       " [809, 4.031914893617022],\n",
       " [810, 3.8174603174603177],\n",
       " [811, 4.184615384615385],\n",
       " [812, 3.739130434782609],\n",
       " [813, 3.343283582089552],\n",
       " [814, 4.055555555555555],\n",
       " [815, 4.068965517241379],\n",
       " [816, 3.6974358974358976],\n",
       " [817, 4.010050251256281],\n",
       " [818, 3.7251461988304095],\n",
       " [819, 3.3225806451612905],\n",
       " [820, 3.4134615384615383],\n",
       " [821, 2.9523809523809526],\n",
       " [822, 3.7226027397260273],\n",
       " [823, 3.8677685950413223],\n",
       " [824, 3.646103896103896],\n",
       " [825, 3.619047619047619],\n",
       " [826, 3.2857142857142856],\n",
       " [827, 3.9545454545454546],\n",
       " [828, 3.4434782608695653],\n",
       " [829, 4.231884057971015],\n",
       " [830, 3.6149425287356323],\n",
       " [831, 4.105263157894737],\n",
       " [832, 3.558139534883721],\n",
       " [833, 4.0476190476190474],\n",
       " [834, 4.16],\n",
       " [835, 2.75],\n",
       " [836, 2.4],\n",
       " [837, 3.260869565217391],\n",
       " [838, 4.090909090909091],\n",
       " [839, 3.988372093023256],\n",
       " [840, 4.219123505976095],\n",
       " [841, 3.576923076923077],\n",
       " [842, 3.8378378378378377],\n",
       " [843, 3.9444444444444446],\n",
       " [844, 3.4523809523809526],\n",
       " [845, 3.980769230769231],\n",
       " [846, 3.91699604743083],\n",
       " [847, 3.6129032258064515],\n",
       " [848, 4.178571428571429],\n",
       " [849, 3.264957264957265],\n",
       " [850, 3.5613718411552346],\n",
       " [851, 3.5921052631578947],\n",
       " [852, 4.117647058823529],\n",
       " [853, 3.890909090909091],\n",
       " [854, 3.027667984189723],\n",
       " [855, 3.4126984126984126],\n",
       " [856, 3.490566037735849],\n",
       " [857, 4.171428571428572],\n",
       " [858, 4.189473684210526],\n",
       " [859, 3.450980392156863],\n",
       " [860, 3.1666666666666665],\n",
       " [861, 3.9375],\n",
       " [862, 3.6724137931034484],\n",
       " [863, 4.225806451612903],\n",
       " [864, 4.050724637681159],\n",
       " [865, 3.8095238095238093],\n",
       " [866, 3.3333333333333335],\n",
       " [867, 3.659090909090909],\n",
       " [868, 3.6],\n",
       " [869, 3.5154394299287413],\n",
       " [870, 3.611111111111111],\n",
       " [871, 3.9069767441860463],\n",
       " [872, 3.635514018691589],\n",
       " [873, 3.8430232558139537],\n",
       " [874, 3.7857142857142856],\n",
       " [875, 4.083333333333333],\n",
       " [876, 3.828828828828829],\n",
       " [877, 3.308056872037915],\n",
       " [878, 4.142857142857143],\n",
       " [879, 4.025],\n",
       " [880, 3.4956521739130433],\n",
       " [881, 2.9354485776805253],\n",
       " [882, 4.0886075949367084],\n",
       " [883, 3.4166666666666665],\n",
       " [884, 4.01010101010101],\n",
       " [885, 4.140625],\n",
       " [886, 3.6285714285714286],\n",
       " [887, 3.5104166666666665],\n",
       " [888, 3.7777777777777777],\n",
       " [889, 2.8405797101449277],\n",
       " [890, 3.969298245614035],\n",
       " [891, 3.7443946188340806],\n",
       " [892, 3.911764705882353],\n",
       " [893, 3.2],\n",
       " [894, 4.442857142857143],\n",
       " [895, 3.953125],\n",
       " [896, 3.984375],\n",
       " [897, 3.5566502463054186],\n",
       " [898, 4.083333333333333],\n",
       " [899, 3.523219814241486],\n",
       " [900, 3.576923076923077],\n",
       " [901, 3.606060606060606],\n",
       " [902, 4.28],\n",
       " [903, 3.4594594594594597],\n",
       " [904, 3.3008130081300813],\n",
       " [905, 3.7886178861788617],\n",
       " [906, 3.5238095238095237],\n",
       " [907, 3.9523809523809526],\n",
       " [908, 3.3076923076923075],\n",
       " [909, 3.9014084507042255],\n",
       " [910, 3.6012269938650308],\n",
       " [911, 3.8685714285714288],\n",
       " [912, 3.7209302325581395],\n",
       " [913, 3.2888888888888888],\n",
       " [914, 4.278688524590164],\n",
       " [915, 2.831578947368421],\n",
       " [916, 3.9454545454545453],\n",
       " [917, 4.068965517241379],\n",
       " [918, 2.9583333333333335],\n",
       " [919, 3.9355828220858897],\n",
       " [920, 3.4615384615384617],\n",
       " [921, 3.6962025316455698],\n",
       " [922, 3.5830903790087465],\n",
       " [923, 3.608695652173913],\n",
       " [924, 3.9899497487437188],\n",
       " [925, 3.1323529411764706],\n",
       " [926, 4.247619047619048],\n",
       " [927, 3.230366492146597],\n",
       " [928, 4.3254716981132075],\n",
       " [929, 3.6816901408450704],\n",
       " [930, 3.0510204081632653],\n",
       " [931, 4.031847133757962],\n",
       " [932, 4.45],\n",
       " [933, 3.7096774193548385],\n",
       " [934, 2.9859437751004014],\n",
       " [935, 3.4896907216494846],\n",
       " [936, 3.5113636363636362],\n",
       " [937, 3.7327586206896552],\n",
       " [938, 3.870967741935484],\n",
       " [939, 3.757575757575758],\n",
       " [940, 3.1923076923076925],\n",
       " [941, 2.2857142857142856],\n",
       " [942, 4.04],\n",
       " [943, 4.296296296296297],\n",
       " [944, 3.8444444444444446],\n",
       " [945, 3.6196319018404908],\n",
       " [946, 4.303030303030303],\n",
       " [947, 3.0],\n",
       " [948, 3.7408123791102517],\n",
       " [949, 3.9295392953929538],\n",
       " [950, 2.963636363636364],\n",
       " [951, 4.523809523809524],\n",
       " [952, 3.9936305732484074],\n",
       " [953, 4.6878306878306875],\n",
       " [954, 3.7777777777777777],\n",
       " [955, 3.5798816568047336],\n",
       " [956, 3.990740740740741],\n",
       " [957, 4.271341463414634],\n",
       " [958, 3.9050632911392404],\n",
       " [959, 3.7395833333333335],\n",
       " [960, 3.9375],\n",
       " [961, 3.74],\n",
       " [962, 4.03921568627451],\n",
       " [963, 3.4339622641509435],\n",
       " [964, 3.717948717948718],\n",
       " [965, 4.116883116883117],\n",
       " [966, 3.5636363636363635],\n",
       " [967, 3.5384615384615383],\n",
       " [968, 4.131147540983607],\n",
       " [969, 4.115384615384615],\n",
       " [970, 3.1493624772313296],\n",
       " [971, 3.3318385650224216],\n",
       " [972, 3.3714285714285714],\n",
       " [973, 3.3963133640552994],\n",
       " [974, 3.7333333333333334],\n",
       " [975, 3.25990099009901],\n",
       " [976, 3.3636363636363638],\n",
       " [977, 3.7625],\n",
       " [978, 3.8863636363636362],\n",
       " [979, 4.04054054054054],\n",
       " [980, 3.2222222222222223],\n",
       " [981, 3.3303964757709252],\n",
       " [982, 4.176470588235294],\n",
       " [983, 4.115384615384615],\n",
       " [984, 3.5417867435158503],\n",
       " [985, 4.212328767123288],\n",
       " [986, 3.772727272727273],\n",
       " [987, 4.017045454545454],\n",
       " [988, 3.8493150684931505],\n",
       " [989, 4.681818181818182],\n",
       " [990, 3.549019607843137],\n",
       " [991, 3.75],\n",
       " [992, 3.4193548387096775],\n",
       " [993, 3.3448275862068964],\n",
       " [994, 4.153846153846154],\n",
       " [995, 3.8979591836734695],\n",
       " [996, 3.935810810810811],\n",
       " [997, 3.933333333333333],\n",
       " [998, 4.118518518518519],\n",
       " [999, 3.186893203883495],\n",
       " [1000, 4.130952380952381],\n",
       " ...]"
      ]
     },
     "execution_count": 154,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "user_mean_list = []\n",
    "\n",
    "for i in user_id: # range(1,6041)\n",
    "    # 1번~6040번 사용자가 매긴 평점들의 평균을 구해주는 코드\n",
    "    user_mean = movie[movie[:,0]==i][:,2].mean()\n",
    "    # 빈 리스트에 사용자 번호와 그 사람이 매긴 평점의 평균을 리스트로 저장\n",
    "    user_mean_list.append([i, user_mean])\n",
    "user_mean_list"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6ab0cb7f",
   "metadata": {},
   "source": [
    "#### 6. 위에서 구한 각 사용자별 평점 평균이 4점 이상인 사용자만 구해보세요~!\n",
    "- 사용자 번호와 명수를 구해봅시다!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 157,
   "id": "d1cca7ec",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[   1,    4],\n",
       "       [   2,    3],\n",
       "       [   3,    3],\n",
       "       ...,\n",
       "       [6038,    3],\n",
       "       [6039,    3],\n",
       "       [6040,    3]], dtype=int64)"
      ]
     },
     "execution_count": 157,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 불리언 인덱싱 적용을 위해 리스트를 배열로 변환\n",
    "user_mean_arr = np.array(user_mean_list,dtype='int64')\n",
    "user_mean_arr"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 162,
   "id": "6d255f4e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[   1    4    7 ... 6027 6032 6034]\n",
      "1544\n"
     ]
    }
   ],
   "source": [
    "print(user_mean_arr[user_mean_arr[:,1]>=4][:,0])\n",
    "print(len(user_mean_arr[user_mean_arr[:,1]>=4][:,0]))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c5dccc1b",
   "metadata": {},
   "source": [
    "-  사용자가 매긴 평점의 평균이 4점 이상인 사람들은 총 1544명"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "80d370d7",
   "metadata": {},
   "source": [
    "#### 7. 10번 영화의 평점 평균 구하기!\n",
    "- 직접 해보세요^_^"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 163,
   "id": "dd1afa3c",
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
     "execution_count": 163,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "movie"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 179,
   "id": "b1aca3aa",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3.5405405405405403"
      ]
     },
     "execution_count": 179,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "movie[movie[:,1]==10][:,2].mean()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a12ea427",
   "metadata": {},
   "source": [
    "#### 8. 각 영화가 받은 평점의 평균 구하기!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 192,
   "id": "250444fe",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([   1,    2,    3, ..., 3950, 3951, 3952], dtype=int64)"
      ]
     },
     "execution_count": 192,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "item_id = np.unique(movie[:,1])\n",
    "item_id"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 193,
   "id": "eb6360ee",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[[1, 4.146846413095811],\n",
       " [2, 3.20114122681883],\n",
       " [3, 3.01673640167364],\n",
       " [4, 2.7294117647058824],\n",
       " [5, 3.0067567567567566],\n",
       " [6, 3.8787234042553194],\n",
       " [7, 3.410480349344978],\n",
       " [8, 3.014705882352941],\n",
       " [9, 2.656862745098039],\n",
       " [10, 3.5405405405405403],\n",
       " [11, 3.7938044530493706],\n",
       " [12, 2.3625],\n",
       " [13, 3.2626262626262625],\n",
       " [14, 3.542483660130719],\n",
       " [15, 2.458904109589041],\n",
       " [16, 3.7932551319648096],\n",
       " [17, 4.027544910179641],\n",
       " [18, 3.337579617834395],\n",
       " [19, 2.480719794344473],\n",
       " [20, 2.5375],\n",
       " [21, 3.6238938053097347],\n",
       " [22, 3.3492063492063493],\n",
       " [23, 2.857142857142857],\n",
       " [24, 3.1794871794871793],\n",
       " [25, 3.6510204081632653],\n",
       " [26, 3.53],\n",
       " [27, 2.9344262295081966],\n",
       " [28, 4.055865921787709],\n",
       " [29, 4.062034739454094],\n",
       " [30, 3.6486486486486487],\n",
       " [31, 3.1134751773049647],\n",
       " [32, 3.945731303772336],\n",
       " [33, 3.0],\n",
       " [34, 3.8914905768132497],\n",
       " [35, 3.3142857142857145],\n",
       " [36, 3.9579741379310347],\n",
       " [37, 3.5],\n",
       " [38, 2.8214285714285716],\n",
       " [39, 3.6233480176211454],\n",
       " [40, 3.933333333333333],\n",
       " [41, 3.958677685950413],\n",
       " [42, 2.8687782805429864],\n",
       " [43, 3.4457831325301207],\n",
       " [44, 2.787781350482315],\n",
       " [45, 3.4246323529411766],\n",
       " [46, 3.108433734939759],\n",
       " [47, 4.106420404573439],\n",
       " [48, 2.9764397905759163],\n",
       " [49, 3.740740740740741],\n",
       " [50, 4.517106001121705],\n",
       " [52, 3.640371229698376],\n",
       " [53, 4.75],\n",
       " [54, 2.5609756097560976],\n",
       " [55, 3.066666666666667],\n",
       " [56, 2.0],\n",
       " [57, 3.404040404040404],\n",
       " [58, 4.093812375249501],\n",
       " [59, 2.75],\n",
       " [60, 3.212885154061625],\n",
       " [61, 3.0],\n",
       " [62, 3.6968576709796674],\n",
       " [63, 2.855855855855856],\n",
       " [64, 2.2658227848101267],\n",
       " [65, 2.062937062937063],\n",
       " [66, 1.6701030927835052],\n",
       " [67, 3.25],\n",
       " [68, 3.45],\n",
       " [69, 3.6551724137931036],\n",
       " [70, 3.1564551422319473],\n",
       " [71, 2.1041666666666665],\n",
       " [72, 3.6344086021505375],\n",
       " [73, 3.8169642857142856],\n",
       " [74, 2.975],\n",
       " [75, 1.9166666666666667],\n",
       " [76, 2.853932584269663],\n",
       " [77, 3.764705882352941],\n",
       " [78, 3.26],\n",
       " [79, 2.6052631578947367],\n",
       " [80, 3.826923076923077],\n",
       " [81, 3.1626506024096384],\n",
       " [82, 3.8764044943820224],\n",
       " [83, 3.696969696969697],\n",
       " [84, 3.0952380952380953],\n",
       " [85, 3.402061855670103],\n",
       " [86, 3.3940677966101696],\n",
       " [87, 2.210526315789474],\n",
       " [88, 2.9427083333333335],\n",
       " [89, 3.074235807860262],\n",
       " [90, 3.6666666666666665],\n",
       " [92, 2.340909090909091],\n",
       " [93, 2.235955056179775],\n",
       " [94, 3.7252747252747254],\n",
       " [95, 2.876175548589342],\n",
       " [96, 3.923076923076923],\n",
       " [97, 3.75],\n",
       " [98, 2.0],\n",
       " [99, 3.46],\n",
       " [100, 3.0625],\n",
       " [101, 3.869565217391304],\n",
       " [102, 1.8166666666666667],\n",
       " [103, 3.212121212121212],\n",
       " [104, 3.526392961876833],\n",
       " [105, 3.2325581395348837],\n",
       " [106, 3.5833333333333335],\n",
       " [107, 3.1484375],\n",
       " [108, 2.857142857142857],\n",
       " [110, 4.234957020057307],\n",
       " [111, 4.183870967741935],\n",
       " [112, 3.443859649122807],\n",
       " [113, 2.981132075471698],\n",
       " [114, 3.090909090909091],\n",
       " [116, 4.097560975609756],\n",
       " [117, 3.632911392405063],\n",
       " [118, 3.073529411764706],\n",
       " [119, 2.4615384615384617],\n",
       " [120, 2.6666666666666665],\n",
       " [121, 4.054054054054054],\n",
       " [122, 2.768041237113402],\n",
       " [123, 3.869565217391304],\n",
       " [124, 3.2142857142857144],\n",
       " [125, 3.8333333333333335],\n",
       " [126, 1.9898989898989898],\n",
       " [127, 1.0],\n",
       " [128, 4.333333333333333],\n",
       " [129, 3.3076923076923075],\n",
       " [130, 4.0],\n",
       " [131, 3.0625],\n",
       " [132, 2.4945054945054945],\n",
       " [133, 1.0],\n",
       " [134, 4.0],\n",
       " [135, 2.81203007518797],\n",
       " [136, 3.25],\n",
       " [137, 3.0],\n",
       " [138, 2.5],\n",
       " [139, 4.0],\n",
       " [140, 3.1654676258992804],\n",
       " [141, 3.5498533724340176],\n",
       " [142, 1.0],\n",
       " [144, 3.392609699769053],\n",
       " [145, 3.2955801104972378],\n",
       " [146, 2.888888888888889],\n",
       " [147, 3.541436464088398],\n",
       " [148, 2.782608695652174],\n",
       " [149, 3.7872340425531914],\n",
       " [150, 4.073541167066347],\n",
       " [151, 3.588447653429603],\n",
       " [152, 3.0],\n",
       " [153, 2.642213642213642],\n",
       " [154, 3.7261904761904763],\n",
       " [155, 3.413793103448276],\n",
       " [156, 3.5606060606060606],\n",
       " [157, 2.732620320855615],\n",
       " [158, 2.9806949806949805],\n",
       " [159, 3.2844827586206895],\n",
       " [160, 2.2389380530973453],\n",
       " [161, 3.723684210526316],\n",
       " [162, 4.063136456211812],\n",
       " [163, 3.4574074074074073],\n",
       " [164, 3.5672823218997363],\n",
       " [165, 3.561212121212121],\n",
       " [166, 2.459016393442623],\n",
       " [167, 3.6],\n",
       " [168, 2.9502762430939224],\n",
       " [169, 2.017699115044248],\n",
       " [170, 3.146417445482866],\n",
       " [171, 3.5698924731182795],\n",
       " [172, 2.576419213973799],\n",
       " [173, 2.3085106382978724],\n",
       " [174, 2.308641975308642],\n",
       " [175, 3.477272727272727],\n",
       " [176, 3.9170731707317072],\n",
       " [177, 2.7338129496402876],\n",
       " [178, 3.473684210526316],\n",
       " [179, 2.2083333333333335],\n",
       " [180, 3.5476718403547673],\n",
       " [181, 1.6129032258064515],\n",
       " [182, 3.142857142857143],\n",
       " [183, 3.4827586206896552],\n",
       " [184, 3.3461538461538463],\n",
       " [185, 2.869947275922671],\n",
       " [186, 2.7630331753554502],\n",
       " [187, 3.238095238095238],\n",
       " [188, 3.221052631578947],\n",
       " [189, 3.4],\n",
       " [190, 3.75],\n",
       " [191, 2.466666666666667],\n",
       " [192, 3.0],\n",
       " [193, 2.0506912442396312],\n",
       " [194, 3.755868544600939],\n",
       " [195, 2.841463414634146],\n",
       " [196, 2.8236363636363637],\n",
       " [197, 3.0588235294117645],\n",
       " [198, 3.2958677685950413],\n",
       " [199, 3.8119658119658117],\n",
       " [200, 2.4166666666666665],\n",
       " [201, 2.6363636363636362],\n",
       " [202, 2.5],\n",
       " [203, 3.0541871921182264],\n",
       " [204, 2.9211822660098523],\n",
       " [205, 3.611764705882353],\n",
       " [206, 3.6707317073170733],\n",
       " [207, 3.132420091324201],\n",
       " [208, 2.6313364055299537],\n",
       " [209, 2.4615384615384617],\n",
       " [210, 3.1463414634146343],\n",
       " [211, 3.5588235294117645],\n",
       " [212, 1.9285714285714286],\n",
       " [213, 4.056910569105691],\n",
       " [214, 4.25],\n",
       " [215, 3.80625],\n",
       " [216, 3.183098591549296],\n",
       " [217, 2.625],\n",
       " [218, 3.128205128205128],\n",
       " [219, 3.1818181818181817],\n",
       " [220, 1.8214285714285714],\n",
       " [222, 3.547112462006079],\n",
       " [223, 3.946883852691218],\n",
       " [224, 3.3911917098445596],\n",
       " [225, 3.173228346456693],\n",
       " [226, 2.0],\n",
       " [227, 2.6744186046511627],\n",
       " [228, 2.1538461538461537],\n",
       " [229, 3.5],\n",
       " [230, 3.4527220630372493],\n",
       " [231, 3.1924242424242424],\n",
       " [232, 4.07514450867052],\n",
       " [233, 3.6127659574468085],\n",
       " [234, 2.2244897959183674],\n",
       " [235, 3.696871628910464],\n",
       " [236, 3.303680981595092],\n",
       " [237, 2.972762645914397],\n",
       " [238, 2.8125],\n",
       " [239, 2.875],\n",
       " [240, 2.7111111111111112],\n",
       " [241, 3.310344827586207],\n",
       " [242, 3.5],\n",
       " [243, 2.1],\n",
       " [244, 1.9],\n",
       " [245, 3.0],\n",
       " [246, 4.18854748603352],\n",
       " [247, 3.8658280922431865],\n",
       " [248, 2.9130434782608696],\n",
       " [249, 3.7586206896551726],\n",
       " [250, 2.6],\n",
       " [251, 3.2777777777777777],\n",
       " [252, 3.2697547683923704],\n",
       " [253, 3.524390243902439],\n",
       " [254, 3.0789473684210527],\n",
       " [255, 2.0606060606060606],\n",
       " [256, 2.6513761467889907],\n",
       " [257, 3.2280701754385963],\n",
       " [258, 2.423611111111111],\n",
       " [259, 2.843137254901961],\n",
       " [260, 4.453694416583082],\n",
       " [261, 3.6491228070175437],\n",
       " [262, 3.872093023255814],\n",
       " [263, 3.857142857142857],\n",
       " [264, 3.2],\n",
       " [265, 3.9326424870466323],\n",
       " [266, 3.425531914893617],\n",
       " [267, 2.7285714285714286],\n",
       " [268, 3.3703703703703702],\n",
       " [269, 3.5272727272727273],\n",
       " [270, 3.037974683544304],\n",
       " [271, 3.142857142857143],\n",
       " [272, 3.7258485639686683],\n",
       " [273, 2.8975409836065573],\n",
       " [274, 2.375],\n",
       " [275, 2.5375],\n",
       " [276, 2.692982456140351],\n",
       " [277, 3.1823529411764704],\n",
       " [278, 2.75],\n",
       " [279, 3.717391304347826],\n",
       " [280, 3.5707547169811322],\n",
       " [281, 3.648068669527897],\n",
       " [282, 3.2232558139534886],\n",
       " [283, 3.0],\n",
       " [286, 3.0],\n",
       " [287, 2.9047619047619047],\n",
       " [288, 3.144285714285714],\n",
       " [289, 3.3417721518987342],\n",
       " [290, 3.9166666666666665],\n",
       " [291, 2.2083333333333335],\n",
       " [292, 3.2687585266030013],\n",
       " [293, 4.106175514626218],\n",
       " [294, 3.0952380952380953],\n",
       " [295, 2.7586206896551726],\n",
       " [296, 4.278212805158913],\n",
       " [297, 3.107142857142857],\n",
       " [298, 3.9130434782608696],\n",
       " [299, 3.664335664335664],\n",
       " [300, 3.7588652482269502],\n",
       " [301, 3.302325581395349],\n",
       " [302, 3.813953488372093],\n",
       " [303, 2.9760765550239237],\n",
       " [304, 3.142857142857143],\n",
       " [305, 2.5039370078740157],\n",
       " [306, 4.227544910179641],\n",
       " [307, 4.098765432098766],\n",
       " [308, 3.9653465346534653],\n",
       " [309, 3.6875],\n",
       " [310, 2.6666666666666665],\n",
       " [311, 3.0],\n",
       " [312, 2.4375],\n",
       " [313, 2.888888888888889],\n",
       " [314, 3.85],\n",
       " [315, 2.65359477124183],\n",
       " [316, 3.490143369175627],\n",
       " [317, 3.1918876755070205],\n",
       " [318, 4.554557700942973],\n",
       " [319, 3.8937728937728937],\n",
       " [320, 3.40625],\n",
       " [321, 3.7540983606557377],\n",
       " [322, 3.712918660287081],\n",
       " [324, 3.9696969696969697],\n",
       " [325, 2.4489795918367347],\n",
       " [326, 4.344262295081967],\n",
       " [327, 2.6145251396648046],\n",
       " [328, 3.111111111111111],\n",
       " [329, 3.3767676767676766],\n",
       " [330, 2.7315436241610738],\n",
       " [331, 3.0952380952380953],\n",
       " [332, 2.546583850931677],\n",
       " [333, 3.502439024390244],\n",
       " [334, 3.8596491228070176],\n",
       " [335, 3.4878048780487805],\n",
       " [336, 2.6842105263157894],\n",
       " [337, 3.8412698412698414],\n",
       " [338, 2.8823529411764706],\n",
       " [339, 3.49925705794948],\n",
       " [340, 3.2738095238095237],\n",
       " [341, 3.838709677419355],\n",
       " [342, 3.6776061776061777],\n",
       " [343, 2.4285714285714284],\n",
       " [344, 3.1488250652741514],\n",
       " [345, 3.8059701492537314],\n",
       " [346, 3.525],\n",
       " [347, 3.1739130434782608],\n",
       " [348, 3.698901098901099],\n",
       " [349, 3.7261567516525025],\n",
       " [350, 3.392233009708738],\n",
       " [351, 3.342412451361868],\n",
       " [352, 3.134453781512605],\n",
       " [353, 3.4455040871934606],\n",
       " [354, 3.1791044776119404],\n",
       " [355, 2.352059925093633],\n",
       " [356, 4.087967183226983],\n",
       " [357, 3.7437145174371453],\n",
       " [358, 3.1702127659574466],\n",
       " [359, 3.210526315789474],\n",
       " [360, 2.4960629921259843],\n",
       " [361, 3.421641791044776],\n",
       " [362, 3.3640167364016738],\n",
       " [363, 4.258064516129032],\n",
       " [364, 3.8608385370205176],\n",
       " [365, 3.1690140845070425],\n",
       " [366, 2.8207171314741037],\n",
       " [367, 3.279050042408821],\n",
       " [368, 3.5236907730673317],\n",
       " [369, 3.310344827586207],\n",
       " [370, 2.8980582524271843],\n",
       " [371, 3.1792452830188678],\n",
       " [372, 3.1542056074766354],\n",
       " [373, 3.856589147286822],\n",
       " [374, 2.1147540983606556],\n",
       " [375, 3.2941176470588234],\n",
       " [376, 3.2457142857142856],\n",
       " [377, 3.5654545454545454],\n",
       " [378, 2.892857142857143],\n",
       " [379, 2.889908256880734],\n",
       " [380, 3.6342857142857143],\n",
       " [381, 3.2606635071090047],\n",
       " [382, 2.9338235294117645],\n",
       " [383, 3.2666666666666666],\n",
       " [384, 2.9],\n",
       " [385, 3.4],\n",
       " [386, 2.6],\n",
       " [387, 2.7450980392156863],\n",
       " [388, 3.6391752577319587],\n",
       " [389, 3.7],\n",
       " [390, 3.542372881355932],\n",
       " [391, 3.275],\n",
       " [392, 2.8],\n",
       " [393, 1.8571428571428572],\n",
       " [394, 3.6666666666666665],\n",
       " [396, 4.0],\n",
       " [397, 2.4166666666666665],\n",
       " [398, 4.0],\n",
       " [401, 3.0],\n",
       " [402, 3.0],\n",
       " [404, 3.75],\n",
       " [405, 2.123152709359606],\n",
       " [406, 3.625],\n",
       " [407, 2.911917098445596],\n",
       " [408, 3.3194444444444446],\n",
       " [409, 3.020408163265306],\n",
       " [410, 2.9071274298056156],\n",
       " [411, 2.6153846153846154],\n",
       " [412, 3.559322033898305],\n",
       " [413, 2.5306122448979593],\n",
       " [414, 2.6555555555555554],\n",
       " [415, 2.4804469273743015],\n",
       " [416, 2.4269662921348316],\n",
       " [417, 3.485576923076923],\n",
       " [418, 2.5172413793103448],\n",
       " [419, 2.1923076923076925],\n",
       " [420, 2.5056818181818183],\n",
       " [421, 3.3617021276595747],\n",
       " [422, 3.1228070175438596],\n",
       " [423, 3.1085972850678734],\n",
       " [424, 2.6],\n",
       " [425, 3.6095238095238096],\n",
       " [426, 3.0817843866171004],\n",
       " [427, 2.3674698795180724],\n",
       " [428, 3.931558935361217],\n",
       " [429, 2.379679144385027],\n",
       " [430, 2.4166666666666665],\n",
       " [431, 3.6910569105691056],\n",
       " [432, 2.579081632653061],\n",
       " [433, 2.7916666666666665],\n",
       " [434, 3.0845481049562684],\n",
       " [435, 2.6060037523452158],\n",
       " [436, 2.652482269503546],\n",
       " [437, 2.046875],\n",
       " [438, 2.625],\n",
       " [439, 4.5],\n",
       " [440, 3.811181434599156],\n",
       " [441, 3.6936236391912907],\n",
       " [442, 2.9921875],\n",
       " [443, 3.3870967741935485],\n",
       " [444, 2.2962962962962963],\n",
       " [445, 2.61],\n",
       " [446, 4.082677165354331],\n",
       " [447, 2.4838709677419355],\n",
       " [448, 3.6008771929824563],\n",
       " [449, 3.6619718309859155],\n",
       " [450, 3.280701754385965],\n",
       " [451, 3.150943396226415],\n",
       " [452, 3.289473684210526],\n",
       " [453, 3.2238805970149254],\n",
       " [454, 3.5473300970873787],\n",
       " [455, 2.5894736842105264],\n",
       " [456, 4.0],\n",
       " [457, 4.103258145363409],\n",
       " [458, 3.2758620689655173],\n",
       " [459, 2.832167832167832],\n",
       " [460, 2.263157894736842],\n",
       " [461, 3.2790697674418605],\n",
       " [462, 2.642857142857143],\n",
       " [463, 2.74468085106383],\n",
       " [464, 2.7824074074074074],\n",
       " [465, 3.3142857142857145],\n",
       " [466, 2.7958115183246073],\n",
       " [467, 3.2037037037037037],\n",
       " [468, 3.2714285714285714],\n",
       " [469, 2.9565217391304346],\n",
       " [470, 1.736842105263158],\n",
       " [471, 3.631051752921536],\n",
       " [472, 2.7045454545454546],\n",
       " [473, 2.225165562913907],\n",
       " [474, 3.825102880658436],\n",
       " [475, 3.9006410256410255],\n",
       " [476, 2.6857142857142855],\n",
       " [477, 3.466666666666667],\n",
       " [478, 2.4583333333333335],\n",
       " [479, 2.7969924812030076],\n",
       " [480, 3.7638473053892216],\n",
       " [481, 3.380952380952381],\n",
       " [482, 3.528409090909091],\n",
       " [483, 3.7432432432432434],\n",
       " [484, 2.6551724137931036],\n",
       " [485, 2.508],\n",
       " [486, 2.8125],\n",
       " [487, 2.6129032258064515],\n",
       " [488, 3.3846153846153846],\n",
       " [489, 2.4742268041237114],\n",
       " [490, 3.324324324324324],\n",
       " [491, 3.3160377358490565],\n",
       " [492, 3.719402985074627],\n",
       " [493, 3.6073825503355703],\n",
       " [494, 3.3461538461538463],\n",
       " [495, 3.380952380952381],\n",
       " [496, 3.2162162162162162],\n",
       " [497, 4.0],\n",
       " [498, 2.74468085106383],\n",
       " [499, 2.7551020408163267],\n",
       " [500, 3.420047732696897],\n",
       " [501, 3.606382978723404],\n",
       " [502, 1.935483870967742],\n",
       " [503, 3.6923076923076925],\n",
       " [504, 2.955056179775281],\n",
       " [505, 2.4927536231884058],\n",
       " [506, 3.491228070175439],\n",
       " [507, 3.522727272727273],\n",
       " [508, 3.894830659536542],\n",
       " [509, 3.674342105263158],\n",
       " [510, 2.4047619047619047],\n",
       " [511, 3.1052631578947367],\n",
       " [512, 2.8715083798882683],\n",
       " [513, 3.1194029850746268],\n",
       " [514, 3.531791907514451],\n",
       " [515, 3.917777777777778],\n",
       " [516, 2.870967741935484],\n",
       " [517, 3.175392670157068],\n",
       " [518, 2.4563758389261743],\n",
       " [519, 1.9405940594059405],\n",
       " [520, 2.93048128342246],\n",
       " [521, 3.3675213675213675],\n",
       " [522, 3.566265060240964],\n",
       " [523, 3.658119658119658],\n",
       " [524, 3.615546218487395],\n",
       " [525, 3.1904761904761907],\n",
       " [526, 2.5],\n",
       " [527, 4.510416666666667],\n",
       " [528, 2.514705882352941],\n",
       " [529, 3.977777777777778],\n",
       " [530, 3.5],\n",
       " [531, 3.769230769230769],\n",
       " [532, 3.0488431876606685],\n",
       " [533, 2.7339901477832513],\n",
       " [534, 3.835664335664336],\n",
       " [535, 3.8172757475083055],\n",
       " [536, 3.1636363636363636],\n",
       " [537, 3.077294685990338],\n",
       " [538, 3.8222222222222224],\n",
       " [539, 3.760649087221095],\n",
       " [540, 2.2189349112426036],\n",
       " [541, 4.273333333333333],\n",
       " [542, 2.674757281553398],\n",
       " [543, 3.3841642228739004],\n",
       " [544, 2.643410852713178],\n",
       " [545, 2.0],\n",
       " [546, 1.8742857142857143],\n",
       " [547, 2.879032258064516],\n",
       " [548, 2.5474452554744524],\n",
       " [549, 3.821656050955414],\n",
       " [550, 3.0168539325842696],\n",
       " [551, 3.717871485943775],\n",
       " [552, 3.2400756143667295],\n",
       " [553, 3.8734177215189876],\n",
       " [554, 2.6153846153846154],\n",
       " [555, 3.9285714285714284],\n",
       " [556, 4.2272727272727275],\n",
       " [557, 4.5],\n",
       " [558, 2.7037037037037037],\n",
       " [559, 3.0],\n",
       " [560, 3.625],\n",
       " [561, 3.6153846153846154],\n",
       " [562, 3.799163179916318],\n",
       " [563, 3.235294117647059],\n",
       " [564, 2.2666666666666666],\n",
       " [565, 3.1311475409836067],\n",
       " [566, 2.923076923076923],\n",
       " [567, 3.5714285714285716],\n",
       " [568, 3.857142857142857],\n",
       " [569, 2.93],\n",
       " [570, 3.217391304347826],\n",
       " [571, 3.588235294117647],\n",
       " [572, 3.0],\n",
       " [573, 3.5238095238095237],\n",
       " [574, 3.4457142857142857],\n",
       " [575, 2.822429906542056],\n",
       " [576, 3.0],\n",
       " [577, 2.963636363636364],\n",
       " [578, 4.5],\n",
       " [579, 2.0],\n",
       " [580, 3.2419354838709675],\n",
       " [581, 4.049645390070922],\n",
       " [582, 3.0],\n",
       " [583, 3.6785714285714284],\n",
       " [584, 4.0],\n",
       " [585, 2.9066985645933014],\n",
       " [586, 3.1348148148148147],\n",
       " [587, 3.49644128113879],\n",
       " [588, 3.788304959289415],\n",
       " [589, 4.058512646281616],\n",
       " [590, 3.9152308752584424],\n",
       " [591, 2.0],\n",
       " [592, 3.6009783368273935],\n",
       " [593, 4.3518231186966645],\n",
       " [594, 3.8453473132372213],\n",
       " [595, 3.8858490566037736],\n",
       " [596, 3.751004016064257],\n",
       " [597, 3.641491395793499],\n",
       " [598, 4.25],\n",
       " [599, 4.087121212121212],\n",
       " [600, 3.0],\n",
       " [601, 3.0],\n",
       " [602, 4.121951219512195],\n",
       " [603, 3.0],\n",
       " [605, 3.314159292035398],\n",
       " [606, 2.225806451612903],\n",
       " [607, 2.0],\n",
       " [608, 4.254675686430561],\n",
       " [609, 2.7761194029850746],\n",
       " [610, 3.546925566343042],\n",
       " [611, 2.4722222222222223],\n",
       " [612, 2.4050632911392404],\n",
       " [613, 3.6341463414634148],\n",
       " [614, 2.6666666666666665],\n",
       " [615, 4.044776119402985],\n",
       " [616, 3.352517985611511],\n",
       " [617, 3.6470588235294117],\n",
       " [618, 2.111111111111111],\n",
       " [619, 2.59375],\n",
       " [621, 3.7142857142857144],\n",
       " [623, 3.0],\n",
       " [624, 4.0],\n",
       " [626, 2.263157894736842],\n",
       " [627, 3.603305785123967],\n",
       " [628, 3.8969072164948453],\n",
       " [630, 2.857142857142857],\n",
       " [631, 2.08],\n",
       " [632, 4.0],\n",
       " [633, 3.6],\n",
       " [634, 1.6666666666666667],\n",
       " [635, 3.6233766233766236],\n",
       " [637, 2.5428571428571427],\n",
       " [638, 3.210526315789474],\n",
       " [639, 2.6153846153846154],\n",
       " [640, 2.676056338028169],\n",
       " [641, 1.0],\n",
       " [642, 2.0],\n",
       " [643, 2.0],\n",
       " [644, 2.0],\n",
       " [645, 3.6],\n",
       " [647, 3.5532879818594103],\n",
       " [648, 3.432874918140144],\n",
       " [649, 4.1875],\n",
       " [650, 3.4719101123595504],\n",
       " [651, 2.0],\n",
       " [652, 2.888888888888889],\n",
       " [653, 3.2254901960784315],\n",
       " [655, 1.0],\n",
       " [656, 2.5641025641025643],\n",
       " [657, 3.0],\n",
       " [658, 3.0],\n",
       " [659, 3.72],\n",
       " [660, 1.5],\n",
       " [661, 3.4647619047619047],\n",
       " [662, 2.984375],\n",
       " [663, 3.4166666666666665],\n",
       " [664, 3.0],\n",
       " [665, 3.657142857142857],\n",
       " [666, 3.3333333333333335],\n",
       " [667, 2.0425531914893615],\n",
       " [668, 4.404255319148936],\n",
       " [669, 4.173913043478261],\n",
       " [670, 4.410714285714286],\n",
       " [671, 3.6798245614035086],\n",
       " [672, 2.0],\n",
       " [673, 2.619893428063943],\n",
       " [674, 3.0155440414507773],\n",
       " [678, 4.245098039215686],\n",
       " [679, 3.5],\n",
       " [680, 3.359375],\n",
       " [681, 3.933333333333333],\n",
       " [682, 3.5],\n",
       " [684, 1.0],\n",
       " [685, 3.3],\n",
       " [687, 3.0],\n",
       " [688, 2.276995305164319],\n",
       " [690, 2.0],\n",
       " [691, 3.0991735537190084],\n",
       " [692, 2.1132075471698113],\n",
       " [694, 2.645390070921986],\n",
       " [695, 3.1777777777777776],\n",
       " [696, 3.25],\n",
       " [697, 2.552941176470588],\n",
       " [698, 2.2],\n",
       " [700, 3.3241379310344827],\n",
       " [701, 4.0],\n",
       " [702, 3.6666666666666665],\n",
       " [703, 1.6],\n",
       " [704, 2.3095238095238093],\n",
       " [705, 3.8333333333333335],\n",
       " [706, 2.5],\n",
       " [707, 3.0872727272727274],\n",
       " [708, 3.434462444771723],\n",
       " [709, 3.0416666666666665],\n",
       " [710, 2.3333333333333335],\n",
       " [711, 2.5],\n",
       " [712, 3.5],\n",
       " [714, 3.888888888888889],\n",
       " [715, 3.6153846153846154],\n",
       " [716, 2.6785714285714284],\n",
       " [717, 4.0],\n",
       " [718, 3.484848484848485],\n",
       " [719, 2.8619246861924688],\n",
       " [720, 4.426940639269406],\n",
       " [722, 3.814814814814815],\n",
       " [724, 3.0865384615384617],\n",
       " [725, 2.791208791208791],\n",
       " [726, 3.0],\n",
       " [728, 3.7649769585253456],\n",
       " [729, 3.6666666666666665],\n",
       " [730, 1.0],\n",
       " [731, 2.851063829787234],\n",
       " [732, 2.8333333333333335],\n",
       " [733, 3.723134328358209],\n",
       " [734, 3.0],\n",
       " [735, 3.3564356435643563],\n",
       " [736, 3.1738738738738737],\n",
       " [737, 2.03],\n",
       " [741, 4.089171974522293],\n",
       " [742, 2.528735632183908],\n",
       " [743, 2.5700934579439254],\n",
       " [744, 2.0],\n",
       " [745, 4.52054794520548],\n",
       " [746, 4.0],\n",
       " [747, 2.0],\n",
       " [748, 3.1510791366906474],\n",
       " [749, 2.75],\n",
       " [750, 4.4498902706656915],\n",
       " [751, 3.533333333333333],\n",
       " [753, 3.15625],\n",
       " [754, 2.923076923076923],\n",
       " [755, 3.7777777777777777],\n",
       " [756, 3.0],\n",
       " [757, 3.75],\n",
       " [758, 4.0],\n",
       " [759, 4.101694915254237],\n",
       " [760, 3.515151515151515],\n",
       " [761, 2.7886178861788617],\n",
       " [762, 2.184563758389262],\n",
       " [763, 3.0],\n",
       " [764, 3.27027027027027],\n",
       " [765, 2.6315789473684212],\n",
       " [766, 3.57],\n",
       " [767, 3.2083333333333335],\n",
       " [769, 3.25],\n",
       " [771, 3.7777777777777777],\n",
       " [774, 4.0],\n",
       " [775, 3.2222222222222223],\n",
       " [776, 3.0],\n",
       " [778, 3.9600532623169107],\n",
       " [779, 2.6923076923076925],\n",
       " [780, 3.5104046242774567],\n",
       " [781, 3.378640776699029],\n",
       " [782, 2.5517241379310347],\n",
       " [783, 3.223076923076923],\n",
       " [784, 2.72987012987013],\n",
       " [785, 3.4784313725490197],\n",
       " [786, 3.123913043478261],\n",
       " [787, 5.0],\n",
       " [788, 2.9957805907172994],\n",
       " [789, 3.0],\n",
       " [790, 3.0],\n",
       " [791, 3.5],\n",
       " [792, 4.0],\n",
       " [793, 2.6],\n",
       " [796, 3.3333333333333335],\n",
       " [798, 2.7058823529411766],\n",
       " [799, 3.3491124260355027],\n",
       " [800, 4.082539682539682],\n",
       " [801, 3.0991735537190084],\n",
       " [802, 3.496487119437939],\n",
       " [803, 3.6842105263157894],\n",
       " [804, 2.9785407725321886],\n",
       " [805, 3.5901162790697674],\n",
       " [806, 3.1666666666666665],\n",
       " [807, 3.0],\n",
       " [808, 3.395348837209302],\n",
       " [809, 2.5714285714285716],\n",
       " [810, 1.4666666666666666],\n",
       " [811, 3.888888888888889],\n",
       " [813, 2.5106382978723403],\n",
       " [814, 3.0],\n",
       " [815, 2.0],\n",
       " [818, 2.560846560846561],\n",
       " [820, 3.25],\n",
       " [821, 2.0],\n",
       " [823, 3.25],\n",
       " [824, 3.9285714285714284],\n",
       " [826, 1.0],\n",
       " [827, 3.0],\n",
       " [828, 2.9074074074074074],\n",
       " [829, 2.2900763358778624],\n",
       " [830, 2.952542372881356],\n",
       " [831, 3.85],\n",
       " [832, 3.478723404255319],\n",
       " [833, 2.1794871794871793],\n",
       " [834, 2.0],\n",
       " [835, 3.1262135922330097],\n",
       " [836, 2.654008438818565],\n",
       " [837, 3.477064220183486],\n",
       " [838, 3.8802395209580838],\n",
       " [839, 2.214814814814815],\n",
       " [840, 2.56],\n",
       " [841, 3.4],\n",
       " [842, 2.589403973509934],\n",
       " [843, 1.0],\n",
       " [844, 3.5714285714285716],\n",
       " [846, 3.736842105263158],\n",
       " [847, 1.8571428571428572],\n",
       " [848, 3.4358974358974357],\n",
       " [849, 2.5107632093933465],\n",
       " [850, 3.6666666666666665],\n",
       " [851, 3.4960629921259843],\n",
       " [852, 3.221138211382114],\n",
       " [853, 4.0],\n",
       " [854, 3.625],\n",
       " [858, 4.524966261808367],\n",
       " [859, 2.0],\n",
       " [860, 3.6],\n",
       " [861, 3.5128205128205128],\n",
       " [862, 3.6451612903225805],\n",
       " [863, 3.5],\n",
       " [864, 3.5833333333333335],\n",
       " [865, 2.0],\n",
       " [866, 3.8234265734265733],\n",
       " [867, 2.2083333333333335],\n",
       " [868, 3.0],\n",
       " [869, 3.0952380952380953],\n",
       " [870, 2.183673469387755],\n",
       " [872, 3.0],\n",
       " [874, 3.125],\n",
       " [875, 3.3863636363636362],\n",
       " [876, 2.857142857142857],\n",
       " [877, 3.2916666666666665],\n",
       " [878, 4.0],\n",
       " [879, 2.827004219409283],\n",
       " [880, 2.200617283950617],\n",
       " [881, 2.6233766233766236],\n",
       " [882, 2.711864406779661],\n",
       " [884, 3.0],\n",
       " [885, 2.5813953488372094],\n",
       " [886, 2.9423076923076925],\n",
       " [887, 2.5],\n",
       " [888, 2.2083333333333335],\n",
       " [889, 2.5],\n",
       " [891, 2.360655737704918],\n",
       " [892, 3.861842105263158],\n",
       " [893, 3.6956521739130435],\n",
       " [895, 1.0],\n",
       " [896, 3.4313725490196076],\n",
       " [897, 3.7551020408163267],\n",
       " [898, 4.3006872852233675],\n",
       " [899, 4.2836218375499335],\n",
       " [900, 3.8513119533527695],\n",
       " [901, 3.6436781609195403],\n",
       " [902, 3.908284023668639],\n",
       " [903, 4.27292817679558],\n",
       " [904, 4.476190476190476],\n",
       " [905, 4.280748663101604],\n",
       " [906, 4.096256684491979],\n",
       " [907, 3.9238095238095236],\n",
       " [908, 4.38403041825095],\n",
       " [909, 4.127098321342926],\n",
       " [910, 4.300480769230769],\n",
       " [911, 4.183006535947713],\n",
       " [912, 4.412822049131217],\n",
       " [913, 4.395973154362416],\n",
       " [914, 4.154088050314465],\n",
       " [915, 3.9643835616438357],\n",
       " [916, 4.216470588235294],\n",
       " [917, 3.675324675324675],\n",
       " [918, 3.7936507936507935],\n",
       " [919, 4.247962747380675],\n",
       " [920, 3.9974048442906573],\n",
       " [921, 3.8940397350993377],\n",
       " [922, 4.491489361702127],\n",
       " [923, 4.388888888888889],\n",
       " [924, 4.068764568764569],\n",
       " [925, 3.25],\n",
       " [926, 4.255583126550868],\n",
       " [927, 3.9761904761904763],\n",
       " [928, 4.204663212435233],\n",
       " [929, 3.78494623655914],\n",
       " [930, 4.29438202247191],\n",
       " [931, 3.912621359223301],\n",
       " [932, 3.9523809523809526],\n",
       " [933, 4.10158013544018],\n",
       " [934, 3.6578947368421053],\n",
       " [935, 3.6338028169014085],\n",
       " [936, 4.075757575757576],\n",
       " [937, 3.75],\n",
       " [938, 3.620320855614973],\n",
       " [939, 3.1818181818181817],\n",
       " [940, 3.9735449735449735],\n",
       " [941, 3.704761904761905],\n",
       " [942, 4.2020547945205475],\n",
       " [943, 3.982456140350877],\n",
       " [944, 3.7938144329896906],\n",
       " [945, 4.147410358565737],\n",
       " [946, 3.8509316770186337],\n",
       " [947, 4.1063829787234045],\n",
       " [948, 3.753846153846154],\n",
       " [949, 3.9767441860465116],\n",
       " [950, 4.239726027397261],\n",
       " [951, 4.249370277078086],\n",
       " [952, 3.6022304832713754],\n",
       " [953, 4.299039780521262],\n",
       " [954, 4.240208877284595],\n",
       " [955, 4.169491525423729],\n",
       " [956, 3.55],\n",
       " [957, 3.2432432432432434],\n",
       " [958, 3.3846153846153846],\n",
       " [959, 3.7413793103448274],\n",
       " [960, 3.45],\n",
       " [961, 3.4782608695652173],\n",
       " [962, 3.5454545454545454],\n",
       " [963, 3.574074074074074],\n",
       " [964, 3.392156862745098],\n",
       " [965, 4.075098814229249],\n",
       " [966, 4.0],\n",
       " [967, 3.260869565217391],\n",
       " [968, 3.6713286713286712],\n",
       " [969, 4.251655629139073],\n",
       " [970, 3.4054054054054053],\n",
       " [971, 4.047970479704797],\n",
       " [972, 3.1666666666666665],\n",
       " [973, 3.9146341463414633],\n",
       " [974, 3.75],\n",
       " [975, 1.5],\n",
       " [976, 3.5714285714285716],\n",
       " [977, 2.0],\n",
       " [978, 3.94],\n",
       " [980, 2.8],\n",
       " [981, 2.75],\n",
       " [982, 3.6790123456790123],\n",
       " [984, 2.6666666666666665],\n",
       " [985, 3.75],\n",
       " [986, 3.603448275862069],\n",
       " [987, 2.9],\n",
       " [988, 3.3768115942028984],\n",
       " [989, 5.0],\n",
       " [990, 2.574074074074074],\n",
       " [991, 3.523529411764706],\n",
       " [992, 2.6],\n",
       " [993, 3.111111111111111],\n",
       " [994, 4.095555555555555],\n",
       " [996, 2.90625],\n",
       " [997, 3.357142857142857],\n",
       " [998, 3.010752688172043],\n",
       " [999, 3.2832167832167833],\n",
       " [1000, 3.05],\n",
       " [1002, 4.25],\n",
       " [1003, 2.9421487603305785],\n",
       " [1004, 2.6633663366336635],\n",
       " [1005, 2.3732394366197185],\n",
       " [1006, 3.08974358974359],\n",
       " [1007, 2.978448275862069],\n",
       " [1008, 3.329896907216495],\n",
       " [1009, 3.185567010309278],\n",
       " [1010, 3.268595041322314],\n",
       " [1011, 2.725925925925926],\n",
       " [1012, 3.7043189368770766],\n",
       " [1013, 3.565891472868217],\n",
       " [1014, 3.4044117647058822],\n",
       " [1015, 3.3461538461538463],\n",
       " [1016, 3.217948717948718],\n",
       " [1017, 3.5869565217391304],\n",
       " [1018, 3.252032520325203],\n",
       " [1019, 3.7026086956521738],\n",
       " [1020, 3.239795918367347],\n",
       " [1021, 2.769230769230769],\n",
       " [1022, 3.755632582322357],\n",
       " [1023, 3.986425339366516],\n",
       " [1024, 3.246031746031746],\n",
       " [1025, 3.6109215017064846],\n",
       " [1026, 3.625],\n",
       " [1027, 3.1627906976744184],\n",
       " [1028, 3.894164193867458],\n",
       " [1029, 3.688380281690141],\n",
       " [1030, 3.0773993808049536],\n",
       " [1031, 3.479623824451411],\n",
       " [1032, 3.697142857142857],\n",
       " [1033, 3.4494773519163764],\n",
       " [1034, 3.6449704142011834],\n",
       " [1035, 3.931972789115646],\n",
       " [1036, 4.121848739495798],\n",
       " [1037, 2.6601626016260163],\n",
       " [1038, 3.272727272727273],\n",
       " [1039, 3.6666666666666665],\n",
       " [1040, 3.0],\n",
       " [1041, 4.037974683544304],\n",
       " [1042, 3.481060606060606],\n",
       " [1043, 2.8425925925925926],\n",
       " [1044, 3.2857142857142856],\n",
       " [1046, 4.066666666666666],\n",
       " [1047, 3.4838709677419355],\n",
       " [1049, 3.328159645232816],\n",
       " [1050, 3.8219178082191783],\n",
       " [1051, 3.4183673469387754],\n",
       " [1053, 2.914285714285714],\n",
       " [1054, 3.308641975308642],\n",
       " [1055, 2.736842105263158],\n",
       " [1056, 3.54],\n",
       " [1057, 3.5583941605839415],\n",
       " [1058, 3.272727272727273],\n",
       " [1059, 3.4008350730688934],\n",
       " [1060, 3.94147582697201],\n",
       " [1061, 3.550802139037433],\n",
       " [1062, 2.5],\n",
       " [1063, 3.1538461538461537],\n",
       " [1064, 2.8947368421052633],\n",
       " [1066, 4.1657142857142855],\n",
       " [1067, 3.782608695652174],\n",
       " [1068, 3.6857142857142855],\n",
       " ...]"
      ]
     },
     "execution_count": 193,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "movie_mean_list = []\n",
    "for i in item_id:\n",
    "    movie_mean = movie[movie[:,1]==i][:,2].mean()\n",
    "    movie_mean_list.append([i,movie_mean])\n",
    "movie_mean_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 195,
   "id": "7368e284",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1000209"
      ]
     },
     "execution_count": 195,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "movie_id = np.array(movie[:,1])\n",
    "movie_id"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 196,
   "id": "450ac84b",
   "metadata": {},
   "outputs": [
    {
     "ename": "KeyboardInterrupt",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
      "Input \u001b[1;32mIn [196]\u001b[0m, in \u001b[0;36m<cell line: 2>\u001b[1;34m()\u001b[0m\n\u001b[0;32m      1\u001b[0m movie_mean_list \u001b[38;5;241m=\u001b[39m []\n\u001b[0;32m      2\u001b[0m \u001b[38;5;28;01mfor\u001b[39;00m i \u001b[38;5;129;01min\u001b[39;00m movie_id:\n\u001b[1;32m----> 3\u001b[0m     movie_mean \u001b[38;5;241m=\u001b[39m movie[\u001b[43mmovie\u001b[49m\u001b[43m[\u001b[49m\u001b[43m:\u001b[49m\u001b[43m,\u001b[49m\u001b[38;5;241;43m1\u001b[39;49m\u001b[43m]\u001b[49m\u001b[38;5;241;43m==\u001b[39;49m\u001b[43mi\u001b[49m][:,\u001b[38;5;241m2\u001b[39m]\u001b[38;5;241m.\u001b[39mmean()\n\u001b[0;32m      4\u001b[0m     movie_mean_list\u001b[38;5;241m.\u001b[39mappend([i,movie_mean])\n\u001b[0;32m      5\u001b[0m movie_mean_list\n",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m: "
     ]
    }
   ],
   "source": [
    "movie_mean_list = []\n",
    "for i in movie_id:\n",
    "    movie_mean = movie[movie[:,1]==i][:,2].mean()\n",
    "    movie_mean_list.append([i,movie_mean])\n",
    "movie_mean_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 198,
   "id": "18b5e232",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "130384"
      ]
     },
     "execution_count": 198,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(movie_mean_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e2dbf1bc",
   "metadata": {},
   "outputs": [],
   "source": [
    "0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "46e5e582",
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
   "toc_position": {
    "height": "calc(100% - 180px)",
    "left": "10px",
    "top": "150px",
    "width": "245.76px"
   },
   "toc_section_display": true,
   "toc_window_display": true
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
