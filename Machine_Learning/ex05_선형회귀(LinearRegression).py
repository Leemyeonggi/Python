{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "adeb6073",
   "metadata": {},
   "source": [
    "# 선형회귀 데이터 로딩(보스턴 주택가격 데이터)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "08b048e8",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.datasets import load_boston\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "b6c69578",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\AI\\Anaconda3\\lib\\site-packages\\sklearn\\utils\\deprecation.py:87: FutureWarning: Function load_boston is deprecated; `load_boston` is deprecated in 1.0 and will be removed in 1.2.\n",
      "\n",
      "    The Boston housing prices dataset has an ethical problem. You can refer to\n",
      "    the documentation of this function for further details.\n",
      "\n",
      "    The scikit-learn maintainers therefore strongly discourage the use of this\n",
      "    dataset unless the purpose of the code is to study and educate about\n",
      "    ethical issues in data science and machine learning.\n",
      "\n",
      "    In this special case, you can fetch the dataset from the original\n",
      "    source::\n",
      "\n",
      "        import pandas as pd\n",
      "        import numpy as np\n",
      "\n",
      "\n",
      "        data_url = \"http://lib.stat.cmu.edu/datasets/boston\"\n",
      "        raw_df = pd.read_csv(data_url, sep=\"\\s+\", skiprows=22, header=None)\n",
      "        data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])\n",
      "        target = raw_df.values[1::2, 2]\n",
      "\n",
      "    Alternative datasets include the California housing dataset (i.e.\n",
      "    :func:`~sklearn.datasets.fetch_california_housing`) and the Ames housing\n",
      "    dataset. You can load the datasets as follows::\n",
      "\n",
      "        from sklearn.datasets import fetch_california_housing\n",
      "        housing = fetch_california_housing()\n",
      "\n",
      "    for the California housing dataset and::\n",
      "\n",
      "        from sklearn.datasets import fetch_openml\n",
      "        housing = fetch_openml(name=\"house_prices\", as_frame=True)\n",
      "\n",
      "    for the Ames housing dataset.\n",
      "    \n",
      "  warnings.warn(msg, category=FutureWarning)\n"
     ]
    }
   ],
   "source": [
    "data = load_boston()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "0d4c3de8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict_keys(['data', 'target', 'feature_names', 'DESCR', 'filename', 'data_module'])"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.keys()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "a1ea7f1c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      ".. _boston_dataset:\n",
      "\n",
      "Boston house prices dataset\n",
      "---------------------------\n",
      "\n",
      "**Data Set Characteristics:**  \n",
      "\n",
      "    :Number of Instances: 506 \n",
      "\n",
      "    :Number of Attributes: 13 numeric/categorical predictive. Median Value (attribute 14) is usually the target.\n",
      "\n",
      "    :Attribute Information (in order):\n",
      "        - CRIM     per capita crime rate by town\n",
      "        - ZN       proportion of residential land zoned for lots over 25,000 sq.ft.\n",
      "        - INDUS    proportion of non-retail business acres per town\n",
      "        - CHAS     Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)\n",
      "        - NOX      nitric oxides concentration (parts per 10 million)\n",
      "        - RM       average number of rooms per dwelling\n",
      "        - AGE      proportion of owner-occupied units built prior to 1940\n",
      "        - DIS      weighted distances to five Boston employment centres\n",
      "        - RAD      index of accessibility to radial highways\n",
      "        - TAX      full-value property-tax rate per $10,000\n",
      "        - PTRATIO  pupil-teacher ratio by town\n",
      "        - B        1000(Bk - 0.63)^2 where Bk is the proportion of black people by town\n",
      "        - LSTAT    % lower status of the population\n",
      "        - MEDV     Median value of owner-occupied homes in $1000's\n",
      "\n",
      "    :Missing Attribute Values: None\n",
      "\n",
      "    :Creator: Harrison, D. and Rubinfeld, D.L.\n",
      "\n",
      "This is a copy of UCI ML housing dataset.\n",
      "https://archive.ics.uci.edu/ml/machine-learning-databases/housing/\n",
      "\n",
      "\n",
      "This dataset was taken from the StatLib library which is maintained at Carnegie Mellon University.\n",
      "\n",
      "The Boston house-price data of Harrison, D. and Rubinfeld, D.L. 'Hedonic\n",
      "prices and the demand for clean air', J. Environ. Economics & Management,\n",
      "vol.5, 81-102, 1978.   Used in Belsley, Kuh & Welsch, 'Regression diagnostics\n",
      "...', Wiley, 1980.   N.B. Various transformations are used in the table on\n",
      "pages 244-261 of the latter.\n",
      "\n",
      "The Boston house-price data has been used in many machine learning papers that address regression\n",
      "problems.   \n",
      "     \n",
      ".. topic:: References\n",
      "\n",
      "   - Belsley, Kuh & Welsch, 'Regression diagnostics: Identifying Influential Data and Sources of Collinearity', Wiley, 1980. 244-261.\n",
      "   - Quinlan,R. (1993). Combining Instance-Based and Model-Based Learning. In Proceedings on the Tenth International Conference of Machine Learning, 236-243, University of Massachusetts, Amherst. Morgan Kaufmann.\n",
      "\n"
     ]
    }
   ],
   "source": [
    "print(data.DESCR)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3cb0d954",
   "metadata": {},
   "source": [
    "# 모델학습"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "c48ac8db",
   "metadata": {},
   "outputs": [],
   "source": [
    "X = data.data\n",
    "y = data.target"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "efb97867",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "705e2423",
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,\n",
    "                                                random_state=722)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "054110e2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "((404, 13), (404,))"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_train.shape, y_train.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "88279775",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "((102, 13), (102,))"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_test.shape, y_test.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "7ec229d6",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 선형회귀모델\n",
    "from sklearn.linear_model import LinearRegression"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "b185f7de",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "LinearRegression()"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 모델학습\n",
    "model = LinearRegression()\n",
    "model.fit(X_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "abb6b1c6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "가중치 : [-1.18313515e-01  5.20521053e-02  1.76355388e-02  4.11554414e+00\n",
      " -2.01952839e+01  2.93408084e+00  1.01479948e-02 -1.56497280e+00\n",
      "  3.16556945e-01 -1.25687293e-02 -1.01868234e+00  6.75071633e-03\n",
      " -5.73138231e-01]\n",
      "절편 : 45.72482696295275\n"
     ]
    }
   ],
   "source": [
    "# 학습된 가중치와 절편 확인\n",
    "print(\"가중치 :\",model.coef_)\n",
    "print(\"절편 :\",model.intercept_)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "db1811a9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.7454536557439619"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 모델평가\n",
    "model.score(X_test,y_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "7cc1dd35",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 다른 평가지표 사용\n",
    "from sklearn.metrics import mean_absolute_error #MAE\n",
    "from sklearn.metrics import mean_squared_error #MSE"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "77ee6399",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "MAE : 3.028568457448007\n",
      "MSE : 17.925235768942024\n"
     ]
    }
   ],
   "source": [
    "pre = model.predict(X_test) # 예측값 생성\n",
    "print(\"MAE :\", mean_absolute_error(y_test,pre))\n",
    "print(\"MSE :\", mean_squared_error(y_test,pre))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8e1a00bd",
   "metadata": {},
   "source": [
    "# 선형모델의 학습 원리\n",
    "1. 선형모델은 최적의 가중치(w)와 절편(b)를 선택하기위해 MSE(평균제곱오차)를 이용해 각 가설의 적합성을 판단한다.\n",
    "2. 최적의 가중치(w)와 절편(b)를 만들기위해서 2가지 방식을 활용한다.\n",
    "    - 해석적 방법(Ordinary Least Squares) -> LinearRegression 클래스로 구현됨\n",
    "    - 경사하강법(Gradient Descent Algorithm) -> SGDRegressor 클래스로 구현됨\n",
    "        - 초기 가중치로부터 기울기 값을 조금씩 수정해서 찾아가는 방식\n",
    "        - 기울기가 낮아지는 방향으로 계속 업데이트하는 공식"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "36830d42",
   "metadata": {},
   "source": [
    "## 가중치변화에따른 MSE변화 그래프를 그려보자"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "5c2c4b9b",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 성적데이터 생성\n",
    "data = pd.DataFrame([[2,20],[4,40],[8,80],[9,90]],\n",
    "                   index=['명기','윤규','동규','영석'],\n",
    "                   columns=['공부시간','성적점수'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "e2a55513",
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
       "      <th>공부시간</th>\n",
       "      <th>성적점수</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>명기</th>\n",
       "      <td>2</td>\n",
       "      <td>20</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>윤규</th>\n",
       "      <td>4</td>\n",
       "      <td>40</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>동규</th>\n",
       "      <td>8</td>\n",
       "      <td>80</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>영석</th>\n",
       "      <td>9</td>\n",
       "      <td>90</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    공부시간  성적점수\n",
       "명기     2    20\n",
       "윤규     4    40\n",
       "동규     8    80\n",
       "영석     9    90"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ea9ef13a",
   "metadata": {},
   "source": [
    "## MSE함수 생성"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "47404ad7",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 문제,정답,가중치를 매개변수로 받는다.\n",
    "def MSE(X,y,w):\n",
    "    # 예측값 생성\n",
    "    y_pre = w*X + 0\n",
    "    # 실제값과 예측값의 차이의 제곱 평균\n",
    "    error = y - y_pre # 오차\n",
    "    return (error**2).mean() # 평균제곱오차"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "b400cfee",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.0"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "MSE(data['공부시간'],data['성적점수'],10) # 결과값이 0이 나와야한다"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1b97ca89",
   "metadata": {},
   "source": [
    "### 그래프 그리기"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "1ac3813b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 0.        ,  0.40816327,  0.81632653,  1.2244898 ,  1.63265306,\n",
       "        2.04081633,  2.44897959,  2.85714286,  3.26530612,  3.67346939,\n",
       "        4.08163265,  4.48979592,  4.89795918,  5.30612245,  5.71428571,\n",
       "        6.12244898,  6.53061224,  6.93877551,  7.34693878,  7.75510204,\n",
       "        8.16326531,  8.57142857,  8.97959184,  9.3877551 ,  9.79591837,\n",
       "       10.20408163, 10.6122449 , 11.02040816, 11.42857143, 11.83673469,\n",
       "       12.24489796, 12.65306122, 13.06122449, 13.46938776, 13.87755102,\n",
       "       14.28571429, 14.69387755, 15.10204082, 15.51020408, 15.91836735,\n",
       "       16.32653061, 16.73469388, 17.14285714, 17.55102041, 17.95918367,\n",
       "       18.36734694, 18.7755102 , 19.18367347, 19.59183673, 20.        ])"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 변화하는 가중치(w) 생성\n",
    "weights = np.linspace(0,20)\n",
    "weights"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "933be8bf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[4125.0,\n",
       " 3795.1374427321953,\n",
       " 3479.019158683882,\n",
       " 3176.6451478550603,\n",
       " 2888.015410245731,\n",
       " 2613.1299458558933,\n",
       " 2351.9887546855475,\n",
       " 2104.5918367346935,\n",
       " 1870.939192003332,\n",
       " 1651.0308204914622,\n",
       " 1444.8667221990836,\n",
       " 1252.4468971261972,\n",
       " 1073.771345272803,\n",
       " 908.8400666389006,\n",
       " 757.6530612244896,\n",
       " 620.2103290295709,\n",
       " 496.5118700541441,\n",
       " 386.5576842982092,\n",
       " 290.3477717617659,\n",
       " 207.88213244481454,\n",
       " 139.1607663473552,\n",
       " 84.1836734693878,\n",
       " 42.950853810912015,\n",
       " 15.46230737192834,\n",
       " 1.718034152436478,\n",
       " 1.718034152436478,\n",
       " 15.46230737192834,\n",
       " 42.95085381091215,\n",
       " 84.1836734693878,\n",
       " 139.1607663473552,\n",
       " 207.88213244481489,\n",
       " 290.347771761766,\n",
       " 386.5576842982092,\n",
       " 496.5118700541442,\n",
       " 620.2103290295709,\n",
       " 757.6530612244901,\n",
       " 908.8400666389006,\n",
       " 1073.7713452728026,\n",
       " 1252.4468971261979,\n",
       " 1444.8667221990838,\n",
       " 1651.0308204914627,\n",
       " 1870.939192003332,\n",
       " 2104.5918367346935,\n",
       " 2351.988754685547,\n",
       " 2613.129945855895,\n",
       " 2888.015410245732,\n",
       " 3176.6451478550607,\n",
       " 3479.019158683883,\n",
       " 3795.1374427321957,\n",
       " 4125.0]"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mse_list = []\n",
    "for w in weights:\n",
    "    mse_list.append(MSE(data['공부시간'],data['성적점수'],w))\n",
    "    \n",
    "mse_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "33d8dde5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 720x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(10,5))\n",
    "plt.plot(mse_list,marker='*')\n",
    "plt.ylabel('MSE')\n",
    "plt.xlabel('W')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5d2e16fc",
   "metadata": {},
   "source": [
    "## 경사하강법으로 구현된 SGDRegressor를 사용해보자."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "63c733b1",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.linear_model import SGDRegressor"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "c81cfb96",
   "metadata": {},
   "outputs": [],
   "source": [
    "sgd_model = SGDRegressor(eta0=0.001,  # 학습률\n",
    "                        max_iter=6000,# 반복횟수 (가중치 업데이트 횟수)\n",
    "                        epsilon=0.001, # 최소 오차 기준값\n",
    "                        n_iter_no_change=15, # 업데이트시 오차가 변경되지 않는걸 허용하는 횟수\n",
    "                        verbose=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "34dfa244",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-- Epoch 1\n",
      "Norm: 1.36, NNZs: 1, Bias: 0.184228, T: 4, Avg. loss: 1873.688518\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 2\n",
      "Norm: 2.25, NNZs: 1, Bias: 0.305653, T: 8, Avg. loss: 1432.173507\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 3\n",
      "Norm: 2.94, NNZs: 1, Bias: 0.401542, T: 12, Avg. loss: 1157.743445\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 4\n",
      "Norm: 3.51, NNZs: 1, Bias: 0.481558, T: 16, Avg. loss: 961.754940\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 5\n",
      "Norm: 4.01, NNZs: 1, Bias: 0.550712, T: 20, Avg. loss: 811.017852\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 6\n",
      "Norm: 4.45, NNZs: 1, Bias: 0.611433, T: 24, Avg. loss: 689.112454\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 7\n",
      "Norm: 4.84, NNZs: 1, Bias: 0.665437, T: 28, Avg. loss: 589.539280\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 8\n",
      "Norm: 5.18, NNZs: 1, Bias: 0.713764, T: 32, Avg. loss: 508.056073\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 9\n",
      "Norm: 5.50, NNZs: 1, Bias: 0.757239, T: 36, Avg. loss: 440.330200\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 10\n",
      "Norm: 5.78, NNZs: 1, Bias: 0.796645, T: 40, Avg. loss: 382.899601\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 11\n",
      "Norm: 6.04, NNZs: 1, Bias: 0.832645, T: 44, Avg. loss: 334.064899\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 12\n",
      "Norm: 6.28, NNZs: 1, Bias: 0.865583, T: 48, Avg. loss: 292.613621\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 13\n",
      "Norm: 6.50, NNZs: 1, Bias: 0.895694, T: 52, Avg. loss: 257.169837\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 14\n",
      "Norm: 6.70, NNZs: 1, Bias: 0.923371, T: 56, Avg. loss: 226.472531\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 15\n",
      "Norm: 6.89, NNZs: 1, Bias: 0.948982, T: 60, Avg. loss: 199.858562\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 16\n",
      "Norm: 7.06, NNZs: 1, Bias: 0.972687, T: 64, Avg. loss: 176.837067\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 17\n",
      "Norm: 7.22, NNZs: 1, Bias: 0.994554, T: 68, Avg. loss: 156.836217\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 18\n",
      "Norm: 7.37, NNZs: 1, Bias: 1.014819, T: 72, Avg. loss: 139.291650\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 19\n",
      "Norm: 7.50, NNZs: 1, Bias: 1.033718, T: 76, Avg. loss: 123.895967\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 20\n",
      "Norm: 7.63, NNZs: 1, Bias: 1.051336, T: 80, Avg. loss: 110.416186\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 21\n",
      "Norm: 7.75, NNZs: 1, Bias: 1.067686, T: 84, Avg. loss: 98.580326\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 22\n",
      "Norm: 7.86, NNZs: 1, Bias: 1.082922, T: 88, Avg. loss: 88.106070\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 23\n",
      "Norm: 7.97, NNZs: 1, Bias: 1.097206, T: 92, Avg. loss: 78.836210\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 24\n",
      "Norm: 8.07, NNZs: 1, Bias: 1.110589, T: 96, Avg. loss: 70.649351\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 25\n",
      "Norm: 8.16, NNZs: 1, Bias: 1.123060, T: 100, Avg. loss: 63.405046\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 26\n",
      "Norm: 8.24, NNZs: 1, Bias: 1.134729, T: 104, Avg. loss: 56.951687\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 27\n",
      "Norm: 8.32, NNZs: 1, Bias: 1.145710, T: 108, Avg. loss: 51.203500\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 28\n",
      "Norm: 8.40, NNZs: 1, Bias: 1.156037, T: 112, Avg. loss: 46.093139\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 29\n",
      "Norm: 8.47, NNZs: 1, Bias: 1.165691, T: 116, Avg. loss: 41.543928\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 30\n",
      "Norm: 8.54, NNZs: 1, Bias: 1.174749, T: 120, Avg. loss: 37.470300\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 31\n",
      "Norm: 8.60, NNZs: 1, Bias: 1.183300, T: 124, Avg. loss: 33.823225\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 32\n",
      "Norm: 8.66, NNZs: 1, Bias: 1.191364, T: 128, Avg. loss: 30.563583\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 33\n",
      "Norm: 8.72, NNZs: 1, Bias: 1.198920, T: 132, Avg. loss: 27.647797\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 34\n",
      "Norm: 8.77, NNZs: 1, Bias: 1.206027, T: 136, Avg. loss: 25.025746\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 35\n",
      "Norm: 8.82, NNZs: 1, Bias: 1.212750, T: 140, Avg. loss: 22.668391\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 36\n",
      "Norm: 8.87, NNZs: 1, Bias: 1.219105, T: 144, Avg. loss: 20.552173\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 37\n",
      "Norm: 8.91, NNZs: 1, Bias: 1.225071, T: 148, Avg. loss: 18.651572\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 38\n",
      "Norm: 8.96, NNZs: 1, Bias: 1.230691, T: 152, Avg. loss: 16.936365\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 39\n",
      "Norm: 9.00, NNZs: 1, Bias: 1.236018, T: 156, Avg. loss: 15.388858\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 40\n",
      "Norm: 9.04, NNZs: 1, Bias: 1.241062, T: 160, Avg. loss: 13.994441\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 41\n",
      "Norm: 9.07, NNZs: 1, Bias: 1.245803, T: 164, Avg. loss: 12.737817\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 42\n",
      "Norm: 9.11, NNZs: 1, Bias: 1.250276, T: 168, Avg. loss: 11.600333\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 43\n",
      "Norm: 9.14, NNZs: 1, Bias: 1.254522, T: 172, Avg. loss: 10.570955\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 44\n",
      "Norm: 9.17, NNZs: 1, Bias: 1.258547, T: 176, Avg. loss: 9.640388\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 45\n",
      "Norm: 9.20, NNZs: 1, Bias: 1.262335, T: 180, Avg. loss: 8.799303\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 46\n",
      "Norm: 9.23, NNZs: 1, Bias: 1.265911, T: 184, Avg. loss: 8.035961\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 47\n",
      "Norm: 9.25, NNZs: 1, Bias: 1.269310, T: 188, Avg. loss: 7.343346\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 48\n",
      "Norm: 9.28, NNZs: 1, Bias: 1.272536, T: 192, Avg. loss: 6.715411\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 49\n",
      "Norm: 9.30, NNZs: 1, Bias: 1.275573, T: 196, Avg. loss: 6.146390\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 50\n",
      "Norm: 9.32, NNZs: 1, Bias: 1.278442, T: 200, Avg. loss: 5.628776\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 51\n",
      "Norm: 9.35, NNZs: 1, Bias: 1.281172, T: 204, Avg. loss: 5.158030\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 52\n",
      "Norm: 9.37, NNZs: 1, Bias: 1.283764, T: 208, Avg. loss: 4.730141\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 53\n",
      "Norm: 9.38, NNZs: 1, Bias: 1.286206, T: 212, Avg. loss: 4.341508\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 54\n",
      "Norm: 9.40, NNZs: 1, Bias: 1.288513, T: 216, Avg. loss: 3.987266\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 55\n",
      "Norm: 9.42, NNZs: 1, Bias: 1.290709, T: 220, Avg. loss: 3.664434\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 56\n",
      "Norm: 9.44, NNZs: 1, Bias: 1.292796, T: 224, Avg. loss: 3.370299\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 57\n",
      "Norm: 9.45, NNZs: 1, Bias: 1.294761, T: 228, Avg. loss: 3.102603\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 58\n",
      "Norm: 9.47, NNZs: 1, Bias: 1.296618, T: 232, Avg. loss: 2.858152\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 59\n",
      "Norm: 9.48, NNZs: 1, Bias: 1.298386, T: 236, Avg. loss: 2.634965\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 60\n",
      "Norm: 9.50, NNZs: 1, Bias: 1.300067, T: 240, Avg. loss: 2.431174\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 61\n",
      "Norm: 9.51, NNZs: 1, Bias: 1.301649, T: 244, Avg. loss: 2.245357\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 62\n",
      "Norm: 9.52, NNZs: 1, Bias: 1.303143, T: 248, Avg. loss: 2.075400\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 63\n",
      "Norm: 9.54, NNZs: 1, Bias: 1.304566, T: 252, Avg. loss: 1.919970\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 64\n",
      "Norm: 9.55, NNZs: 1, Bias: 1.305919, T: 256, Avg. loss: 1.777755\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 65\n",
      "Norm: 9.56, NNZs: 1, Bias: 1.307190, T: 260, Avg. loss: 1.647868\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 66\n",
      "Norm: 9.57, NNZs: 1, Bias: 1.308390, T: 264, Avg. loss: 1.528892\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 67\n",
      "Norm: 9.58, NNZs: 1, Bias: 1.309532, T: 268, Avg. loss: 1.419921\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 68\n",
      "Norm: 9.59, NNZs: 1, Bias: 1.310618, T: 272, Avg. loss: 1.320023\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 69\n",
      "Norm: 9.60, NNZs: 1, Bias: 1.311637, T: 276, Avg. loss: 1.228644\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 70\n",
      "Norm: 9.61, NNZs: 1, Bias: 1.312597, T: 280, Avg. loss: 1.144830\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 71\n",
      "Norm: 9.61, NNZs: 1, Bias: 1.313511, T: 284, Avg. loss: 1.067961\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 72\n",
      "Norm: 9.62, NNZs: 1, Bias: 1.314380, T: 288, Avg. loss: 0.997360\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 73\n",
      "Norm: 9.63, NNZs: 1, Bias: 1.315192, T: 292, Avg. loss: 0.932689\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 74\n",
      "Norm: 9.64, NNZs: 1, Bias: 1.315956, T: 296, Avg. loss: 0.873300\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 75\n",
      "Norm: 9.64, NNZs: 1, Bias: 1.316683, T: 300, Avg. loss: 0.818766\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 76\n",
      "Norm: 9.65, NNZs: 1, Bias: 1.317373, T: 304, Avg. loss: 0.768586\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 77\n",
      "Norm: 9.66, NNZs: 1, Bias: 1.318016, T: 308, Avg. loss: 0.722562\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 78\n",
      "Norm: 9.66, NNZs: 1, Bias: 1.318620, T: 312, Avg. loss: 0.680251\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 79\n",
      "Norm: 9.67, NNZs: 1, Bias: 1.319193, T: 316, Avg. loss: 0.641355\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 80\n",
      "Norm: 9.68, NNZs: 1, Bias: 1.319736, T: 320, Avg. loss: 0.605500\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 81\n",
      "Norm: 9.68, NNZs: 1, Bias: 1.320240, T: 324, Avg. loss: 0.572576\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 82\n",
      "Norm: 9.69, NNZs: 1, Bias: 1.320711, T: 328, Avg. loss: 0.542277\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 83\n",
      "Norm: 9.69, NNZs: 1, Bias: 1.321157, T: 332, Avg. loss: 0.514397\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 84\n",
      "Norm: 9.70, NNZs: 1, Bias: 1.321579, T: 336, Avg. loss: 0.488649\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 85\n",
      "Norm: 9.70, NNZs: 1, Bias: 1.321968, T: 340, Avg. loss: 0.464979\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 86\n",
      "Norm: 9.70, NNZs: 1, Bias: 1.322329, T: 344, Avg. loss: 0.443176\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 87\n",
      "Norm: 9.71, NNZs: 1, Bias: 1.322670, T: 348, Avg. loss: 0.423097\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 88\n",
      "Norm: 9.71, NNZs: 1, Bias: 1.322991, T: 352, Avg. loss: 0.404518\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 89\n",
      "Norm: 9.72, NNZs: 1, Bias: 1.323285, T: 356, Avg. loss: 0.387422\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 90\n",
      "Norm: 9.72, NNZs: 1, Bias: 1.323555, T: 360, Avg. loss: 0.371660\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 91\n",
      "Norm: 9.72, NNZs: 1, Bias: 1.323810, T: 364, Avg. loss: 0.357134\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 92\n",
      "Norm: 9.73, NNZs: 1, Bias: 1.324048, T: 368, Avg. loss: 0.343666\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 93\n",
      "Norm: 9.73, NNZs: 1, Bias: 1.324262, T: 372, Avg. loss: 0.331262\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 94\n",
      "Norm: 9.73, NNZs: 1, Bias: 1.324457, T: 376, Avg. loss: 0.319816\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 95\n",
      "Norm: 9.74, NNZs: 1, Bias: 1.324639, T: 380, Avg. loss: 0.309261\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 96\n",
      "Norm: 9.74, NNZs: 1, Bias: 1.324807, T: 384, Avg. loss: 0.299455\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 97\n",
      "Norm: 9.74, NNZs: 1, Bias: 1.324956, T: 388, Avg. loss: 0.290415\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 98\n",
      "Norm: 9.75, NNZs: 1, Bias: 1.325088, T: 392, Avg. loss: 0.282066\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 99\n",
      "Norm: 9.75, NNZs: 1, Bias: 1.325209, T: 396, Avg. loss: 0.274364\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 100\n",
      "Norm: 9.75, NNZs: 1, Bias: 1.325320, T: 400, Avg. loss: 0.267193\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 101\n",
      "Norm: 9.75, NNZs: 1, Bias: 1.325414, T: 404, Avg. loss: 0.260575\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 102\n",
      "Norm: 9.76, NNZs: 1, Bias: 1.325493, T: 408, Avg. loss: 0.254460\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 103\n",
      "Norm: 9.76, NNZs: 1, Bias: 1.325564, T: 412, Avg. loss: 0.248816\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 104\n",
      "Norm: 9.76, NNZs: 1, Bias: 1.325627, T: 416, Avg. loss: 0.243548\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 105\n",
      "Norm: 9.76, NNZs: 1, Bias: 1.325674, T: 420, Avg. loss: 0.238683\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 106\n",
      "Norm: 9.76, NNZs: 1, Bias: 1.325710, T: 424, Avg. loss: 0.234183\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 107\n",
      "Norm: 9.77, NNZs: 1, Bias: 1.325739, T: 428, Avg. loss: 0.230030\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 108\n",
      "Norm: 9.77, NNZs: 1, Bias: 1.325761, T: 432, Avg. loss: 0.226143\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 109\n",
      "Norm: 9.77, NNZs: 1, Bias: 1.325770, T: 436, Avg. loss: 0.222550\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 110\n",
      "Norm: 9.77, NNZs: 1, Bias: 1.325769, T: 440, Avg. loss: 0.219224\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 111\n",
      "Norm: 9.77, NNZs: 1, Bias: 1.325762, T: 444, Avg. loss: 0.216155\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 112\n",
      "Norm: 9.77, NNZs: 1, Bias: 1.325751, T: 448, Avg. loss: 0.213273\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 113\n",
      "Norm: 9.78, NNZs: 1, Bias: 1.325727, T: 452, Avg. loss: 0.210608\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 114\n",
      "Norm: 9.78, NNZs: 1, Bias: 1.325695, T: 456, Avg. loss: 0.208137\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 115\n",
      "Norm: 9.78, NNZs: 1, Bias: 1.325660, T: 460, Avg. loss: 0.205859\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 116\n",
      "Norm: 9.78, NNZs: 1, Bias: 1.325619, T: 464, Avg. loss: 0.203712\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 117\n",
      "Norm: 9.78, NNZs: 1, Bias: 1.325569, T: 468, Avg. loss: 0.201724\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 118\n",
      "Norm: 9.78, NNZs: 1, Bias: 1.325511, T: 472, Avg. loss: 0.199880\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 119\n",
      "Norm: 9.78, NNZs: 1, Bias: 1.325451, T: 476, Avg. loss: 0.198181\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 120\n",
      "Norm: 9.78, NNZs: 1, Bias: 1.325386, T: 480, Avg. loss: 0.196573\n",
      "Total training time: 0.00 seconds.\n",
      "-- Epoch 121\n",
      "Norm: 9.79, NNZs: 1, Bias: 1.325313, T: 484, Avg. loss: 0.195083\n",
      "Total training time: 0.01 seconds.\n",
      "-- Epoch 122\n",
      "Norm: 9.79, NNZs: 1, Bias: 1.325234, T: 488, Avg. loss: 0.193699\n",
      "Total training time: 0.01 seconds.\n",
      "-- Epoch 123\n",
      "Norm: 9.79, NNZs: 1, Bias: 1.325152, T: 492, Avg. loss: 0.192424\n",
      "Total training time: 0.01 seconds.\n",
      "-- Epoch 124\n",
      "Norm: 9.79, NNZs: 1, Bias: 1.325068, T: 496, Avg. loss: 0.191212\n",
      "Total training time: 0.01 seconds.\n",
      "-- Epoch 125\n",
      "Norm: 9.79, NNZs: 1, Bias: 1.324976, T: 500, Avg. loss: 0.190089\n",
      "Total training time: 0.01 seconds.\n",
      "-- Epoch 126\n",
      "Norm: 9.79, NNZs: 1, Bias: 1.324878, T: 504, Avg. loss: 0.189043\n",
      "Total training time: 0.01 seconds.\n",
      "-- Epoch 127\n",
      "Norm: 9.79, NNZs: 1, Bias: 1.324779, T: 508, Avg. loss: 0.188082\n",
      "Total training time: 0.01 seconds.\n",
      "-- Epoch 128\n",
      "Norm: 9.79, NNZs: 1, Bias: 1.324678, T: 512, Avg. loss: 0.187163\n",
      "Total training time: 0.01 seconds.\n",
      "-- Epoch 129\n",
      "Norm: 9.79, NNZs: 1, Bias: 1.324570, T: 516, Avg. loss: 0.186310\n",
      "Total training time: 0.01 seconds.\n",
      "-- Epoch 130\n",
      "Norm: 9.79, NNZs: 1, Bias: 1.324457, T: 520, Avg. loss: 0.185514\n",
      "Total training time: 0.01 seconds.\n",
      "-- Epoch 131\n",
      "Norm: 9.79, NNZs: 1, Bias: 1.324343, T: 524, Avg. loss: 0.184785\n",
      "Total training time: 0.01 seconds.\n",
      "-- Epoch 132\n",
      "Norm: 9.79, NNZs: 1, Bias: 1.324228, T: 528, Avg. loss: 0.184082\n",
      "Total training time: 0.01 seconds.\n",
      "-- Epoch 133\n",
      "Norm: 9.80, NNZs: 1, Bias: 1.324107, T: 532, Avg. loss: 0.183430\n",
      "Total training time: 0.01 seconds.\n",
      "-- Epoch 134\n",
      "Norm: 9.80, NNZs: 1, Bias: 1.323981, T: 536, Avg. loss: 0.182820\n",
      "Total training time: 0.01 seconds.\n",
      "-- Epoch 135\n",
      "Norm: 9.80, NNZs: 1, Bias: 1.323854, T: 540, Avg. loss: 0.182262\n",
      "Total training time: 0.01 seconds.\n",
      "-- Epoch 136\n",
      "Norm: 9.80, NNZs: 1, Bias: 1.323727, T: 544, Avg. loss: 0.181720\n",
      "Total training time: 0.01 seconds.\n",
      "-- Epoch 137\n",
      "Norm: 9.80, NNZs: 1, Bias: 1.323595, T: 548, Avg. loss: 0.181217\n",
      "Total training time: 0.01 seconds.\n",
      "-- Epoch 138\n",
      "Norm: 9.80, NNZs: 1, Bias: 1.323458, T: 552, Avg. loss: 0.180744\n",
      "Total training time: 0.01 seconds.\n",
      "-- Epoch 139\n",
      "Norm: 9.80, NNZs: 1, Bias: 1.323321, T: 556, Avg. loss: 0.180314\n",
      "Total training time: 0.01 seconds.\n",
      "-- Epoch 140\n",
      "Norm: 9.80, NNZs: 1, Bias: 1.323184, T: 560, Avg. loss: 0.179892\n",
      "Total training time: 0.01 seconds.\n",
      "-- Epoch 141\n",
      "Norm: 9.80, NNZs: 1, Bias: 1.323042, T: 564, Avg. loss: 0.179500\n",
      "Total training time: 0.01 seconds.\n",
      "Convergence after 141 epochs took 0.01 seconds\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "SGDRegressor(epsilon=0.001, eta0=0.001, max_iter=6000, n_iter_no_change=15,\n",
       "             verbose=1)"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sgd_model.fit(data[['공부시간']],data['성적점수'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "5be234d4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "가중치 : [9.80037822]\n",
      "절편 : [1.32304192]\n"
     ]
    }
   ],
   "source": [
    "print('가중치 :',sgd_model.coef_)\n",
    "print('절편 :',sgd_model.intercept_)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "bfc464c2",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\AI\\Anaconda3\\lib\\site-packages\\sklearn\\base.py:450: UserWarning: X does not have valid feature names, but SGDRegressor was fitted with feature names\n",
      "  warnings.warn(\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "array([69.92568947, 50.32493303])"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sgd_model.predict([[7],[5]])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "166f7c64",
   "metadata": {},
   "source": [
    "# 다항 회귀\n",
    "- 선형 모델의 수식에서 입력특성에 2차항이 포함된 경우\n",
    "- 고차항이 포함되면 데이터의 특성을 더 fit하게 맞출 수 있어 성능 개선의 여지가 있다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "0381af01",
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\AI\\Anaconda3\\lib\\site-packages\\sklearn\\utils\\deprecation.py:87: FutureWarning: Function load_boston is deprecated; `load_boston` is deprecated in 1.0 and will be removed in 1.2.\n",
      "\n",
      "    The Boston housing prices dataset has an ethical problem. You can refer to\n",
      "    the documentation of this function for further details.\n",
      "\n",
      "    The scikit-learn maintainers therefore strongly discourage the use of this\n",
      "    dataset unless the purpose of the code is to study and educate about\n",
      "    ethical issues in data science and machine learning.\n",
      "\n",
      "    In this special case, you can fetch the dataset from the original\n",
      "    source::\n",
      "\n",
      "        import pandas as pd\n",
      "        import numpy as np\n",
      "\n",
      "\n",
      "        data_url = \"http://lib.stat.cmu.edu/datasets/boston\"\n",
      "        raw_df = pd.read_csv(data_url, sep=\"\\s+\", skiprows=22, header=None)\n",
      "        data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])\n",
      "        target = raw_df.values[1::2, 2]\n",
      "\n",
      "    Alternative datasets include the California housing dataset (i.e.\n",
      "    :func:`~sklearn.datasets.fetch_california_housing`) and the Ames housing\n",
      "    dataset. You can load the datasets as follows::\n",
      "\n",
      "        from sklearn.datasets import fetch_california_housing\n",
      "        housing = fetch_california_housing()\n",
      "\n",
      "    for the California housing dataset and::\n",
      "\n",
      "        from sklearn.datasets import fetch_openml\n",
      "        housing = fetch_openml(name=\"house_prices\", as_frame=True)\n",
      "\n",
      "    for the Ames housing dataset.\n",
      "    \n",
      "  warnings.warn(msg, category=FutureWarning)\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "dict_keys(['data', 'target', 'feature_names', 'DESCR', 'filename', 'data_module'])"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "boston = load_boston()\n",
    "boston.keys()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "808304e5",
   "metadata": {},
   "outputs": [],
   "source": [
    "data = pd.DataFrame(boston.data, columns=boston.feature_names)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "aba4e35c",
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train,X_test,y_train,y_test = train_test_split(data,boston.target,\n",
    "                                                random_state=726)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "0e2df5a0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 360x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(5,5)) # 가로, 세로 크기\n",
    "plt.scatter(X_train['LSTAT'],y_train, label='original')\n",
    "\n",
    "# 선형모델 학습\n",
    "LSTAT_model = LinearRegression()\n",
    "LSTAT_model.fit(X_train[['LSTAT']],y_train)\n",
    "# 선형모델의 예측결과 확인\n",
    "pre = LSTAT_model.predict(X_train[['LSTAT']])\n",
    "plt.scatter(X_train[['LSTAT']],pre,label='predict')\n",
    "\n",
    "plt.legend() # 범례\n",
    "plt.xlabel('LSTAT')\n",
    "plt.ylabel('PRICE')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "681b02b1",
   "metadata": {},
   "source": [
    "## 다항회귀 구현하기\n",
    "- 특성확장을 통해서 다항식을 만들어준다.\n",
    "- sklearn의 PolynomialFeatures를 이용한다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "1a37eea9",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 특성확장\n",
    "X_train['LSTAT x ZN'] = X_train['LSTAT'] * X_train['LSTAT']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "139b1ef1",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 모델학습\n",
    "LSTAT_model2 = LinearRegression()\n",
    "LSTAT_model2.fit(X_train[['LSTAT','LSTAT x LSTAT']],y_train)\n",
    "# 모델예측\n",
    "pre2 = LSTAT_model2.predict(X_train[['LSTAT','LSTAT x LSTAT']])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "8424e386",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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mmKjKMWHimMYJyvPzT3WFBtFKT50zjHMtAtO5eaF67CK3Xtxj/NhwltRlPShlmOYmqpK/mnkV4hfO6PusaJknldffZWLL74YgGXLllFbW2u7b2NjI/PmzYu+XrduHV//+tcZOHAgQ4YMYeHChWkZk4pjDHfWDGbuxKHqHitKmmhtda5qZcW4ceOYPn267fvx4ti1a1ceffRRNm3axJ/+9CduuukmGhsbkxluO9StjkPdY6Uo2bAIXrkD9u2A7n3h3NthyISUTrlt2za+9a1vceaZZ1JfX88//uM/8uijj/LVr36VKVOm8OKLL/LjH/+Ynj17MmPGDA4fPszJJ5/Mww8/zFFHHRUVsl69erXLeXzkkUeoq6vjN7/5DZ988gn/8i//wocffgjA/fffz69//Ws++OADhg4dytixY5k9e3b02D59+nDssceye/duxwK7XlBxjCEfVhEoStrZsAiW3wDBcGBx38eh15CyQG7ZsoX58+dTXV3NlClTohZdly5dWLVqFZ999hnjx4/n5Zdfplu3btx9993MmTOHW265heuuu44VK1bwD//wD0ycONHy/DfccAPf+MY3ePrpp2ltbWX//v3U1tayceNG1q1b12H/N998k+bmZk4++eSUPheoWx0lEzXvFCUveOWOI8IYIdgU2p4iJ5xwAtXV1QBcffXVrFq1CiAqdmvWrOFvf/sb1dXVDB06lAULFvDRRx+xefNm+vfvzymnnIKIcPXVV1uef8WKFfzwhz8EQlV6nNZj79q1i+9973s8/PDDlJWlLm1qOYbRJYBK0bJvR2LbEyC+cVXkdaR0mTGGsWPH8uSTT7bbb926dWltEPbFF19w0UUXceedd1rWk0wGtRzD6BJApWjp3jex7Qmwfft2/vKXvwDw5JNPMmrUqHbvjxw5ktWrV/P+++8DcPDgQd59910GDBjA1q1b+eCDD6LHWnHuuedy//33A6HgzhdffMHRRx/N3//+9+g+zc3NXHbZZUyaNIkrrkhfkS8VxzC6BFApWs69Hfxxf8f+QGh7ipx22mksWLCAIUOGsGfPnqgLHKF379488sgjXHnllQwZMoSRI0eyefNmunTpwgMPPMBFF13EqFGj2rVUiOW+++5j5cqVDB48mOHDh7Np0yaOOeYYqqurGTRoENOmTWPRokW89tprPPLIIwwdOpShQ4dazkcmipYs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\n",
      "text/plain": [
       "<Figure size 360x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(5,5))\n",
    "plt.scatter(X_train['LSTAT'],y_train, label='original') # 오리지날 데이터\n",
    "plt.scatter(X_train['LSTAT'],pre2, label='predict2') # 다항회귀 결과\n",
    "\n",
    "plt.legend()\n",
    "plt.xlabel('LSTAT')\n",
    "plt.ylabel('PRICE')`\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "83c7ea95",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0457763a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6af07365",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7db2024d",
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
