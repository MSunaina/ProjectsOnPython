import random
def choose():
    words=['Computer','Technology','Software','Compilation','Interpreter','Coding','Testing','Developer']
    pick=random.choice(words)
    return(pick)
def jumbled(word):
    jumble="".join(random.sample(word,len(word)))
    return(jumble)
def play():
    p1=input("Hello,Enter first player name:")
    p2=input("Hello,Enter second player name:")
    pp1=0
    pp2=0
    turn=0
    while(1):
        #computer task
        picked_word=choose()
        #Questions
        q=jumbled(picked_word)
        print(q)
        #player1
        if turn%2==0:
            print(p1,"It's your turn")
            ans=input("Guess the word:")
            if ans==picked_word:
                print("Right")
                pp1+=1
                print("Your score:",pp1)
            else:
                print("Try again")
                print("The word is",picked_word)
                print("Your score:",pp1)
            c=int(input("1(continue)or 0(quit)"))
            if c==0:
                print("Thank You For Playing",p1,"and",p2)
                print(p1," Your Score:",pp1)
                print(p2,"Your Score:",pp2)
                break
        else:
            print(p2,"It's your turn")
            ans=input("Guess the word:")
            if ans==picked_word:
                print("Right")
                pp2+=1
                print("Your score:",pp2)
            else:
                print("Try again")
                print("The word is",picked_word)
                print("Your score:",pp2)
            c=int(input("1(continue)or 0(quit)"))
            if c==0:
                print("Thank You For Playing",p1,"and",p2)
                print(p1," Your Score:",pp1)
                print(p2," Your Score:",pp2)
                break
        turn=turn+1
play()