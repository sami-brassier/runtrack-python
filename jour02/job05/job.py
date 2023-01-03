def calcule(num1,operator,num2):
  return eval('{}{}{}'.format(num1, operator, num2))

print(calcule(1,'+',4))