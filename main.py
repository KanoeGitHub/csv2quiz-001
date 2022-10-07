#!/usr/bin/env python3

import random
import pandas as pd
import time
import sys

#Grobal Variable
words = []
sentences = []
filepath = './test.csv'
wordColumnName = 'word'
sentColumnName = 'sent'
Points = 0
quizNum = []

def argCheck():
	global filepath
	global wordColumnName
	global sentColumnName
	args = sys.argv
	
	if 1 >= len(args):
		return ()
	elif 2 == len(args):
		filepath = args[1]
	elif 3== len(args):
		filepath = args[1]
		wordColumnName = args[2]
	elif 4 == len(args):
		filepath = args[1]
		wordColumnName = args[2]
		sentColumnName = args[3]
	
def readCSV(filepath, wName, sName):
	#ファイルの読み込み読み込み
	originFile = pd.read_csv(filepath, encoding='utf-8')
	global words
	global sentences
	#単語列の読み込み
	words = originFile[wName]
	#説明文の読み込み
	sentences = originFile[sName]

def checkAnswer(answer):
	global quizNum
	global words
	global Points
	if (answer == words[quizNum[0]]):
		print("Answer:", "正解!!!")
		Points = 1 + Points
	else:
		print("Answer:", "不正解!!!")
	del quizNum[0]

def main():
	argCheck()
	readCSV(filepath, wordColumnName, sentColumnName)
	
	global quizNum
	global sentences
	wordNum = len(words)
	
	if (wordNum < 20):
		quizNum = list(range(wordNum))
	else:
		quizNum = list(range(20))
		
	random.shuffle(quizNum)
	
	for i in range(len(quizNum)):
		print("・題" + str(i+1) + ": " + sentences[quizNum[0]])
		print("")
		print("・回答 → ", end="")
		
		answer = input()
		checkAnswer(answer)
		if i != len(quizNum):
			print("==========")
			print("=↓次の問題↓=")
			print("==========")
			#time.sleep(1)
		
	print("得点は "+ str(Points)+"点 です！")
	print("End Quiz")
		
	
if __name__ == "__main__":
	main()
	