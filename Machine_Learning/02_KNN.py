{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "95848919",
   "metadata": {},
   "source": [
    "# 요구사항 분석 및 문제 정의\n",
    "\n",
    "- 간단한 EDA와 관련된 함수를 학습\n",
    "- BMI 데이터를 확인해 보고 잘 분류가 될 수 있는지 시각화\n",
    "- KNN의 개념에 대해 학습\n",
    "- KNN을 이용해서 학습\n",
    "- 머신러닝 프로세스에 대해 학습"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fb8597cb",
   "metadata": {},
   "source": [
    "# 데이터 수집"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "8d9922dc",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "5c259aab",
   "metadata": {},
   "outputs": [],
   "source": [
    "bmi = pd.read_csv('data/bmi_500.csv')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3d42e07f",
   "metadata": {},
   "source": [
    "# EDA(탐색적 데이터 분석)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "a77534a0",
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
       "      <th>Gender</th>\n",
       "      <th>Height</th>\n",
       "      <th>Weight</th>\n",
       "      <th>Label</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Male</td>\n",
       "      <td>174</td>\n",
       "      <td>96</td>\n",
       "      <td>Obesity</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Male</td>\n",
       "      <td>189</td>\n",
       "      <td>87</td>\n",
       "      <td>Normal</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Female</td>\n",
       "      <td>185</td>\n",
       "      <td>110</td>\n",
       "      <td>Obesity</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Female</td>\n",
       "      <td>195</td>\n",
       "      <td>104</td>\n",
       "      <td>Overweight</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Male</td>\n",
       "      <td>149</td>\n",
       "      <td>61</td>\n",
       "      <td>Overweight</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Male</td>\n",
       "      <td>189</td>\n",
       "      <td>104</td>\n",
       "      <td>Overweight</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Male</td>\n",
       "      <td>147</td>\n",
       "      <td>92</td>\n",
       "      <td>Extreme Obesity</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Male</td>\n",
       "      <td>154</td>\n",
       "      <td>111</td>\n",
       "      <td>Extreme Obesity</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Male</td>\n",
       "      <td>174</td>\n",
       "      <td>90</td>\n",
       "      <td>Overweight</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Gender  Height  Weight            Label\n",
       "0    Male     174      96          Obesity\n",
       "1    Male     189      87           Normal\n",
       "2  Female     185     110          Obesity\n",
       "3  Female     195     104       Overweight\n",
       "4    Male     149      61       Overweight\n",
       "5    Male     189     104       Overweight\n",
       "6    Male     147      92  Extreme Obesity\n",
       "7    Male     154     111  Extreme Obesity\n",
       "8    Male     174      90       Overweight"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 처음부터 일부 데이터를 확인\n",
    "# 괄호안에 숫자를 입력하면 해당 숫자만큼 출력\n",
    "bmi.head(9)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "6796323c",
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
       "      <th>Gender</th>\n",
       "      <th>Height</th>\n",
       "      <th>Weight</th>\n",
       "      <th>Label</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>495</th>\n",
       "      <td>Female</td>\n",
       "      <td>150</td>\n",
       "      <td>153</td>\n",
       "      <td>Extreme Obesity</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>496</th>\n",
       "      <td>Female</td>\n",
       "      <td>184</td>\n",
       "      <td>121</td>\n",
       "      <td>Obesity</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>497</th>\n",
       "      <td>Female</td>\n",
       "      <td>141</td>\n",
       "      <td>136</td>\n",
       "      <td>Extreme Obesity</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>498</th>\n",
       "      <td>Male</td>\n",
       "      <td>150</td>\n",
       "      <td>95</td>\n",
       "      <td>Extreme Obesity</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>499</th>\n",
       "      <td>Male</td>\n",
       "      <td>173</td>\n",
       "      <td>131</td>\n",
       "      <td>Extreme Obesity</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     Gender  Height  Weight            Label\n",
       "495  Female     150     153  Extreme Obesity\n",
       "496  Female     184     121          Obesity\n",
       "497  Female     141     136  Extreme Obesity\n",
       "498    Male     150      95  Extreme Obesity\n",
       "499    Male     173     131  Extreme Obesity"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 끝에서부터 일부 데이터를 확인\n",
    "bmi.tail()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "f0419392",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 500 entries, 0 to 499\n",
      "Data columns (total 4 columns):\n",
      " #   Column  Non-Null Count  Dtype \n",
      "---  ------  --------------  ----- \n",
      " 0   Gender  500 non-null    object\n",
      " 1   Height  500 non-null    int64 \n",
      " 2   Weight  500 non-null    int64 \n",
      " 3   Label   500 non-null    object\n",
      "dtypes: int64(2), object(2)\n",
      "memory usage: 15.8+ KB\n"
     ]
    }
   ],
   "source": [
    "# 데이터의 정보를 출력하는 함수\n",
    "# 데이터의 수, 컬럼의 수,컬럼의 특성/데이터 타입 - 결측치 확인\n",
    "# Dtype : object(범주형), int / float (수치형)\n",
    "bmi.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "83a0cf7a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['Male', 'Female'], dtype=object)"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 범주형 컬럼의 클래스의 목록을 출력하는 함수 중복제거\n",
    "bmi[\"Gender\"].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "66c42d88",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Female    255\n",
       "Male      245\n",
       "Name: Gender, dtype: int64"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 범주형 컬럼의 클래스별 갯수를 확인\n",
    "# 데이터가 한쪽으로 치우쳐 있는지 확인가능\n",
    "bmi[\"Gender\"].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "8688db8b",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-0.12191368980139153\n",
      "-0.037692236922098034\n"
     ]
    }
   ],
   "source": [
    "# 수치형 데이터의 편향(치우침)을 확인하는 함수\n",
    "# 0이면 정규분포\n",
    "# 양수이면 왼쪽으로 치우친 데이터이고 음수이면 오른쪽으로 치우친 데이터를 표시\n",
    "print(bmi[\"Height\"].skew())\n",
    "print(bmi[\"Weight\"].skew())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "5c6cac60",
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
       "      <th>Height</th>\n",
       "      <th>Weight</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>500.000000</td>\n",
       "      <td>500.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>169.944000</td>\n",
       "      <td>106.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>16.375261</td>\n",
       "      <td>32.382607</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>140.000000</td>\n",
       "      <td>50.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>156.000000</td>\n",
       "      <td>80.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>170.500000</td>\n",
       "      <td>106.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>184.000000</td>\n",
       "      <td>136.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>199.000000</td>\n",
       "      <td>160.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           Height      Weight\n",
       "count  500.000000  500.000000\n",
       "mean   169.944000  106.000000\n",
       "std     16.375261   32.382607\n",
       "min    140.000000   50.000000\n",
       "25%    156.000000   80.000000\n",
       "50%    170.500000  106.000000\n",
       "75%    184.000000  136.000000\n",
       "max    199.000000  160.000000"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 데이터의 간단한 기술통계를 보여주는 함수\n",
    "# 데이터의 개수, 평균, 표준편차, 최소/25%/중간값/75%/최대값\n",
    "# 결측치, 이상치, 편향(치우침정도) 을 알수있음\n",
    "bmi.describe()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5a16062a",
   "metadata": {},
   "source": [
    "## BMI 데이터가 분류가 될 수 있는 데이터인지 확인"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "e7e0d3c8",
   "metadata": {},
   "outputs": [],
   "source": [
    "# matplotlib : 파이썬 그래프 시각화 도구\n",
    "# seaborn : matplotlib에 고급 시각화 도구를 제공\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# scatter : 산포도를 그리는 함수(2차원 좌표에 점을 찍는 함수)\n",
    "# x 좌표 : Weight, y 좌표 : Height\n",
    "def myScatter(label, color):\n",
    "    # 파라미터로 넘어온 라벨의 해당 값들을 저장 - 불리언 인덱싱\n",
    "    tmp = bmi[bmi[\"Label\"] == label]\n",
    "    \n",
    "    # 입력한 라벨값만 산포도를 그림\n",
    "    # scatter(x좌표, y좌표, 색상, 라벨)\n",
    "    plt.scatter(tmp['Weight'],tmp[\"Height\"],\n",
    "               c = color, label = label)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "acd34641",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['Obesity', 'Normal', 'Overweight', 'Extreme Obesity', 'Weak',\n",
       "       'Extremely Weak'], dtype=object)"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bmi[\"Label\"].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "50545e3a",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "image/png": "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NXbD+vqz2eN+G6xxezasevU85/Z/AqM99psLXFPR8c8++2zTEKxYsaKuixBcYqIxVngwK6ZPd/9u7HZj4uPL73veRIzJyHAfwm4PvFv4tzID1xsYZWCXgVLnz1HGbrcbrCuP+zZ9+nQTHx9vEhMTzfVgdtvtpgys9+IsV0ZGhom1qgcR3UTEAGbUKExBQdX+BVasmF7BPucZY2Iq2CfRGOM61xOC7DPB8wMNcax4502c+00wxsSaFSumm++++8AY87UxZp0xZr/PH8l+5/avrdtPXxvz2dfGrPS4fbbOmJ/2O/fd4Nx3g/fzKrjZbDbTtWtH9+21154yxmwwS5c+b3r2vMC8+upsM3jwJe79mzZt4v591673jIiYL76YZ4z52nz00XPm5puvNmVla0xp6Vdm2LC+5tNPF5tdu3YZu91uNm7caEpLS02PHj3MjTfeaMrKysy7775rhg8fbowxZurUqWbBggXGGGMOHjxoOnbsaAoKCsyKFSvMsGHDjDHGPPTQQ+bpp582xhjz0UcfmREjRpgjR454nbkVK1aY/v37G2OM6du3r8nPzzcXXHCBMcaYm266ycydO9d89NFH5uabbzZlZWWmtLTUDBs2zHz66afGGGPy8vKMMcYUFhaazp07m/37rc+madOm5qeffjK9evUyS5cuNaF89913ftuAtaYKf9y1OqrKGLPXGFNqjCnDWuuyl/OhHKyvJi7tgR9rs2wnrWA5uufPhwNBJowZ45Uxt6IpHvHxVuUleIqn/cBCrCG3HSifr/Eq/fr180ssaLPZmDFjBpmZmQzNyKBv+/bYgKicHGT0aJKSkgBrMl5iqHXOfcTGxnLrrbeSmJjItGn+WWqr31Yqrk14JiucCUzAOj84f04A+lC+jGwB/iOcYp37HcPqH3BNOPwX/s1ann0BVq4oq7nJhrsmsosAXQhlsCsb/07pcJvaypuqXLdrr/010I6BAyfRuXMXJk2awosv/otgXbOJiadz8cVWLXjp0i9ZuvQrundPoUePMXz/fRbbt68BttKhQwJdunTBZrPRuXNnBgwYgIjQpUsXdyqapUuX8vjjj9OtWzf69etHUVGR37Dt8ePH88orrwAwb948r9qAS69evfj22285evQoJ06coFmzZpx55pns2LGDzz//nEsuuYSlS5eydOlSunfvTo8ePfj+++/Zvn07AM8+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\n",
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
    "# 그래프의 크기 설정\n",
    "# plt.figure(figsize=(10,10))\n",
    "\n",
    "myScatter(\"Obesity\",\"black\")\n",
    "myScatter(\"Normal\",\"red\")\n",
    "myScatter(\"Overweight\",\"blue\")\n",
    "myScatter(\"Extreme Obesity\",\"yellow\")\n",
    "myScatter(\"Weak\",\"green\")\n",
    "myScatter(\"Extremely Weak\",\"pink\")\n",
    "\n",
    "\n",
    "# 범례 추가 (loc : 범례의 위치)\n",
    "# loc를 써주지 않으면 알아서 데이터가 가장 작게 분포된 위치에 표시\n",
    "plt.legend(loc = \"upper right\")\n",
    "\n",
    "# x축 라벨 표시(기본적으로 한글은 지원하지 않음)\n",
    "plt.xlabel(\"Weight\")\n",
    "\n",
    "# y축 라벨 표시(기본적으로 한글은 지원하지 않음)\n",
    "plt.ylabel(\"Height\")\n",
    "\n",
    "# x축 눈금의 범위\n",
    "plt.xlim(0,200)\n",
    "\n",
    "# y축 눈금의 범위\n",
    "plt.ylim(0,250)\n",
    "\n",
    "# 제목 표시\n",
    "plt.title(\"BMI data\")\n",
    "\n",
    "# 격자 표시\n",
    "plt.grid()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "24d8ca49",
   "metadata": {},
   "source": [
    "## 학습 데이터로 변환\n",
    "- 특성데이터와 라벨데이터로 분리\n",
    "- 훈련데이터와 테스터데이터로 분리"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "c3b0d9ab",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "350.0"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "500*0.7"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "6f0b195e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "((500, 2), (500,))"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 특성데이터와 라벨데이터로 분리\n",
    "bmi_X = bmi.loc[:,\"Height\":\"Weight\"]\n",
    "bmi_y = bmi.loc[:,\"Label\"]\n",
    "\n",
    "bmi_X.shape, bmi_y.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "82137ebe",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "((350, 2), (350,), (150, 2), (150,))"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 훈련데이터와 테스트데이터로 분리 (훈련 70%, 테스트 30%)\n",
    "X_train = bmi_X.iloc[:350,:]\n",
    "y_train = bmi_y.iloc[:350]\n",
    "X_test = bmi_X.iloc[350:,:]\n",
    "y_test = bmi_y.iloc[350:]\n",
    "\n",
    "X_train.shape,y_train.shape,X_test.shape,y_test.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3d1d79bd",
   "metadata": {},
   "source": [
    "# KNN으로 BMI 데이터 학습"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "4d42078d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "KNeighborsClassifier(n_neighbors=3)"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.neighbors import KNeighborsClassifier\n",
    "\n",
    "# n_neighbors : 이웃의 수\n",
    "# 이웃의 수가 적으면 과대적합\n",
    "# 이웃의 수가 많으면 과소적합\n",
    "# Hyper Parameter Tuning : 적당한 이웃의 수를 결정하는 것\n",
    "knn_model = KNeighborsClassifier(n_neighbors=3)\n",
    "# 훈련은 훈련데이터로\n",
    "knn_model.fit(X_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "d25a8c5e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "훈련 정확도 :  0.9342857142857143\n",
      "테스트 정확도 :  0.9\n"
     ]
    }
   ],
   "source": [
    "# 정확도 계산\n",
    "# 훈련정확도와 테스트정확도가 모두 낮으면 -> 과소적합\n",
    "# 훈련정확도보다 테스트정확도가 높으면 -> 과소적합\n",
    "# 훈련정확도와 테스트정확도가 크게 차이나면 -> 과대적합\n",
    "# 일반화모델 : 훈련정확도가 테스트정확도보다 약간 높은 모델\n",
    "print(\"훈련 정확도 : \",knn_model.score(X_train,y_train))\n",
    "print(\"테스트 정확도 : \",knn_model.score(X_test,y_test))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "43effb6b",
   "metadata": {},
   "source": [
    "- 이웃의 수가 감소하면 과대적합이 생김"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "cfc2dba6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "훈련 정확도 :  1.0\n",
      "테스트 정확도 :  0.8933333333333333\n"
     ]
    }
   ],
   "source": [
    "knn_model2 = KNeighborsClassifier(n_neighbors=1)\n",
    "knn_model2.fit(X_train,y_train)\n",
    "\n",
    "print(\"훈련 정확도 : \",knn_model2.score(X_train,y_train))\n",
    "print(\"테스트 정확도 : \",knn_model2.score(X_test,y_test))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "aa552012",
   "metadata": {},
   "source": [
    "- 이웃의 수가 증가하면 과소적합이 생김"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "31c13b62",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "훈련 정확도 :  0.9085714285714286\n",
      "테스트 정확도 :  0.94\n"
     ]
    }
   ],
   "source": [
    "knn_model3 = KNeighborsClassifier(n_neighbors=10)\n",
    "knn_model3.fit(X_train,y_train)\n",
    "\n",
    "print(\"훈련 정확도 : \",knn_model3.score(X_train,y_train))\n",
    "print(\"테스트 정확도 : \",knn_model3.score(X_test,y_test))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "af9649e2",
   "metadata": {},
   "source": [
    "- 일반화된 모델을 찾아보자 - 하이퍼파라미터 튜닝"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "7e3a4a84",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 이웃의 수마다의 정확도\n",
    "train_acc = []\n",
    "test_acc = []\n",
    "\n",
    "# 사용할 이웃의 범위 값들을 정의\n",
    "neighbor = range(1,20)\n",
    "\n",
    "for i in neighbor:\n",
    "    knn_model3 = KNeighborsClassifier(n_neighbors=i)\n",
    "    knn_model3.fit(X_train,y_train)\n",
    "    \n",
    "    # 이웃의 수마다의 훈련데이터 정확도와 테스트데이터 정확도를 리스트에 저장\n",
    "    train_acc.append(knn_model3.score(X_train,y_train))\n",
    "    test_acc.append(knn_model3.score(X_test,y_test))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "8f474d3a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.legend.Legend at 0x2925e7e91f0>"
      ]
     },
     "execution_count": 22,
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
    "# 시각화\n",
    "x = train_acc\n",
    "y = test_acc\n",
    "plt.plot(neighbor,x, label=\"Train\")\n",
    "plt.plot(neighbor,y, label=\"Test\")\n",
    "plt.legend()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "497ab6c5",
   "metadata": {},
   "source": [
    "- 특성의 수를 증가시켜서 과소적합을 줄여보자"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "05a8671e",
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
       "      <th>Gender</th>\n",
       "      <th>Height</th>\n",
       "      <th>Weight</th>\n",
       "      <th>Label</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Male</td>\n",
       "      <td>174</td>\n",
       "      <td>96</td>\n",
       "      <td>Obesity</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Male</td>\n",
       "      <td>189</td>\n",
       "      <td>87</td>\n",
       "      <td>Normal</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Female</td>\n",
       "      <td>185</td>\n",
       "      <td>110</td>\n",
       "      <td>Obesity</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Female</td>\n",
       "      <td>195</td>\n",
       "      <td>104</td>\n",
       "      <td>Overweight</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Male</td>\n",
       "      <td>149</td>\n",
       "      <td>61</td>\n",
       "      <td>Overweight</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Gender  Height  Weight       Label\n",
       "0    Male     174      96     Obesity\n",
       "1    Male     189      87      Normal\n",
       "2  Female     185     110     Obesity\n",
       "3  Female     195     104  Overweight\n",
       "4    Male     149      61  Overweight"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bmi.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "278335a1",
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
       "      <th>Gender</th>\n",
       "      <th>Height</th>\n",
       "      <th>Weight</th>\n",
       "      <th>Label</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>174</td>\n",
       "      <td>96</td>\n",
       "      <td>Obesity</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0</td>\n",
       "      <td>189</td>\n",
       "      <td>87</td>\n",
       "      <td>Normal</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>185</td>\n",
       "      <td>110</td>\n",
       "      <td>Obesity</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>195</td>\n",
       "      <td>104</td>\n",
       "      <td>Overweight</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0</td>\n",
       "      <td>149</td>\n",
       "      <td>61</td>\n",
       "      <td>Overweight</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>495</th>\n",
       "      <td>1</td>\n",
       "      <td>150</td>\n",
       "      <td>153</td>\n",
       "      <td>Extreme Obesity</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>496</th>\n",
       "      <td>1</td>\n",
       "      <td>184</td>\n",
       "      <td>121</td>\n",
       "      <td>Obesity</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>497</th>\n",
       "      <td>1</td>\n",
       "      <td>141</td>\n",
       "      <td>136</td>\n",
       "      <td>Extreme Obesity</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>498</th>\n",
       "      <td>0</td>\n",
       "      <td>150</td>\n",
       "      <td>95</td>\n",
       "      <td>Extreme Obesity</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>499</th>\n",
       "      <td>0</td>\n",
       "      <td>173</td>\n",
       "      <td>131</td>\n",
       "      <td>Extreme Obesity</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>500 rows × 4 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     Gender  Height  Weight            Label\n",
       "0         0     174      96          Obesity\n",
       "1         0     189      87           Normal\n",
       "2         1     185     110          Obesity\n",
       "3         1     195     104       Overweight\n",
       "4         0     149      61       Overweight\n",
       "..      ...     ...     ...              ...\n",
       "495       1     150     153  Extreme Obesity\n",
       "496       1     184     121          Obesity\n",
       "497       1     141     136  Extreme Obesity\n",
       "498       0     150      95  Extreme Obesity\n",
       "499       0     173     131  Extreme Obesity\n",
       "\n",
       "[500 rows x 4 columns]"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Gender 컬럼에서 Male -> 0으로 Female -> 1로 변경\n",
    "# bmi1=bmi['Gender'].replace(['Male','Female'],[0,1])\n",
    "bmi['Gender'] = bmi['Gender'].replace(\"Male\",0).replace(\"Female\",1)\n",
    "bmi"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "43ae1dac",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "((500, 3), (500,))"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 특성데이터와 라벨데이터로 분리\n",
    "bmi_X = bmi.loc[:,\"Gender\":\"Weight\"]\n",
    "bmi_y = bmi.loc[:,\"Label\"]\n",
    "\n",
    "bmi_X.shape, bmi_y.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "41877672",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "((350, 3), (350,), (150, 3), (150,))"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 훈련데이터와 테스트데이터로 분리 (훈련 70%, 테스트 30%)\n",
    "X_train = bmi_X.iloc[:350,:]\n",
    "y_train = bmi_y.iloc[:350]\n",
    "X_test = bmi_X.iloc[350:,:]\n",
    "y_test = bmi_y.iloc[350:]\n",
    "\n",
    "X_train.shape,y_train.shape,X_test.shape,y_test.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "097425d3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "훈련 정확도 :  0.9085714285714286\n",
      "테스트 정확도 :  0.9266666666666666\n"
     ]
    }
   ],
   "source": [
    "knn_model3 = KNeighborsClassifier(n_neighbors=10)\n",
    "knn_model3.fit(X_train,y_train)\n",
    "\n",
    "print(\"훈련 정확도 : \",knn_model3.score(X_train,y_train))\n",
    "print(\"테스트 정확도 : \",knn_model3.score(X_test,y_test))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "4455e473",
   "metadata": {},
   "outputs": [],
   "source": [
    "train_acc = []\n",
    "test_acc = []\n",
    "\n",
    "# 사용할 이웃의 범위 값들을 정의\n",
    "neighbor = range(1,20)\n",
    "\n",
    "for i in neighbor:\n",
    "    knn_model3 = KNeighborsClassifier(n_neighbors=i)\n",
    "    knn_model3.fit(X_train,y_train)\n",
    "    \n",
    "    # 이웃의 수마다의 훈련데이터 정확도와 테스트데이터 정확도를 리스트에 저장\n",
    "    train_acc.append(knn_model3.score(X_train,y_train))\n",
    "    test_acc.append(knn_model3.score(X_test,y_test))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "3890be50",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.legend.Legend at 0x2925e861430>"
      ]
     },
     "execution_count": 29,
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
    "x = train_acc\n",
    "y = test_acc\n",
    "plt.plot(neighbor,x, label =\"Train\")\n",
    "plt.plot(neighbor,y, label =\"Test\")\n",
    "plt.legend()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f8494ea5",
   "metadata": {},
   "source": [
    "- 특성들끼리 각각 곱해서 새로운 특성을 추가"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "455a1a64",
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
       "      <th>Gender</th>\n",
       "      <th>Height</th>\n",
       "      <th>Weight</th>\n",
       "      <th>Gender*Gender</th>\n",
       "      <th>Gender*Height</th>\n",
       "      <th>Gender*Weight</th>\n",
       "      <th>Height*Height</th>\n",
       "      <th>Height*Weight</th>\n",
       "      <th>Weight*Weight</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>174</td>\n",
       "      <td>96</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>30276</td>\n",
       "      <td>16704</td>\n",
       "      <td>9216</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0</td>\n",
       "      <td>189</td>\n",
       "      <td>87</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>35721</td>\n",
       "      <td>16443</td>\n",
       "      <td>7569</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>185</td>\n",
       "      <td>110</td>\n",
       "      <td>1</td>\n",
       "      <td>185</td>\n",
       "      <td>110</td>\n",
       "      <td>34225</td>\n",
       "      <td>20350</td>\n",
       "      <td>12100</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>195</td>\n",
       "      <td>104</td>\n",
       "      <td>1</td>\n",
       "      <td>195</td>\n",
       "      <td>104</td>\n",
       "      <td>38025</td>\n",
       "      <td>20280</td>\n",
       "      <td>10816</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0</td>\n",
       "      <td>149</td>\n",
       "      <td>61</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>22201</td>\n",
       "      <td>9089</td>\n",
       "      <td>3721</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Gender  Height  Weight  Gender*Gender  Gender*Height  Gender*Weight  \\\n",
       "0       0     174      96              0              0              0   \n",
       "1       0     189      87              0              0              0   \n",
       "2       1     185     110              1            185            110   \n",
       "3       1     195     104              1            195            104   \n",
       "4       0     149      61              0              0              0   \n",
       "\n",
       "   Height*Height  Height*Weight  Weight*Weight  \n",
       "0          30276          16704           9216  \n",
       "1          35721          16443           7569  \n",
       "2          34225          20350          12100  \n",
       "3          38025          20280          10816  \n",
       "4          22201           9089           3721  "
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_train2 = X_train.copy()\n",
    "\n",
    "# 컬럼의 이름들을 가져온다\n",
    "col = X_train2.columns\n",
    "\n",
    "for i in range(col.size):\n",
    "    for j in range(i,col.size):\n",
    "        X_train2[col[i]+'*'+col[j]] = X_train2[col[i]]*X_train2[col[j]]\n",
    "\n",
    "X_train2.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "bf8bbdfc",
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
       "      <th>Gender</th>\n",
       "      <th>Height</th>\n",
       "      <th>Weight</th>\n",
       "      <th>Gender*Gender</th>\n",
       "      <th>Gender*Height</th>\n",
       "      <th>Gender*Weight</th>\n",
       "      <th>Height*Height</th>\n",
       "      <th>Height*Weight</th>\n",
       "      <th>Weight*Weight</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>350</th>\n",
       "      <td>0</td>\n",
       "      <td>184</td>\n",
       "      <td>83</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>33856</td>\n",
       "      <td>15272</td>\n",
       "      <td>6889</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>351</th>\n",
       "      <td>0</td>\n",
       "      <td>197</td>\n",
       "      <td>88</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>38809</td>\n",
       "      <td>17336</td>\n",
       "      <td>7744</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>352</th>\n",
       "      <td>1</td>\n",
       "      <td>160</td>\n",
       "      <td>51</td>\n",
       "      <td>1</td>\n",
       "      <td>160</td>\n",
       "      <td>51</td>\n",
       "      <td>25600</td>\n",
       "      <td>8160</td>\n",
       "      <td>2601</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>353</th>\n",
       "      <td>0</td>\n",
       "      <td>184</td>\n",
       "      <td>153</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>33856</td>\n",
       "      <td>28152</td>\n",
       "      <td>23409</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>354</th>\n",
       "      <td>0</td>\n",
       "      <td>190</td>\n",
       "      <td>50</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>36100</td>\n",
       "      <td>9500</td>\n",
       "      <td>2500</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     Gender  Height  Weight  Gender*Gender  Gender*Height  Gender*Weight  \\\n",
       "350       0     184      83              0              0              0   \n",
       "351       0     197      88              0              0              0   \n",
       "352       1     160      51              1            160             51   \n",
       "353       0     184     153              0              0              0   \n",
       "354       0     190      50              0              0              0   \n",
       "\n",
       "     Height*Height  Height*Weight  Weight*Weight  \n",
       "350          33856          15272           6889  \n",
       "351          38809          17336           7744  \n",
       "352          25600           8160           2601  \n",
       "353          33856          28152          23409  \n",
       "354          36100           9500           2500  "
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_test2 = X_test.copy()\n",
    "\n",
    "# 컬럼의 이름들을 가져온다\n",
    "col = X_test2.columns\n",
    "\n",
    "for i in range(col.size):\n",
    "    for j in range(i,col.size):\n",
    "        X_test2[col[i]+'*'+col[j]] = X_test2[col[i]]*X_test2[col[j]]\n",
    "\n",
    "X_test2.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "153a2770",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.legend.Legend at 0x2925e8e08b0>"
      ]
     },
     "execution_count": 32,
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
    "train_acc = []\n",
    "test_acc = []\n",
    "\n",
    "# 사용할 이웃의 범위 값들을 정의\n",
    "neighbor = range(1,20)\n",
    "\n",
    "for i in neighbor:\n",
    "    knn_model3 = KNeighborsClassifier(n_neighbors=i)\n",
    "    knn_model3.fit(X_train2,y_train)\n",
    "    \n",
    "    # 이웃의 수마다의 훈련데이터 정확도와 테스트데이터 정확도를 리스트에 저장\n",
    "    train_acc.append(knn_model3.score(X_train2,y_train))\n",
    "    test_acc.append(knn_model3.score(X_test2,y_test))\n",
    "    \n",
    "x = train_acc\n",
    "y = test_acc\n",
    "plt.plot(neighbor,x, label =\"Train\")\n",
    "plt.plot(neighbor,y, label =\"Test\")\n",
    "plt.legend()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7f0524fe",
   "metadata": {},
   "source": [
    "# 보스턴집값 데이터를 이용한 KNN 회귀"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f770ec75",
   "metadata": {},
   "source": [
    "## 문제정의\n",
    "\n",
    "- 보스턴 집값 데이터에서 어떤 특성이 집값에 얼마만큼 영향을 주는지 분석\n",
    "- 다중 공선성 문제에 대한 이해\n",
    "- KNN을 이용한 회귀분석"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4557f9a3",
   "metadata": {},
   "source": [
    "## 데이터 수집"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "21aa10aa",
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
    },
    {
     "data": {
      "text/plain": [
       "dict_keys(['data', 'target', 'feature_names', 'DESCR', 'filename', 'data_module'])"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# sklearn에서는 교육용 데이터셋으로 딕셔너리형태로 데이터를 제공\n",
    "from sklearn.datasets import load_boston\n",
    "\n",
    "boston = load_boston()\n",
    "\n",
    "boston.keys()\n",
    "# data : 특성데이터\n",
    "# target : 라벨 데이터\n",
    "# feature_names : 컬럼명\n",
    "# DESCR : 컬럼에 대한 설명"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4c081546",
   "metadata": {},
   "source": [
    "## 데이터 시각화 및 분석\n",
    "\n",
    "- 딕셔너리를 데이터프레임으로 변환\n",
    "- 특성과 라벨 간의 상관관계 분석\n",
    "- 분석 결과를 히트맵으로 시각화"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "c477b4c5",
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
       "      <th>CRIM</th>\n",
       "      <th>ZN</th>\n",
       "      <th>INDUS</th>\n",
       "      <th>CHAS</th>\n",
       "      <th>NOX</th>\n",
       "      <th>RM</th>\n",
       "      <th>AGE</th>\n",
       "      <th>DIS</th>\n",
       "      <th>RAD</th>\n",
       "      <th>TAX</th>\n",
       "      <th>PTRATIO</th>\n",
       "      <th>B</th>\n",
       "      <th>LSTAT</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0.00632</td>\n",
       "      <td>18.0</td>\n",
       "      <td>2.31</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.538</td>\n",
       "      <td>6.575</td>\n",
       "      <td>65.2</td>\n",
       "      <td>4.0900</td>\n",
       "      <td>1.0</td>\n",
       "      <td>296.0</td>\n",
       "      <td>15.3</td>\n",
       "      <td>396.90</td>\n",
       "      <td>4.98</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0.02731</td>\n",
       "      <td>0.0</td>\n",
       "      <td>7.07</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.469</td>\n",
       "      <td>6.421</td>\n",
       "      <td>78.9</td>\n",
       "      <td>4.9671</td>\n",
       "      <td>2.0</td>\n",
       "      <td>242.0</td>\n",
       "      <td>17.8</td>\n",
       "      <td>396.90</td>\n",
       "      <td>9.14</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0.02729</td>\n",
       "      <td>0.0</td>\n",
       "      <td>7.07</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.469</td>\n",
       "      <td>7.185</td>\n",
       "      <td>61.1</td>\n",
       "      <td>4.9671</td>\n",
       "      <td>2.0</td>\n",
       "      <td>242.0</td>\n",
       "      <td>17.8</td>\n",
       "      <td>392.83</td>\n",
       "      <td>4.03</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0.03237</td>\n",
       "      <td>0.0</td>\n",
       "      <td>2.18</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.458</td>\n",
       "      <td>6.998</td>\n",
       "      <td>45.8</td>\n",
       "      <td>6.0622</td>\n",
       "      <td>3.0</td>\n",
       "      <td>222.0</td>\n",
       "      <td>18.7</td>\n",
       "      <td>394.63</td>\n",
       "      <td>2.94</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0.06905</td>\n",
       "      <td>0.0</td>\n",
       "      <td>2.18</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.458</td>\n",
       "      <td>7.147</td>\n",
       "      <td>54.2</td>\n",
       "      <td>6.0622</td>\n",
       "      <td>3.0</td>\n",
       "      <td>222.0</td>\n",
       "      <td>18.7</td>\n",
       "      <td>396.90</td>\n",
       "      <td>5.33</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      CRIM    ZN  INDUS  CHAS    NOX     RM   AGE     DIS  RAD    TAX  \\\n",
       "0  0.00632  18.0   2.31   0.0  0.538  6.575  65.2  4.0900  1.0  296.0   \n",
       "1  0.02731   0.0   7.07   0.0  0.469  6.421  78.9  4.9671  2.0  242.0   \n",
       "2  0.02729   0.0   7.07   0.0  0.469  7.185  61.1  4.9671  2.0  242.0   \n",
       "3  0.03237   0.0   2.18   0.0  0.458  6.998  45.8  6.0622  3.0  222.0   \n",
       "4  0.06905   0.0   2.18   0.0  0.458  7.147  54.2  6.0622  3.0  222.0   \n",
       "\n",
       "   PTRATIO       B  LSTAT  \n",
       "0     15.3  396.90   4.98  \n",
       "1     17.8  396.90   9.14  \n",
       "2     17.8  392.83   4.03  \n",
       "3     18.7  394.63   2.94  \n",
       "4     18.7  396.90   5.33  "
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "df_feature = pd.DataFrame(boston['data'],columns=boston['feature_names'])\n",
    "\n",
    "df_feature.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "1073bce5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 506 entries, 0 to 505\n",
      "Data columns (total 13 columns):\n",
      " #   Column   Non-Null Count  Dtype  \n",
      "---  ------   --------------  -----  \n",
      " 0   CRIM     506 non-null    float64\n",
      " 1   ZN       506 non-null    float64\n",
      " 2   INDUS    506 non-null    float64\n",
      " 3   CHAS     506 non-null    float64\n",
      " 4   NOX      506 non-null    float64\n",
      " 5   RM       506 non-null    float64\n",
      " 6   AGE      506 non-null    float64\n",
      " 7   DIS      506 non-null    float64\n",
      " 8   RAD      506 non-null    float64\n",
      " 9   TAX      506 non-null    float64\n",
      " 10  PTRATIO  506 non-null    float64\n",
      " 11  B        506 non-null    float64\n",
      " 12  LSTAT    506 non-null    float64\n",
      "dtypes: float64(13)\n",
      "memory usage: 51.5 KB\n"
     ]
    }
   ],
   "source": [
    "df_feature.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "f38517fc",
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
       "      <th>CRIM</th>\n",
       "      <th>ZN</th>\n",
       "      <th>INDUS</th>\n",
       "      <th>CHAS</th>\n",
       "      <th>NOX</th>\n",
       "      <th>RM</th>\n",
       "      <th>AGE</th>\n",
       "      <th>DIS</th>\n",
       "      <th>RAD</th>\n",
       "      <th>TAX</th>\n",
       "      <th>PTRATIO</th>\n",
       "      <th>B</th>\n",
       "      <th>LSTAT</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>506.000000</td>\n",
       "      <td>506.000000</td>\n",
       "      <td>506.000000</td>\n",
       "      <td>506.000000</td>\n",
       "      <td>506.000000</td>\n",
       "      <td>506.000000</td>\n",
       "      <td>506.000000</td>\n",
       "      <td>506.000000</td>\n",
       "      <td>506.000000</td>\n",
       "      <td>506.000000</td>\n",
       "      <td>506.000000</td>\n",
       "      <td>506.000000</td>\n",
       "      <td>506.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>3.613524</td>\n",
       "      <td>11.363636</td>\n",
       "      <td>11.136779</td>\n",
       "      <td>0.069170</td>\n",
       "      <td>0.554695</td>\n",
       "      <td>6.284634</td>\n",
       "      <td>68.574901</td>\n",
       "      <td>3.795043</td>\n",
       "      <td>9.549407</td>\n",
       "      <td>408.237154</td>\n",
       "      <td>18.455534</td>\n",
       "      <td>356.674032</td>\n",
       "      <td>12.653063</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>8.601545</td>\n",
       "      <td>23.322453</td>\n",
       "      <td>6.860353</td>\n",
       "      <td>0.253994</td>\n",
       "      <td>0.115878</td>\n",
       "      <td>0.702617</td>\n",
       "      <td>28.148861</td>\n",
       "      <td>2.105710</td>\n",
       "      <td>8.707259</td>\n",
       "      <td>168.537116</td>\n",
       "      <td>2.164946</td>\n",
       "      <td>91.294864</td>\n",
       "      <td>7.141062</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>0.006320</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.460000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.385000</td>\n",
       "      <td>3.561000</td>\n",
       "      <td>2.900000</td>\n",
       "      <td>1.129600</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>187.000000</td>\n",
       "      <td>12.600000</td>\n",
       "      <td>0.320000</td>\n",
       "      <td>1.730000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>0.082045</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>5.190000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.449000</td>\n",
       "      <td>5.885500</td>\n",
       "      <td>45.025000</td>\n",
       "      <td>2.100175</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>279.000000</td>\n",
       "      <td>17.400000</td>\n",
       "      <td>375.377500</td>\n",
       "      <td>6.950000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>0.256510</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>9.690000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.538000</td>\n",
       "      <td>6.208500</td>\n",
       "      <td>77.500000</td>\n",
       "      <td>3.207450</td>\n",
       "      <td>5.000000</td>\n",
       "      <td>330.000000</td>\n",
       "      <td>19.050000</td>\n",
       "      <td>391.440000</td>\n",
       "      <td>11.360000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>3.677083</td>\n",
       "      <td>12.500000</td>\n",
       "      <td>18.100000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.624000</td>\n",
       "      <td>6.623500</td>\n",
       "      <td>94.075000</td>\n",
       "      <td>5.188425</td>\n",
       "      <td>24.000000</td>\n",
       "      <td>666.000000</td>\n",
       "      <td>20.200000</td>\n",
       "      <td>396.225000</td>\n",
       "      <td>16.955000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>88.976200</td>\n",
       "      <td>100.000000</td>\n",
       "      <td>27.740000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.871000</td>\n",
       "      <td>8.780000</td>\n",
       "      <td>100.000000</td>\n",
       "      <td>12.126500</td>\n",
       "      <td>24.000000</td>\n",
       "      <td>711.000000</td>\n",
       "      <td>22.000000</td>\n",
       "      <td>396.900000</td>\n",
       "      <td>37.970000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             CRIM          ZN       INDUS        CHAS         NOX          RM  \\\n",
       "count  506.000000  506.000000  506.000000  506.000000  506.000000  506.000000   \n",
       "mean     3.613524   11.363636   11.136779    0.069170    0.554695    6.284634   \n",
       "std      8.601545   23.322453    6.860353    0.253994    0.115878    0.702617   \n",
       "min      0.006320    0.000000    0.460000    0.000000    0.385000    3.561000   \n",
       "25%      0.082045    0.000000    5.190000    0.000000    0.449000    5.885500   \n",
       "50%      0.256510    0.000000    9.690000    0.000000    0.538000    6.208500   \n",
       "75%      3.677083   12.500000   18.100000    0.000000    0.624000    6.623500   \n",
       "max     88.976200  100.000000   27.740000    1.000000    0.871000    8.780000   \n",
       "\n",
       "              AGE         DIS         RAD         TAX     PTRATIO           B  \\\n",
       "count  506.000000  506.000000  506.000000  506.000000  506.000000  506.000000   \n",
       "mean    68.574901    3.795043    9.549407  408.237154   18.455534  356.674032   \n",
       "std     28.148861    2.105710    8.707259  168.537116    2.164946   91.294864   \n",
       "min      2.900000    1.129600    1.000000  187.000000   12.600000    0.320000   \n",
       "25%     45.025000    2.100175    4.000000  279.000000   17.400000  375.377500   \n",
       "50%     77.500000    3.207450    5.000000  330.000000   19.050000  391.440000   \n",
       "75%     94.075000    5.188425   24.000000  666.000000   20.200000  396.225000   \n",
       "max    100.000000   12.126500   24.000000  711.000000   22.000000  396.900000   \n",
       "\n",
       "            LSTAT  \n",
       "count  506.000000  \n",
       "mean    12.653063  \n",
       "std      7.141062  \n",
       "min      1.730000  \n",
       "25%      6.950000  \n",
       "50%     11.360000  \n",
       "75%     16.955000  \n",
       "max     37.970000  "
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_feature.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "5eaf1353",
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
       "      <th>price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>24.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>21.6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>34.7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>33.4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>36.2</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   price\n",
       "0   24.0\n",
       "1   21.6\n",
       "2   34.7\n",
       "3   33.4\n",
       "4   36.2"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_label = pd.DataFrame(boston['target'], columns=['price'])\n",
    "\n",
    "df_label.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "0cf56f53",
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
       "      <th>CRIM</th>\n",
       "      <th>ZN</th>\n",
       "      <th>INDUS</th>\n",
       "      <th>CHAS</th>\n",
       "      <th>NOX</th>\n",
       "      <th>RM</th>\n",
       "      <th>AGE</th>\n",
       "      <th>DIS</th>\n",
       "      <th>RAD</th>\n",
       "      <th>TAX</th>\n",
       "      <th>PTRATIO</th>\n",
       "      <th>B</th>\n",
       "      <th>LSTAT</th>\n",
       "      <th>price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0.00632</td>\n",
       "      <td>18.0</td>\n",
       "      <td>2.31</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.538</td>\n",
       "      <td>6.575</td>\n",
       "      <td>65.2</td>\n",
       "      <td>4.0900</td>\n",
       "      <td>1.0</td>\n",
       "      <td>296.0</td>\n",
       "      <td>15.3</td>\n",
       "      <td>396.90</td>\n",
       "      <td>4.98</td>\n",
       "      <td>24.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0.02731</td>\n",
       "      <td>0.0</td>\n",
       "      <td>7.07</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.469</td>\n",
       "      <td>6.421</td>\n",
       "      <td>78.9</td>\n",
       "      <td>4.9671</td>\n",
       "      <td>2.0</td>\n",
       "      <td>242.0</td>\n",
       "      <td>17.8</td>\n",
       "      <td>396.90</td>\n",
       "      <td>9.14</td>\n",
       "      <td>21.6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0.02729</td>\n",
       "      <td>0.0</td>\n",
       "      <td>7.07</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.469</td>\n",
       "      <td>7.185</td>\n",
       "      <td>61.1</td>\n",
       "      <td>4.9671</td>\n",
       "      <td>2.0</td>\n",
       "      <td>242.0</td>\n",
       "      <td>17.8</td>\n",
       "      <td>392.83</td>\n",
       "      <td>4.03</td>\n",
       "      <td>34.7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0.03237</td>\n",
       "      <td>0.0</td>\n",
       "      <td>2.18</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.458</td>\n",
       "      <td>6.998</td>\n",
       "      <td>45.8</td>\n",
       "      <td>6.0622</td>\n",
       "      <td>3.0</td>\n",
       "      <td>222.0</td>\n",
       "      <td>18.7</td>\n",
       "      <td>394.63</td>\n",
       "      <td>2.94</td>\n",
       "      <td>33.4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0.06905</td>\n",
       "      <td>0.0</td>\n",
       "      <td>2.18</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.458</td>\n",
       "      <td>7.147</td>\n",
       "      <td>54.2</td>\n",
       "      <td>6.0622</td>\n",
       "      <td>3.0</td>\n",
       "      <td>222.0</td>\n",
       "      <td>18.7</td>\n",
       "      <td>396.90</td>\n",
       "      <td>5.33</td>\n",
       "      <td>36.2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>501</th>\n",
       "      <td>0.06263</td>\n",
       "      <td>0.0</td>\n",
       "      <td>11.93</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.573</td>\n",
       "      <td>6.593</td>\n",
       "      <td>69.1</td>\n",
       "      <td>2.4786</td>\n",
       "      <td>1.0</td>\n",
       "      <td>273.0</td>\n",
       "      <td>21.0</td>\n",
       "      <td>391.99</td>\n",
       "      <td>9.67</td>\n",
       "      <td>22.4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>502</th>\n",
       "      <td>0.04527</td>\n",
       "      <td>0.0</td>\n",
       "      <td>11.93</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.573</td>\n",
       "      <td>6.120</td>\n",
       "      <td>76.7</td>\n",
       "      <td>2.2875</td>\n",
       "      <td>1.0</td>\n",
       "      <td>273.0</td>\n",
       "      <td>21.0</td>\n",
       "      <td>396.90</td>\n",
       "      <td>9.08</td>\n",
       "      <td>20.6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>503</th>\n",
       "      <td>0.06076</td>\n",
       "      <td>0.0</td>\n",
       "      <td>11.93</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.573</td>\n",
       "      <td>6.976</td>\n",
       "      <td>91.0</td>\n",
       "      <td>2.1675</td>\n",
       "      <td>1.0</td>\n",
       "      <td>273.0</td>\n",
       "      <td>21.0</td>\n",
       "      <td>396.90</td>\n",
       "      <td>5.64</td>\n",
       "      <td>23.9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>504</th>\n",
       "      <td>0.10959</td>\n",
       "      <td>0.0</td>\n",
       "      <td>11.93</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.573</td>\n",
       "      <td>6.794</td>\n",
       "      <td>89.3</td>\n",
       "      <td>2.3889</td>\n",
       "      <td>1.0</td>\n",
       "      <td>273.0</td>\n",
       "      <td>21.0</td>\n",
       "      <td>393.45</td>\n",
       "      <td>6.48</td>\n",
       "      <td>22.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>505</th>\n",
       "      <td>0.04741</td>\n",
       "      <td>0.0</td>\n",
       "      <td>11.93</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.573</td>\n",
       "      <td>6.030</td>\n",
       "      <td>80.8</td>\n",
       "      <td>2.5050</td>\n",
       "      <td>1.0</td>\n",
       "      <td>273.0</td>\n",
       "      <td>21.0</td>\n",
       "      <td>396.90</td>\n",
       "      <td>7.88</td>\n",
       "      <td>11.9</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>506 rows × 14 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "        CRIM    ZN  INDUS  CHAS    NOX     RM   AGE     DIS  RAD    TAX  \\\n",
       "0    0.00632  18.0   2.31   0.0  0.538  6.575  65.2  4.0900  1.0  296.0   \n",
       "1    0.02731   0.0   7.07   0.0  0.469  6.421  78.9  4.9671  2.0  242.0   \n",
       "2    0.02729   0.0   7.07   0.0  0.469  7.185  61.1  4.9671  2.0  242.0   \n",
       "3    0.03237   0.0   2.18   0.0  0.458  6.998  45.8  6.0622  3.0  222.0   \n",
       "4    0.06905   0.0   2.18   0.0  0.458  7.147  54.2  6.0622  3.0  222.0   \n",
       "..       ...   ...    ...   ...    ...    ...   ...     ...  ...    ...   \n",
       "501  0.06263   0.0  11.93   0.0  0.573  6.593  69.1  2.4786  1.0  273.0   \n",
       "502  0.04527   0.0  11.93   0.0  0.573  6.120  76.7  2.2875  1.0  273.0   \n",
       "503  0.06076   0.0  11.93   0.0  0.573  6.976  91.0  2.1675  1.0  273.0   \n",
       "504  0.10959   0.0  11.93   0.0  0.573  6.794  89.3  2.3889  1.0  273.0   \n",
       "505  0.04741   0.0  11.93   0.0  0.573  6.030  80.8  2.5050  1.0  273.0   \n",
       "\n",
       "     PTRATIO       B  LSTAT  price  \n",
       "0       15.3  396.90   4.98   24.0  \n",
       "1       17.8  396.90   9.14   21.6  \n",
       "2       17.8  392.83   4.03   34.7  \n",
       "3       18.7  394.63   2.94   33.4  \n",
       "4       18.7  396.90   5.33   36.2  \n",
       "..       ...     ...    ...    ...  \n",
       "501     21.0  391.99   9.67   22.4  \n",
       "502     21.0  396.90   9.08   20.6  \n",
       "503     21.0  396.90   5.64   23.9  \n",
       "504     21.0  393.45   6.48   22.0  \n",
       "505     21.0  396.90   7.88   11.9  \n",
       "\n",
       "[506 rows x 14 columns]"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 특성데이터와 라벨데이터를 하나의 데이터프레임으로 병합\n",
    "# axis=1 : 열 방향으로 병합\n",
    "df_boston = pd.concat([df_feature,df_label],axis=1)\n",
    "df_boston"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "df080495",
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
       "      <th>CRIM</th>\n",
       "      <th>ZN</th>\n",
       "      <th>INDUS</th>\n",
       "      <th>CHAS</th>\n",
       "      <th>NOX</th>\n",
       "      <th>RM</th>\n",
       "      <th>AGE</th>\n",
       "      <th>DIS</th>\n",
       "      <th>RAD</th>\n",
       "      <th>TAX</th>\n",
       "      <th>PTRATIO</th>\n",
       "      <th>B</th>\n",
       "      <th>LSTAT</th>\n",
       "      <th>price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>CRIM</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.200469</td>\n",
       "      <td>0.406583</td>\n",
       "      <td>-0.055892</td>\n",
       "      <td>0.420972</td>\n",
       "      <td>-0.219247</td>\n",
       "      <td>0.352734</td>\n",
       "      <td>-0.379670</td>\n",
       "      <td>0.625505</td>\n",
       "      <td>0.582764</td>\n",
       "      <td>0.289946</td>\n",
       "      <td>-0.385064</td>\n",
       "      <td>0.455621</td>\n",
       "      <td>-0.388305</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>ZN</th>\n",
       "      <td>-0.200469</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.533828</td>\n",
       "      <td>-0.042697</td>\n",
       "      <td>-0.516604</td>\n",
       "      <td>0.311991</td>\n",
       "      <td>-0.569537</td>\n",
       "      <td>0.664408</td>\n",
       "      <td>-0.311948</td>\n",
       "      <td>-0.314563</td>\n",
       "      <td>-0.391679</td>\n",
       "      <td>0.175520</td>\n",
       "      <td>-0.412995</td>\n",
       "      <td>0.360445</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>INDUS</th>\n",
       "      <td>0.406583</td>\n",
       "      <td>-0.533828</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.062938</td>\n",
       "      <td>0.763651</td>\n",
       "      <td>-0.391676</td>\n",
       "      <td>0.644779</td>\n",
       "      <td>-0.708027</td>\n",
       "      <td>0.595129</td>\n",
       "      <td>0.720760</td>\n",
       "      <td>0.383248</td>\n",
       "      <td>-0.356977</td>\n",
       "      <td>0.603800</td>\n",
       "      <td>-0.483725</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>CHAS</th>\n",
       "      <td>-0.055892</td>\n",
       "      <td>-0.042697</td>\n",
       "      <td>0.062938</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.091203</td>\n",
       "      <td>0.091251</td>\n",
       "      <td>0.086518</td>\n",
       "      <td>-0.099176</td>\n",
       "      <td>-0.007368</td>\n",
       "      <td>-0.035587</td>\n",
       "      <td>-0.121515</td>\n",
       "      <td>0.048788</td>\n",
       "      <td>-0.053929</td>\n",
       "      <td>0.175260</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>NOX</th>\n",
       "      <td>0.420972</td>\n",
       "      <td>-0.516604</td>\n",
       "      <td>0.763651</td>\n",
       "      <td>0.091203</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.302188</td>\n",
       "      <td>0.731470</td>\n",
       "      <td>-0.769230</td>\n",
       "      <td>0.611441</td>\n",
       "      <td>0.668023</td>\n",
       "      <td>0.188933</td>\n",
       "      <td>-0.380051</td>\n",
       "      <td>0.590879</td>\n",
       "      <td>-0.427321</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>RM</th>\n",
       "      <td>-0.219247</td>\n",
       "      <td>0.311991</td>\n",
       "      <td>-0.391676</td>\n",
       "      <td>0.091251</td>\n",
       "      <td>-0.302188</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.240265</td>\n",
       "      <td>0.205246</td>\n",
       "      <td>-0.209847</td>\n",
       "      <td>-0.292048</td>\n",
       "      <td>-0.355501</td>\n",
       "      <td>0.128069</td>\n",
       "      <td>-0.613808</td>\n",
       "      <td>0.695360</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>AGE</th>\n",
       "      <td>0.352734</td>\n",
       "      <td>-0.569537</td>\n",
       "      <td>0.644779</td>\n",
       "      <td>0.086518</td>\n",
       "      <td>0.731470</td>\n",
       "      <td>-0.240265</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.747881</td>\n",
       "      <td>0.456022</td>\n",
       "      <td>0.506456</td>\n",
       "      <td>0.261515</td>\n",
       "      <td>-0.273534</td>\n",
       "      <td>0.602339</td>\n",
       "      <td>-0.376955</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>DIS</th>\n",
       "      <td>-0.379670</td>\n",
       "      <td>0.664408</td>\n",
       "      <td>-0.708027</td>\n",
       "      <td>-0.099176</td>\n",
       "      <td>-0.769230</td>\n",
       "      <td>0.205246</td>\n",
       "      <td>-0.747881</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.494588</td>\n",
       "      <td>-0.534432</td>\n",
       "      <td>-0.232471</td>\n",
       "      <td>0.291512</td>\n",
       "      <td>-0.496996</td>\n",
       "      <td>0.249929</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>RAD</th>\n",
       "      <td>0.625505</td>\n",
       "      <td>-0.311948</td>\n",
       "      <td>0.595129</td>\n",
       "      <td>-0.007368</td>\n",
       "      <td>0.611441</td>\n",
       "      <td>-0.209847</td>\n",
       "      <td>0.456022</td>\n",
       "      <td>-0.494588</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.910228</td>\n",
       "      <td>0.464741</td>\n",
       "      <td>-0.444413</td>\n",
       "      <td>0.488676</td>\n",
       "      <td>-0.381626</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>TAX</th>\n",
       "      <td>0.582764</td>\n",
       "      <td>-0.314563</td>\n",
       "      <td>0.720760</td>\n",
       "      <td>-0.035587</td>\n",
       "      <td>0.668023</td>\n",
       "      <td>-0.292048</td>\n",
       "      <td>0.506456</td>\n",
       "      <td>-0.534432</td>\n",
       "      <td>0.910228</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.460853</td>\n",
       "      <td>-0.441808</td>\n",
       "      <td>0.543993</td>\n",
       "      <td>-0.468536</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>PTRATIO</th>\n",
       "      <td>0.289946</td>\n",
       "      <td>-0.391679</td>\n",
       "      <td>0.383248</td>\n",
       "      <td>-0.121515</td>\n",
       "      <td>0.188933</td>\n",
       "      <td>-0.355501</td>\n",
       "      <td>0.261515</td>\n",
       "      <td>-0.232471</td>\n",
       "      <td>0.464741</td>\n",
       "      <td>0.460853</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.177383</td>\n",
       "      <td>0.374044</td>\n",
       "      <td>-0.507787</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>B</th>\n",
       "      <td>-0.385064</td>\n",
       "      <td>0.175520</td>\n",
       "      <td>-0.356977</td>\n",
       "      <td>0.048788</td>\n",
       "      <td>-0.380051</td>\n",
       "      <td>0.128069</td>\n",
       "      <td>-0.273534</td>\n",
       "      <td>0.291512</td>\n",
       "      <td>-0.444413</td>\n",
       "      <td>-0.441808</td>\n",
       "      <td>-0.177383</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.366087</td>\n",
       "      <td>0.333461</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>LSTAT</th>\n",
       "      <td>0.455621</td>\n",
       "      <td>-0.412995</td>\n",
       "      <td>0.603800</td>\n",
       "      <td>-0.053929</td>\n",
       "      <td>0.590879</td>\n",
       "      <td>-0.613808</td>\n",
       "      <td>0.602339</td>\n",
       "      <td>-0.496996</td>\n",
       "      <td>0.488676</td>\n",
       "      <td>0.543993</td>\n",
       "      <td>0.374044</td>\n",
       "      <td>-0.366087</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.737663</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>price</th>\n",
       "      <td>-0.388305</td>\n",
       "      <td>0.360445</td>\n",
       "      <td>-0.483725</td>\n",
       "      <td>0.175260</td>\n",
       "      <td>-0.427321</td>\n",
       "      <td>0.695360</td>\n",
       "      <td>-0.376955</td>\n",
       "      <td>0.249929</td>\n",
       "      <td>-0.381626</td>\n",
       "      <td>-0.468536</td>\n",
       "      <td>-0.507787</td>\n",
       "      <td>0.333461</td>\n",
       "      <td>-0.737663</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             CRIM        ZN     INDUS      CHAS       NOX        RM       AGE  \\\n",
       "CRIM     1.000000 -0.200469  0.406583 -0.055892  0.420972 -0.219247  0.352734   \n",
       "ZN      -0.200469  1.000000 -0.533828 -0.042697 -0.516604  0.311991 -0.569537   \n",
       "INDUS    0.406583 -0.533828  1.000000  0.062938  0.763651 -0.391676  0.644779   \n",
       "CHAS    -0.055892 -0.042697  0.062938  1.000000  0.091203  0.091251  0.086518   \n",
       "NOX      0.420972 -0.516604  0.763651  0.091203  1.000000 -0.302188  0.731470   \n",
       "RM      -0.219247  0.311991 -0.391676  0.091251 -0.302188  1.000000 -0.240265   \n",
       "AGE      0.352734 -0.569537  0.644779  0.086518  0.731470 -0.240265  1.000000   \n",
       "DIS     -0.379670  0.664408 -0.708027 -0.099176 -0.769230  0.205246 -0.747881   \n",
       "RAD      0.625505 -0.311948  0.595129 -0.007368  0.611441 -0.209847  0.456022   \n",
       "TAX      0.582764 -0.314563  0.720760 -0.035587  0.668023 -0.292048  0.506456   \n",
       "PTRATIO  0.289946 -0.391679  0.383248 -0.121515  0.188933 -0.355501  0.261515   \n",
       "B       -0.385064  0.175520 -0.356977  0.048788 -0.380051  0.128069 -0.273534   \n",
       "LSTAT    0.455621 -0.412995  0.603800 -0.053929  0.590879 -0.613808  0.602339   \n",
       "price   -0.388305  0.360445 -0.483725  0.175260 -0.427321  0.695360 -0.376955   \n",
       "\n",
       "              DIS       RAD       TAX   PTRATIO         B     LSTAT     price  \n",
       "CRIM    -0.379670  0.625505  0.582764  0.289946 -0.385064  0.455621 -0.388305  \n",
       "ZN       0.664408 -0.311948 -0.314563 -0.391679  0.175520 -0.412995  0.360445  \n",
       "INDUS   -0.708027  0.595129  0.720760  0.383248 -0.356977  0.603800 -0.483725  \n",
       "CHAS    -0.099176 -0.007368 -0.035587 -0.121515  0.048788 -0.053929  0.175260  \n",
       "NOX     -0.769230  0.611441  0.668023  0.188933 -0.380051  0.590879 -0.427321  \n",
       "RM       0.205246 -0.209847 -0.292048 -0.355501  0.128069 -0.613808  0.695360  \n",
       "AGE     -0.747881  0.456022  0.506456  0.261515 -0.273534  0.602339 -0.376955  \n",
       "DIS      1.000000 -0.494588 -0.534432 -0.232471  0.291512 -0.496996  0.249929  \n",
       "RAD     -0.494588  1.000000  0.910228  0.464741 -0.444413  0.488676 -0.381626  \n",
       "TAX     -0.534432  0.910228  1.000000  0.460853 -0.441808  0.543993 -0.468536  \n",
       "PTRATIO -0.232471  0.464741  0.460853  1.000000 -0.177383  0.374044 -0.507787  \n",
       "B        0.291512 -0.444413 -0.441808 -0.177383  1.000000 -0.366087  0.333461  \n",
       "LSTAT   -0.496996  0.488676  0.543993  0.374044 -0.366087  1.000000 -0.737663  \n",
       "price    0.249929 -0.381626 -0.468536 -0.507787  0.333461 -0.737663  1.000000  "
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 특성과 라벨의 상관관계 분석\n",
    "df_boston.corr()\n",
    "\n",
    "# 양의 값 : 집 값을 올리는 정도\n",
    "# 음의 값 : 집 값을 떨어뜨리는 정도\n",
    "# 0에 가까운 값 : 집 값과 관련이 없는 특성 -> 삭제, 처리 후에 사용\n",
    "\n",
    "# 다중공선성\n",
    "#      - 특성간의 공선성 (데이터의 유사성) 문제\n",
    "#      - 특성과 특성 간의 상관관계가 90% 이상인 것\n",
    "#      - 특성과 라벨 간의 상관관계가 더 낮은 특성을 삭제하거나 처리 -> 해결방법\n",
    "#      - 특성과 라벨의 공선성 (데이터의 유사성) 문제\n",
    "#      - 특성과 라벨간의 상관관계가 90% 이상인 것\n",
    "#      - 해당 특성을 삭제하거나 처리"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b9cfa411",
   "metadata": {},
   "source": [
    "- train_test_split : 훈련데이터와 테스트데이터를 분리해주는 함수\n",
    "    - 훈련 75%, 테스트 25%로 분리"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "5f2c5198",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "((379, 13), (127, 13), (379,), (127,))"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "\n",
    "# random_state : 랜덤 시드를 설정 (항상 같은 데이터셋을 사용하기 위한 것)\n",
    "X_train, X_test, y_train, y_test = train_test_split(boston['data'],\n",
    "                                                   boston['target'],\n",
    "                                                    random_state = 7)\n",
    "X_train.shape, X_test.shape, y_train.shape, y_test.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "99bc1948",
   "metadata": {},
   "source": [
    "# 모델 선택 및 훈련"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "b98ad57c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "KNeighborsRegressor()"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.neighbors import KNeighborsRegressor\n",
    "\n",
    "knn_model4 = KNeighborsRegressor(n_neighbors=5)\n",
    "knn_model4.fit(X_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "d5a9a77b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "훈련오차 : 25.2812073878628\n",
      "테스트 오차 : 40.725077165354335\n"
     ]
    }
   ],
   "source": [
    "# 평가 (회귀분석에서 평가도구로 오차)\n",
    "# 오차가 적으면 좋은 모델 인가요?\n",
    "# 1번 모델의 오차 : 10,- 100 => -90\n",
    "# 2번 모델의 오차 : 2, 3 => 5\n",
    "# -> 음수오차로 인해서 직접 비교하기 어려운 문제\n",
    "# -> 음수를 양수로 변경하는 방법 : \n",
    "#               제곱 -> 평균제곱오차 (Mean Squared Error : MSE)\n",
    "#               절대값 -> 평균절대값오차 (Mean Absolute Error : MAE)\n",
    "# MSE를 더 사용하는 이유 : 제곱하기때문에 좋은 모델과 나쁜 모델을 구분하기 쉬움\n",
    "from sklearn.metrics import mean_squared_error\n",
    "\n",
    "pred_train = knn_model4.predict(X_train)\n",
    "pred_test = knn_model4.predict(X_test)\n",
    "\n",
    "print(\"훈련오차 :\",mean_squared_error(pred_train,y_train))\n",
    "print(\"테스트 오차 :\",mean_squared_error(pred_test,y_test))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "939ef5f8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "훈련 오차 : 5.028042102833149\n",
      "테스트 오차 : 6.381620261763805\n"
     ]
    }
   ],
   "source": [
    "# MSE는 제곱을 한 값이라 원래 값이 아님 -> 제곱근 사용\n",
    "import numpy as np\n",
    "\n",
    "print(\"훈련 오차 :\",np.sqrt(mean_squared_error(pred_train,y_train)))\n",
    "print(\"테스트 오차 :\",np.sqrt(mean_squared_error(pred_test,y_test)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b1e0abe3",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "58c8dcb7",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "11094b87",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8dd6420f",
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
