#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':

    # List for dictionaries with bank accounts
    requisites = []

    # Endless program call
    while True:

        # Entering the required command
        command = input ("Enter Command: ").lower()

        # Command to end the program
        if command == "exit":
            break

        # Command to add bank accounts
        elif command == "add":

            while True:
                s_b_a = input("Enter the sender's bank account: ")

                # Checking the spelling of a bank account
                if len(s_b_a) != 20 or s_b_a.isdigit() is False:
                    print("Incorrect bank account!")
                else:
                    break

            while True:
                b_a = input("Enter the beneficiary's account: ")

                # Checking the spelling of a bank account
                if len(b_a) != 20 or b_a.isdigit() is False:
                    print("Incorrect bank account!")
                else:
                    break

            t_a = input("Enter transfer amount in ₽: ")

            # Creating dictionary with bank account
            requisite = {
                "s_b_a": s_b_a,
                "b_a": b_a,
                "t_a": t_a,
            }

            # Adding to the list
            requisites.append(requisite)

            # Sorting
            if len(requisites) > 1:
                requisites.sort(key=lambda item: item.get("s_b_a", ""))

        # Command for displaying entered values
        elif command == "list":

            # Create a table header
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 2,
                '-' * 25,
                '-' * 25,
                '-' * 10
            )
            print(line)
            print(
                '| {:^2} | {:^25} | {:^25} | {:^10} |'.format(
                    "№",
                    "Sender bank account",
                    "beneficiary account",
                    "Amount",
                )
            )
            print(line)

            # Filling the table with entered values
            for ind, requisite in enumerate(requisites, 1):
                print(
                    '| {:^2} | {:^25} | {:^25} | {:^10} |'.format(
                        ind,
                        requisite.get('s_b_a'),
                        requisite.get('b_a'),
                        requisite.get('t_a'),
                    )
                )
                print(line)

        # The command to receive the withdrawn amount from bank account
        elif command.startswith("select "):

            # Splitting input into 2 words
            parts = command.split(" ", maxsplit=1)

            # Assign value to second word (number of bank account)
            bank_acc = int(parts[1])

            full_summa = 0
            for requisite in requisites:

                # Comparison of each dictionary from the list by key "s_b_a" with the entered one
                if int(requisite.get("s_b_a")) == bank_acc:

                    # Calculation of the withdrawn amount from bank account
                    full_summa += float(requisite.get("t_a"))

            # Checking for the existence of such an account
            if full_summa == 0:
                print("This bank account does not exist")
            else:
                print("The sum of all transfers of the entered", end=" ")
                print(f"bank account is equal to {full_summa}")

        # Help Command
        elif command == 'help':
            print("Command List:\n")
            print("add - Add bank account;")
            print("list - Display a list of bank accounts;")
            print("select <bank account> -", end=" ")
            print("The withdrawn amount from account;")
            print("help - Display Help;")
            print("exit - End the program.")
            print("\n")

        # Incorrect command message
        else:
            print(f"Invalid command {command}", file=sys.stderr)
