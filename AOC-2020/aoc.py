from days import *
code_to_execute = input("choose a day to solve: ")
input_file = "input/"+code_to_execute+".txt"
#execute function from chosen file
mapping = {1:one, 2:two,3:three,4:four,5:five,6:six,7:seven,8:eight,9:nine,10:ten}
mapping[int(code_to_execute)].main(input_file)
