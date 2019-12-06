# !/usr/bin/env python3
# Justin Mantis
# 12/5/19
# Quarterly Sales Thing
def Welcome_Greating():
    print("The Quarterly Sales prgram")
    print()

def Calculation(sales_list, Q1, Q2, Q3, Q4):
    total = 0
    count = len(sales_list)

    # Getting total
    total += float(Q1)
    total += float(Q2)
    total += float(Q3)
    total += float(Q4)
    total = round(total, 2)
    

    # Getting average
    average =  round(total / count, 2)
    

    # Getting lowest & highest numbers
    minu = min(sales_list)
    maxim = max(sales_list)
    return total, average, minu, maxim
def Quarterly_Sales():
    
    # defines list
    sales_list = []

    Q1 = input("Enter sales for Q1: ")
    Q2 = input("Enter sales for Q2: ")
    Q3 = input("Enter sales for Q3: ")
    Q4 = input("Enter sales for Q4: ")
    sales_list.append(Q1)
    sales_list.append(Q2)
    sales_list.append(Q3)
    sales_list.append(Q4)
    return sales_list, Q1, Q2, Q3, Q4
def main():
    Welcome_Greating()
    sales_list, Q1, Q2, Q3, Q4 = Quarterly_Sales()
    total, average, minu, maxim = Calculation(sales_list, Q1, Q2, Q3, Q4)

    #Print's Display
    print()
    print("Total:             ", total)
    print("Average Quarter:   ", average)
    print("Lowest Quarter:    ", minu)
    print("Highest Quarter:   ", maxim)



main()