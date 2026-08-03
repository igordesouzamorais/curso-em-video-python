c = float(input('Qual a temperatura em graus Celsius: '))
f = ((c * 9) / 5) + 32
k = c + 273.15

print('{:.2f}°C equivale a {:.2f}°F'.format(c, f))
print('{:.2f}°C equivale a {:.2f}°K'.format(c, k))
