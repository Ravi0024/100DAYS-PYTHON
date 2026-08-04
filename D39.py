"   day - 27 kbc solun      "
questions =  questions = [
        [
            "What is the capital city of India?",
            "1. Mumbai", "2. New Delhi", "3. Kolkata", "4. Chennai", 2
        ],
        [
            "Which planet is known as the Red Planet?",
            "1. Earth", "2. Venus", "3. Mars", "4. Jupiter", 3
        ],
        [
            "Who wrote the national anthem of India?",
            "1. Rabindranath Tagore", "2. Bankim Chandra Chatterjee", "3. Subhash Chandra Bose", "4. Mahatma Gandhi", 1
        ],
        [
            "Which is the smallest state in India by area?",
            "1. Sikkim", "2. Goa", "3. Tripura", "4. Mizoram", 2
        ],
        [
            "What is the national currency of Japan?",
            "1. Yuan", "2. Won", "3. Dollar", "4. Yen", 4
        ]
    ]
levels = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000]
money = 0

for i in range(0 , len(questions)):
    question = questions[i]
    
    print(f"\n\nQuestion for Rs. {levels[i]}")
    print(f" a.{question[1]}           b.{question[2]} ")
    print(f" c.{question[3]}           d.{question[4]} ")

    reply = int(input("Enter your answer (1-4): "))

    if(reply == question[-1]):
        print(f"correct answer, you have won RS.{levels[i]}")
        money = levels[i]

        if(i==4):
            money = 10000
        elif (i==9):
            money = 320000
        elif (i==14):
            money = "jackpot"
    else:
        print("wrong answer!")
        break
print(f"\nyour take home money is Rs. {money}")