copies = int(input("enter number of receipt copies:"))
items = int(input("enter number of items in each receipy:"))

for copy in range(1,copies+1):
    print("\nReceipt copy:", copy)
    print("-----------------------")

    for items in range(1,items + 1):
        print("item number:", items)

    print("-----------------------")

print("\nALL receipts printed successfully!")
