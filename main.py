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
choice =  ['foo', 'bar', 'baz']

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
		print("")
		Points = 1 + Points
	else:
		print("Answer:", "不正解!!!")
		print("正解は: "+ words[quizNum[0]] +"です")
		print("")
	del quizNum[0]

def quiz1():
	global quizNum
	global sentences

	for i in range(len(quizNum)):
		print("・問題" + str(i+1) + ": " + sentences[quizNum[0]])
		print("")
		print("・回答 → ", end="")
		
		answer = input()
		checkAnswer(answer)

		if i != len(quizNum):
			print("==========")
			print("=↓次の問題↓=")
			print("==========")
			
def quiz2():
	global quizNum
	global sentences
	for i in range(len(quizNum)):
		createChoice()
		print("・問題" + str(i+1) + ": " + sentences[quizNum[0]])
		print("")
		for i in range(3):
			print("選択肢 "+str(i+1)+" :" + str(choice[i]) +" | ", end="")
		print("")
		print("選択肢の番号を入力してください: ", end="")

		inputJudge = False

		while (not inputJudge):
			try:
				answer = int(input()) -1
				if (answer <= 2 and answer >= 0):
					checkAnswer(choice[answer])
					inputJudge = True
				else:
					print("正しい選択肢の番号を入力してください: ", end="")
			except:
				print("正しい選択肢の番号を入力してください: ", end="")

		if i != len(quizNum):
			print("============")
			print("=↓次の問題↓=")
			print("============")
			#time.sleep(1)

def createChoice():
	global choice
	choice[0] = words[quizNum[0]]
	
	randValue = random.randint(0,len(words)-1)
	while (quizNum[0] == randValue):
		randValue = random.randint(0,len(words)-1)
	choice[1] = words[randValue]

	randValue2 = random.randint(0,len(words)-1)
	while (quizNum[0] == randValue or randValue == randValue2):
		randValue2 = random.randint(0,len(words)-1)
	choice[2] = words[randValue2]

	random.shuffle(choice)

def main():
	argCheck()
	readCSV(filepath, wordColumnName, sentColumnName)
	
	global quizNum
	global sentences
	questionsNum = 0
	MaxQuestionNum = 20
	wordNum = len(words)
	
	if (wordNum < MaxQuestionNum):
		quizNum = list(range(wordNum))
		questionsNum = wordNum
	else:
		quizNum = list(range(MaxQuestionNum))
		questionsNum = MaxQuestionNum
		
	random.shuffle(quizNum)
	
	print("どちらのクイズを選びますか?（1: 一致/2: 三択）")

	inputJudge = False
	while (not inputJudge):
		try: 
			modeselect = int(input())
			if (modeselect == 1):
				quiz1()
				inputJudge = True
			elif (modeselect == 2):
				quiz2()
				inputJudge = True
			else:
				print("正しい選択肢の番号を入力してください: ", end="")
		except:
			print("正しい選択肢の番号を入力してください: ", end="")
		
	print("得点は "+ str(Points)+"/" + str(questionsNum) + "点です！")
	print("End Quiz")
	
	
if __name__ == "__main__":
	main()
	