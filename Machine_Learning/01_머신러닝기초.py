{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "62bbc5ec",
   "metadata": {},
   "source": [
    "# 머신러닝 학습 방법\n",
    "\n",
    "- 거리 기반 학습\n",
    "- 수식 기반 학습\n",
    "- 논리 기반 학습\n",
    "- 확률 기반 학습 (나이브베이즈)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a54ae453",
   "metadata": {},
   "source": [
    "## 거리 기반 학습으로 AND 논리를 학습하는 모델을 만들자\n",
    "- 머신러닝 모델 종류 : KNN , SVM"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "6f5288ac",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[[0, 0, 0], [0, 1, 0], [0, 1, 0], [1, 1, 1]]"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# AND 논리 선언\n",
    "data = [[0,0,0],\n",
    "        [0,1,0],\n",
    "        [0,1,0],\n",
    "        [1,1,1]]\n",
    "data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "323b87ff",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "0\n",
      "0\n",
      "1\n"
     ]
    }
   ],
   "source": [
    "# 입력된 데이터(x1, x2)에서 가장 가까운 데이터의 라벨을 출력\n",
    "def distanceML(x1,x2):\n",
    "    # 최종 결과값\n",
    "    result = 0\n",
    "    # 최소 거리를 비교하기 위한 값\n",
    "    minDis = 99\n",
    "    \n",
    "    # 전체 데이터에서 한 행씩 데이터를 가져온다\n",
    "    for row in data:\n",
    "        # 특성 데이터와 라벨 데이터를 분리   # 특성 데이터는 거의 대문자\n",
    "        X = row[0:2] \n",
    "        y = row[2]\n",
    "        #print(X,y)\n",
    "        \n",
    "        # 입력된 데이터 (x1, x2)와 각 특성데이터간의 거리 계산\n",
    "        # abs : 절대값을 계산 (음수를 없애기 위해서 - 거리는 음수가 없기때문)\n",
    "        d = abs(x1 - X[0]) + abs(x2 - X[1])\n",
    "        \n",
    "        # 거리가 최소인 데이터를 검색\n",
    "        if minDis > d:\n",
    "            minDis = d\n",
    "            result = y\n",
    "    # 거리가 가장 작은 데이터의 라벨값을 반환\n",
    "    return result\n",
    "        \n",
    "print(distanceML(0,0))\n",
    "print(distanceML(0,1))\n",
    "print(distanceML(1,0))\n",
    "print(distanceML(1,1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "2b63a38d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "정상\n"
     ]
    }
   ],
   "source": [
    "data = [[150,40,'저체중'],\n",
    "         [200,100,'비만'],\n",
    "         [180,150,'비만'],\n",
    "        [160,40,'저체중'],\n",
    "        [170,70,'정상']]\n",
    "data\n",
    "print(distanceML(178,83))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b330f523",
   "metadata": {},
   "source": [
    "## 수식 기반 학습으로 AND 논리를 학습하는 모델을 만들자\n",
    "\n",
    "- Linear Regression (선형회귀), Ridge, Lasso\n",
    "- Logistic Regression"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "1d3856cc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[[0, 0, 0], [0, 1, 0], [0, 1, 0], [1, 1, 1]]"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# AND 논리 선언\n",
    "data = [[0,0,0],\n",
    "        [0,1,0],\n",
    "        [0,1,0],\n",
    "        [1,1,1]]\n",
    "data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "282f486d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "0\n",
      "0\n",
      "1\n"
     ]
    }
   ],
   "source": [
    "def andML(x1, x2):\n",
    "    w1,w2,b = 1,1,-1   # 여러분이 직접 맞춰보세요 (-1.0과 1.0사이 값)\n",
    "    \n",
    "    # and 논리를 만드는 수식\n",
    "    temp = w1 * x1 + w2 * x2 + b\n",
    "    \n",
    "    if temp <= 0.5 :\n",
    "        return 0\n",
    "    else:\n",
    "        return 1\n",
    "    \n",
    "print(andML(0,0))\n",
    "print(andML(0,1))\n",
    "print(andML(1,0))\n",
    "print(andML(1,1))\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8d739acb",
   "metadata": {},
   "source": [
    "## 논리 기반 학습으로 AND논리를 학습하는 모델을 만들자\n",
    "\n",
    "- Decision Tree (의사결정)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "906c1b15",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "0\n",
      "0\n",
      "1\n"
     ]
    }
   ],
   "source": [
    "def logicalML(x1,x2):\n",
    "    if x1==0 and x2==0:\n",
    "        return 0\n",
    "    elif x1==0 and x2==1:\n",
    "        return 0\n",
    "    elif x1==1 and x2==0:\n",
    "        return 0\n",
    "    elif x1==1 and x2==1:\n",
    "        return 1\n",
    "    \n",
    "print(logicalML(0,0))\n",
    "print(logicalML(1,0))\n",
    "print(logicalML(0,1))\n",
    "print(logicalML(1,1))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "dc288ed0",
   "metadata": {},
   "source": [
    "## 앙상블 (Ensemble)\n",
    "\n",
    "- Random Forest, Adaboost, GBM, Xgboost, LightGBM 등등\n",
    "\n",
    "- 여러 개의 모델을 사용해서 투표나 확률을 계산하는 방식 -voting, stacking\n",
    "- 데이터를 쪼개서 적용하는 방식 - bagging, boosting"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fe25e194",
   "metadata": {},
   "source": [
    "# Scikit-learn 프레임워크를 활용한 학습\n",
    "\n",
    "- Scikit-learn 프레임워크 : 머신러닝과 관련된 데이터, 모델, 함수 등을 다양하게 제공하는 가장 많이 활용되는 머신러닝 프레임워크"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "ef0fa377",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>A</th>\n",
       "      <th>B</th>\n",
       "      <th>AND</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   A  B  AND\n",
       "0  0  0    0\n",
       "1  0  1    0\n",
       "2  1  0    0\n",
       "3  1  1    1"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# AND 논리 선언\n",
    "data = [[0,0,0],\n",
    "        [0,1,0],\n",
    "        [1,0,0],\n",
    "        [1,1,1]]\n",
    "\n",
    "# pandas 데이터로 변환\n",
    "import pandas as pd\n",
    "df_data = pd.DataFrame(data, columns=['A','B','AND'])\n",
    "df_data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "a115215d",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "# 특성데이터와 라벨데이터로 분리\n",
    "X = df_data.loc[:,:'B']\n",
    "y = df_data.loc[:,'AND'] # Series 데이터\n",
    "y1 = df_data.iloc[:,2:] # DataFrame 데이터 나중에 오류남"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "8e1f7661",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>A</th>\n",
       "      <th>B</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   A  B\n",
       "0  0  0\n",
       "1  0  1\n",
       "2  1  0\n",
       "3  1  1"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "fd1400c3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(4,)\n",
      "(4, 1)\n"
     ]
    }
   ],
   "source": [
    "print(y.shape)\n",
    "print(y1.shape) # 크기가 다름 주로 인덱싱으로 자르려고 해야함 슬라이싱X"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "e73e7e7b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "KNeighborsClassifier(n_neighbors=1)"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# KNN 모델을 로드\n",
    "from sklearn.neighbors import KNeighborsClassifier\n",
    "\n",
    "# 모델 선언\n",
    "# n_neighbors : 가까이에 있는 참고하는 데이터의 수 \n",
    "knn_model = KNeighborsClassifier(n_neighbors=1)\n",
    "\n",
    "# 특성데이터와 라벨데이터를 입력해서 훈련 - fit(특성데이터, 라벨데이터)\n",
    "knn_model.fit(X,y)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "12151f4a",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\AI\\Anaconda3\\lib\\site-packages\\sklearn\\base.py:450: UserWarning: X does not have valid feature names, but KNeighborsClassifier was fitted with feature names\n",
      "  warnings.warn(\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "array([1, 0, 0, 0], dtype=int64)"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 새로운 데이터를 입력해서 예측\n",
    "new_X = [[1,1],[0,1],[0,0],[1,0]]\n",
    "new_y = [1,0,0,0]\n",
    "\n",
    "# predict() : 생성된 모델을 이용해 새로운 특성데이터의 라벨데이터를 예측\n",
    "pred_y = knn_model.predict(new_X)\n",
    "\n",
    "pred_y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "78962922",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1.0\n",
      "1.0\n"
     ]
    }
   ],
   "source": [
    "# 평가 (score, accuracy_score) - 정확도 구하는 함수\n",
    "# score() : 훈련하고나서 특성데이터와 라벨데이터로 정확도를 계산\n",
    "# accuracy_score() : 예측한 라벨과 원래 라벨을 비교하여 정확도를 계산\n",
    "\n",
    "from sklearn.metrics import accuracy_score\n",
    "\n",
    "print(knn_model.score(X,y))\n",
    "print(accuracy_score(pred_y, new_y))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "32b4845b",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a132e04e",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cdc69aec",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "796355c4",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1d49848e",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "26bd4779",
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
