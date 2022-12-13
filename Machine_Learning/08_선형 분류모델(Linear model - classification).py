{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "85bf5de8",
   "metadata": {},
   "source": [
    "### 목표\n",
    "- 손글씨를 분류하는 모델을 만들어보자.\n",
    "- 예측의 불확실성을 확인해보자.\n",
    "- 이미지 데이터에 형태를 이해.\n",
    "- 다양한 분류평가지표를 이해하자."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "011035df",
   "metadata": {},
   "source": [
    "### 데이터 로딩"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "db2b3ce8",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "from sklearn.model_selection import train_test_split"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "9edc97a7",
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
       "      <th>label</th>\n",
       "      <th>pixel0</th>\n",
       "      <th>pixel1</th>\n",
       "      <th>pixel2</th>\n",
       "      <th>pixel3</th>\n",
       "      <th>pixel4</th>\n",
       "      <th>pixel5</th>\n",
       "      <th>pixel6</th>\n",
       "      <th>pixel7</th>\n",
       "      <th>pixel8</th>\n",
       "      <th>...</th>\n",
       "      <th>pixel774</th>\n",
       "      <th>pixel775</th>\n",
       "      <th>pixel776</th>\n",
       "      <th>pixel777</th>\n",
       "      <th>pixel778</th>\n",
       "      <th>pixel779</th>\n",
       "      <th>pixel780</th>\n",
       "      <th>pixel781</th>\n",
       "      <th>pixel782</th>\n",
       "      <th>pixel783</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 785 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "   label  pixel0  pixel1  pixel2  pixel3  pixel4  pixel5  pixel6  pixel7  \\\n",
       "0      1       0       0       0       0       0       0       0       0   \n",
       "1      0       0       0       0       0       0       0       0       0   \n",
       "2      1       0       0       0       0       0       0       0       0   \n",
       "3      4       0       0       0       0       0       0       0       0   \n",
       "4      0       0       0       0       0       0       0       0       0   \n",
       "\n",
       "   pixel8  ...  pixel774  pixel775  pixel776  pixel777  pixel778  pixel779  \\\n",
       "0       0  ...         0         0         0         0         0         0   \n",
       "1       0  ...         0         0         0         0         0         0   \n",
       "2       0  ...         0         0         0         0         0         0   \n",
       "3       0  ...         0         0         0         0         0         0   \n",
       "4       0  ...         0         0         0         0         0         0   \n",
       "\n",
       "   pixel780  pixel781  pixel782  pixel783  \n",
       "0         0         0         0         0  \n",
       "1         0         0         0         0  \n",
       "2         0         0         0         0  \n",
       "3         0         0         0         0  \n",
       "4         0         0         0         0  \n",
       "\n",
       "[5 rows x 785 columns]"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "digit_train = pd.read_csv('./data/digit_train.csv')\n",
    "digit_train.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "a156abe6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.image.AxesImage at 0x1a089a68130>"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# 이미지 확인\n",
    "img = digit_train.iloc[40006,1:]\n",
    "img_reshape = img.values.reshape(28,28)\n",
    "plt.imshow(img_reshape, cmap='gray')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "2447e748",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# 데이터 분포 확인\n",
    "plt.hist(img)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "d0b5b055",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1    4684\n",
       "7    4401\n",
       "3    4351\n",
       "9    4188\n",
       "2    4177\n",
       "6    4137\n",
       "0    4132\n",
       "4    4072\n",
       "8    4063\n",
       "5    3795\n",
       "Name: label, dtype: int64"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 손글씨(정답) 종류\n",
    "digit_train['label'].value_counts()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e3f5ac50",
   "metadata": {},
   "source": [
    "#### 훈련용 데이터와 검증용 데이터 분리"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "57f2c1a5",
   "metadata": {},
   "outputs": [],
   "source": [
    "X = digit_train.iloc[:,1:]\n",
    "y = digit_train.iloc[:,0]\n",
    "\n",
    "X_train, X_test, y_train, y_test = train_test_split(X,y,\n",
    "                                 random_state=728,\n",
    "                                 test_size=0.3)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "71ed4fa4",
   "metadata": {},
   "source": [
    "#### 모델링\n",
    "- KNN\n",
    "- Decision Tree\n",
    "- LogisticRegression\n",
    "- SVM"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "8d4cfeeb",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.neighbors import KNeighborsClassifier\n",
    "from sklearn.tree import DecisionTreeClassifier\n",
    "from sklearn.linear_model import LogisticRegression\n",
    "from sklearn.svm import LinearSVC # 분류용 SVM 모델\n",
    "from sklearn.linear_model import SGDClassifier # 경사하강법 적용 선형분류모델"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "909a46d3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "((29400, 784), (29400,), (12600, 784), (12600,))"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_train.shape, y_train.shape, X_test.shape , y_test.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "e9dce481",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "KNN 테스트 정확도 : 0.9671428571428572\n",
      "tree 테스트 정확도 : 0.848015873015873\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\AI\\Anaconda3\\lib\\site-packages\\sklearn\\linear_model\\_logistic.py:814: ConvergenceWarning: lbfgs failed to converge (status=1):\n",
      "STOP: TOTAL NO. of ITERATIONS REACHED LIMIT.\n",
      "\n",
      "Increase the number of iterations (max_iter) or scale the data as shown in:\n",
      "    https://scikit-learn.org/stable/modules/preprocessing.html\n",
      "Please also refer to the documentation for alternative solver options:\n",
      "    https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression\n",
      "  n_iter_i = _check_optimize_result(\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Logis 테스트 정확도 : 0.9137301587301587\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\AI\\Anaconda3\\lib\\site-packages\\sklearn\\svm\\_base.py:1206: ConvergenceWarning: Liblinear failed to converge, increase the number of iterations.\n",
      "  warnings.warn(\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "svc 테스트 정확도 : 0.8717460317460317\n",
      "SGDC 테스트 정확도 : 0.8796825396825397\n"
     ]
    }
   ],
   "source": [
    "knn_model = KNeighborsClassifier()\n",
    "knn_model.fit(X_train,y_train)\n",
    "print(\"KNN 테스트 정확도 :\",knn_model.score(X_test,y_test))\n",
    "\n",
    "model_tree = DecisionTreeClassifier()\n",
    "model_tree.fit(X_train,y_train)\n",
    "print(\"tree 테스트 정확도 :\",model_tree.score(X_test,y_test))\n",
    "\n",
    "model_Logis = LogisticRegression()\n",
    "model_Logis.fit(X_train,y_train)\n",
    "print(\"Logis 테스트 정확도 :\",model_Logis.score(X_test,y_test))\n",
    "\n",
    "model_svc = LinearSVC()\n",
    "model_svc.fit(X_train,y_train)\n",
    "print(\"svc 테스트 정확도 :\",model_svc.score(X_test,y_test))\n",
    "\n",
    "model_SGDC = SGDClassifier()\n",
    "model_SGDC.fit(X_train,y_train)\n",
    "print(\"SGDC 테스트 정확도 :\",model_SGDC.score(X_test,y_test))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ba307293",
   "metadata": {},
   "source": [
    "#### 교차검증 활용 점수 확인"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "bf49f6de",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\AI\\Anaconda3\\lib\\site-packages\\sklearn\\linear_model\\_logistic.py:814: ConvergenceWarning: lbfgs failed to converge (status=1):\n",
      "STOP: TOTAL NO. of ITERATIONS REACHED LIMIT.\n",
      "\n",
      "Increase the number of iterations (max_iter) or scale the data as shown in:\n",
      "    https://scikit-learn.org/stable/modules/preprocessing.html\n",
      "Please also refer to the documentation for alternative solver options:\n",
      "    https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression\n",
      "  n_iter_i = _check_optimize_result(\n",
      "C:\\Users\\AI\\Anaconda3\\lib\\site-packages\\sklearn\\linear_model\\_logistic.py:814: ConvergenceWarning: lbfgs failed to converge (status=1):\n",
      "STOP: TOTAL NO. of ITERATIONS REACHED LIMIT.\n",
      "\n",
      "Increase the number of iterations (max_iter) or scale the data as shown in:\n",
      "    https://scikit-learn.org/stable/modules/preprocessing.html\n",
      "Please also refer to the documentation for alternative solver options:\n",
      "    https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression\n",
      "  n_iter_i = _check_optimize_result(\n",
      "C:\\Users\\AI\\Anaconda3\\lib\\site-packages\\sklearn\\linear_model\\_logistic.py:814: ConvergenceWarning: lbfgs failed to converge (status=1):\n",
      "STOP: TOTAL NO. of ITERATIONS REACHED LIMIT.\n",
      "\n",
      "Increase the number of iterations (max_iter) or scale the data as shown in:\n",
      "    https://scikit-learn.org/stable/modules/preprocessing.html\n",
      "Please also refer to the documentation for alternative solver options:\n",
      "    https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression\n",
      "  n_iter_i = _check_optimize_result(\n",
      "C:\\Users\\AI\\Anaconda3\\lib\\site-packages\\sklearn\\svm\\_base.py:1206: ConvergenceWarning: Liblinear failed to converge, increase the number of iterations.\n",
      "  warnings.warn(\n",
      "C:\\Users\\AI\\Anaconda3\\lib\\site-packages\\sklearn\\svm\\_base.py:1206: ConvergenceWarning: Liblinear failed to converge, increase the number of iterations.\n",
      "  warnings.warn(\n",
      "C:\\Users\\AI\\Anaconda3\\lib\\site-packages\\sklearn\\svm\\_base.py:1206: ConvergenceWarning: Liblinear failed to converge, increase the number of iterations.\n",
      "  warnings.warn(\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "knn 최종점수 : 0.9642142857142857\n",
      "tree 최종점수 : 0.8484047619047619\n",
      "Logis 최종점수 : 0.9128095238095238\n",
      "svc 최종점수 : 0.8597619047619047\n",
      "SGDC 최종점수 : 0.8685952380952382\n"
     ]
    }
   ],
   "source": [
    "from sklearn.model_selection import cross_val_score\n",
    "import numpy as np\n",
    "\n",
    "knn_model2=KNeighborsClassifier()\n",
    "model_tree2=DecisionTreeClassifier()\n",
    "model_Logis2=LogisticRegression()\n",
    "model_svc2=LinearSVC()\n",
    "model_SGDC2=SGDClassifier()\n",
    "\n",
    "\n",
    "knn_score = cross_val_score(knn_model2,X,y, cv=3)\n",
    "tree_score = cross_val_score(model_tree2,X,y, cv=3)\n",
    "Logis_score = cross_val_score(model_Logis2,X,y, cv=3)\n",
    "svc_score = cross_val_score(model_svc2,X,y, cv=3)\n",
    "SGDC_score = cross_val_score(model_SGDC2,X,y, cv=3)\n",
    "\n",
    "\n",
    "print(\"knn 최종점수 :\",np.mean(knn_score))\n",
    "print(\"tree 최종점수 :\",np.mean(tree_score))\n",
    "print(\"Logis 최종점수 :\",np.mean(Logis_score))\n",
    "print(\"svc 최종점수 :\",np.mean(svc_score))\n",
    "print(\"SGDC 최종점수 :\",np.mean(SGDC_score))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "58017a78",
   "metadata": {},
   "source": [
    "#### 스케일링 추가\n",
    "- minmax 스케일러 활용"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "d8e51a06",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.preprocessing import MinMaxScaler"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "7c4521c3",
   "metadata": {},
   "outputs": [],
   "source": [
    "minmax_scaler = MinMaxScaler()\n",
    "X_scaled = minmax_scaler.fit(X).transform(X)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "028a3f57",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\AI\\Anaconda3\\lib\\site-packages\\sklearn\\linear_model\\_logistic.py:814: ConvergenceWarning: lbfgs failed to converge (status=1):\n",
      "STOP: TOTAL NO. of ITERATIONS REACHED LIMIT.\n",
      "\n",
      "Increase the number of iterations (max_iter) or scale the data as shown in:\n",
      "    https://scikit-learn.org/stable/modules/preprocessing.html\n",
      "Please also refer to the documentation for alternative solver options:\n",
      "    https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression\n",
      "  n_iter_i = _check_optimize_result(\n",
      "C:\\Users\\AI\\Anaconda3\\lib\\site-packages\\sklearn\\linear_model\\_logistic.py:814: ConvergenceWarning: lbfgs failed to converge (status=1):\n",
      "STOP: TOTAL NO. of ITERATIONS REACHED LIMIT.\n",
      "\n",
      "Increase the number of iterations (max_iter) or scale the data as shown in:\n",
      "    https://scikit-learn.org/stable/modules/preprocessing.html\n",
      "Please also refer to the documentation for alternative solver options:\n",
      "    https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression\n",
      "  n_iter_i = _check_optimize_result(\n",
      "C:\\Users\\AI\\Anaconda3\\lib\\site-packages\\sklearn\\linear_model\\_logistic.py:814: ConvergenceWarning: lbfgs failed to converge (status=1):\n",
      "STOP: TOTAL NO. of ITERATIONS REACHED LIMIT.\n",
      "\n",
      "Increase the number of iterations (max_iter) or scale the data as shown in:\n",
      "    https://scikit-learn.org/stable/modules/preprocessing.html\n",
      "Please also refer to the documentation for alternative solver options:\n",
      "    https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression\n",
      "  n_iter_i = _check_optimize_result(\n",
      "C:\\Users\\AI\\Anaconda3\\lib\\site-packages\\sklearn\\svm\\_base.py:1206: ConvergenceWarning: Liblinear failed to converge, increase the number of iterations.\n",
      "  warnings.warn(\n",
      "C:\\Users\\AI\\Anaconda3\\lib\\site-packages\\sklearn\\svm\\_base.py:1206: ConvergenceWarning: Liblinear failed to converge, increase the number of iterations.\n",
      "  warnings.warn(\n",
      "C:\\Users\\AI\\Anaconda3\\lib\\site-packages\\sklearn\\svm\\_base.py:1206: ConvergenceWarning: Liblinear failed to converge, increase the number of iterations.\n",
      "  warnings.warn(\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "knn 최종점수 : 0.9641904761904762\n",
      "tree 최종점수 : 0.8471666666666667\n",
      "Logis 최종점수 : 0.9162857142857144\n",
      "svc 최종점수 : 0.9077619047619048\n",
      "SGDC 최종점수 : 0.9073095238095238\n"
     ]
    }
   ],
   "source": [
    "knn_model3=KNeighborsClassifier()\n",
    "model_tree3=DecisionTreeClassifier()\n",
    "model_Logis3=LogisticRegression()\n",
    "model_svc3=LinearSVC()\n",
    "model_SGDC3=SGDClassifier()\n",
    "\n",
    "\n",
    "knn_score = cross_val_score(knn_model3,X_scaled,y, cv=3)\n",
    "tree_score = cross_val_score(model_tree3,X_scaled,y, cv=3)\n",
    "Logis_score = cross_val_score(model_Logis3,X_scaled,y, cv=3)\n",
    "svc_score = cross_val_score(model_svc3,X_scaled,y, cv=3)\n",
    "SGDC_score = cross_val_score(model_SGDC3,X_scaled,y, cv=3)\n",
    "\n",
    "\n",
    "print(\"knn 최종점수 :\",np.mean(knn_score))\n",
    "print(\"tree 최종점수 :\",np.mean(tree_score))\n",
    "print(\"Logis 최종점수 :\",np.mean(Logis_score))\n",
    "print(\"svc 최종점수 :\",np.mean(svc_score))\n",
    "print(\"SGDC 최종점수 :\",np.mean(SGDC_score))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "18ea7277",
   "metadata": {},
   "source": [
    "### 예측의 불확실성 확인\n",
    "- 분류모델의 예측 결과를 정하기전에 항상 확률을 계산한다.\n",
    "- 분류모델이 예측한 값이 같더라도 확신의 정도(불확실성)가 전부 다르다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "41a308fc",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\AI\\Anaconda3\\lib\\site-packages\\sklearn\\linear_model\\_logistic.py:814: ConvergenceWarning: lbfgs failed to converge (status=1):\n",
      "STOP: TOTAL NO. of ITERATIONS REACHED LIMIT.\n",
      "\n",
      "Increase the number of iterations (max_iter) or scale the data as shown in:\n",
      "    https://scikit-learn.org/stable/modules/preprocessing.html\n",
      "Please also refer to the documentation for alternative solver options:\n",
      "    https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression\n",
      "  n_iter_i = _check_optimize_result(\n"
     ]
    }
   ],
   "source": [
    "Logi_model4 = LogisticRegression()\n",
    "Logi_model4.fit(X_train,y_train)\n",
    "pre = Logi_model4.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "d36d0442",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([7, 8, 0, ..., 1, 8, 6], dtype=int64)"
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pre"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "92c2df2b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([3.11558278e-04, 6.24913195e-16, 1.44809349e-08, 3.34688120e-05,\n",
       "       2.29328889e-06, 3.77046576e-02, 2.90272570e-08, 6.88094921e-01,\n",
       "       3.56026156e-04, 2.73497032e-01])"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pre_proba = Logi_model4.predict_proba(X_test) # predict_proba : 확률을 볼수있음 7일확률 68%, 9일확률 27%\n",
    "pre_proba[0]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "dbc7fb09",
   "metadata": {},
   "source": [
    "### 모델 평가\n",
    "- 정확도 : 전체중에서 정확히 맞춘 비율\n",
    "- 오차행렬\n",
    "- 정밀도\n",
    "- 재현율\n",
    "- F1 스코어\n",
    "- ROC AUC"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "e011a882",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.metrics import confusion_matrix # 오차행렬\n",
    "from sklearn.metrics import classification_report # 분류평가지표를 리포팅"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "53fb22a0",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1160,    1,    2,    4,    0,    7,   14,    4,    2,    1],\n",
       "       [   0, 1374,    1,    5,    1,    3,    2,    2,   19,    1],\n",
       "       [   9,   23, 1140,   29,   12,    4,   12,    9,   35,   12],\n",
       "       [   4,    2,   38, 1194,    0,   34,    2,   12,   32,   16],\n",
       "       [   4,    3,   11,    2, 1091,    2,   10,    5,   13,   50],\n",
       "       [  19,    3,    5,   43,    8,  939,   26,   10,   37,   16],\n",
       "       [  12,    2,   11,    1,   12,   16, 1198,    0,    6,    1],\n",
       "       [   3,    2,   18,    7,   12,    1,    3, 1275,    4,   47],\n",
       "       [  19,   28,   11,   31,   12,   36,    4,    9, 1074,   23],\n",
       "       [  10,    3,    2,   15,   36,    8,    0,   49,   12, 1068]],\n",
       "      dtype=int64)"
      ]
     },
     "execution_count": 64,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# confusion_matrix (실제정답, 예측값)\n",
    "confusion_matrix(y_test,pre)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "25ec1c32",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "              precision    recall  f1-score   support\n",
      "\n",
      "           0       0.94      0.97      0.95      1195\n",
      "           1       0.95      0.98      0.96      1408\n",
      "           2       0.92      0.89      0.90      1285\n",
      "           3       0.90      0.90      0.90      1334\n",
      "           4       0.92      0.92      0.92      1191\n",
      "           5       0.89      0.85      0.87      1106\n",
      "           6       0.94      0.95      0.95      1259\n",
      "           7       0.93      0.93      0.93      1372\n",
      "           8       0.87      0.86      0.87      1247\n",
      "           9       0.86      0.89      0.88      1203\n",
      "\n",
      "    accuracy                           0.91     12600\n",
      "   macro avg       0.91      0.91      0.91     12600\n",
      "weighted avg       0.91      0.91      0.91     12600\n",
      "\n"
     ]
    }
   ],
   "source": [
    "# classification_report (실제정답, 예측값)\n",
    "# 정밀도(precision)가 높으면 기준이 깐깐함, 재현율(recall)이 높으면 기준이 헤픔\n",
    "print(classification_report(y_test,pre))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fc0bacfd",
   "metadata": {},
   "source": [
    "### 모델 활용하기"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "72fb01a5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: pillow in c:\\users\\ai\\anaconda3\\lib\\site-packages (9.0.1)\n"
     ]
    }
   ],
   "source": [
    "!pip install pillow"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "1f04d850",
   "metadata": {},
   "outputs": [],
   "source": [
    "from PIL import Image"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "8d78751c",
   "metadata": {},
   "outputs": [],
   "source": [
    "img = Image.open(\"./data/3.png\").convert(\"L\") # 사진을 열어서 흑백채널로 변경"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "a884420b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(28, 28)"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np_img = np.array(img) # 모델에 넣을 수 있도록 numpy 배열로 변경\n",
    "np_img.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "e4f5e45e",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\AI\\Anaconda3\\lib\\site-packages\\sklearn\\base.py:450: UserWarning: X does not have valid feature names, but LogisticRegression was fitted with feature names\n",
      "  warnings.warn(\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "array([3], dtype=int64)"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Logi_model4.predict(np_img.reshape(1,784)) # 학습데이터처럼 1차원으로 사진 펴주기"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "1cd27717",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\AI\\Anaconda3\\lib\\site-packages\\sklearn\\base.py:450: UserWarning: X does not have valid feature names, but LogisticRegression was fitted with feature names\n",
      "  warnings.warn(\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "array([[1.75989150e-06, 3.28736790e-07, 1.68175320e-04, 9.99468060e-01,\n",
       "        5.91195085e-15, 1.01964434e-06, 3.60648067e-04, 2.74950996e-17,\n",
       "        8.67098584e-09, 3.98572010e-11]])"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Logi_model4.predict_proba(np_img.reshape(1,784))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9bd6c499",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1ed18c51",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6c1be46a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b651e0ac",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "415a878e",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a6318daa",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fbfc201a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0a14fac1",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "34db9cca",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f4ef3a64",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "46d701ed",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f5d0c2c7",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "01abd4b7",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8b8fa207",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f613849c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1ff2aded",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c7907e73",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6a4ac7eb",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f8f4dd00",
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
