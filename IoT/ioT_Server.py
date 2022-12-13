{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "23ee74d1",
   "metadata": {},
   "source": [
    "#### Flask Server\n",
    "- Python 언어기반 마이크로 웹 프레임워크"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "a828b231",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, render_template"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "bd98560d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "\u001b[31m   WARNING: This is a development server. Do not use it in a production deployment.\u001b[0m\n",
      "\u001b[2m   Use a production WSGI server instead.\u001b[0m\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://172.20.10.8:5041/ (Press CTRL+C to quit)\n",
      "172.20.10.8 - - [01/Aug/2022 17:34:34] \"GET / HTTP/1.1\" 200 -\n",
      "172.20.10.8 - - [01/Aug/2022 17:34:34] \"GET /favicon.ico HTTP/1.1\" 404 -\n",
      "172.20.10.8 - - [01/Aug/2022 17:34:42] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 2\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.8 - - [01/Aug/2022 17:34:46] \"GET / HTTP/1.1\" 200 -\n",
      "172.20.10.8 - - [01/Aug/2022 17:34:47] \"GET /led/off HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "LED꺼짐\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.8 - - [01/Aug/2022 17:34:49] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.8 - - [01/Aug/2022 17:35:47] \"GET /led/on HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "LED켜짐\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.8 - - [01/Aug/2022 17:35:50] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:40:33] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:40:33] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:40:34] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:40:34] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:40:35] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:40:35] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:40:51] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:41:12] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.8 - - [01/Aug/2022 17:41:21] \"GET /led/on HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "LED켜짐\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.8 - - [01/Aug/2022 17:41:24] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:41:25] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:41:29] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.8 - - [01/Aug/2022 17:41:31] \"GET /led/off HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "LED꺼짐\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.8 - - [01/Aug/2022 17:41:32] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:41:33] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:41:34] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:41:35] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:41:41] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:41:42] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:42:00] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:42:04] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:42:05] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:42:06] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:42:07] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:42:08] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:42:11] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:42:15] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:42:16] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:42:17] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:42:17] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:42:18] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:42:19] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:42:20] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:42:21] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:42:22] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:42:23] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:42:24] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:42:25] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:43:30] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:43:31] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:43:31] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:43:32] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:43:32] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:43:33] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:43:33] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:43:34] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:43:35] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:43:35] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:43:36] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:43:37] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.8 - - [01/Aug/2022 17:43:37] \"GET /led/on HTTP/1.1\" 200 -\n",
      "172.20.10.9 - - [01/Aug/2022 17:43:37] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "LED켜짐\n",
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:43:38] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:43:38] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:43:39] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:43:39] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:43:40] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:43:41] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:43:41] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:43:42] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:43:42] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:43:43] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:43:44] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:43:44] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:43:45] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:43:45] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:43:46] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:43:47] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:43:47] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:43:48] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:43:48] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:43:49] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:43:50] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:43:50] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:43:51] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:43:51] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:43:52] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:43:53] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:43:53] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:43:54] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:43:55] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:43:55] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:43:56] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:43:56] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:43:57] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:43:57] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:43:58] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:43:59] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:43:59] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:00] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:00] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:01] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:01] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:02] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:03] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:03] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:04] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:05] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:05] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:06] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:07] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:07] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:08] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:08] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:09] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:09] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:10] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:10] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:11] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:12] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:12] \"GET /led HTTP/1.1\" 200 -\n",
      "172.20.10.8 - - [01/Aug/2022 17:44:12] \"GET /led/on HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n",
      "LED켜짐\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:13] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:14] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:14] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:15] \"GET /led HTTP/1.1\" 200 -\n",
      "172.20.10.8 - - [01/Aug/2022 17:44:15] \"GET /led/on HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n",
      "LED켜짐\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:16] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:16] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:17] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:17] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:18] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n",
      "현재 led상태 : 1"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.8 - - [01/Aug/2022 17:44:18] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:18] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:19] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:20] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:20] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:21] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:21] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:22] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:23] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:23] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:24] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:24] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:25] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:26] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:26] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:27] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:27] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:28] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:28] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:29] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:30] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:30] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:31] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:31] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:32] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:33] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:33] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:34] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:34] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:35] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:35] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:36] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:37] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:37] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:38] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:38] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:39] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:39] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:40] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:41] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:41] \"GET /led HTTP/1.1\" 200 -\n",
      "172.20.10.8 - - [01/Aug/2022 17:44:41] \"GET /led/on HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n",
      "LED켜짐\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:42] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.8 - - [01/Aug/2022 17:44:42] \"GET /led/off HTTP/1.1\" 200 -\n",
      "172.20.10.9 - - [01/Aug/2022 17:44:42] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "LED꺼짐\n",
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:43] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.8 - - [01/Aug/2022 17:44:43] \"GET /led/off HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "LED꺼짐\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:43] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.8 - - [01/Aug/2022 17:44:44] \"GET /led/on HTTP/1.1\" 200 -\n",
      "172.20.10.9 - - [01/Aug/2022 17:44:44] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "LED켜짐\n",
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.8 - - [01/Aug/2022 17:44:44] \"GET /led/on HTTP/1.1\" 200 -\n",
      "172.20.10.8 - - [01/Aug/2022 17:44:44] \"GET /led/on HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "LED켜짐\n",
      "LED켜짐\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:44] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.8 - - [01/Aug/2022 17:44:45] \"GET /led/off HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "LED꺼짐\n",
      "LED꺼짐"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.8 - - [01/Aug/2022 17:44:45] \"GET /led/off HTTP/1.1\" 200 -\n",
      "172.20.10.9 - - [01/Aug/2022 17:44:45] \"GET /led HTTP/1.1\" 200 -\n",
      "172.20.10.8 - - [01/Aug/2022 17:44:45] \"GET /led/off HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "현재 led상태 : 0\n",
      "LED꺼짐\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.8 - - [01/Aug/2022 17:44:46] \"GET /led/on HTTP/1.1\" 200 -\n",
      "172.20.10.9 - - [01/Aug/2022 17:44:46] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "LED켜짐\n",
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:46] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:47] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:47] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:48] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:49] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:49] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.8 - - [01/Aug/2022 17:44:50] \"GET /led/on HTTP/1.1\" 200 -\n",
      "172.20.10.9 - - [01/Aug/2022 17:44:50] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "LED켜짐\n",
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.8 - - [01/Aug/2022 17:44:50] \"GET /led/off HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "LED꺼짐\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:50] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:51] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:51] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:52] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:53] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:53] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:54] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:54] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:55] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:56] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:56] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:57] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:58] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:58] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:59] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:44:59] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:45:00] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:45:01] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:45:01] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:45:02] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:45:02] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:45:03] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:45:03] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:45:04] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:45:05] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:45:05] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:45:06] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:45:06] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:45:07] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:45:08] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:45:08] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:45:09] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:45:10] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:45:10] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:45:11] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:45:12] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:45:13] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:45:17] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:45:18] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:45:18] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:45:19] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:45:19] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:45:20] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:45:21] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:45:21] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:45:22] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:45:22] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.8 - - [01/Aug/2022 17:45:23] \"GET /led/on HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "LED켜짐\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:45:23] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:45:24] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:45:24] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:45:25] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:45:26] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:45:26] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:45:27] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:45:28] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:45:28] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:45:29] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:45:29] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:45:30] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:45:31] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:45:31] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:45:32] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:45:32] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:45:33] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:45:33] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:45:34] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:45:35] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:45:35] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:45:36] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:45:36] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:45:37] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:45:38] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:45:38] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:45:39] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:45:39] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:45:58] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:45:59] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:46:00] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:46:01] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:46:01] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:46:05] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:04] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:04] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:05] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:05] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:06] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:06] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:07] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:08] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:08] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:09] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.8 - - [01/Aug/2022 17:47:09] \"GET /led/off HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "LED꺼짐\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:09] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:10] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:11] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:11] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:12] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:12] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:13] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:14] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:14] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:15] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:16] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:17] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:17] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:18] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:19] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:19] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:20] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:20] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:21] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:21] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:22] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:23] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:23] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:24] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:24] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:25] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:25] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:26] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:27] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:27] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:28] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:29] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:30] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:30] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:31] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:31] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:32] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:32] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:33] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:34] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:34] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:35] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:35] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:36] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:36] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:37] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:37] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:38] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:39] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:39] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:40] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:40] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:41] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:42] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:42] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:43] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:43] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:44] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:44] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:45] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:45] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:46] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:47] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:47] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:48] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:48] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:49] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:50] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:50] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:51] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:51] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:52] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:53] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:53] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:54] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:54] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:55] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:56] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:56] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:57] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:57] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:58] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:58] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:59] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:47:59] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:00] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:00] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:01] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:02] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:02] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:03] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:03] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:04] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:04] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:05] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:05] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:06] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:07] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:07] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:08] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:08] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:09] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:09] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:10] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:11] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:11] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:12] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:13] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:13] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:14] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:14] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:15] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:16] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:16] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:17] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:18] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:18] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:19] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:19] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:20] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:21] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:21] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:22] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:22] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:23] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:24] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:24] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:25] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:26] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:27] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:27] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:28] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:28] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:29] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:29] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:30] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:30] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:31] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:32] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:32] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:33] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:33] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:34] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:35] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:36] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:36] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:37] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:38] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:43] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:44] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:45] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:46] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:47] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:48] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:49] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:50] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:50] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:51] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:52] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:52] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:53] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:54] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:54] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:55] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:55] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:56] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:57] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:58] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:48:59] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:03] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:03] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:04] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:04] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:05] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:06] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:06] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:07] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:07] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:08] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:08] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:09] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:10] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:11] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:11] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:12] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:12] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:13] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:14] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:14] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:15] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:16] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:16] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:17] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:18] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:18] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:19] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:20] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:20] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:21] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:21] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:22] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:23] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:23] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:24] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:24] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:25] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:26] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:26] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:27] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:27] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:28] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:29] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:29] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:30] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:32] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:34] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:35] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:37] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:38] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:39] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:39] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:40] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:41] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:41] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:42] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:42] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:43] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:44] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:44] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:45] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:45] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:46] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:46] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:47] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:47] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:48] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:49] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:49] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:50] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:50] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:51] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:51] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:52] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:53] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:53] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:54] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:54] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:55] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:55] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:56] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:56] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:57] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:58] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:58] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:59] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:49:59] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:00] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:01] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:02] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:03] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:03] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:04] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:04] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:05] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:06] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:10] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:13] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:16] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:17] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:18] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:18] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:19] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:20] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:20] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:21] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:21] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:22] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:22] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:23] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:24] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:24] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:25] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:25] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:26] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:26] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:27] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:27] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:28] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:29] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:29] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:30] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:30] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:31] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:31] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:32] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:32] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:33] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:33] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:34] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:35] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:35] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:36] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:37] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:37] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:38] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:39] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:40] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:41] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:42] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:42] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:43] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:44] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:44] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:45] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:46] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:46] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:47] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:48] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:48] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:49] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:49] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:50] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:51] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:52] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:52] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:53] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:54] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:54] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:55] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:55] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:56] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:56] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:57] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:50:58] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:51:02] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:51:03] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:51:04] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:51:04] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:51:05] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:51:05] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:51:06] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:51:06] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:51:07] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:51:07] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:51:08] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:51:09] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:51:09] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:51:10] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:51:11] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:51:11] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:51:12] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:51:12] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:51:13] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:51:14] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:51:14] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:51:15] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:51:15] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:51:16] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:51:17] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:51:17] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:51:18] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:51:18] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:51:19] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:51:19] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:51:20] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:51:21] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:51:21] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:51:22] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:51:22] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:51:23] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:51:24] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:51:24] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:51:54] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:51:55] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "172.20.10.9 - - [01/Aug/2022 17:51:56] \"GET /led HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "현재 led상태 : 0\n"
     ]
    }
   ],
   "source": [
    "# 기본형태\n",
    "app = Flask(__name__)\n",
    "\n",
    "led = '2'\n",
    "\n",
    "@app.route('/')\n",
    "def index():\n",
    "    return render_template('index.html')\n",
    "\n",
    "@app.route('/led')\n",
    "def state():\n",
    "    global led\n",
    "    print(f\"현재 led상태 : {led}\")\n",
    "    return led\n",
    "\n",
    "@app.route('/led/on')\n",
    "def led_on():\n",
    "    global led\n",
    "    led = '1'\n",
    "    print(\"LED켜짐\")\n",
    "    return 'LED ON'\n",
    "\n",
    "@app.route('/led/off')\n",
    "def led_off():\n",
    "    global led\n",
    "    led = '0'\n",
    "    print(\"LED꺼짐\")\n",
    "    return 'LED OFF'\n",
    "\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run(host='172.20.10.8',port=5041)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "752581e1",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "58456037",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4a794cba",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9dcdcd02",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2afae281",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f2cc9096",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a477ed78",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "63a2f528",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a26ecdbe",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1b73b2f1",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2767dbf0",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c6b2c3b0",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d00fb86a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c3e148e1",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8b45f68c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cf8d95a7",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "380cbf32",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "afce758b",
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
