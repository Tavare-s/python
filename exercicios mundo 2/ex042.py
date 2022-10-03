print('=-'*40)
ab = float(input('lado A B: '))
cd = float(input('lado C D: '))
ef = float(input('lado E F: '))
if ab + cd <= ef or ef + ab <= cd or cd + ef <= ab:
    print('NAO É POSSIVEL FAZER UM TRIANGULO')
elif ab == cd == ef:
    print('esse é um triangulo EQUILÁTERO')
elif ab == cd or cd == ef or ab == ef:
    print('esse é um triangulo ISÓSCELES')
else:
    ab!= cd != ef
    print('esse é um triangulo escaleno')
print('=-'*40)