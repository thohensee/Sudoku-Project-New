
# Homework 1 - Movie Ticket Software

#Display showtimes
print("Available movies today:\n"
      "A)12 Strong: 1)2:30 2)4:40 3)7:50 4)10:50\n"
      "B)Coco: 1)12:40 2)3:45\n"
      "C)The Post: 1)12:45 2)3:35 3)7:05 4)9:55")

#Take in user input and validate
movie = input("Movie choice: ")

time = int(input("Showtime: "))
if not(movie == "A" or movie == "B" or movie == "C"):
      print("Invalid option; please restart app...")
      exit()
match movie:
      case "A":
            if not(time == 1 or time == 2 or time == 3 or time == 4):
                  print("Invalid option; please restart app...")
                  exit()
      case "B":
            if not(time == 1 or time == 2):
                  print("Invalid option; please restart app...")
                  exit()
      case "C":
            if not(time == 1 or time == 2 or time == 3 or time == 4):
                  print("Invalid option; please restart app...")
                  exit()

adult = int(input("Adult tickets: "))
if adult > 30:
      print("Invalid option; please restart app...")
      exit()

kid = int(input("Kid tickets: "))
if adult + kid > 30:
      print("Invalid option; please restart app...")
      exit()

# Evaluate ticket prices
match movie:
      case "A":
            aCost = 12.45
            kCost = 9.68
      case "B":
            if time == 1:
                  aCost = 11.17
                  kCost = 8.0
            else:
                  aCost = 12.45
                  kCost = 9.68
      case "C":
            if time == 1:
                  aCost = 11.17
                  kCost = 8.0
            else:
                  aCost = 12.45
                  kCost = 9.68

# Calculate ticket costs
cost = adult*aCost + kid*kCost

#Output
print(f"Total cost: ${cost}")


