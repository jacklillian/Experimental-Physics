# Chapter Four Exercise One

import numpy as np

acct_balance= float(raw_input("How much money is in your lunch account?"))                        # prompts user to enter input defining their lunch account balance in dollars
day_of_month= eval(raw_input("What day of the month is today?"))                                  # prompts user to enter input defining the day of the month
days_in_month= eval(raw_input("How many days in this month?"))                                    # prompts user to enter the amount of days in the present month

permitted_spending= acct_balance/((days_in_month+1.0) - day_of_month)                             # calculates the amount of money, in dollars, the user can spend on lunch each day for the rest of the month
print ("You can spend ${0:0.2f} each day for the rest of the month.".format (permitted_spending)) # prints output displaing the permitted spending, in dollars, on lunch each day for the rest of the month

