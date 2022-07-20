{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "fd473088",
   "metadata": {},
   "source": [
    "# 문제정의"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "86247aa6",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f242c8d0",
   "metadata": {},
   "source": [
    "# 데이터 수집"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "49cb021f",
   "metadata": {},
   "outputs": [],
   "source": [
    "train = pd.read_csv(\"data/class_train.csv\",index_col='no')\n",
    "test = pd.read_csv(\"data/class_test.csv\",index_col='no')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3799151a",
   "metadata": {},
   "source": [
    "# 탐색적 데이터 분석 및 전처리"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "2c9ae4a9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "((29305, 15), (19537, 14))"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train.shape, test.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "41aeac06",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Int64Index: 29305 entries, 1 to 29305\n",
      "Data columns (total 15 columns):\n",
      " #   Column          Non-Null Count  Dtype \n",
      "---  ------          --------------  ----- \n",
      " 0   age             29305 non-null  int64 \n",
      " 1   workclass       29305 non-null  object\n",
      " 2   fnlwgt          29305 non-null  int64 \n",
      " 3   education       29305 non-null  object\n",
      " 4   education-num   29305 non-null  int64 \n",
      " 5   marital-status  29305 non-null  object\n",
      " 6   occupation      29305 non-null  object\n",
      " 7   relationship    29305 non-null  object\n",
      " 8   race            29305 non-null  object\n",
      " 9   sex             29305 non-null  object\n",
      " 10  capital-gain    29305 non-null  int64 \n",
      " 11  capital-loss    29305 non-null  int64 \n",
      " 12  hours-per-week  29305 non-null  int64 \n",
      " 13  native-country  29305 non-null  object\n",
      " 14  income          29305 non-null  int64 \n",
      "dtypes: int64(7), object(8)\n",
      "memory usage: 3.6+ MB\n"
     ]
    }
   ],
   "source": [
    "train.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "9a3d5253",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Int64Index: 19537 entries, 29306 to 48842\n",
      "Data columns (total 14 columns):\n",
      " #   Column          Non-Null Count  Dtype \n",
      "---  ------          --------------  ----- \n",
      " 0   age             19537 non-null  int64 \n",
      " 1   workclass       19537 non-null  object\n",
      " 2   fnlwgt          19537 non-null  int64 \n",
      " 3   education       19537 non-null  object\n",
      " 4   education-num   19537 non-null  int64 \n",
      " 5   marital-status  19537 non-null  object\n",
      " 6   occupation      19537 non-null  object\n",
      " 7   relationship    19537 non-null  object\n",
      " 8   race            19537 non-null  object\n",
      " 9   sex             19537 non-null  object\n",
      " 10  capital-gain    19537 non-null  int64 \n",
      " 11  capital-loss    19537 non-null  int64 \n",
      " 12  hours-per-week  19537 non-null  int64 \n",
      " 13  native-country  19537 non-null  object\n",
      "dtypes: int64(6), object(8)\n",
      "memory usage: 2.2+ MB\n"
     ]
    }
   ],
   "source": [
    "test.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "d21a1954",
   "metadata": {
    "scrolled": true
   },
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
       "      <th>age</th>\n",
       "      <th>workclass</th>\n",
       "      <th>fnlwgt</th>\n",
       "      <th>education</th>\n",
       "      <th>education-num</th>\n",
       "      <th>marital-status</th>\n",
       "      <th>occupation</th>\n",
       "      <th>relationship</th>\n",
       "      <th>race</th>\n",
       "      <th>sex</th>\n",
       "      <th>capital-gain</th>\n",
       "      <th>capital-loss</th>\n",
       "      <th>hours-per-week</th>\n",
       "      <th>native-country</th>\n",
       "      <th>income</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>no</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>25</td>\n",
       "      <td>Private</td>\n",
       "      <td>219199</td>\n",
       "      <td>11th</td>\n",
       "      <td>7</td>\n",
       "      <td>Divorced</td>\n",
       "      <td>Machine-op-inspct</td>\n",
       "      <td>Not-in-family</td>\n",
       "      <td>White</td>\n",
       "      <td>Male</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>40</td>\n",
       "      <td>United-States</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>39</td>\n",
       "      <td>Private</td>\n",
       "      <td>52978</td>\n",
       "      <td>Some-college</td>\n",
       "      <td>10</td>\n",
       "      <td>Divorced</td>\n",
       "      <td>Other-service</td>\n",
       "      <td>Not-in-family</td>\n",
       "      <td>White</td>\n",
       "      <td>Female</td>\n",
       "      <td>0</td>\n",
       "      <td>1721</td>\n",
       "      <td>55</td>\n",
       "      <td>United-States</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>35</td>\n",
       "      <td>Private</td>\n",
       "      <td>196899</td>\n",
       "      <td>Bachelors</td>\n",
       "      <td>13</td>\n",
       "      <td>Never-married</td>\n",
       "      <td>Handlers-cleaners</td>\n",
       "      <td>Not-in-family</td>\n",
       "      <td>Asian-Pac-Islander</td>\n",
       "      <td>Female</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>50</td>\n",
       "      <td>Haiti</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>64</td>\n",
       "      <td>Private</td>\n",
       "      <td>135527</td>\n",
       "      <td>Assoc-voc</td>\n",
       "      <td>11</td>\n",
       "      <td>Divorced</td>\n",
       "      <td>Tech-support</td>\n",
       "      <td>Not-in-family</td>\n",
       "      <td>White</td>\n",
       "      <td>Female</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>40</td>\n",
       "      <td>United-States</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>24</td>\n",
       "      <td>Private</td>\n",
       "      <td>60783</td>\n",
       "      <td>Some-college</td>\n",
       "      <td>10</td>\n",
       "      <td>Married-civ-spouse</td>\n",
       "      <td>Transport-moving</td>\n",
       "      <td>Husband</td>\n",
       "      <td>White</td>\n",
       "      <td>Male</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>70</td>\n",
       "      <td>United-States</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    age workclass  fnlwgt      education  education-num       marital-status  \\\n",
       "no                                                                             \n",
       "1    25   Private  219199           11th              7             Divorced   \n",
       "2    39   Private   52978   Some-college             10             Divorced   \n",
       "3    35   Private  196899      Bachelors             13        Never-married   \n",
       "4    64   Private  135527      Assoc-voc             11             Divorced   \n",
       "5    24   Private   60783   Some-college             10   Married-civ-spouse   \n",
       "\n",
       "            occupation    relationship                 race      sex  \\\n",
       "no                                                                     \n",
       "1    Machine-op-inspct   Not-in-family                White     Male   \n",
       "2        Other-service   Not-in-family                White   Female   \n",
       "3    Handlers-cleaners   Not-in-family   Asian-Pac-Islander   Female   \n",
       "4         Tech-support   Not-in-family                White   Female   \n",
       "5     Transport-moving         Husband                White     Male   \n",
       "\n",
       "    capital-gain  capital-loss  hours-per-week  native-country  income  \n",
       "no                                                                      \n",
       "1              0             0              40   United-States       0  \n",
       "2              0          1721              55   United-States       0  \n",
       "3              0             0              50           Haiti       0  \n",
       "4              0             0              40   United-States       0  \n",
       "5              0             0              70   United-States       1  "
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "7afbfcfb",
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
       "      <th>age</th>\n",
       "      <th>workclass</th>\n",
       "      <th>fnlwgt</th>\n",
       "      <th>education</th>\n",
       "      <th>education-num</th>\n",
       "      <th>marital-status</th>\n",
       "      <th>occupation</th>\n",
       "      <th>relationship</th>\n",
       "      <th>race</th>\n",
       "      <th>sex</th>\n",
       "      <th>capital-gain</th>\n",
       "      <th>capital-loss</th>\n",
       "      <th>hours-per-week</th>\n",
       "      <th>native-country</th>\n",
       "      <th>income</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>no</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>29301</th>\n",
       "      <td>20</td>\n",
       "      <td>Private</td>\n",
       "      <td>100605</td>\n",
       "      <td>HS-grad</td>\n",
       "      <td>9</td>\n",
       "      <td>Never-married</td>\n",
       "      <td>Sales</td>\n",
       "      <td>Own-child</td>\n",
       "      <td>Other</td>\n",
       "      <td>Male</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>40</td>\n",
       "      <td>Puerto-Rico</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>29302</th>\n",
       "      <td>21</td>\n",
       "      <td>Private</td>\n",
       "      <td>372636</td>\n",
       "      <td>HS-grad</td>\n",
       "      <td>9</td>\n",
       "      <td>Never-married</td>\n",
       "      <td>Sales</td>\n",
       "      <td>Own-child</td>\n",
       "      <td>Black</td>\n",
       "      <td>Male</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>40</td>\n",
       "      <td>United-States</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>29303</th>\n",
       "      <td>18</td>\n",
       "      <td>Self-emp-not-inc</td>\n",
       "      <td>258474</td>\n",
       "      <td>10th</td>\n",
       "      <td>6</td>\n",
       "      <td>Never-married</td>\n",
       "      <td>Farming-fishing</td>\n",
       "      <td>Own-child</td>\n",
       "      <td>White</td>\n",
       "      <td>Male</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>40</td>\n",
       "      <td>United-States</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>29304</th>\n",
       "      <td>33</td>\n",
       "      <td>Private</td>\n",
       "      <td>157446</td>\n",
       "      <td>11th</td>\n",
       "      <td>7</td>\n",
       "      <td>Never-married</td>\n",
       "      <td>Craft-repair</td>\n",
       "      <td>Not-in-family</td>\n",
       "      <td>White</td>\n",
       "      <td>Male</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>65</td>\n",
       "      <td>United-States</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>29305</th>\n",
       "      <td>65</td>\n",
       "      <td>?</td>\n",
       "      <td>94809</td>\n",
       "      <td>HS-grad</td>\n",
       "      <td>9</td>\n",
       "      <td>Widowed</td>\n",
       "      <td>?</td>\n",
       "      <td>Not-in-family</td>\n",
       "      <td>White</td>\n",
       "      <td>Female</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>40</td>\n",
       "      <td>United-States</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       age          workclass  fnlwgt education  education-num  \\\n",
       "no                                                               \n",
       "29301   20            Private  100605   HS-grad              9   \n",
       "29302   21            Private  372636   HS-grad              9   \n",
       "29303   18   Self-emp-not-inc  258474      10th              6   \n",
       "29304   33            Private  157446      11th              7   \n",
       "29305   65                  ?   94809   HS-grad              9   \n",
       "\n",
       "       marital-status        occupation    relationship    race      sex  \\\n",
       "no                                                                         \n",
       "29301   Never-married             Sales       Own-child   Other     Male   \n",
       "29302   Never-married             Sales       Own-child   Black     Male   \n",
       "29303   Never-married   Farming-fishing       Own-child   White     Male   \n",
       "29304   Never-married      Craft-repair   Not-in-family   White     Male   \n",
       "29305         Widowed                 ?   Not-in-family   White   Female   \n",
       "\n",
       "       capital-gain  capital-loss  hours-per-week  native-country  income  \n",
       "no                                                                         \n",
       "29301             0             0              40     Puerto-Rico       0  \n",
       "29302             0             0              40   United-States       0  \n",
       "29303             0             0              40   United-States       0  \n",
       "29304             0             0              65   United-States       0  \n",
       "29305             0             0              40   United-States       0  "
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train.tail()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "10dbf7a7",
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
       "      <th>age</th>\n",
       "      <th>fnlwgt</th>\n",
       "      <th>education-num</th>\n",
       "      <th>capital-gain</th>\n",
       "      <th>capital-loss</th>\n",
       "      <th>hours-per-week</th>\n",
       "      <th>income</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>29305.000000</td>\n",
       "      <td>2.930500e+04</td>\n",
       "      <td>29305.000000</td>\n",
       "      <td>29305.000000</td>\n",
       "      <td>29305.000000</td>\n",
       "      <td>29305.000000</td>\n",
       "      <td>29305.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>38.659171</td>\n",
       "      <td>1.897357e+05</td>\n",
       "      <td>10.083057</td>\n",
       "      <td>1084.531786</td>\n",
       "      <td>87.073571</td>\n",
       "      <td>40.440096</td>\n",
       "      <td>0.240403</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>13.743827</td>\n",
       "      <td>1.056348e+05</td>\n",
       "      <td>2.570371</td>\n",
       "      <td>7495.715677</td>\n",
       "      <td>401.225580</td>\n",
       "      <td>12.332840</td>\n",
       "      <td>0.427335</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>17.000000</td>\n",
       "      <td>1.376900e+04</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>28.000000</td>\n",
       "      <td>1.176060e+05</td>\n",
       "      <td>9.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>40.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>37.000000</td>\n",
       "      <td>1.779550e+05</td>\n",
       "      <td>10.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>40.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>48.000000</td>\n",
       "      <td>2.377130e+05</td>\n",
       "      <td>12.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>45.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>90.000000</td>\n",
       "      <td>1.490400e+06</td>\n",
       "      <td>16.000000</td>\n",
       "      <td>99999.000000</td>\n",
       "      <td>4356.000000</td>\n",
       "      <td>99.000000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                age        fnlwgt  education-num  capital-gain  capital-loss  \\\n",
       "count  29305.000000  2.930500e+04   29305.000000  29305.000000  29305.000000   \n",
       "mean      38.659171  1.897357e+05      10.083057   1084.531786     87.073571   \n",
       "std       13.743827  1.056348e+05       2.570371   7495.715677    401.225580   \n",
       "min       17.000000  1.376900e+04       1.000000      0.000000      0.000000   \n",
       "25%       28.000000  1.176060e+05       9.000000      0.000000      0.000000   \n",
       "50%       37.000000  1.779550e+05      10.000000      0.000000      0.000000   \n",
       "75%       48.000000  2.377130e+05      12.000000      0.000000      0.000000   \n",
       "max       90.000000  1.490400e+06      16.000000  99999.000000   4356.000000   \n",
       "\n",
       "       hours-per-week        income  \n",
       "count    29305.000000  29305.000000  \n",
       "mean        40.440096      0.240403  \n",
       "std         12.332840      0.427335  \n",
       "min          1.000000      0.000000  \n",
       "25%         40.000000      0.000000  \n",
       "50%         40.000000      0.000000  \n",
       "75%         45.000000      0.000000  \n",
       "max         99.000000      1.000000  "
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "9bfd3fa5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['age', 'workclass', 'fnlwgt', 'education', 'education-num',\n",
       "       'marital-status', 'occupation', 'relationship', 'race', 'sex',\n",
       "       'capital-gain', 'capital-loss', 'hours-per-week', 'native-country',\n",
       "       'income'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "a8c7e930",
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
       "      <th>age</th>\n",
       "      <th>fnlwgt</th>\n",
       "      <th>education-num</th>\n",
       "      <th>capital-gain</th>\n",
       "      <th>capital-loss</th>\n",
       "      <th>hours-per-week</th>\n",
       "      <th>income</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>age</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.075753</td>\n",
       "      <td>0.035084</td>\n",
       "      <td>0.078498</td>\n",
       "      <td>0.054413</td>\n",
       "      <td>0.073100</td>\n",
       "      <td>0.238460</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>fnlwgt</th>\n",
       "      <td>-0.075753</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.030600</td>\n",
       "      <td>-0.005051</td>\n",
       "      <td>-0.001513</td>\n",
       "      <td>-0.010154</td>\n",
       "      <td>-0.002994</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>education-num</th>\n",
       "      <td>0.035084</td>\n",
       "      <td>-0.030600</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.127651</td>\n",
       "      <td>0.083925</td>\n",
       "      <td>0.147569</td>\n",
       "      <td>0.331798</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>capital-gain</th>\n",
       "      <td>0.078498</td>\n",
       "      <td>-0.005051</td>\n",
       "      <td>0.127651</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.031401</td>\n",
       "      <td>0.088609</td>\n",
       "      <td>0.221387</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>capital-loss</th>\n",
       "      <td>0.054413</td>\n",
       "      <td>-0.001513</td>\n",
       "      <td>0.083925</td>\n",
       "      <td>-0.031401</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.055271</td>\n",
       "      <td>0.135645</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>hours-per-week</th>\n",
       "      <td>0.073100</td>\n",
       "      <td>-0.010154</td>\n",
       "      <td>0.147569</td>\n",
       "      <td>0.088609</td>\n",
       "      <td>0.055271</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.231045</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>income</th>\n",
       "      <td>0.238460</td>\n",
       "      <td>-0.002994</td>\n",
       "      <td>0.331798</td>\n",
       "      <td>0.221387</td>\n",
       "      <td>0.135645</td>\n",
       "      <td>0.231045</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                     age    fnlwgt  education-num  capital-gain  capital-loss  \\\n",
       "age             1.000000 -0.075753       0.035084      0.078498      0.054413   \n",
       "fnlwgt         -0.075753  1.000000      -0.030600     -0.005051     -0.001513   \n",
       "education-num   0.035084 -0.030600       1.000000      0.127651      0.083925   \n",
       "capital-gain    0.078498 -0.005051       0.127651      1.000000     -0.031401   \n",
       "capital-loss    0.054413 -0.001513       0.083925     -0.031401      1.000000   \n",
       "hours-per-week  0.073100 -0.010154       0.147569      0.088609      0.055271   \n",
       "income          0.238460 -0.002994       0.331798      0.221387      0.135645   \n",
       "\n",
       "                hours-per-week    income  \n",
       "age                   0.073100  0.238460  \n",
       "fnlwgt               -0.010154 -0.002994  \n",
       "education-num         0.147569  0.331798  \n",
       "capital-gain          0.088609  0.221387  \n",
       "capital-loss          0.055271  0.135645  \n",
       "hours-per-week        1.000000  0.231045  \n",
       "income                0.231045  1.000000  "
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train.corr()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "4ba1ad70",
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([' Private', ' Self-emp-not-inc', ' Local-gov', ' ?', ' State-gov',\n",
       "       ' Self-emp-inc', ' Federal-gov', ' Without-pay', ' Never-worked'],\n",
       "      dtype=object)"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train['workclass'].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "02f3e53e",
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       " Private             20410\n",
       " Self-emp-not-inc     2305\n",
       " Local-gov            1868\n",
       " ?                    1663\n",
       " State-gov            1201\n",
       " Self-emp-inc          987\n",
       " Federal-gov           854\n",
       " Without-pay            12\n",
       " Never-worked            5\n",
       "Name: workclass, dtype: int64"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train['workclass'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "be396114",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       " Private             14632\n",
       " Self-emp-not-inc     1557\n",
       " Local-gov            1268\n",
       " State-gov             780\n",
       " Self-emp-inc          708\n",
       " Federal-gov           578\n",
       " Without-pay             9\n",
       " Never-worked            5\n",
       "Name: workclass, dtype: int64"
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train['workclass'] = train['workclass'].replace('Private',' Private')# 많은 값으로 대체\n",
    "test['workclass'] = test['workclass'].replace(' ?',' Private')\n",
    "test['workclass'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "48da3458",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([' Machine-op-inspct', ' Other-service', ' Handlers-cleaners',\n",
       "       ' Tech-support', ' Transport-moving', ' Farming-fishing',\n",
       "       ' Prof-specialty', ' Priv-house-serv', ' Adm-clerical',\n",
       "       ' Protective-serv', ' Exec-managerial', ' ?', ' Craft-repair',\n",
       "       ' Sales', ' Armed-Forces'], dtype=object)"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train['occupation'].unique()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "4a13d360",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       " Craft-repair         2480\n",
       " Exec-managerial      2477\n",
       " Prof-specialty       2448\n",
       " Sales                2212\n",
       " Adm-clerical         2171\n",
       " Other-service        1948\n",
       " Machine-op-inspct    1211\n",
       " Other                1141\n",
       " Transport-moving      962\n",
       " Handlers-cleaners     823\n",
       " Farming-fishing       602\n",
       " Tech-support          581\n",
       " Protective-serv       380\n",
       " Priv-house-serv        96\n",
       " Armed-Forces            5\n",
       "Name: occupation, dtype: int64"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train['occupation'].value_counts()\n",
    "train['occupation'] = train['occupation'].replace(' ?', ' Other')# 다 또이또이해서 새로운 컬럼 생성\n",
    "test['occupation'] = test['occupation'].replace(' ?', ' Other')\n",
    "test['occupation'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "662c9665",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([' United-States', ' Haiti', ' Mexico', ' Puerto-Rico',\n",
       "       ' Philippines', ' ?', ' Germany', ' Peru', ' Ecuador', ' Iran',\n",
       "       ' Thailand', ' Dominican-Republic', ' Poland', ' Scotland',\n",
       "       ' Italy', ' Jamaica', ' China', ' Portugal', ' Columbia',\n",
       "       ' Hungary', ' Vietnam', ' Taiwan', ' Canada', ' Hong',\n",
       "       ' Guatemala', ' El-Salvador', ' England',\n",
       "       ' Outlying-US(Guam-USVI-etc)', ' India', ' France', ' Cuba',\n",
       "       ' Greece', ' Trinadad&Tobago', ' South', ' Japan', ' Yugoslavia',\n",
       "       ' Nicaragua', ' Ireland', ' Cambodia', ' Laos', ' Honduras',\n",
       "       ' Holand-Netherlands'], dtype=object)"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train['native-country'].unique()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "e7a92da2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       " United-States                 17893\n",
       " Mexico                          372\n",
       " Philippines                     117\n",
       " Germany                          82\n",
       " Canada                           71\n",
       " Puerto-Rico                      67\n",
       " India                            61\n",
       " El-Salvador                      59\n",
       " China                            54\n",
       " England                          52\n",
       " Italy                            45\n",
       " Cuba                             44\n",
       " Dominican-Republic               42\n",
       " South                            41\n",
       " Jamaica                          38\n",
       " Japan                            38\n",
       " Guatemala                        37\n",
       " Vietnam                          36\n",
       " Poland                           34\n",
       " Columbia                         32\n",
       " Taiwan                           26\n",
       " Greece                           24\n",
       " Ecuador                          24\n",
       " Portugal                         24\n",
       " Haiti                            24\n",
       " Nicaragua                        21\n",
       " Peru                             21\n",
       " Iran                             21\n",
       " France                           18\n",
       " Thailand                         15\n",
       " Trinadad&Tobago                  14\n",
       " Ireland                          14\n",
       " Scotland                         12\n",
       " Hong                             11\n",
       " Laos                             10\n",
       " Yugoslavia                       10\n",
       " Honduras                          9\n",
       " Cambodia                          9\n",
       " Outlying-US(Guam-USVI-etc)        8\n",
       " Hungary                           7\n",
       "Name: native-country, dtype: int64"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train['native-country'] = train['native-country'].replace(\" ?\",' United-States') # 많은 컬럼값으로 대체\n",
    "test['native-country'] = test['native-country'].replace(\" ?\",' United-States')\n",
    "test['native-country'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "3c25e07a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='occupation', ylabel='count'>"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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1bwaNmyoL774Qlu3bpWPj49+++03Pfvss1q4cKGGDBmiLVu2ZNlutWrV0tq1a/X+++/L4XCoTp06mjJlivz8/K65DXMjPj5eEydOVFRUlKKjo9WsWTNNnz5du3btynId8fX11eLFi7Vy5UqVKVNGpUqV0t133+0yz9y2ec2aNbV48WJ5e3urSpUqmj17dqb3e/78eU2aNEl//vmnfH19FRoaqmbNml11WdfyvrJr/6ZNm6pu3bqKiYnRv//9b40bN06XLl2Sl5eXwsLCVL9+fbd8Nt98843mz5+v1NRUValSRS+99JLKlCmTp/7nSt9//71mz54tSSpdurReeeUVXbp0ybluSnJeWf/EE0+oWbNmeuCBB/Tjjz+qePHimjNnjqpUqaK2bduqU6dO2r59uyRpxowZuuuuu3Lso86fP6+jR49q+PDh2rdvn8LCwvT666+7/ar648eP69FHH1WZMmXk7++vBQsW5GndyGu/eObMGU2aNEknT56U3W7X008/raCgIC1YsEA//fSTTp06pQEDBrj0X61atXKpuW3bturatau2bdsmu92uxx57TO+++66OHj2qCRMmqEuXLlkup3nz5rr//vu1du1a3XLLLTp//ry6deumr776SnXr1tXBgwe1YMECRUVF6ejRozpx4oT++c9/atSoUUpJSdGUKVMUGRmp8uXLy2az6bHHHsvXcPC3337TSy+9pEuXLuncuXMaPny4BgwY4NI2gwYN0qZNm3TXXXcpMjJSSUlJevbZZ7VkyRIdOnRIQ4cO1dChQ13W05YtW6pjx46KjIyUt7e3Xn31VVWtWlU7d+7UtGnT5O3trfr16+vQoUNaunSpS02vv/669u7dq6lTpyosLExTp07VkiVLFB8fr8mTJys1NVV+fn6aOXOm/vGPf0iSJk+erJ9++knS5e3ltttuU9u2bbVkyRLt2rVL3377rS5cuKBjx46pRYsWeuGFFyRJr7zyijZv3qwyZcooICBAbdu2Ve/evfOtfa+mSZMmztCpbdu2uvvuu7V//36tWLFCW7du1XvvvSebzaY6dero+eef13vvvefSNq1bt3bOKz4+Ps/bRVbHOdn18XfeeacOHjyoqKgoTZw4UXFxcYqOjlavXr305JNPOutYu3atS38yYsQIbdmyRV5eXtq5c6cWLVqUqyuB3Nm+s2fP1lNPPaXVq1er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0KGDJKl+/foqXbq0/vzzT0mXx9bx8fFRhQoV1LBhQ0VGRqpTp07ZvveaNWuqQoUKkqQaNWrowoULatCggebOnauoqCjdf//9Lj/769evnySpdu3aCggI0MGDB7V7927nlRitW7d2uUrretlsNqWlpWWanpKS4vwW+0rt2rWTzWZTzZo1nW2/fft2JSYmavXq1ZKkS5cuOa9Kuuuuu2S3Z17ty5cvLz8/P/Xv319t2rTRs88+Kz8/v1zPq3v37tqwYYPatGmjTZs2aenSpUpJSXHOP6t2W7ZsmY4ePeps55SUFN111115b7gsZPUTxfSrX7t166Y9e/boP//5j/7880+dP39ely5dkpT1OnL48GG1bt1axYsXlyR16tRJDofDZd65bac2bdpowIABat++vTp27JjlN9G7d+/WnDlznDV/+OGHuVpWXt/XyZMnc2z/e+65R5LUrFkzPfHEE9q/f79at26tQYMG5eYjyLOff/7ZeXWddPnndKVLl77u/qddu3YaPXq02rdvr3bt2qlFixY5jiHo5+fn/FVHr169XH46nN5Wbdu2VWhoqE6fPp1jH3XlFfsFqVy5cs4refK6buS1X9yxY4fzqsmqVavqnnvu0c8//ywpb20QFBQkSapUqZICAwNlt9tVqVIlXbx4UZKyXU737t01c+ZMDRo0SOvXr9fTTz+dad5NmjSRr6+vypUrp5tvvllxcXHatm2b+vXrJ5vNpsqVK7v84iGvsvtZdGhoqL799lu99dZb+u2335ztLmVum4zv/5577lGxYsVUuXJl5/u/UsZ96//+9z/99ttvKleunGrVqiVJ6tu3b56G1GrdurVefPFFffvtt2rbtq3atGnj/Fv79u0lSbfffnuWYzE3aNBAJUqUkHT5s7lw4YK2b9+uzp07y9fXV76+vs55uFN0dLRzbOnk5GTdfffdzj5D+r9+bffu3WrTpo3zZ7kPPvignnvuuRznndftIrvjnKv18Y888oh27Nihd955R7///rtSUlL0999/Z1tXnz599Mknn6h+/frasWOH8yp4d8ht+2aU1fFBVrLqz3fs2KGuXbuqWLFiki6/17Vr12Z77FWzZk0dPnxYjzzyiIKCgjR+/HhJuTvm9Pb2VoMGDdS3b1+1a9dODz/8sMqXL6/vv/9e+/fv144dOyRd3ucePHhQt99+u6pVq6aSJUs6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\n",
      "text/plain": [
       "<Figure size 1800x576 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.set(rc = {'figure.figsize':(25,8)})\n",
    "sns.countplot(data = train, x = 'occupation', hue = 'income')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "923289b7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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sixYsCAf/ehHt9o6pLa2No2NjVm1atVW52tqatLY2Ji1a9emuro6lZWVW51PstU1lZWVqa6uzpo1a9KvX7/tmu/FvmUTgJ2rpqZ3V48AAAAA3d6qVRWprOy055k7XUVFxQ41hE7/QsnHH388Z511ViZPnpwePXpk2bJlHa+Vy+WUSqW0t7enVCptc/5Pf/65vzz+82sqKrb/v7jVqzekvb28Y4vp5sQnoLM0Na3v6hEAAACg22tvb09ra/s253vvuVt261W10z9v0+aWrH9u533PVnt7+1YNoaKi9KIPKXdq3F6yZEk+85nPZOrUqTnhhBPy0EMPpampqeP1pqam1NbWpn///ludb25uTm1tbfr06ZP169enra0tPXr06Hh/8sJT383Nzenfv39aW1uzcePG7LXXXp25HAAAAACAwtmtV1XGTL5lp9/31lljsz4vHbe/9a2F+epXb0xra2tOOWV0Pvzhf9opn99pz6g/88wzOfvsszN79uyccMIJSZL3vve9efLJJ/PUU0+lra0t9957b4YOHZp99tknvXr1ypIlS5IkDQ0NGTp0aKqqqlJXV5f58+cnSerr6zN06NAkyZFHHpn6+vokyfz581NXV5eqqp3/vz4AAAAAAPDyNDWtyvXXz83cuTfkpptuzd1335Unn/zdTrl3pz25feONN2bz5s259NJLO86deuqpufTSS/PpT386mzdvzpFHHpljjz02STJ79uxMmzYtGzZsyODBgzNu3LgkyfTp0zNlypRce+21GTBgQObMmZMkmThxYqZMmZITTjghvXv3zuzZsztrKQAAAAAAvAw/+9lD+bu/q8uee74+SfKBDxydRYu+m/32e+srvnenxe1p06Zl2rRpf/W1u+++e5tzBxxwQO64445tzu+zzz752te+ts35vfbaK1/+8pdf+aAAAAAAAHSK5uam9O37ho7jvn3fkF//+lc75d7F/epMAAAAAABe1drb21MqlTqOy+VyKipKL3LF9hO3AQAAAADoFLW1/bJ6dXPH8Zo1q/OGN9TslHuL2wAAAAAAdIq6ukOyZMnirF27Nps2bcqiRd/LoYcevlPu3Wl7bgMAAAAA0PU2bW7JrbPGdsp9X0pNTW0+8YlP5TOfOSstLa0ZOfKkvOtdQ3bK54vbAAAAAADd2PrnNmV9NnXZ5x9zzLE55phjd/p9bUsCAAAA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rl3baUMBAAAAAMCL2a643dbWlmeffbbjeM2aNZ01DwAAAAAAvKTtitsf/ehH85GPfCRXXHFFrrzyyowePTqjR49+yes2bNiQESNG5Omnn06SPPDAAxk5cmSOOeaYXH755R3ve/TRRzNq1KgMHz48559/flpbW5MkK1euzNixY3PsscdmwoQJ2bhxY5Lkueeey/jx43Pcccdl7NixaWpq2uGFAwAAAABQXNsVt4888sgkSUtLS5544ok0NjZm2LBhL3rNww8/nNGjR2fZsmVJkk2bNmXq1KmZO3du5s+fn6VLl+YHP/hBkmTSpEm58MILc99996VcLmfevHlJkhkzZmTMmDFZuHBhhgwZkrlz5yZJrrjiitTV1WXBggU55ZRTMnPmzJe1eAAAAAAAimm74vaUKVMyduzYTJo0KZdddlk++9nPZurUqS96zbx58zJ9+vTU1tYmSR555JHsu+++GThwYCorKzNy5MgsXLgwK1asyKZNm3LggQcmSUaNGpWFCxempaUlixcvzvDhw7c6nySLFi3KyJEjkyQjRozI/fffn5aWlpf1FwAAAAAAQPFUbs+b1q5dm3HjxiVJevXqldNPPz319fUves1fPk29atWq1NTUdBzX1tamsbFxm/M1NTVpbGzM2rVrU11dncrKyq3O/+W9KisrU11dnTVr1qRfv37bs5wkSd++1dv9XgBemZqa3l09AgAAANDNbFfcbmtrS2NjY0c8bm5uTrlc3qEPam9vT6lU6jgul8splUp/8/yf/vxzf3n859dUVGzXQ+gdVq/ekPb2HVtDdyc+AZ2lqWl9V48AAAAAFExFRelFH1Lerrh9+umn54Mf/GDe//73p1Qq5YEHHsjkyZN3aJD+/ftv9cWPTU1Nqa2t3eZ8c3Nzamtr06dPn6xfvz5tbW3p0aNHx/uTF576bm5uTv/+/dPa2pqNGzdmr7322qF5AAAAAAAoru163Pnkk0/OTTfdlHe9610ZMmRIbrzxxo49r7fXe9/73jz55JN56qmn0tbWlnvvvTdDhw7NPvvsk169emXJkiVJkoaGhgwdOjRVVVWpq6vL/PnzkyT19fUZOnRokhe+4PJP26LMnz8/dXV1qaqq2qF5AAAAAAAoru16cjtJDjjggBxwwAEv+4N69eqVSy+9NJ/+9KezefPmHHnkkTn22GOTJLNnz860adOyYcOG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//vfz7p16/Loo4++5D1++tOfblcEBwCAl1Iul/PJT34y73znO/PNb34zPXv2zK9//euMHz8+//7v/75TfxcGYOcStwFe4+6888788Ic/zLp167J8+fL8/d//fb74xS/mpz/9aa6++upMmDAh3/ve9/KTn/wkNTU1eec735kLL7wwf/jDH1IqlfL5z38+RxxxRJ599tlMmjQpf/jDHzJo0KBs3rz5r35ec3NzWlpa0tLSkp49e+bggw/OxRdfnPb29vzbv/1bVq1albPPPjvXXHNNLr/88jz44INZt25damtrc/nll+fOO+/MqlWrMn78+Nxyyy1Zvnx5LrnkkmzatCl77713ZsyYkYEDB+amm27KXXfdlYqKirznPe/JRRddtIv/ZgEAKIKHHnooK1euzFe/+tWUSqUkybve9a5MmDAhp59+enr37t3xu3CSLFq0KLfeemtWr16dT37yk/nIRz6SjRs35qKLLsrjjz+etra2fOITn8iIESNy55135q677sqzzz6bD3zgA/nc5z7XlUsF6HbEbQDy85//PPfee2969OiRY489NqNHj+547YgjjshRRx2VQw45JO9///tz7rnn5sMf/nCOPvrorFq1KmPGjEl9fX2uuuqqvOtd78r111+fxYsXZ8GCBX/1s8aNG5ezzjorhx9+eA455JAcfvjh+dCHPpRevXpl2rRpGTduXK655po89dRT+d3vfpfbbrstFRUVmTx5cu6+++6MHz8+t912W/7zP/8ze+yxR6ZNm5Yvf/nLeeMb35gf/vCHueCCC3LjjTfmuuuuyw9/+MP06NEj559/fhobG9OvX79d9VcKAEBB/PKXv8yQIUM6wvafvO9978vuu+++1e/C3/zmN7Nly5Z8/etfz+OPP55x48blIx/5SK699toMHjw4X/rSl7Jhw4aceuqpee9735skaWxszPz581NZKcEA7Gz+yQrQzVVUbPv1CuVyeatf3g866KBUV1cnSQYOHJh169b9zfs98MAD+d3vfperrroqSdLa2prly5fnoYceyr//+78neeFfBAYOHPhXr3/Tm96Ue++9N7/85S/zwAMPpL6+Pv/93/+d+vr6rd6377775l/+5V/y9a9/PU8++WR+8Ytf5M1vfvNW71m2bFmWL1+eCRMmdJzbsGFDevTokYMOOignn3xyjj766Hz84x8XtgEA+KtKpVLa2tq2Od/S0rJN8E6So48+OqVSKfvvv3/Wrl2b5IXfkTdt2pRvfOMbSZI//vGPefzxx5O88BS4sA3QOfzTFaCb23PPPbN+/fqtzq1evTqvf/3rO4579erV8XOpVEq5XP6b92tvb89XvvKV7LXXXkmSVatWpW/fvttc16NHjyTJ+eefn6VLlyZJ/u3f/i3f/va3M3bs2LznPe/Je97znnzyk5/Mqaeemh//+Mcde3wnydKlS/P5z38+p59+eoYPH56Kiopt5mpvb8+b3vSmNDQ0JEna2trS3NycJJk7d25+8Ytf5P7778+ZZ56Z2bNn2ysRAIBtvPe9783Xvva1tLS0pKqqquP8L37xiwwZMmSb9//p99w/D9/t7e257LLLMnjw4CQvbMX3+te/Pvfcc0922223Tl4BwGvXto/zAdCtVFdXZ9999819993Xce7222/P4Ycfvt336NGjR8fTLIcddlhuvfXWJMlvf/vbjBw5Ms8//3wOP/zwjsj8yCOP5Pe//32SZObMmWloaEhDQ0Pe/e53p7GxMddcc022bNmSJGlqasqaNWvy9re/PZWVlWltbU2SLF68OIccckhGjx6dt7zlLVm0aFHHDH+a561vfWvWrVuXn/3sZ0mSb3zjG/nCF76QNWvW5Pjjj8/b3/72TJw4MX//93+fxx577JX8NQIA0E3V1dXlbW97Wy6++OK0tLQkeeFBi2uvvTaf+tSntvpd+G857LDD8r//9/9O8sLDHyeeeGKeeeaZTp8d4LXOk9sArwGXXXZZvvjFL+aaa65JS0tL3vGOd+TCCy/c7uuPOOKIzJkzJ7179860adNy4YUXZuTIkUmSWbNmpbq6Op/5zGcyZcqUnHDCCXnrW9/6N7clueCCC/KlL30pxx57bHbfffdUVVXlC1/4QgYNGpSWlpa88Y1vzGmnnZbZs2fnnHPO6ficIUOG5Omnn06S/OM//mPGjx+fG264IVdeeWVmzpyZzZs3p7q6Ol/60pfSp0+ffOQjH8nJJ5+c3XffPfvtt18+/OEPv8K/RQAAuqurr746l19+eUaMGJEePXrk9a9/fS677LIceuihaW5u7vhd+G8555xz8sUvfjEjRoxIW1tbJk2alDe/+c0dD2EA0DlK5Rf7/54DAAAAAMCrkG1JAAAAAAAoHHEbAAAAAIDCEbcBAAAAACgccRsAAAAAgMIRtwEAAAAAKBxxGwAAdpGrr7463/nOd5IkV155Zerr67t2oJfhjDPOyJo1a7p6DAAASGVXDwAAAK8VP/3pT/O2t70tSTJx4sQunubl+fGPf9zVIwAAQBJxGwAAXpaf/vSnufzyyzNw4MA8/vjjaW1tzYwZM9KnT59cdNFF2bhxY5qamnLAAQfkiiuuyB133JGlS5dm1qxZ6dGjR7773e9m//33T3V1db7//e/ny1/+cpLkiSeeyOmnn55FixZl2bJlmTlzZp599tm0tbXltNNOy8knn/xX57njjjty0003paKiInvvvXe+9KUvZcCAAbn99tvzta99LRUVFXnDG96QCy64IPvtt1+mTJmS/fffP//8z/+cJFsdH3XUUfnQhz6UBx98MM8880xOOumkfPazn815552XJPnYxz6W//zP/8zYsWPznve8J4899lhOPPHE3H777fne976XioqKPP/88znqqKPyzW9+M3369Nk1/6UAAPCaYlsSAAB4mR555JGcccYZqa+vz6hRo3L55Zdn3rx5+eAHP5h58+blW9/6Vp5++uksWrQoY8eOzZAhQzJ58uQMGzas4x4nnHBClixZkqampiTJnXfemVGjRqVcLuczn/lMPv/5z+fOO+/MzTffnP/6r//KL37xi23m+M1vfpPZs2fnhhtuyD333JOjjjoq1157bR588MHccMMN+epXv5q77747I0aMyNlnn51yufySa/vjH/+YW2+9Nbfddlv+67/+K8uXL88ll1ySJPnKV76SAQMGJEn233//LFiwIBMmTMjrX//6/PCHP0ySfPOb38zhhx8ubAMA0GnEbQAAeJne+MY35p3vfGeS5F3velfWrVuXSZMmpU+fPrn++uvzxS9+MatWrcof//jHv3mP6urqDBs2LHfffXfa2tpyzz335OSTT86yZcvy+9//PlOnTs1JJ52Uj370o9m0aVN+/etfb3OPBx98MP/wD//QEZxPP/30XHTRRfnhD3+Y448/viMwjxo1Ko2NjXn66adfcm1HH310kqRfv37p27dv1q1b91ffV1dX1/Hz2LFjM2/evCTJ7bffntGjR7/k5wAAwMtlWxIAAHiZdtttt46fS6VSyuVyPve5z6WtrS3HHXdc/vEf/zHPPPPMSz4p/U//9E+54IILMmjQoAwaNCgDBw7MY489lt69e6ehoaHjfc3Nzendu3euvPLKfO9730uSHHXUUdl7771TKpU63rdp06asWLEi7e3t23xWuVxOa2trx7x/0tLSstX7evXqtc3a/prXve51HT+PHDkyc+bMyU9+8pP88Y9/zPve974XXTcAALwSntwGAICd6Ec/+lHOPvvsHH/88UmShx9+OG1tbUmSHj16pLW1dZtrDjzwwCTJNddck1NOOSVJst9++2W33XbriNvPPPNMRowYkaVLl2bixIlpaGhIQ0NDJk6cmEMPPTQPPvhgVq1alSS57bbbctlll+X9739/5s+fnzVr1iRJvvGNb2SvvfbKvvvum7333jtLly5NkjQ2Nuahhx7arvX9rTUkye67754TTzwxU6dOzamnnrpd9wMAgJfLk9sAALATnXvuuTn77LPzute9LtXV1Xnf+96X3//+90leeMp6zpw52zwlnSSnnHJK5s6dm//1v/5XkqRnz56ZO3duZs6cmRtuuCGtra2ZOHFiDj744G2ufcc73pFJkyblzDPPTJLU1NTk4osvTr9+/XL66afnYx/7WNrb29OnT59cd911qaioyGmnnZYvfOELGT58eN70pjflsMMO2671HXvssTnttNPyH//xH3/19VGjRnXsOw4AAJ2pVN6eb5MBAAB4CeVyOddff31WrFiRGTNmdPU4AAB0c57cBgAAdoqjjz46tbW1mTt3blePAgDAa4AntwEAAAAAKBxfKAkAAAAAQOGI2wAAAAAAFI64DQAAAABA4YjbAAAAAAAUjrgNAAAAAEDh/F9Bbij2JFI/SwAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 1800x576 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.set(rc = {'figure.figsize':(25,8)})\n",
    "sns.countplot(data = train, x = 'native-country', hue = 'income')\n",
    "country_dic = {' United-States':' United-States'}\n",
    "country_mapping = train['native-country'].map(country_dic)\n",
    "country_mapping[country_mapping.isnull()]\n",
    "train['native-country'] = country_mapping.fillna('Other')\n",
    "country_mapping = test['native-country'].map(country_dic)\n",
    "test['native-country'] = country_mapping.fillna('Other')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "eaa3f29b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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C922DwAAdm+1tbV561vfmhkzZnR8Z8yyZcsyd+7cfOpTn+r4PfWVHHnkkfmnf/qnJC/8rceTTz45v/3tbzt9doA9nSe3Aeg0I0eOzA9+8IPU1dUlST70oQ/lggsuSH19fZJk6NChefbZZ5Mkf/u3f5tx48bl29/+dr7+9a/nsssuy+bNm9OnT5/8/d//fbftAQCA3d83v/nNXHXVVRkxYkR69OiRN7zhDbnyyitzxBFHpKWlJbNnz07fvn1f9v0XXHBBvvzlL2fEiBHZunVrJkyYkDe/+c0dD2wA0DlK5Rf/fXAAAAAAANjFOZYEAAAAAIDCEbcBAAAAACgccRsAAAAAgMIRtwEAAAAAKBxxGwAAAACAwhG3AQCgQN72trdlzZo1nfZ6AAAoCnEbAAAAAIDCEbcBAKCTjRw5Mg8++GCS5K677so73vGObNq0KUkyZcqU/OM//mO+8IUvZMSIEamvr8/MmTPT1taWJBk6dGguvPDC1NXV5T/+4z867tnc3JwRI0Zk3rx5SZJHHnkkp512WkaMGJFTTjml4/P+6A9/+EMmTpyYj33sY6mrq8uoUaPy1FNPJUl++MMf5pRTTsmoUaNy2mmnZcmSJa+4DgAAuwJxGwAAOtnw4cNz//33J0n+5V/+JW94wxvy0EMPpVwu5yc/+Unuv//+7Lfffrnzzjtz22235fHHH8///b//N0nS2tqaY489NosXL8473vGOJElTU1POPPPMjBs3Lg0NDWltbc3555+f888/P3fddVe+8pWvZMaMGWlvb++Y4f7778++++6bm2++OYsXL87QoUM7wvjMmTMzbdq03H777bnwwgvz85///BXXAQBgVyBuAwBAJ/tj3C6Xy3nooYdy5pln5mc/+1kefvjhvPnNb86vfvWrfPzjH0+pVErPnj1z+umnd8TwJKmtrd3mfuecc0722muv1NfXJ0meeOKJVFRU5G//9m+TvPC095133pmKiv/9df+EE07IKaecku9973v56le/ml/84hf5wx/+kCQ56aSTcsEFF2TKlClZt25dzjnnnFdcBwCAXYG4DQAAnextb3tbWltb8+Mf/zhvectbcuyxx+ZnP/tZ7r333tTV1aW9vT2lUqnj9e3t7R3HkiTJ3nvvvc39Lr300lRUVOQ73/lOkqRHjx7bvD95IXj/6T1uuummTJkyJb179059fX1GjBiRcrmcJLnoooty0003ZejQobn99tvT0NDwiusAALArELcBAKAL/J//83/yta99LX/913+dQw45JBs2bMidd96Z448/Pn/zN3+TG2+8MeVyOVu2bMn8+fNz9NFHv+y9Dj/88FxxxRWZO3dunnjiiRx88MEplUr52c9+liT55S9/mU984hPbHEvy05/+NKecckpOO+20HHTQQbn33nuzdevWtLW15bjjjsvzzz+f0aNHZ9q0aXn88cezZcuWl10HAIBdQWV3DwAAAHuC4cOH54YbbuiI1kcffXQef/zxDBo0KFOnTs1Xv/rV1NfXp7W1NR/4wAdy3nnnveL9Dj744HzqU5/KhAkTcsstt+Qb3/hGZsyYkZkzZ6aqqirf+MY30rNnz47Xn3322bnkkkty6623JnkhkD/xxBOprKzM5MmT84UvfCGVlZUplUqZMWNGevbs+bLrAACwKyiV//h3EQEAAAAAoCAcSwIAAAAAQOGI2wAAAAAAFI64DQAAAABA4YjbAAAAAAAUjrgNAAAAAEDhiNsAAAAAABSOuA0AAAAAQOH8fzo7eF6X56y/AAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 1800x576 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.set(rc = {'figure.figsize':(25,8)})\n",
    "sns.countplot(data = train, x = 'workclass', hue = 'income')\n",
    "workclass_dic = {' Private':' Private'}\n",
    "workclass_mapping = train['workclass'].map(workclass_dic)\n",
    "workclass_mapping[workclass_mapping.isnull()]\n",
    "train['workclass'] = workclass_mapping.fillna('Other')\n",
    "workclass_mapping = test['workclass'].map(workclass_dic)\n",
    "test['workclass'] = workclass_mapping.fillna('Other')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "59aad9cf",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='age', ylabel='count'>"
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABasAAAHiCAYAAADmn5BLAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/YYfK9AAAACXBIWXMAAAsTAAALEwEAmpwYAABPaUlEQVR4nO3dfZyVdZ0//vcMM8x4M5TijLjIUt4UhQWmaaRCmiKopKGbCknmmneFRX2lFllN1xsiWze33O3G3F+KX0XSIL6IlpaPFEtlS74kWqGgojsMiDKgc39+f+zXWcXrjHMu5sx1Zub5fDx8PJhznXnN+zrn3dV13nPN5yrL5XK5AAAAAACADJVnXQAAAAAAABhWAwAAAACQOcNqAAAAAAAyZ1gNAAAAAEDmDKsBAAAAAMicYTUAAAAAAJmryLqAnrJly/bo6MhlXQYAAAAAAAnKy8tijz12y7u93wyrOzpyhtUAAAAAAH2UZUAAAAAAAMicYTUAAAAAAJkzrAYAAAAAIHP9Zs1qAADobe3tbbFlS0O0tbVkXUpBKioGxx571MagQT4OAABQOpydAgBASlu2NER19a6x227DoqysLOtyuiWXy8X27Vtjy5aG2GuvfbIuBwAAOlkGBAAAUmpra4nddhvSZwbVERFlZWWx225D+tzV4AAA9H+G1QAAsBP60qD6DX2xZgAA+j/DagAAAAAAMmdYDQAAPeipp56MuXNnZ10GAAD0OWW5XC6XdRE9YfPmbdHR0S92BQCAPuK//mt9DBs2MusyUunLtQMA0DeVl5fF0KG7591e0Yu1AABAv/ef//l4XH/9/Bg16oOx2267xdq1f42NG+tj//0PjLlzr4hdd901/vSn1fEv//LtaGp6PSorK+OLX/xKHHLIR+OJJ/4Q3//+d6O5uSkqKirjC1+4MD72sY/HsmW/iN/85oHI5Triv/7rpait3Ts+9alT4mc/WxjPP/9cnH769DjzzM9GRMTSpT+Pu+5aFLlcRwwZ8u746ldnx8iR78n2RQEAgG4wrAYAgCJ5+uk18d3v/nuUl5fHeed9Ln7961/F8cefEHPmfC2+/vV/jI9//Mh46qk1cc0134x//dcfxNy5X4958/45Ro8+KJ55Zm3MnHle/OhHP42IiFWr/hD/3/93e9TW1sWMGWfEr351X3z3u/8Wa9f+Nc4///Nx+unT4okn/hD33PN/4sYbfxzV1dXx6KO/izlz/lcsWLAo41cCAADemWE1AAAUyeGHfzwGDx4cERH77XdAbN26Ndau/WuUlw+Kj3/8yIiIGDXqA/HTn94RjzzyUOy7774xevRB/+/5+8eHPjQm/vCHlVFWVhajRn0w9t57WERE/M3f/E0cdtjHory8PIYP3zdaWpqjqakpHnnkoXjhhefjggvO6ayhsbExtm59NYYMeVcv7z0AABTGsBoAAIpk8OCqzn+XlZVFLpeLQYMGRVlZ2Vue98wzf4329o6IeOvjHR25aGtri8rKys6h9xsqKt5+Kt/e3hHHH39CXHTRxf/v+zti06aGqKkZ0kN7BAAAxVOedQEAADCQ/O3f/vdNDR977HcREfH000/FxRdfGKNHHxTPPbcunnxydUREPPPM2njiif+Mgw8+pNvZhx8+Ln71q3tj06ZNERHx85//LL785Qt7eA8AAKA4XFkNAAC9aPDgwXHNNd+O7373O/H9798QlZUVcfXV34499tgz/umfvhXXX//taG5uirKy8pgz5/L4278dGatXr+pW9mGHfSymT/9czJp1UZSXl8euu+4WV1/97bddyQ0AAKWoLJfL5bIuoids3rwtOjr6xa4AANBH/Nd/rY9hw0ZmXUYqfbl2AAD6pvLyshg6dPf823uxFgAAAAAASGQZEEpKzZDqqK6qzLu9qbk1Grc29WJFAAAAAEBvMKympFRXVca02Qvybr9t/vRoDMNqAAAAAOhviroMyOLFi+PEE0+ME088Mb71rW9FRMSKFStiypQpMXHixLj++us7n7tmzZqYOnVqHH/88XHppZdGW1tbMUsDAAAAAKCEFG1Y/frrr8fVV18dt9xySyxevDgef/zxeOCBB2LOnDlx4403xrJly2L16tXx4IMPRkTEJZdcEpdddlnce++9kcvlYuHChcUqDQAAAACAElO0YXV7e3t0dHTE66+/Hm1tbdHW1ha77757jBw5MkaMGBEVFRUxZcqUWL58eWzYsCGamppi7NixERExderUWL58ebFKAwAAAACgxBRtzerdd989vvzlL8fkyZNjl112iY9+9KOxcePGqK2t7XxOXV1d1NfXv+3x2traqK+vL+jnDR26e4/VTmmrra3JugQAgIiI2LixPCoq3nr9x667VUXV4J4/zW5uaYvXtjf3WF55ebnzKgAASkrR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MSP3i1/8IjdhwoTcc889l2ttbc2dc845ud/85jepsu67777c2rVrc6effnruQx/6UO53v/tdt/YvKesHP/hB7rjjjss1NjbmOjo6crNnz87dfPPNqbJuvvnm3HHHHZfbvn17rq2tLXf66afnfvvb36bex1wul/vLX/6SO+qoo3Kf/exnU+ecdNJJne9hdyVl3XXXXbkjjjgit2bNmlwul8vNmjUrt2DBgp3av1yusH7Pl5Wm5/P1Q5qe//3vf58744wzcq2trbnXX389d/TRR+fWrFmTqueTstauXZuq5/NlFdrzXeUU2u/5snK5wvq9q6w0PZ/vPUzT813tYy5XWM/ny0rT8/my0vR8LpfLrVixInf44Yfnvv71r+def/31VP2elJXL5VL1e1LWM888k+oYn5T13HPPper5fPuYyxXe80k5afo9KauxsTFVv+er6w2F9Hu+rLTnNTtmpe33jo6O3JFHHplrbW3tfCxtzydl5XLpej4pK03PJ+Wk7fd8+5fLFd7v+bLS9HxSVtqe72ofc7nCej5fVpqeT8pK0/PPPfdc7sgjj8y99NJLuZaWltyZZ56Z+81vfpOq3/Nlpen3pKz/+I//SHWMT8pasGBBqp7Pt4+5XOE9ny+r0J5PyvnlL3+Zqt+72r9crrB+z5eVpt/z9UPac5o3/PnPf84dd9xxuRdffHGnzmvenLV58+adOq95c9YTTzyxU+c1SVlpz2vevH+5XLpzmqSsnTmveXPWhg0bduq8Zse63pDmvGbHrJ05r3lz1h//+MdUPf/aa6/lPvrRj+Y2b96ca21tzZ122mm5+++/v+CeT8p5+OGHU/V7Utbtt9+eqt+Tsu64445U/Z5vH3O5wns+X1aank/K+tWvflVwz3e1f7lcYf2eLytNvydl/e///b9TzydPOumkXGNjY66trS13/vnn5xYvXrzTx/h+uwzIwoUL4/LLL4+6urq3bZs/f36cccYZ8Z73vCdVTnt7e2zbti3a29ujubk5qqqqUtX09NNPx9ixYzu/Pvroo+NXv/rVO+bU1tbGN77xjRg8eHBUVlbG/vvvH+vWrYuRI0fGiBEjoqKiIqZMmRLLly9PlfXiiy/GokWL4txzz+28Uqc7krJaWlri8ssvj9133z3Kysrife97X7z44oupssrKyuL//J//E7vuumts3bo1tm3bFkOGDEm9jy0tLXHZZZfFxRdfnHr/XnzxxXjxxRdjzpw5MWXKlLjhhhuio6MjVdaGDRti7NixMWrUqIiImDt3brd+45evrjcU0u/5stL0fL5+SNPzhx12WPz0pz+NioqK2Lx5c7S3t8fWrVtT9XxS1q677pqq55OyqqqqCu75fDWl6fd8WYX2e76s6urqVD2flLVmzZpUPZ9vH99QSM/ny0rT80lZq1atStXzr7zySlx//fVxwQUXRETEqlWrUvV7UlZEpOr3pKzBgwenOsYnZY0YMSJVz+fbxzQ9v2PO66+/nqrfk7IefvjhVP2eb//eUEi/58tKe16zY1ba85pnnnkmIiLOOeec+NSnPhW33npr6p5PyopI1/NJWWl6Piknbb/n2780/Z6Ulbbnk7LS9ny+fXxDIT2fLytNzydlpen5X/7yl3HCCSfEsGHDorKyMq6//vrYZZddUvV7UtaYMWNS9XtS1rHHHpvqGJ+UdcIJJ6Tq+Xz7mKbnk7JGjRpVcM8n5bS3t6fq93z794ZC+j1fVpp+T8qqra1NdYx/s29+85sxa9aseP7551Of1+yYteeee6Y+r9kxa+jQoanPa3bM+vCHP5z6vObNOXvuuWeqfk/K2mWXXVKf1+yY9X//7/9NfV6zY9aee+7Z+Vih5zVJWWnPa3bMevHFF1P1fHt7e3R0dMTrr78ebW1t0dbWFrvvvnvBPZ+UU1VVlarfk7Le+973pur3pKz9998/Vb/n28c0PZ8vK03PJ2X9+c9/Lrjn89X0hkL6PV9Wmn5Pytq0aVOqfn/yySfjyCOPjN133z0GDRoURx11VNx55507fYzvt8Pqq6++Og499NC3Pb5u3bp49NFHY8aMGalzvvnNb8ZZZ50VRx11VGzZsiUmTZqUKmvUqFHxxBNPxEsvvRTt7e2xfPny2LRp0zvmHHjggTF27NjO/bnnnnuirKwsamtrO59TV1cX9fX1qbLe+JONY489tlv71VXWSSedFEcccURERLz88suxYMGC+OQnP5m6rsrKyli4cGEce+yxUVtb23mgSJP1ne98J0499dQYMWJE6v076qij4mMf+1hcc801sXDhwnj88cdj0aJFqbIGDx4cu+66a8yaNStOPvnk+Nd//dduHeDz7d8bXxfS7/my0vR8UtYJJ5yQqucjIiorK+OGG26IE088McaNGxcbN25M1fNJWXvvvXeqnk/K+pu/+ZtUPZ9UU5p+z5dVaL/ny2pra0vV80lZDQ0NqXo+3z5GFN7z+bLSHud3zPrwhz+cqucvu+yymDVrVufrsTP9vmNWRKTu9x2zhg8fnqrf89WVtueTstL0/I45mzZtSt3vO2atX78+db8n7V9Eun5Pykrb7ztmpT2v2bp1a4wbNy6+//3vx3/8x3/E7bffHi+++GKqnk/Kevjhh1P1fFLWunXrCu75fDWl6fd8WWn6PSlr8eLFqXo+KSttz+fbx4jCez5fVpqeT8p69dVXC+759evXR3t7e1xwwQVx8sknx2233Zb6GJ+U9a53vStVvydlpT2nyVdXmp7Pl5Wm55OympubC+75pJy0/Z5v/yIK7/d8WWn6PSkr7TH+DStWrIimpqaYPHnyTp3X7JgVkf68ZsesnTmvSaor7XnNjjlpz+N3zNqZ85ods3bmvCZpHyPSndckZaU9r9kxK23P77777vHlL385Jk+eHBMmTIjhw4en6vmknI985COp+j0p66Mf/Wiqfs9XV5p+z5eVpueTsmpra1P1fFLWoEGDCu75fPsXUXi/58tK0+9JWWlnNaNHj46HHnooXnnllWhubo4HHngg/vM//3OnjvER/XhYnc8dd9wR06ZNK2gtxjdraGiI6667LpYuXRoPPfRQjBkzJq699tpUWe9973vja1/7Wlx44YUxffr0eP/73x+VlZXd/v6//OUvcc4558Ts2bNjxIgRb1kPKJfLFbTO55uzCv0tZney6uvr43Of+1yceuqpBa2NmpT1mc98Jn7/+9/HXnvtFd/73vdSZW3YsCFeeumlOPXUUwvZtbfl7LfffvH9738/6urqYpdddomzzjorHnzwwVRZ7e3t8dBDD8VXv/rVuOuuu+L111/vXEOo0Kw3Xqu0/f7mrN12222nen7H12tnev7iiy+ORx55JF566aVYt27dTvX8m7MWLlzY7e/rblaank/KSdvvb8664447Uvf7jlmPPPLITvX8m7NaWlp2queTXq+0Pf/mrO9///s71fNvznrssccK7vk777wz9tlnnxg3blznYx0dHan6PSkrra6yCu33rrIK7fmkrIcffrjgnk/KGTFiRKp+T8pKe4zv6rUqtN+TstKe1yRlpT2vOfjgg2P+/PlRU1MTe+65Z5x22mlxww03pOr5pKxCjlHdzSqk57vKKbTf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yJxhNQAAAAAAmTOsBgAAAAAgc4bVAAAAAABkriLrAgAAYKDp6OiIa665Jp544onYvn175HK5uOqqq+K9731v/MM//EM899xz8e53vztqa2vjwAMPjJkzZ8batWvj6quvjldeeSXa29vjrLPOitNOOy3rXQEAgB5jWA0AAL3siSeeiI0bN8Ydd9wR5eXl8cMf/jB+9KMfxa677hoHHHBA/OAHP4iNGzfG1KlT48ADD4y2tra4+OKLY/78+TF69OhobGyM008/PQ444IAYO3Zs1rsDAAA9wrAaAAB62cEHHxzvete74vbbb4/nn38+fv/738duu+0Wjz32WNx9990REVFXVxeTJk2KiIh169bFc889F3PmzOnMaGpqiieffNKwGgCAfsOwGgAAetlvfvObuPrqq+Pzn/98fPKTn4z99tsvlixZEhUVFZHL5TqfV17+37eYaW9vj5qamli8eHHntk2bNkVNTU2v1w4AAMXiBosAANDLHn744Tj66KNj2rRpcdBBB8WvfvWraG9vjwkTJsSiRYsiImLLli3xq1/9KsrKyuK9731vVFdXdw6rX3rppTjppJNi9erVWe4GAAD0qLLcmy/dAAAAim7t2rXxta99Ldrb26OtrS2OOOKIuO+++2Lx4sUxd+7czhss5nK5+MQnPhHnnntuPPXUU503WGxra4sZM2bEmWeemfWuAABAjzGsBgCAErFgwYL44Ac/GAcffHC0tLTEtGnTYubMmTFhwoSsSwMAgKKzZjUAAJSIAw44IP7pn/4pOjo6orW1NSZNmmRQDQDAgOHKagAAAAAAMucGiwAAAAAAZM6wGgAAAACAzBlWAwAAAACQOcNqAAAAAAAyZ1gNAAAAAEDm/n/qMzSPFHPwVwAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 1800x576 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.set(rc = {'figure.figsize':(25,8)})\n",
    "sns.countplot(data = train, x = 'age', hue = 'income')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "51332edd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['age', 'workclass', 'fnlwgt', 'education', 'education-num',\n",
       "       'marital-status', 'occupation', 'relationship', 'race', 'sex',\n",
       "       'capital-gain', 'capital-loss', 'hours-per-week', 'native-country',\n",
       "       'income'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "id": "c007d064",
   "metadata": {},
   "outputs": [],
   "source": [
    "education_dic = {' HS-grad':' HS-grad',' Some-college':' Some-college',' Bachelors':' Bachelors',' Masters':' Masters',' Assoc-voc':' Assoc-voc',' 11th':' 11th',' Assoc-acdm':' Assoc-acdm'}\n",
    "education_mapping = train['education'].map(education_dic)\n",
    "education_mapping[education_mapping.isnull()]\n",
    "train['education'] = education_mapping.fillna('Other')\n",
    "education_mapping = test['education'].map(education_dic)\n",
    "test['education'] = education_mapping.fillna('Other')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "9d79f99d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       " HS-grad         6349\n",
       "Other            4621\n",
       " Some-college    4320\n",
       " Bachelors       3177\n",
       " Masters         1070\n",
       "Name: education, dtype: int64"
      ]
     },
     "execution_count": 85,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "test['education'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "id": "bd88e8b6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       " White    16681\n",
       "Other      2856\n",
       "Name: race, dtype: int64"
      ]
     },
     "execution_count": 76,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "race_dic = {' White':' White'}\n",
    "race_mapping = train['race'].map(race_dic)\n",
    "race_mapping[race_mapping.isnull()]\n",
    "train['race'] = race_mapping.fillna('Other')\n",
    "race_mapping = test['race'].map(race_dic)\n",
    "test['race'] = race_mapping.fillna('Other')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "id": "66804792",
   "metadata": {},
   "outputs": [],
   "source": [
    "categorical_features = ['workclass','education','marital-status','occupation','relationship','race','sex','native-country']\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "id": "7f9443e0",
   "metadata": {},
   "outputs": [],
   "source": [
    "for feature_name in categorical_features:\n",
    "    one_hot = pd.get_dummies(train[feature_name], prefix=feature_name)\n",
    "    train = pd.concat([train, one_hot], axis=1)\n",
    "    train.drop(feature_name, axis=1, inplace = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "id": "ab4a2cf7",
   "metadata": {},
   "outputs": [],
   "source": [
    "for feature_name in categorical_features:\n",
    "    one_hot = pd.get_dummies(test[feature_name], prefix=feature_name)\n",
    "    test = pd.concat([test, one_hot], axis=1) \n",
    "    test.drop(feature_name, axis=1, inplace = True) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "id": "e0e0c345",
   "metadata": {
    "scrolled": true
   },
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
       "      <th>age</th>\n",
       "      <th>fnlwgt</th>\n",
       "      <th>education-num</th>\n",
       "      <th>capital-gain</th>\n",
       "      <th>capital-loss</th>\n",
       "      <th>hours-per-week</th>\n",
       "      <th>income</th>\n",
       "      <th>workclass_ Private</th>\n",
       "      <th>workclass_Other</th>\n",
       "      <th>education_ Bachelors</th>\n",
       "      <th>...</th>\n",
       "      <th>relationship_ Other-relative</th>\n",
       "      <th>relationship_ Own-child</th>\n",
       "      <th>relationship_ Unmarried</th>\n",
       "      <th>relationship_ Wife</th>\n",
       "      <th>race_ White</th>\n",
       "      <th>race_Other</th>\n",
       "      <th>sex_ Female</th>\n",
       "      <th>sex_ Male</th>\n",
       "      <th>native-country_ United-States</th>\n",
       "      <th>native-country_Other</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>no</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>25</td>\n",
       "      <td>219199</td>\n",
       "      <td>7</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>40</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>39</td>\n",
       "      <td>52978</td>\n",
       "      <td>10</td>\n",
       "      <td>0</td>\n",
       "      <td>1721</td>\n",
       "      <td>55</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>35</td>\n",
       "      <td>196899</td>\n",
       "      <td>13</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>50</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>64</td>\n",
       "      <td>135527</td>\n",
       "      <td>11</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>40</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>24</td>\n",
       "      <td>60783</td>\n",
       "      <td>10</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>70</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 48 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "    age  fnlwgt  education-num  capital-gain  capital-loss  hours-per-week  \\\n",
       "no                                                                           \n",
       "1    25  219199              7             0             0              40   \n",
       "2    39   52978             10             0          1721              55   \n",
       "3    35  196899             13             0             0              50   \n",
       "4    64  135527             11             0             0              40   \n",
       "5    24   60783             10             0             0              70   \n",
       "\n",
       "    income  workclass_ Private  workclass_Other  education_ Bachelors  ...  \\\n",
       "no                                                                     ...   \n",
       "1        0                   1                0                     0  ...   \n",
       "2        0                   1                0                     0  ...   \n",
       "3        0                   1                0                     1  ...   \n",
       "4        0                   1                0                     0  ...   \n",
       "5        1                   1                0                     0  ...   \n",
       "\n",
       "    relationship_ Other-relative  relationship_ Own-child  \\\n",
       "no                                                          \n",
       "1                              0                        0   \n",
       "2                              0                        0   \n",
       "3                              0                        0   \n",
       "4                              0                        0   \n",
       "5                              0                        0   \n",
       "\n",
       "    relationship_ Unmarried  relationship_ Wife  race_ White  race_Other  \\\n",
       "no                                                                         \n",
       "1                         0                   0            1           0   \n",
       "2                         0                   0            1           0   \n",
       "3                         0                   0            0           1   \n",
       "4                         0                   0            1           0   \n",
       "5                         0                   0            1           0   \n",
       "\n",
       "    sex_ Female  sex_ Male  native-country_ United-States  \\\n",
       "no                                                          \n",
       "1             0          1                              1   \n",
       "2             1          0                              1   \n",
       "3             1          0                              0   \n",
       "4             1          0                              1   \n",
       "5             0          1                              1   \n",
       "\n",
       "    native-country_Other  \n",
       "no                        \n",
       "1                      0  \n",
       "2                      0  \n",
       "3                      1  \n",
       "4                      0  \n",
       "5                      0  \n",
       "\n",
       "[5 rows x 48 columns]"
      ]
     },
     "execution_count": 91,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "id": "515f6a03",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "((29305, 48), (19537, 47))"
      ]
     },
     "execution_count": 92,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train.shape, test.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "id": "2dd0f2f1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'income'}"
      ]
     },
     "execution_count": 93,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "set(train.columns) - set(test.columns)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "id": "6bf38ba6",
   "metadata": {},
   "outputs": [],
   "source": [
    "train.sort_index(axis=1, inplace=True)\n",
    "test.sort_index(axis=1, inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "id": "4d5f5590",
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train = train.drop(['income'],axis=1)\n",
    "y_train = train.income\n",
    "X_test = test"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "id": "09de7b16",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "((29305, 47), (29305,))"
      ]
     },
     "execution_count": 99,
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
   "execution_count": 100,
   "id": "51a76757",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.neighbors import KNeighborsClassifier\n",
    "from sklearn.tree import DecisionTreeClassifier"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "id": "5da8a412",
   "metadata": {},
   "outputs": [],
   "source": [
    "knn_model = KNeighborsClassifier()\n",
    "tree_model = DecisionTreeClassifier()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "id": "403cc0a8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DecisionTreeClassifier()"
      ]
     },
     "execution_count": 102,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "knn_model.fit(X_train, y_train)\n",
    "tree_model.fit(X_train, y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "id": "a5c0fbc2",
   "metadata": {},
   "outputs": [],
   "source": [
    "knn_pre = knn_model.predict(X_test)\n",
    "tree_pre = tree_model.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "id": "50b40b88",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "id": "efe76b53",
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train2,X_val,y_train2,y_val = train_test_split(X_train,y_train,\n",
    "                                                test_size=0.3,\n",
    "                                                random_state=719)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "id": "2a19d4b6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "((20513, 47), (20513,))"
      ]
     },
     "execution_count": 106,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_train2.shape, y_train2.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "id": "ac86c6da",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "((8792, 47), (8792,))"
      ]
     },
     "execution_count": 107,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_val.shape, y_val.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "id": "2210e289",
   "metadata": {},
   "outputs": [],
   "source": [
    "train_score = [] # 훈련데이터의 점수가 들어갈 리스트\n",
    "val_score = [] # 검증데이터의 점수가 들어갈 리스트\n",
    "\n",
    "for n in range(1,20):\n",
    "    # 이웃을 1~19개까지 변경하면서 모델생성\n",
    "    model = KNeighborsClassifier(n_neighbors=n)\n",
    "    # 모델 학습\n",
    "    model.fit(X_train2,y_train2)\n",
    "    # 훈련데이터에 대한 점수 누적\n",
    "    train_score.append(model.score(X_train2,y_train2))\n",
    "    # 검증데이터에 대한 점수 누적\n",
    "    val_score.append(model.score(X_val,y_val))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "id": "1e5e317a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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IiKi88QA2IQMykjG8dxSnMi1a10KERERERE1QQyATUj/LomQJGAjJ4MhIiIiIqLzwADYhERHmJHeJhYbd6kzpxIREREREZ0LBsAmZlDXZGQXOnAk26Z1KURERERE1MQwADYxfTsnQq+TsPEPDgMlIiIiIqJzwwDYxERYjOjePg4bd2dD4TBQIiIiIiI6BwyATdDArskoKHHhwIlirUshIiIiIqImhAGwCeqdlgCjQcdhoEREREREdE4YAJsgi9mAXh3jsWl3NmRF0bocIiIiIiJqIhgAm6iBGckoKfNgz9EirUshIiIiIqImggGwierZMR5hJj02/JGtdSlERERERNREMAA2USajHn06JWLLnlx4ZQ4DJSIiIiKis2MAbMIGdU1CmcuLHYcKtC6FiIiIiIiaAAbAJqxruziEhxmwcReHgRIRERER0dkxADZhBr0O/bok4bd9eXB5ZK3LISIiIiKiIMcA2MQNykiCyy1j+4F8rUshIiIiIqIgxwDYxHVpE4vocBNnAyUiIiIiorNiAGzidDoJA9KTsPVAPhwur9blEBERERFREGMAbAYGdk2GV1bw275crUshIiIiIqIgxgDYDHRsGYX4qDBs3JWjdSlERERERBTEGACbAUmSMDAjCTsPFcDu8GhdDhERERERBSkGwGZiYEYyZEVgyx52AYmIiIiIqHYMgM1Em+QIJMdZOQyUiIiIiIjqxADYTEiShEEZSdh9pBBFdpfW5RARERERURBiAGxGBmYkQwDYtJtdQCIiIiIiqokBsBlpmRCO1KQIbNzFm8ITEREREVFNDIDNzMCMJBw4UYK8IofWpRARERERUZBhAGxmBmYkA+AwUCIiIiIiqokBsJlJjLGgQ8sobOAwUCIiIiIiqoYBsBkamJGMo9l2nMov1boUIiIiIiIKIgyAzdCA9CRIAO8JSEREREREVTAANkOxkWZ0aRODjbuyIYTQuhwiIiIiIgoSDIDN1MCMZJzKL8OxHLvWpRARERERUZBgAGym+nVJhE6SOAyUiIiIiIj8GACbqUirCV3bx3IYKBERERER+QU0AK5atQpjx47F6NGj8eGHH9bYv3btWkyYMAETJkzAvffei9JSddbKkydP4rrrrsNll12G2267zb+dzs2gjGTkFTtx8FSJ1qUQEREREVEQCFgAzM7OxsKFC/HRRx9h+fLl+PTTT7F/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Op1o164dnnvuuUCVGbSE2wHH6pcgFBnWy+6BFFb3vTyIiIiIiIjqgzeCD0JCkeFY8zLk4ztgGXsfDK26al0SERERERE1AWe7EXzAhoDS+XP98gnkY9tgvmA6wx8RERERETUYBsAg4/7jB3h2fAtj99EwdR2pdTlERERERNSMMAAGEe/xHXCtXwx9m14wD56qdTlERERERNTMMAAGCbnoJBzfvQZdbEtYLr4Vko7/NERERERE1LCYMoKA4rTBsfolSHojLGPugWSyaF0SERERERE1QwyAGhOyB85v/g1RWgDL6DnQRSZoXRIRERERETVTDIAaEkLA+fP7kE/vRdiImdAnp2ldEhERERERNWMMgBpyb/0K3r3rYeo7Cca0wVqXQ0REREREzRwDoEY8h7bAvfFzGDoMhKnfFVqXQ0REREREIYABUANy3mE4f3wTusT2CLtoJiRJ0rokIiIiIiIKAQyAjUwpLVRn/DRHwDJmDiSDSeuSiIiIiIgoRDAANiLhccGx5iUIjxOWy+ZCZ43RuiQiIiIiIgohDICNRAgFzh/fgpJ3FJaLZ0Mfn6p1SUREREREFGIYABuJe9NSeA9vgXnwNTC07aN1OUREREREFIIYABuB9/gOuH//Esb0ETD2GKN1OUREREREFKIMWhcQCiRLNEy9x8PU/wrO+ElERERERJphAGwE+vhUXvNHRERERESa4xBQIiIiIiKiEMEASEREREREFCIYAImIiIiIiEIEAyAREREREVGIYAAkIiIiIiIKEQyAREREREREIYIBkIiIiIiIKEQwABIREREREYUIBkAiIiIiIqIQYdC6gEDQ6SStSyAiIiIiImp0Z8tCkhBCNFItREREREREpCEOASUiIiIiIgoRDIBEREREREQhggGQiIiIiIgoRDAAEhERERERhQgGQCIiIiIiohDBAEhERERERBQiGACJiIiIiIhCBAMgERERERFRiGAAJCIiIiIiChEMgERERERERCGCAbAR2O12jB8/HsePH9e6lDN69dVXMW7cOIwbNw7PPfec1uXU6eWXX8bYsWMxbtw4LFq0SOtyzurZZ5/FvHnztC7jjKZPn45x48Zh0qRJmDRpErZu3ap1SbX64YcfMHnyZFx++eV48skntS6nVp999pn/5zhp0iT069cPjz/+uNZl1WnFihX+/++fffZZrcup01tvvYUxY8ZgwoQJeOONN7Qup4bqv+czMzMxYcIEjB49GgsXLtS4ugq1vR898MADWLp0qYZV1VS9zk8//RTjx4/HhAkT8NBDD8HtdmtcYYXqtX700UcYN24cxo4di2effRZCCI0rVNX1WWTx4sWYPn26RlXVVL3Ohx56CKNHj/b/Tv322281rlBVvc7ffvsNV199NcaNG4e//e1vQfvf6Nq1a6u8Rw0ePBizZ8/WukQANX+m69atw8SJEzF+/Hg88MADQfMzrV7n0qVLMXbsWEyYMAFPPvkkvF6vxhXWg6CA+v3338X48eNFt27dxLFjx7Qup07r168X11xzjXC5XMLtdosbbrhBfPPNN1qXVcOGDRvE1KlThcfjEQ6HQ4wcOVIcOHBA67LqlJmZKQYNGiQefPBBrUupk6IoYtiwYcLj8WhdyhkdPXpUDBs2TJw6dUq43W5x7bXXip9++knrss5o7969YtSoUSI/P1/rUmpVVlYmBgwYIPLz84XH4xFTpkwR69ev17qsGtavXy/Gjx8vbDab8Hq9Yvbs2WLNmjVal+VX/fe8w+EQI0aMEEePHhUej0fMmDEjKP5brV7n6dOnxezZs0XPnj3FF198oXV5ftXrPHjwoBg1apSw2WxCURTxwAMPiEWLFmldphCiZq1Hjx4Vo0aNEqWlpcLr9YprrrlG/Pzzz1qXWednkX379okLL7xQXH/99RpWV6G2OsePHy+ys7M1rqyq6nXabDZxwQUXiF27dgkhhJg7d6748MMPNa5SdabPoTk5OeKSSy4Rhw4d0qa4Smqrc/jw4WL//v1CCCHuuususWTJEi1LFELUrPPAgQPiwgsv9P83umDBAvHee+9pXOXZsQMYYEuWLMGCBQuQlJSkdSlnlJiYiHnz5sFkMsFoNKJjx444efKk1mXVMHDgQPznP/+BwWBAfn4+ZFmG1WrVuqxaFRUVYeHChbj11lu1LuWMDh48CACYMWMGJk6ciMWLF2tcUe2+/fZbjB07FikpKTAajVi4cCF69eqldVln9Nhjj2Hu3LmIi4vTupRaybIMRVHgcDjg9Xrh9XphNpu1LquGP/74A8OGDUNERAT0ej0uvPBCfPfdd1qX5Vf99/y2bdvQtm1bpKamwmAwYMKECVi9erXGVdasc9WqVbjkkktw+eWXa1xZVdXrNJlMWLBgASIiIiBJEjp37hw070/Va01NTcV///tfWK1WlJSUwG63IyoqSuMqa/8s4na78eijj2LOnDkaVlZV9TodDgdOnjyJv//975gwYQJeeeUVKIqicZU161y/fj169+6N9PR0AMDDDz+MUaNGaVmi35k+hz733HOYOnUq2rVr1/iFVVNbnbIsw263Q5ZluFyuoHh/ql7nnj170Lt3b//6yJEjg+r9qS4GrQto7v75z39qXUK9dOrUyb98+PBhfP311/j44481rKhuRqMRr7zyCt577z1cdtllSE5O1rqkWj366KOYO3cuTp06pXUpZ1RSUoIhQ4bgkUcegcfjwQ033ID27dvjggsu0Lq0Ko4cOQKj0Yhbb70Vp06dwkUXXYR77rlH67LqlJmZCafTGXQfriuLiIjA3XffjcsvvxwWiwUDBgxA3759tS6rhm7duuGpp57C7NmzYbFY8MMPPwTNsDqg5u/5nJwcJCYm+teTkpKQnZ3d2GXVUL3OmTNnAgC2bNmiRTl1ql5nq1at0KpVKwBAQUEBPvzwQzz99NNalFZDbe/xRqMRS5YswbPPPouePXv6Q4GWaqvzhRdewFVXXYXWrVtrUFHtqteZl5eHwYMHY8GCBYiMjMTs2bPx+eef4+qrr9aoQlX1Oo8cOQKr1Yq5c+fi4MGD6Nu3b9Bc+lHX59DDhw9j48aNQfM5tbY6HnvsMUyfPh0RERFo3bo1LrvsMg0qq6p6nenp6XjmmWdw6tQpJCUlYfXq1cjLy9OouvpjB5Cq2LdvH2bMmIEHHnggKP4iVJc5c+YgKysLp06dwpIlS7Qup4bPPvsMLVq0wJAhQ7Qu5az69OmD5557DpGRkYiLi8OUKVOwdu1arcuqQZZlZGVl4amnnsKnn36Kbdu2YdmyZVqXVadPPvkEf/3rX7Uu44x2796NL774Aj/++CN+/vln6HQ6vPvuu1qXVcOQIUMwefJkTJ8+HTNnzkS/fv1gNBq1LqtOiqJAkiT/uhCiyjqdn+zsbNx444246qqrMGjQIK3LOaOrr74aGzZsQEJCAl599VWty6lh/fr1OHXqFK666iqtSzmj1NRUvPbaa0hKSoLFYsH06dOD9v1p3bp1+Nvf/oalS5fC4XDgrbfe0rqsM/r0008xbdo0mEwmrUupVW5uLp5//nl8+eWXWLduHXr16hU0f/iprH379rj33ntx22234brrrkOXLl2C+v2pHAMg+W3ZsgU33XQT7r33Xlx55ZVal1OrAwcOYNeuXQAAi8WC0aNHY8+ePRpXVdNXX32F9evXY9KkSXjllVfwww8/4KmnntK6rFpt3rwZWVlZ/nUhBAyG4BsckJCQgCFDhiAuLg5hYWG49NJLsW3bNq3LqpXb7camTZtw8cUXa13KGa1btw5DhgxBfHw8TCYTJk+ejI0bN2pdVg12ux2jR4/GqlWr8MEHH8BkMiE1NVXrsuqUkpKC3Nxc/3pubm7QXwYQ7A4cOICpU6fiyiuvxB133KF1OXU6deqUv6NqMBgwbty4oHyP+vLLL7Fv3z5MmjQJDz/8MHbs2BGUIyr27NmDNWvW+NeD+f2pV69eSE1NhV6vx+WXXx6070/lvv/+e4wdO1brMuq0efNmdO7cGW3atIFOp8PVV18dlO9PLpcLPXv2xPLly/HJJ58gOTk5qN+fyjEAEgD1TeuOO+7A888/j3HjxmldTp2OHz+Ohx9+GG63G263G99//z369eundVk1LFq0CF9++SVWrFiBOXPm4OKLL8bf//53rcuqlc1mw3PPPQeXywW73Y5ly5YFzbULlY0cORLr1q1DSUkJZFnGzz//jG7dumldVq327NmDdu3aBe31qeXS09ORmZmJsrIyCCHwww8/oEePHlqXVcPx48dx++23w+v1wmaz4fPPPw/qobW9evXCoUOHcOTIEciyjC+//BLDhw/Xuqwmy2634+abb8bdd9+NGTNmaF3OGdlsNtx///0oKSmBEAJr1qwJyveop59+Gl9//TVWrFiBJ598Et27d8dLL72kdVk1CCHw1FNPobi4GB6PB59++mlQvj8NGzYMO3fu9F/y8eOPPwbt+xOgDqV2Op1BHVQ6d+6Mbdu2+YdTfv/990H5/lRWVoabbroJdrsdbrcbixcvDupgXS74/oxCmnj33XfhcrnwzDPP+LdNnToV1157rYZV1TRixAhs27YNV1xxBfR6PUaPHh3UgbUpGDlyJLZu3YorrrgCiqJg2rRp6NOnj9Zl1dCrVy/MnDkT06ZNg8fjwQUXXBC0w5eOHTuGlJQUrcs4q2HDhuGPP/7A5MmTYTQa0aNHD9xyyy1al1VDeno6Ro8ejYkTJ0KWZdx0001B+aG6nNlsxjPPPIO77roLLpcLI0aMCIprV5qqzz//HHl5eVi0aJH/1j8XX3wx7r77bo0rq6lz58645ZZbMHXqVOj1evTv3z/oh4IHs/T0dNxyyy249tpr4fV6MXr0aIwfP17rsmpo0aIFHn/8cdx6661wuVzIyMjAgw8+qHVZdTp+/HjQv0d17NgRd999N2644Qbo9Xq0bds2KG+pFBsbizvuuAPXXHMNvF6v/3Y1wU4SwXQlPREREREREQUMh4ASERERERGFCAZAIiIiIiKiEMEASEREREREFCIYAImIiIiIiEIEAyAREREREVGIYAAkIiI6Ty+//DKWL19+xmOWLl2K2bNn17pv+vTpWL16dQAqIyIiqh3vA0hERHSegvFedERERGfCAEhERM3Ohg0bsHDhQqSmpmLfvn3wer34xz/+ccYbyPfo0QO33HIL1q9fj5ycHMycORPTpk0DAHz22Wf4+OOPoSgKYmJi8Mgjj6Bjx46YN28eOnXqhJtvvhlr167F888/D51Oh4yMDGRmZuKjjz4CAOTm5uKWW27BqVOnoNfr8cILL6Bjx44AgG+//RZvvfUWnE4nJkyYgNtuuw0A8N133+HVV1+FoigIDw/HQw89hJ49e+Lf//43fv/9d+Tk5KBLly647bbbMH/+fLjdbgghMGXKFFx33XUB/gkTEVFTxSGgRETULG3btg0zZszA8uXLMXnyZCxcuPCMx7vdbsTGxuKTTz7BK6+8gqeffhoulwsbN27E8uXL8eGHH2L58uWYOXMm7rzzzirnFhYW4oEHHsC//vUvrFixAoMGDUJ2drZ//7FjxzB//nysWrUK/fv3x7vvvuvfV1paiiVLlmDJkiVYuXIl1q5diwMHDmDBggX497//jZUrV2LOnDm4/fbbYbfbAQAnTpzAsmXL8Pzzz+Pdd9/FxRdfjKVLl+Ktt97C5s2boShKA/4kiYioOWEHkIiImqWWLVsiIyMDANC1a1csW7bsrOdccsklAIBu3brB7XajrKwMP/30E44cOYKpU6f6jyspKUFRUZF/ffPmzejYsSPS09MBAFdeeSWefPJJ//6ePXuibdu2AICMjAx8++23/n1TpkyBwWBAREQExowZg8zMTLRp0waDBw9GamoqAGDIkCGIi4vDjh07AAC9e/eGwaC+hY8aNQoPPvggtm3bhiFDhuDhhx+GTse/7xIRUe0YAImIqFkKCwvzL0uSBCHEWc8xm83+4wFACAFFUTBp0iTcf//9AABFUZCTk4Po6Gj/eXq9vsbzVw5h5WGttlr0er1/WQgBg8EARVH8NVTe5/V6AQBWq9W/feTIkVizZg0yMzORlZWF1157DUuXLkVKSspZXy8REYUe/omQiIjoDIYNG4b//ve/yMnJAQB8/PHHuPHGG6sc07dvXxw+fBi7d+8GAKxZswYlJSU1Qlxtli9fDiEEiouL8fXXX+PCCy/EkCFDsG7dOhw7dgwAkJWVhVOnTqFXr141zr/33nvx1VdfYdy4cViwYAEiIiJw9OjRP/uyiYiomWIHkIiI6AyGDRuGWbNmYcaMGZAkCREREXj11VerhLuYmBi8+OKLePDBB6HT6dC9e3cYDAZYLJazPn9kZCQmT54Mp9OJ66+/HoMHDwYALFiwAHfeeSdkWUZYWBj+7//+D5GRkTXOv/322zF//nx8+umn0Ov1uPTSSzFgwICG+wEQEVGzIon6jIkhIiKiOtntdrz++uu46667YLFYsHPnTsyePRs///xzvbqAREREjYUdQCIiCgnvvPMOVq1aVeu+m2++GRMnTjzv546IiIDRaPRP6GIwGPDSSy8x/BERUdBhB5CIiIiIiChEcBIYIiIiIiKiEMEASEREREREFCIYAImIiIiIiEIEAyAREREREVGIYAAkIiIiIiIKEf8fKvLPWpgwITMAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 1080x360 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(15,5))\n",
    "plt.plot(range(1,20), train_score, label='train')\n",
    "plt.plot(range(1,20), val_score, label='test')\n",
    "plt.xticks(range(1,20))\n",
    "plt.grid()\n",
    "plt.legend()\n",
    "plt.ylabel('accuracy')\n",
    "plt.xlabel('n_neighbors')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 113,
   "id": "b3773de3",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import cross_val_score"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "id": "c7d67863",
   "metadata": {},
   "outputs": [],
   "source": [
    "test_score = []\n",
    "for d in range(1,30):\n",
    "    model = DecisionTreeClassifier(max_depth=d, random_state=720)\n",
    "    result = cross_val_score(model, X_train, y_train, cv=5) # 교차검증함수\n",
    "    test_score.append(result.mean())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "id": "1a853392",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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AAAAAIKGANiEsgsruPwTAAAAQNAQAJtIWaVHZZUepcazBQQAAACA4CAANhEWgAEAAAAQbATAJpJdWC5J3AMIAAAAIGgIgE0kx1Uhm9WixNiwYLcCAAAAoJUiADaRnMIKJcc5ZbPyLQcAAAAQHKSRJpLjqlAql38CAAAACKIQMz/5woUL9cILL8jr9WrKlCm65pprAue2bNmiWbNmBY5dLpdiYmL08ccfKy8vT/fee6/y8vIUFhamJ598Um3btjWzVVN5fX7lFVWqf9ekYLcCAAAAoBUzbQYwNzdXc+bM0TvvvKP58+frvffe086dOwPne/bsqQULFmjBggV69913FRMTowcffFCSNHPmTI0cOVLz58/XhAkT9OSTT5rVZpMoOFwln99gBhAAAABAUJkWAJcvX67BgwcrNjZW4eHhGj16tBYtWlTnc1988UUNGjRIAwcOlMvl0tatWzVp0iRJ0hVXXKHbb7/drDabRE5hzRYQaWwBAQAAACCITLsENC8vT0lJP17ymJycrMzMzJ88r7S0VHPnztXChQslSQcOHFCbNm00e/ZsrVmzRklJSbrvvvvMarNJ5BWxByAAAACA4DNtBtDv98tisQSODcM45viIjz76SBdccIESEhIkSV6vVz/88IMGDx6sDz/8UOeff/4x9wqeinp3StDV53dVRJg92K0AAAAAaMVMC4CpqanKz88PHOfn5ys5Ofknz/viiy80ZsyYwHFSUpIiIiI0cuRISdK4cePqnDk8lbRJjNCFg9oFuw0AAAAArZxpAfCcc87RihUr5HK5VFlZqcWLF2v48OHHPMcwDG3evFn9+/cPPNa+fXulpqbqm2++kSR99dVX6tWrl1ltAgAAAECrYVoATElJ0R133KHrr79el156qcaNG6eMjAxNmzZNGzdulFSz9YPdbldoaOgxH/vcc8/pn//8p8aNG6c33nhDjz76qFltAgAAAECrYTEMwwh2E42tsLBMfn+L+7IAAAAA4GdZrRYlJETWf74JewEAAAAABBEBEAAAAABaCQIgAAAAALQSBEAAAAAAaCUIgAAAAADQShAAAQAAAKCVCAl2A2awWi3BbgEAAAAAmtwvZaEWuQ8gAAAAAOCnuAQUAAAAAFoJAiAAAAAAtBIEQAAAAABoJQiAAAAAANBKEAABAAAAoJUgAAIAAABAK0EABAAAAIBWggAIAAAAAK0EARAAAAAAWgkCYBMoKyvTuHHjdPDgQdNrPf/88xo7dqzGjh2rJ554wtRazzzzjMaMGaOxY8fqtddeM7XWEY8//rhmzZplao3rrrtOY8eO1YQJEzRhwgRt2LDBtFpffvmlLr/8cl188cX6y1/+YlodSXr//fcDX9OECRM0YMAAPfzww6bVW7BgQeDP4uOPP25aHUl66aWXNHr0aI0fP14vvPCCKTWO/3u8fPlyjR8/XqNGjdKcOXNMrSVJM2fO1Lx58xq1Tl213nvvPY0bN07jx4/Xn//8Z7ndbtNqvfPOOxo7dqzGjBmjxx9/XIZhNFqtuuod8dZbb+m6664ztdaf//xnjRo1KvD37fPPPzet1vr163XllVdq7Nix+uMf/2jaz+ybb745ZgwZPHiwpk+fbkotSVq6dKkuueQSjRs3TjNnzjT1z+K8efM0ZswYjR8/Xn/5y1/k9XobrVZdv5fNGj/qew3g8Xg0ZcoUrVy50tRaZo0fddUya/z4uddRZowdddUza/yoq5ZZ48fxtcwcP+r6uswaP+qqZeb4YRoDpvr++++NcePGGb169TIOHDhgaq1ly5YZV111lVFdXW243W7j+uuvNxYvXmxKrZUrVxqTJk0yPB6PUVlZaYwcOdLYtWuXKbWOWL58uXHWWWcZd911l2k1/H6/MXToUMPj8ZhW44j9+/cbQ4cONbKzsw23221cffXVxtdff216XcMwjO3btxsXXnihUVhYaMrnr6ioMAYNGmQUFhYaHo/HmDhxorFs2TJTai1btswYN26cUVpaani9XmP69OnGZ5991qg1jv97XFlZaYwYMcLYv3+/4fF4jKlTpzbaz+74Wjk5Ocb06dONjIwM48MPP2yUGvXV2r17t3HhhRcapaWlht/vN2bOnGm89tprptTav3+/ceGFFxrl5eWG1+s1rrrqKuPbb79tlFp11Ttix44dxrBhw4xrr73W1Frjxo0zcnNzG61GfbVKS0uNIUOGGFu2bDEMwzDuuOMO4+233zal1tHy8vKM888/39izZ49ptYYPH27s3LnTMAzD+MMf/mDMnTvXlFq7du0yhg0bFvh5PfDAA8arr77aKLXq+r28cOFCU8aP+l4D7Nq1y7jqqquMPn36GN99910jfFV113rxxRdNGT/qqvXaa6+ZMn783OsoM8aO+uqZMX7UVWvevHmmjB+/9Hq0MceP+mqZMX7U9+ferPHDTMwAmmzu3Ll64IEHlJycbHqtpKQkzZo1Sw6HQ3a7XZ07d1ZWVpYptc4880y98cYbCgkJUWFhoXw+n8LDw02pJUnFxcWaM2eOfvvb35pWQ5J2794tSZo6daouueQSvfXWW6bV+vzzzzVmzBilpqbKbrdrzpw56tu3r2n1jvbggw/qjjvuUHx8vCmf3+fzye/3q7KyUl6vV16vV6GhoabU+uGHHzR06FBFRkbKZrNp2LBh+uKLLxq1xvF/jzMzM9WhQwe1a9dOISEhGj9+vBYtWmRKrYULF+r888/XxRdf3Cif/+dqORwOPfDAA4qMjJTFYlG3bt0abQw5vla7du303//+V+Hh4SopKVFZWZmio6MbpVZd9STJ7Xbr/vvv12233dZodeqqVVlZqaysLN19990aP368nn32Wfn9flNqLVu2TP369VOPHj0kSffee68uvPBCU2od7YknntCkSZN02mmnmVbL5/OprKxMPp9P1dXVjTaGHF9r27Zt6tevX+B45MiRjTaG1PV7ee/evaaMH/W9Bvjggw908803N+rvl7pqud1uU8aPumpZLBZTxo/6vodmjR311TNj/Kir1qFDh0wZP37p9Whjjh/11TJj/Kjvz71Z44eZQoLdQEv317/+tclqde3aNfD+3r179emnn+rf//63afXsdrueffZZvfrqq7rooouUkpJiWq37779fd9xxh7Kzs02rIUklJSU6++yzdd9998nj8ej6669Xx44dNWTIkEavtW/fPtntdv32t79Vdna2zj33XN1+++2NXud4y5cvV1VVlSmB4ojIyEjNmDFDF198sZxOpwYNGqQzzjjDlFq9evXSo48+qunTp8vpdOrLL79s9EsJj/97nJeXp6SkpMBxcnKycnNzTal18803S5LWrl3bKJ//52qlp6crPT1dkuRyufT222/rscceM6WWVDOGzJ07V48//rgyMjICL0LMqvfUU0/piiuuUNu2bRutTl21CgoKNHjwYD3wwAOKiorS9OnT9cEHH+jKK69s9Fr79u1TeHi47rjjDu3evVtnnHFGo10mX9/vr71792rVqlWN+vutrs/14IMP6rrrrlNkZKTatm2riy66yJRaPXr00OzZs5Wdna3k5GQtWrRIBQUFjVKrrt/L1157rSnjR32vAY68yP7Xv/71q2s0tFZjjh/11TJj/KivllljR1313n77ba1atarRx4+6at14442mjB8/93q0sceP+mqlp6c3+vhR38/r/fffN2X8MBMzgC3Qjh07NHXqVM2cObPR/nW2PrfddptWrFih7OxszZ0715Qa77//vtLS0nT22Web8vmP1r9/fz3xxBOKiopSfHy8Jk6cqG+++caUWj6fTytWrNCjjz6q9957T5mZmfrPf/5jSq2jvfvuu7rxxhtNrbF161Z9+OGH+uqrr/Ttt9/KarXqlVdeMaXW2Wefrcsvv1zXXXedbr75Zg0YMEB2u92UWkf4/X5ZLJbAsWEYxxyf6nJzczVlyhRdccUVOuuss0ytdeWVV2rlypVKTEzU888/b1qdZcuWKTs7W1dccYVpNY5o166d/v73vys5OVlOp1PXXXedqePI0qVL9cc//lHz5s1TZWWlXnrpJVNqHfHee+9p8uTJcjgcptXIz8/Xk08+qY8//lhLly5V3759G+0fI47XsWNH3Xnnnfrd736na665Rt27d2/0MeTo38vt2rUzdfxoytcAddUya/yoq5ZZ48fRtQ4dOmT62HF0vU6dOpk6fhxdy+zxo66fmVnjx9G1IiIiTB0/jv95mT1+mIEA2MKsXbtWN9xwg+68805ddtllptXZtWuXtmzZIklyOp0aNWqUtm3bZkqtTz75RMuWLdOECRP07LPP6ssvv9Sjjz5qSq01a9ZoxYoVgWPDMBQSYs5EeWJios4++2zFx8crLCxMF1xwgTIzM02pdYTb7dbq1at13nnnmVpn6dKlOvvss5WQkCCHw6HLL79cq1atMqVWWVmZRo0apYULF+rNN9+Uw+FQu3btTKl1RGpqqvLz8wPH+fn5TXKZd1PYtWuXJk2apMsuu0y///3vTauTnZ0dmNUMCQnR2LFjTRtDJOnjjz/Wjh07NGHCBN17773atGmTaTPu27Zt02effRY4Nnsc6du3r9q1ayebzaaLL77Y9HFkyZIlGjNmjKk11qxZo27duql9+/ayWq268sorTRtDqqurlZGRofnz5+vdd99VSkpKo44hx/9eNnP8aKrXAPXVMmv8OL6WmePH8bXMHjuOr2fm+HF8LTPHj/r+LJoxfhxfy8zx4/haZo8fpgnmDYityciRI01fBCYrK8s466yzjOXLl5taxzAM4+uvvzYuv/xyo7q62qiurjZu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\n",
      "text/plain": [
       "<Figure size 1080x360 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(15,5))\n",
    "plt.plot(range(1,30), test_score, label=['test'])\n",
    "plt.xticks(range(1,30))\n",
    "plt.grid()\n",
    "plt.legend()\n",
    "plt.ylabel('accuracy')\n",
    "plt.xlabel('max_depth')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "930e34b4",
   "metadata": {},
   "source": [
    "- KNN : 14\n",
    "- DecisionTree : 7"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "id": "f0eaaa47",
   "metadata": {},
   "outputs": [],
   "source": [
    "final_knn = KNeighborsClassifier(n_neighbors=7)\n",
    "final_tree = DecisionTreeClassifier(max_depth=4, random_state=720)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "id": "1e124b0c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DecisionTreeClassifier(max_depth=4, random_state=720)"
      ]
     },
     "execution_count": 117,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "final_knn.fit(X_train,y_train)\n",
    "final_tree.fit(X_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 118,
   "id": "831cc725",
   "metadata": {},
   "outputs": [],
   "source": [
    "knn_pre = final_knn.predict(X_test)\n",
    "tree_pre = final_tree.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 119,
   "id": "0d25e66a",
   "metadata": {},
   "outputs": [],
   "source": [
    "submission = pd.read_csv('./data/sample_class_submission.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 120,
   "id": "e643fe0c",
   "metadata": {},
   "outputs": [],
   "source": [
    "submission[\"income\"] = knn_pre"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 121,
   "id": "5a9f33e5",
   "metadata": {},
   "outputs": [],
   "source": [
    "submission.to_csv(\"./data/knn_pre_class.csv\", index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 122,
   "id": "5dbe82a5",
   "metadata": {},
   "outputs": [],
   "source": [
    "submission['income'] = tree_pre\n",
    "submission.to_csv(\"./data/tree_pre_class.csv\", index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "eaaa8dfb",
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
