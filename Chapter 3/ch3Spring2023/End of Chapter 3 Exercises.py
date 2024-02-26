print("Output for question 1:")
Midterm = [95, 78, 77, 86, 90, 88, 81, 66]
from HelperModule import RoundedAverage
max_value = max(Midterm)
min_value = min(Midterm)
range_value = max_value - min_value
Average = RoundedAverage(Midterm)
print(f"The range for the Midterm scores is: {max_value}-{min_value} = {range_value}")
print(f"The average for the Midterm scores is: {sum(Midterm)}/{len(Midterm)} = {Average}")
print()

print("Output for question 2:")
inp= "University of Kentucky"
print(inp[5:10]) #rsity
print(inp[-1]) #y
print(inp[:10]) #University
print(inp[5:]) #rsity of Kentucky
print()

print("Output for question 3:")
email= "John.Smith@uky.edu"
print(email.find("y")) #13
print()

print("Output for question 4:")
llst=[[1,2,3,5],[2,2,6,8],[2,3,5,9],[3,5,4,7],[1,3,5,0]] 
print(llst[2]) # [2,3,5,9] 
print(llst[2][2]) # 5 
print(llst[3][0]) # 3
print()

print("Output for question 5:")
llst=[1, "a", "hello", 2]
llst.remove(1) #["a", "hello", 2]
print(llst)
print()

print("Output for question 6:")
llst=[1, "a", "hello", 2]
llst.append("hi")
print(llst) # [1, "a", "hello", 2, "hi"]
print()

print("Output for question 7:")
Scores2 = {'blue':[5, 5, 10], 'white':[5, 7, 12]}
print(Scores2['blue'][2]) # 10
print()

print("Output for question 8:")
tpl=(1,2,3,9,0)
print(tpl[3:4]) # 9,
print()

print("Output for question 9:")
lst=[1, "a", "hello", 2]
dict_={x:y for x,y in enumerate(lst)}
print(dict_) # {0: 1, 1: 'a', 2: 'hello', 3: 2}
#print(dict_[2])
print()