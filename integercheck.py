# This code will verify if the Given number is positive integer or Negative Integer


def main(first_input):
  empty = ""
  if first_input == empty:
    print(" Seems like argument is empty ")
    quit()
  else:
    string_capture = ""
    if True:
      string_capture += str(first_input)

    string_length = len(string_capture)
    #print(" Length of your input is ",string_capture)
    empty_arr = []
    for x in range(string_length):
      empty_arr.append(string_capture[x])
    #print(empty_arr)
    if empty_arr[0] == '-':
      print(" " + str(first_input) + " is a Negative Number ")
    else:
      print(" " + str(first_input) + " is a Positive Number ")
    


main(21) #or the number you wish to enter be it positive or negative.


