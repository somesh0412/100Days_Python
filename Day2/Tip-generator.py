print("welcom to Tip generator")
Bill = float(input("Enter the total bill\n"))
Tip = float(input("Enter the percentage of tip will you want to give 10 or 15\n "))
Split = float(input("Enter the pepole split bill\n"))
Amount = (Bill * Tip) / 100
TotalBill = (Bill + Amount)
BillPerPerson = round(TotalBill / Split, 2) 
BillWithTip = print("the total biii is" ,BillPerPerson)
