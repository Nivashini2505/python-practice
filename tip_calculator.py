print("welcome to the tip calculator ")
total_bill=float(input("what was the total bill?"))
tip_estimate=int(input("how much tip would you like to give? 10,12 or 15"))
no_of_people=int(input("How many people to slpit the bill?"))
amount_each_pay=float((total_bill+tip_estimate)/no_of_people)

print(round(amount_each_pay,2))