total_seconds = int(input("Enter the total seconds: "))
hours = total_seconds//3600
minutes = (total_seconds%3600)//60
seconds = total_seconds%60

print(f"Time duration of {total_seconds} seconds in the HH:MM:SS format is",
      f"{hours:02d}:{minutes:02d}:{seconds:2d}")