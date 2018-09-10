
import csv
import sys

dateList = []
profitLossList = []
monthlyChange = []

budgetData = {
    "monthYear": dateList,
    "profitLoss": profitLossList,
    "monthlyChange": monthlyChange
}

with open('budget_data.csv', "r", newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    next(csvreader, None)
    
    for row in csvreader:
        profitLossList.append(row[1])
        dateList.append(row[0])

def profitLossCalc():
    i = 1
    for num in range(len(profitLossList)-1):
        change = int(budgetData["profitLoss"][i])-int(budgetData["profitLoss"][i-1])
        monthlyChange.append(
            int(budgetData["profitLoss"][i])-int(budgetData["profitLoss"][i-1])
         )
        i += 1

profitLossCalc()



averageChange = sum(monthlyChange)/len(monthlyChange)
greatestIncrease = max(monthlyChange)
greatestDecrease = min(monthlyChange)
greatestIncreaseMonth = dateList[monthlyChange.index(greatestIncrease)+1]
greatestDecreaseMonth = dateList[monthlyChange.index(greatestDecrease)+1]

totalPL = 0
for num in profitLossList:
    totalPL += int(num)

def budgetSummary():
    print(
"""
Financial Analysis
----------------------------
"""
"Total Months: " , len(profitLossList),
f"\nTotal: ${totalPL}",
f"\nAverage Change: ${round(averageChange,2)}",
"\nGreatest Increase in Profits:" , greatestIncreaseMonth , f"(${greatestIncrease})",
"\nGreatest Decrease in Profits:" , greatestDecreaseMonth , f"(${greatestDecrease})"
)

budgetSummary()

sys.stdout = open("budget_data_homework.txt", "w")
print (budgetSummary())