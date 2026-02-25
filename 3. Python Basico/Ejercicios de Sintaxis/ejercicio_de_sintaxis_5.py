number_of_scores = int(input("Please input the number of scores: "))
all_scores = []
approved_scores = []
failed_scores = []
counter = 1

while counter <= number_of_scores:
    all_scores.append(float(input("Please enter the score: ")))
    counter = counter + 1

for x in all_scores:
    if x < 70:
        failed_scores.append(x)
    else:
        approved_scores.append(x)

#total average
total_average = sum(all_scores)/len(all_scores)

#approved_scores
try: 
    approved_average = sum(approved_scores)/ len(approved_scores)
except ZeroDivisionError:
    approved_average = "There are no approved scores"

#failed scores
try: 
    failed_average = sum(failed_scores)/len(failed_scores)
except ZeroDivisionError:
    failed_average = "There are no failed scores"

print('The number of approved scores is:', len(approved_scores))
print('The number of failed scores is:', len(failed_scores))
print(f'The total average is: {total_average}')
print(f'The average of approved scores is: {approved_average}')
print(f'The average of failed scores is: {failed_average}')