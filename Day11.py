#program for mart
items = []
while True:
    display = input('Press enter to continue.')
    print('Welcome to the mart')
    print('1. Add items you wish to purchase\n2. Payment\n3. Exit mart')
    choice = input('Enter the number of your choice : ')

    if choice == '1':
        print('Add items')
        print('To add item fill the blocks manually')
        # while True:

        item = {}
        item['name'] = input('Item name : ')
        while True:
            try:
                item['quantity'] = int(input('Item quantity : '))
                break
            except ValueError:
                print('Quantity should only be in digits')
        while True:
            try:
                item['price'] = int(input('Price $ : '))
                break
            except ValueError:
                print('Price should only be in digits')
        print('Item has been successfully added.')
        items.append(item)

    elif choice == '2':
        print('payment')
        print(items)
        payment = input('please pay the amount at the chekout counter! ')


    elif choice == '3':
        print('happy shopping')
        print('please do visit again')
        break

    else:
        print('You entered an invalid option')
