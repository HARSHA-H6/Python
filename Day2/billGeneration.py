APPLE_GST = 0.12
ORANGE_GST=0.05

buyer_name = input("Enter Buyer Name: ")
apple_price_kg = int(input("Enter Apple price per kg: "))
apple_quantity_kg = float(input("Enter Apple Quantity in Kg: "))
orange_price_kg = int(input("Enter orange price per kg: "))
orange_quantity_kg = float(input("Enter orange Quantity in Kg: "))

total_price_apple = apple_price_kg*apple_quantity_kg
total_price_orange = orange_price_kg*orange_quantity_kg

total_gst_apple = total_price_apple*APPLE_GST
total_gst_orange = total_price_orange*ORANGE_GST

total_billing_apple = total_price_apple+total_gst_apple
total_billing_orange = total_price_orange+total_gst_orange

total_amount  = total_billing_apple+total_billing_orange

total_round_amount = round(total_amount)

print(f"\nBuyer Name: {buyer_name}")
print(f"-"*75)
print(f"| {'Item Code ':^10} | {"Price/Unit ":^10} | {"#Unit ":^5}",
      f"{'Price ':^5} | {'GST ':^10} | {'Total w/ GST ':^10} |")
print(f"-"*75)
print(f"| {'Apple ':^1} | {'Rs '+str(apple_price_kg) :^10} | {apple_quantity_kg:^5}",
      f"| {'Rs '+str(total_price_apple): ^5}| {'Rs '+str(total_gst_apple):^10}",
      f"| {'Rs '+str(total_billing_apple):^10} |")

print(f"-"*75)
print(f"| {'Orange ':^10} | {'Rs '+str(orange_price_kg) :^10} | {orange_quantity_kg:^5}",
      f"| {'Rs '+str(total_price_orange): ^5}| {'Rs '+str(total_gst_orange):^10}",
      f"| {'Rs '+str(total_billing_orange):^10} |")

print(f"{'-'*75}")

print(f"Total {' '*54} \u20B9 {total_amount:.2f}")
print(f"Total Round {' '*48} \u20B9 {total_round_amount: .2f}")
print(f"{'-'*74}")