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

print( "\n".join( f"{input_num} x {i} = {i*input_num}" for i in range(1,11) ) )