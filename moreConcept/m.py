score =[10,30,59,88,999,56,59,1000,2000,3000]

print(len(score))  #length of the list

Total_score = sum(score)  #sum of all the elements in the list
print(f"Total score: {Total_score}")
# both are give differnt output because in for loop we are adding each element one by one and in sum() function it is adding all the elements at once.
sum=0
for i in score:
    sum+=i
    print(f"Total score using for loop: {sum}") 

max_score = score[0]
for element in score:
    if element > max_score:
        max_score = element
print(f"Highest score: {max_score}")

for x in range(10):
    if x%3==0:
        continue
    print(x)

    for y in range(100):
        if y%10==0:
            break
        print(y)

   