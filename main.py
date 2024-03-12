def calculate_imc(weight, height):
  imc = weight / (height**2)
  return imc


weight = float(input("Insira seu peso em kg: "))
height = float(input("Insira sua altura em metros: "))

result = calculate_imc(weight, height)
print("Seu IMC é:", result)
if result < 18.5:
  print("Abaixo do peso")
elif result < 25:
  print("Peso normal")
elif result < 30:
  print("Sobrepeso")
else:
  print("Obesidade")
