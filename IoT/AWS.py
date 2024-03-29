{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1542690d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: boto3 in c:\\users\\ai\\anaconda3\\lib\\site-packages (1.21.32)\n",
      "Requirement already satisfied: jmespath<2.0.0,>=0.7.1 in c:\\users\\ai\\anaconda3\\lib\\site-packages (from boto3) (0.10.0)\n",
      "Requirement already satisfied: botocore<1.25.0,>=1.24.32 in c:\\users\\ai\\anaconda3\\lib\\site-packages (from boto3) (1.24.32)\n",
      "Requirement already satisfied: s3transfer<0.6.0,>=0.5.0 in c:\\users\\ai\\anaconda3\\lib\\site-packages (from boto3) (0.5.0)\n",
      "Requirement already satisfied: python-dateutil<3.0.0,>=2.1 in c:\\users\\ai\\anaconda3\\lib\\site-packages (from botocore<1.25.0,>=1.24.32->boto3) (2.8.2)\n",
      "Requirement already satisfied: urllib3<1.27,>=1.25.4 in c:\\users\\ai\\anaconda3\\lib\\site-packages (from botocore<1.25.0,>=1.24.32->boto3) (1.26.9)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\ai\\anaconda3\\lib\\site-packages (from python-dateutil<3.0.0,>=2.1->botocore<1.25.0,>=1.24.32->boto3) (1.16.0)\n"
     ]
    }
   ],
   "source": [
    "!pip3 install boto3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "2c424303",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Detected labels in human.jpg\n",
      "강아지가 아닙니다\n",
      "Labels detected: 11\n"
     ]
    }
   ],
   "source": [
    "import boto3\n",
    "\n",
    "def detect_labels_local_file(photo):\n",
    "    \n",
    "    client=boto3.client('rekognition')\n",
    "    \n",
    "    with open(photo, 'rb') as image:\n",
    "        response = client.detect_labels(Image={'Bytes': image.read()})\n",
    "        \n",
    "    print('Detected labels in ' + photo)\n",
    "#     print(response)\n",
    "    \n",
    "    check = True\n",
    "    \n",
    "    for label in response['Labels']:\n",
    "        \n",
    "        if label[\"Name\"] == 'Dog':\n",
    "            print('강아지일 확률은 {:.2f}%입니다.'.format(label['Confidence']))\n",
    "        # 강아지가 아닌 사진을 넣었을 때 (즉, label중에 'Dog'이 없을 때)\n",
    "        # '강아지가 아닙니다' 출력\n",
    "#         print (label['Name'] + ' : ' + str(label['Confidence']))\n",
    "            check = False\n",
    "    if check == True:\n",
    "        print('강아지가 아닙니다')\n",
    "    return len(response['Labels'])\n",
    "\n",
    "def main():\n",
    "    photo='human.jpg'\n",
    "    label_count=detect_labels_local_file(photo)\n",
    "    print(\"Labels detected: \" + str(label_count))\n",
    "    \n",
    "if __name__ == \"__main__\":\n",
    "    main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "e39eeee8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "동일 인물일 확률은 8.677624702453613%입니다\n",
      "Face matches: 1\n"
     ]
    }
   ],
   "source": [
    "import boto3\n",
    "\n",
    "def compare_faces(sourceFile, targetFile):\n",
    "    \n",
    "    client=boto3.client('rekognition')\n",
    "    imageSource=open(sourceFile,'rb')\n",
    "    imageTarget=open(targetFile,'rb')\n",
    "    response=client.compare_faces(SimilarityThreshold=0,\n",
    "                                  SourceImage={'Bytes': imageSource.read()},\n",
    "                                  TargetImage={'Bytes': imageTarget.read()})\n",
    "    \n",
    "    for faceMatch in response['FaceMatches']:\n",
    "        \n",
    "        print('동일 인물일 확률은 {}%입니다'.format(faceMatch['Similarity']))\n",
    "        \n",
    "    imageSource.close()\n",
    "    imageTarget.close()\n",
    "    return len(response['FaceMatches'])\n",
    "\n",
    "def main():\n",
    "    source_file='KakaoTalk_20220913_135353228.jpg'\n",
    "    target_file='KakaoTalk_20220913_135231226.jpg'\n",
    "    face_matches=compare_faces(source_file, target_file)\n",
    "    print(\"Face matches: \" + str(face_matches))\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "ebfb7a8f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Detected faces for lee482.jpg\n",
      "Celebrities detected: 0\n"
     ]
    }
   ],
   "source": [
    "import boto3\n",
    "import json\n",
    "def recognize_celebrities(photo):\n",
    "    client=boto3.client('rekognition')\n",
    "    with open(photo, 'rb') as image:\n",
    "        response = client.recognize_celebrities(Image={'Bytes': image.read()})\n",
    "    print('Detected faces for ' + photo)\n",
    "    for celebrity in response['CelebrityFaces']:\n",
    "        print ('Name: ' + celebrity['Name'])\n",
    "    return len(response['CelebrityFaces'])\n",
    "def main():\n",
    "    photo='lee482.jpg'\n",
    "    celeb_count=recognize_celebrities(photo)\n",
    "    print(\"Celebrities detected: \" + str(celeb_count))\n",
    "if __name__ == \"__main__\":\n",
    "    main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "3f400996",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Detected faces for KakaoTalk_20220913_135353228.jpg\n",
      "The detected face is between 13 and 21 years old\n",
      "Gender: {'Value': 'Female', 'Confidence': 99.99954986572266}\n",
      "Smile: {'Value': True, 'Confidence': 94.46623229980469}\n",
      "Eyeglasses: {'Value': False, 'Confidence': 97.70550537109375}\n",
      "Emotions: {'Type': 'HAPPY', 'Confidence': 98.62644958496094}\n",
      "Faces detected: 1\n"
     ]
    }
   ],
   "source": [
    "#Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.\n",
    "#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)\n",
    "import boto3\n",
    "import json\n",
    "def detect_faces(photo):\n",
    "    client=boto3.client('rekognition')\n",
    "    with open(photo, 'rb') as image:\n",
    "        response = client.detect_faces(Image={'Bytes': image.read()},Attributes=['ALL'])\n",
    "    print('Detected faces for ' + photo)\n",
    "    for faceDetail in response['FaceDetails']:\n",
    "        print('The detected face is between ' + str(faceDetail['AgeRange']['Low'])\n",
    "              + ' and ' + str(faceDetail['AgeRange']['High']) + ' years old')\n",
    "\t\t# Access predictions for individual face details and print them\n",
    "        print(\"Gender: \" + str(faceDetail['Gender']))\n",
    "        print(\"Smile: \" + str(faceDetail['Smile']))\n",
    "        print(\"Eyeglasses: \" + str(faceDetail['Eyeglasses']))\n",
    "        print(\"Emotions: \" + str(faceDetail['Emotions'][0]))\n",
    "    return len(response['FaceDetails'])\n",
    "def main():\n",
    "    photo='KakaoTalk_20220913_135353228.jpg'\n",
    "    face_count=detect_faces(photo)\n",
    "    print(\"Faces detected: \" + str(face_count))\n",
    "if __name__ == \"__main__\":\n",
    "    main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cdfdf8bd",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "73c7358a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "17f9264b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "aaf794fd",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6835ed63",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4a72ccd2",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d543e422",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ef72e0c6",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "34b8d8b1",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9eca7c74",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "085a60b3",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2b6f04e5",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3c16d49c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cafd818e",
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
