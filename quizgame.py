questionlist = ['pehla prashn', 'dusra prashn', 'three prashn']
answerlist = ['tarak', 'mehta', 'oolta']
score = 0
for question in questionlist:
    print(question)
    answer = input('your answer is: \n')
    index = questionlist.index(question)
    if answer == answerlist[index]:
        print('correct')
        score +=2
    else:
        print('incorrect')
        score -= 1

print('Your Final Score is : ',score)
