# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1=name1.lower()
name2=name2.lower()
name1_count_true= name1.count("t")+name1.count("r")+name1.count("u")+name1.count("e")
name2_count_true=name2.count("t")+name2.count("r")+name2.count("u")+name2.count("e")

true_count=name1_count_true+name2_count_true

name1_count_love=name1.count("t")+name1.count("r")+name1.count("u")+name1.count("e")
name2_count_love=name2.count("l")+name2.count("o")+name2.count("v")+name2.count("e")
love_count= name1_count_love+name2_count_love
love_score=int(str(true_count)+str(love_count))
print(love_score)

if love_score<10 or love_score>90:
  print(f"Your Score is {love_score}, you go together like coke and mentos")
elif love_score>40 and love_score<50:
  print(f"your scroe is {love_score}, you are alright together")
else:
  print(f"your score is {love_score}")






