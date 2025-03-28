

numero: int = 0

for num in range(numero, 11):
    if num % 2 == 0:
        continue
    print(num)

while True:
    numero += 1
    if numero % 2 == 0:
        continue
    if numero > 20:
        break
    print(numero   )