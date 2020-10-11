# # Write your code here
# import random
# import sqlite3
#
# conn = sqlite3.connect('card.s3db')
# cur = conn.cursor()
# cur.execute('CREATE TABLE IF NOT EXISTS card '
#             '(id INTEGER PRIMARY KEY AUTOINCREMENT, '
#             'number TEXT, '
#             'pin TEXT, '
#             'balance INTEGER DEFAULT 0);')
# conn.commit()
#
#
# class Create(card=None):
# 	def __init__(self,card):
# 		self.card_no = '400000'
# 		self.N = 0
# 		self.new_card = ''
# 		self.card = card
#
# 	def check_card(self,card):
# 		Create.luhn_algorithm(card)
# 	def rand_n(self):
# 		mini = pow(10, self.N - 1)
# 		maxi = pow(10, self.N) - 1
# 		return str(random.randint(mini, maxi))
#
# 	def create_no(self):
# 		self.N = 10
# 		self.new_card = self.card_no + Create.rand_n(self)
# 		Create.luhn_algorithm(self)
#
# 		return self.new_card
#
# 	def create_pin(self):
# 		self.N = 4
# 		card_pin = Create.rand_n(self)
# 		return str(card_pin)
#
# 	def luhn_algorithm(self,cards=None):
# 		card = ''
# 		no = len(self.new_card[:-1]) + 1
# 		for i in range(1, no):
# 			j = int(self.new_card[(i - 1)])
# 			if i % 2 != 0:
# 				if (j * 2) > 9:
# 					card += str((j * 2) - 9)
# 				else:
# 					card += str(j * 2)
# 			else:
# 				card += str(j)
# 		card += self.new_card[-1]
# 		card = [int(x) for x in card]
# 		if sum(card) % 10 != 0:
# 			Create.create_no(self)
#
#
# def login():
# 	welcome = '''\n1. Balance
# 2. Add income
# 3. Do transfer
# 4. Close account
# 5. Log out
# 0. Exit'''
# 	while True:
# 		print(welcome)
# 		user_input = input()
# 		print()
# 		cur.execute('SELECT balance FROM card')
# 		balance = cur.fetchone()
# 		if user_input == '1':
# 			print(f'Balance: {balance}')
# 		elif user_input == '5':
# 			print('You have successfully logged out!')
# 			return None
# 		elif user_input == '0':
# 			print('\n Bye!')
# 			exit()
# 		elif user_input == '2':
# 			amount = int(input('Enter income: \n'))
# 			cur.execute('INSERT INTO card(balance) VALUES (?)', balance + amount)
# 			conn.commit()
# 			print('Income was added!')
# 		elif user_input == '3':
# 			cur.execute('SELECT number FROM card')
# 			card = cur.fetchone()
# 			print('Transfer\nEnter card number:\n')
# 			crd = input()
# 			if crd == card:
# 				print("You can't transfer money to the same account!")
# 			elif
#
# def print_menu():
# 	print('''1. Create an account
# 2. Log into account
# 0. Exit''')
#
#
# card = Create()
# cards = {}
# while True:
# 	print_menu()
# 	action = input()
# 	print()
# 	if action == '1':
# 		card_num, card_pin = card.create_no(), card.create_pin()
# 		cur.execute('INSERT INTO card(number,pin) VALUES (?,?)', (card_num, card_pin))
# 		conn.commit()
# 		print(f'Your card has been created')
# 		print(f'Your card number:\n{card_num}')
# 		print(f'Your card PIN:\n{card_pin}')
# 		print()
# 	elif action == '2':
# 		u_card = input('Enter your card number:\n')
# 		u_pin = input('Enter your PIN:\n')
# 		cur.execute('SELECT pin,number FROM card WHERE number ={0};'.format(u_card))
# 		pin = cur.fetchone()
# 		if pin and pin[0] == u_pin:
# 			print('\nYou have successfully logged in!')
# 			login()
# 		else:
# 			print('\nWrong card number or PIN!')
# 		print()
# 	elif action == '0':
# 		print('Bye!')
# 		exit()

import random
import sqlite3


def luhn_method(card_num: str) -> str:
    """ The function add checksum number to card_number (15 digits) """

    # Multiply odd digits by 2
    luhn_number = [int(card_num[i]) if ((i + 1) % 2 == 0) else int(card_num[i]) * 2 for i in range(len(card_num))]

    # Subtract 9 to number over 9
    for i in range(len(luhn_number)):
        if luhn_number[i] > 9:
            luhn_number[i] -= 9

    # Sum number
    luhn_sum = sum(luhn_number)
    if luhn_sum % 10 == 0:
        check_sum = 0
    else:
        check_sum = (luhn_sum - luhn_sum % 10 + 10) - luhn_sum

    # Add checksum to card number
    card_num += str(check_sum)

    return card_num


