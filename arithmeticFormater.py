def arithmetic_arranger(problems, see = True):
  first_operand = list()
  operator = list()
  second_operand = list()
  max_length = list()
  dashes = list()
  operation = list()
  upper_part = ""
  lower_part = ""
  dashesline = ""
  results = ""
  index = 0
  # Get the length of the list, if it is higher than 5, print an error
  if len(problems) > 5:
    print(" Error: Too many problems")

  # Divide the list into sub lists
  for increment in problems:
    new_item = increment.split()

    # Assign first, second operand and operator
    first_operand.append(new_item[0])
    operator.append(new_item[1])
    second_operand.append(new_item[2])

  # Checking if the operands are only digits (must be separated into
  # two different for loops if we do not want to see the error written 4 times)
  for go_over in first_operand:
    if not go_over.isnumeric():
      print("Error: Numbers must only contain digits")
  for go_over in second_operand:
    if not go_over.isnumeric():
      print("Error: Numbers must only contain digits")

  # Checking if numbers are not above 4 digits (must be separated into
  # two different for loops if we do not want to see the error written 4 times)
  for go_over in first_operand:
    if len(go_over) > 4:
      print("Error: Numbers cannot be more than four digits")
  for go_over in second_operand:
    if len(go_over) > 4:
      print("Error: Numbers cannot be more than four digits")

  # Checking if the operator is a '+' or a '-'
  for go_over in operator:
    index += 1
    if go_over == "*" or go_over == "/":
      print("Error: Operator must be '+' or '-'")
    # Doing the calculation for '+' and '-'
    elif go_over == "+":
      operation.append(
          str(int(first_operand[index - 1]) + int(second_operand[index - 1])))
    elif go_over == "-":
      operation.append(
          str(int(first_operand[index - 1]) - int(second_operand[index - 1])))

  for go_over in range(len(first_operand)):
    max_length.append(
        max(len(first_operand[go_over]), len(second_operand[go_over])))
    dashes.append("-" * (2 + max_length[go_over]))

  for go_over in range(len(first_operand)):
    if see == True:
      if go_over == 0:
        upper_part += first_operand[go_over].rjust(2 + max_length[go_over])
        lower_part += operator[go_over].ljust(
            0) + " " + second_operand[go_over]
        dashesline += dashes[go_over]
        results += operation[go_over].rjust(2 + max_length[go_over])
      else:
        upper_part += "    " + first_operand[go_over].rjust(
            2 + max_length[go_over])
        lower_part += "    " + operator[go_over].ljust(
            0) + " " + second_operand[go_over].rjust(max_length[go_over])
        dashesline += "    " + dashes[go_over]
        results += "    " + operation[go_over].rjust(2 + max_length[go_over])

      arranged_problems = upper_part + "\n" + lower_part + "\n" + dashesline + "\n" + results

    else:
      if go_over == 0:
        upper_part += first_operand[go_over].rjust(2 + max_length[go_over])
        lower_part += operator[go_over].ljust(
            0) + " " + second_operand[go_over]
      else:
        upper_part += "    " + first_operand[go_over].rjust(
            2 + max_length[go_over])
        lower_part += "    " + operator[go_over].ljust(
            0) + " " + second_operand[go_over].rjust(max_length[go_over])

      arranged_problems = upper_part + "\n" + lower_part
    return arranged_problems
