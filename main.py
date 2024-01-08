# function that makes sure input is valid
def valid_input(prompt:str):
  while True:
    try:
      res = int(input(prompt))
      if res > 0:
        return res
      print("Value must be a positive integer")
    except ValueError:
      print("Value must be a positive integer")

input_num = valid_input("Enter a positive integer: ")

# Using list comprehension loop
print( "\n".join( f"{input_num} x {i} = {i*input_num}" for i in range(1,11) ) )

#Separate results by 3 lines
print("\n" * 3)

# Using while Loop
counter = 0
while counter <= 10:
  print( f"{input_num} x {counter} = {counter*input_num}" )
  counter += 1