# Database holds information about client cards
conn = sqlite3.connect('card.s3db')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS card '
            '(id INTEGER PRIMARY KEY AUTOINCREMENT, '
            'number TEXT, '
            'pin TEXT, '
            'balance INTEGER DEFAULT 0);')

# Main cycle
while True:
    # Main menu
    option = input("1. Create an account\n"
                   "2. Log into account\n"
                   "0. Exit\n>")

    # Exit option
    if option == '0':
        exit()

    # Create account option
    elif option == '1':
        # Generating 15 digits of credit card number (without the last checksum digit)
        card_number = '400000'
        for _ in range(9):
            card_number += str(random.randint(0, 9))

        card_number = luhn_method(card_number)

        # Generating PIN
        pin = ''
        for _ in range(4):
            pin += str(random.randint(0, 9))

        # Save card + pin to database
        cur.execute('INSERT INTO card (number, pin, balance) VALUES (?, ?, ?)', (card_number, pin, 0))
        conn.commit()

        # Output information about created credit card
        print()
        print('Your card has been created')
        print(f'Your card number:\n{card_number}')
        print(f'Your card PIN:\n{pin}\n')

    # Login option
    elif option == '2':
        input_card = input("Enter your card number:\n>")
        input_pin = input("Enter your pin:\n>")

        # Search input card number and pin in DB
        cur.execute("SELECT pin FROM card WHERE number = '" + input_card + "';")
        card_info = cur.fetchone()

        if card_info and card_info[0] == input_pin:
            # Welcome message
            print("\nYou have successfully logged in!")
            print()

            # Cycle inside account
            while True:
                cur.execute("SELECT id, number, pin, balance FROM card WHERE number = '" + input_card + "';")
                card_info = cur.fetchone()

                # Unpack sqlite tuple
                db_id = card_info[0]
                db_number = card_info[1]
                db_pin = card_info[2]
                db_balance = int(card_info[3])

                # Main menu inside account
                logged_option = input("1. Balance\n"
                                      "2. Add income\n"
                                      "3. Do transfer\n"
                                      "4. Close account\n"
                                      "5. Log out\n"
                                      "0. Exit\n>")

                # Balance
                if logged_option == '1':
                    cur.execute(f"SELECT balance FROM card WHERE id = {db_id};")
                    db_balance = cur.fetchone()[0]
                    print(f"\nBalance: {db_balance}\n")
                    continue

                # Add income
                elif logged_option == '2':
                    print("\nEnter income:")
                    input_income = int(input('> '))

                    # Update balance in DB
                    cur.execute(f'UPDATE card SET balance = balance + {input_income} WHERE id = {db_id};')
                    conn.commit()
                    print('Income was added!\n')
                    continue

                # Do transfer
                elif logged_option == '3':
                    print("\nTransfer")
                    print("Enter card number:")

                    # target card number
                    in_card_tr = input('> ')

                    # check if the same card number has been entered
                    if in_card_tr == db_number:
                        print("You can't transfer money to the same account!")
                        continue

                    # apply Luhn algorithm on target card number
                    if luhn_method(in_card_tr[:-1]) != in_card_tr:
                        print("Probably you made mistake in the card number. Please try again!\n")
                        continue

                    # Search target card in DB
                    cur.execute(f"SELECT id, number FROM card WHERE number = '{in_card_tr}';")
                    target_card_info = cur.fetchone()

                    if not target_card_info:
                        print("Such a card does not exist.\n")
                        continue

                    # Unpack target card info
                    db_id_trg = target_card_info[0]
                    db_number_trg = target_card_info[1]

                    # Ask for amount of money to transfer
                    print("Enter how much money you want to transfer:")
                    transfer_amount = int(input('> '))

                    if transfer_amount > db_balance:
                        print("Not enough money!\n")
                        continue

                    print("Target number", db_number_trg, db_id_trg)
                    print("Current number", db_number, db_id)

                    # Transfer money
                    cur.execute(f"UPDATE card SET balance = balance + {transfer_amount} WHERE id = {db_id_trg};")
                    cur.execute(f"UPDATE card SET balance = balance - {transfer_amount} WHERE id = {db_id};")
                    conn.commit()

                    print("Success!\n")

                # Close account
                elif logged_option == '4':
                    cur.execute(f"DELETE FROM card WHERE id = {db_id};")
                    conn.commit()

                    print("\nThe account has been closed!\n")
                    break

                elif logged_option == '5':
                    print("\nYou have successfully logged out!\n")
                    break

                elif logged_option == '0':
                    print('Bye!')
                    conn.close()
                    exit()
        else:
            print("\nWrong card number or PIN!\n")
            continue