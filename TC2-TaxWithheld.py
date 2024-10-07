# Tax Withheld Calculator

# Write a console program that calculates the total amount of tax withheld from an employee’s weekly salary.
# The total withheld tax amount is calculated by combining the amount of provincial tax withheld and the amount of 
# federal tax withheld, minus a per-dependent deduction from the total tax withheld. The user will enter their pre-tax 
# weekly salary amount and the number of dependents they wish to claim. 
# 
# The program will calculate and output the amount of provincial tax withheld, amount of federal tax withheld, the 
# dependent tax deduction, and the user’s final take-home amount.
# Provincial withholding tax is calculated at 6.0%. Federal withholding tax is calculated at 25.0%. 
# The tax deduction for dependents is calculated at 2.0% of the employee’s salary per dependent.

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    weeklySalary = float(input("Enter the full amount of your weekly salary: ")) #input for weekly salary
    dependants = int(input("Enter how many dependants you have: ")) #input for dependants

    provTax = weeklySalary * 0.06   #calculates provincial tax
    fedTax = weeklySalary * 0.25    #calculates federal tax
    depDeduction = dependants * (weeklySalary * 0.02)   #calculates dependants deduction
    totalWithheld = (provTax + fedTax) - depDeduction   #calculates total amount of money withheld
    totalTake = weeklySalary - totalWithheld    #calculates weekly salary minus total deductions

    print("Provincial Tax Withheld: ${0:.2f}\nFederal Tax Withheld: ${1:.2f}\nDependent Deduction for {2} dependents: ${3:.2f}\nTotal Withheld: ${4:.2f}\nTotal Take-Home Pay: ${5:.2f}".format(provTax,fedTax,dependants,depDeduction,totalWithheld,totalTake)) #formatted print statement using newline command and .format to inject our values





    # YOUR CODE ENDS HERE

main()
