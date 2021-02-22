#coding: utf-8
wordlist = list(input())

TatsuyaList = []
for i in range(0, int(len(wordlist))):
    TatsuyaList.append(wordlist[i])
    TatsuyaList.append('゛')

print(*TatsuyaList)