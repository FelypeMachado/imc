imc_kg = float(input("Coloque seu peso em QUILOS: "))
imc_altura = float(input("Coloque sua altura em METROS: "))
imc = imc_kg / (imc_altura ** 2)
print(f"Seu IMC é de {imc:.2f}")

if imc < 18.5:
    status = "Abaixo do peso"
elif 18.5 <= imc < 24.9:
    status = "Peso normal"
elif 25 <= imc < 29.9:
    status = "Sobrepeso"
else:
    status = "Obesidade"

print(f"Seu IMC é de {imc:.2f}. Status: {status}")