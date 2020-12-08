import random

f=open("input.txt","r")
result="'"
for lines in f:
    if(lines=="\n"):
        continue
    result+=lines

words_dict={}

words=result.split(' ')

for i in range(len(words)-1):
    if words[i] not in words_dict:
        words_dict[words[i]]={}
    if words[i+1] not in words_dict[words[i]]:
            words_dict[words[i]][words[i+1]]=0
    words_dict[words[i]][words[i+1]]+=1



current_word=input()
word_count=int(input())
while(word_count>0):
    try:
        word=random.choices(list(words_dict[current_word].keys()),weights=words_dict[current_word].values())[0]
    except:
        break
    print(word,end=" ")
    current_word=word
    word_count-=1