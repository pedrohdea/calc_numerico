from pprint import pprint
from numpy import pi

## Programa par acalcular a área e o comprimento de uma circunferência

def circulo():
    raio = int(input('Digite o valor de um raio: '))

    comprimento = 2*pi*raio
    area = pi*(raio**2)

    print('área: ',area)
    print('comprimento: ', comprimento)

def bhaskara():
    print('ax² + bx + c = 0\n')
    a = int(input('Digite o valor de a: '))
    b = int(input('Digite o valor de b: '))
    c = int(input('Digite o valor de c: '))
    delta = (b*b) - (4*a*c)
    delta = delta**0.5
    x_pos = (-b + delta) / (2*a)
    x_neg = (-b - delta) / (2*a)

    print('x1:' ,x_pos)
    print('x2:' ,x_neg)

def sistema():
    print('\n   ax + b = k1')
    print('\n   cx + d = k2')
    
    a = int(input('\nDigite o valor de a: '))
    b = int(input('Digite o valor de b: '))
    k1 = int(input('Digite o valor de k1: '))
    
    c = int(input('Digite o valor de c: '))
    d = int(input('Digite o valor de d: '))
    k2 = int(input('Digite o valor de k2: '))

    det_a = ((a*d) - (b*c))
    if det_a == 0:
        print('Não é possivel resolver o sistema')
        return
    
    y = ((a*k2) - (c*k1))/det_a
    x = (k1 - (b*y))/a

    print('\nx: ',x)
    print('y: ',y)

EXERCICIOS = {
    '01': circulo,
    '02': bhaskara,
    '03': sistema,
}

def main():
    pprint('Escolha o exercício: ')

if __name__ == '__main__':
    pprint(EXERCICIOS)
    chose = input('Escolha o exercicio: ')
    exercicio = EXERCICIOS[chose]
    exercicio()
