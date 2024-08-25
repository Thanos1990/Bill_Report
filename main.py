from datetime import datetime
from flat import Bill, Flatmate
from reports import PdfReport

amount = float(input("User, enter the bill amount: "))

name1 = input("What is your name? ")
days_in_house1 = int(input(f"hey {name1}, how many days you stayed? "))

name2 = input("What is your name? ")
days_in_house2 = int(input(f"hey {name2}, how many days you stayed? "))

the_bill = Bill(amount=amount,period=datetime.now().strftime('%B-%Y'))
flatmate1 = Flatmate(name=name1, days_in_house=days_in_house1)
flatmate2 = Flatmate(name=name2, days_in_house=days_in_house2)

print(f"{name1} pays ", flatmate1.pays(bill=the_bill, flatmate2=flatmate2))
print(f"{name2} pays ", flatmate2.pays(bill=the_bill, flatmate2=flatmate1))

pdf_report = PdfReport(filename=r"C:\Users\thana\OneDrive\Documents\Udemy\Python_OOP\App_2\files\bill.pdf")
pdf_report.generate(flatmate1=flatmate1, flatmate2=flatmate2, bill=the_bill)