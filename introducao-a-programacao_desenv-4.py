def calculadora (num1, num2, oper) :
  
  oper = int(oper)
  num1 = float(num1)
  num2 = float(num2)
  
  if oper == 1 :
    return (num1 + num2)
  elif oper == 2 :
    return (num1 - num2)
  elif oper == 3 :
    return (num1 * num2)
  elif oper == 4 :
    return (num1 / num2)
  else :
    return 0
