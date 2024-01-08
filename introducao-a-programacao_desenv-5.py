def moduloCalculo (num1, num2, oper) :

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
    if num2 == 0.0 :
      return("Impossível dividir por 0, favor verificar os dados e tentar novamente!")
    else :
      return (num1 / num2)

def calculadora () :
    print("Digite o operador, sendo:")
    print("1: Soma")
    print("2: Subtração")
    print("3: Multiplicação")
    print("4: Divisão")
    print("0: Sair")
    operEntrada = int(input())
    if operEntrada < 0 or operEntrada > 4 :
      print ("Essa opção não existe")
      calculadora ()
    elif operEntrada == 0 :
      return
    else :
      valorEntrada1 = input("Digite o primeiro valor da operação")
      valorEntrada2 = input("Digite o segundo valor da operação")
      print("Resultado:")
      print(moduloCalculo (valorEntrada1, valorEntrada2, operEntrada))
      calculadora ()

calculadora ()
