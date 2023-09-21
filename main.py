import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker
cashier_instance = Cashier




def main():
    loop = 1
    sm = sandwich_maker_instance(resources)
    cash = cashier_instance()
    while loop != 0:
        choice = input('What would you like?\n 1. Small, 2. Medium, 3. Large, 4. Off, 5. Report\n')
        if choice == '1':
            if sm.check_resources('small') == True:
                print('Total: ' + str(recipes['small']['cost']))
                cash.process_coins()
                if cash.transaction_result(recipes['small']['cost']) == True:
                    sm.make_sandwich('small', recipes['small']['ingredients'])
                    print('Small sandwich coming up!')
                else:
                    print("Insufficient Funds.")
            else:
                print('Insufficient resources.')
        elif choice == '2':
            if sm.check_resources('medium') == True:
                print('Total: ' + str(recipes['medium']['cost']))
                cash.process_coins()
                if cash.transaction_result(recipes['medium']['cost']) == True:
                    sm.make_sandwich('medium', recipes['medium']['ingredients'])
                    print('Medium sandwich coming up!!')
                else:
                    print("Insufficient Funds.")
            else:
                print('Insufficient resources.')
        elif choice == '3':
            if sm.check_resources('large') == True:
                print('Total: ' + str(recipes['large']['cost']))
                cash.process_coins()
                if cash.transaction_result(recipes['large']['cost']) == True:
                    sm.make_sandwich('large', recipes['large']['ingredients'])
                    print('Large sandwich coming up!!')
                else:
                    print("Insufficient Funds.")
            else:
                print('Insufficient resources.')
        elif choice == '4':
            print('Powering off machine...')
            loop = 0
        elif choice == '5':
            print("Bread:", sm.machine_resources['bread'], " Slice(s).")
            print("Ham:", sm.machine_resources['cheese'], " Slice(s).")
            print("Cheese:", sm.machine_resources['ham'], " Pound(s).")

if __name__=="__main__":
    main()