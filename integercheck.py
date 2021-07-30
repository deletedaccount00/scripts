# This code will verify if the Given number is positive integer or Negative Integer

def operator_verify(first_input):
  empty = ""
  if first_input == empty:
    print(" Input is empty ")
    quit()
  else:
    string_length = len(first_input)
    #print(" Length of your input is ",string_length)
    empty_arr = []
    for x in range(string_length):
      empty_arr.append(first_input[x])
    #print(empty_arr)
    if empty_arr[0] == '-':
      print(" " + first_input + " is a Negative Number ")
    else:
      print(" " + first_input + " is a Positive Number ")
      
input_one = input(" Enter the Number ")
operator_verify(input_one)  
