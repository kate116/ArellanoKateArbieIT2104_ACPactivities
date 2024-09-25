def calculate_discount():
    PurchaseAmount = float(input("Enter the total purchase amount: "))
    print(f"Initial Purchase Amount: {PurchaseAmount: .2f}")


    if PurchaseAmount > 5000:
        discount_rate = 0.10
    else:
        discount_rate = 0.05

    discount_amount = PurchaseAmount*discount_rate
    final_price = PurchaseAmount - discount_amount
    print(f"Discount: {discount_amount: .2f}")
    print(f"Final Price: {final_price: .2f}")

    TryAgain = (input("Do you want to try again? (yes/no): "))
    if TryAgain == 'yes':
       calculate_discount()
    else:
        print("Thank you!")

calculate_discount()




        

