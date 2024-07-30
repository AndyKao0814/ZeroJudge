print("a leap year" if (lambda y: y % 4 == 0 and (y % 100 != 0 or y % 400 == 0))(int(input())) else "a normal year")
