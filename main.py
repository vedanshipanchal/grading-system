book1 = int(input("Enter page:"))
book2 = int(input("Enter page:"))
book3 = int(input("Enter page:"))
book4 = int(input("Enter page:"))
book5 = int(input("Enter page:"))
total = book1+book2+book3+book4+book5
avg = total/5
if avg>=90 and avg<=100:
   print("A professional reader")
elif avg>=81 and avg<=91:
   print("A good reader")
elif avg>=61 and avg<71:
   print("normal reader")
else:
   print("A begginer reader")