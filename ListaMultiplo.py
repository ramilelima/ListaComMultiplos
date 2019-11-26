for i in range(150):
    if i % 7 == 0:
        print('Múltiplo de 7')
    elif i % 11 == 0:
        print('Múltiplo de 11')
    elif i % 7 == 0 and i % 11 == 0:
        print('Múltiplo de 7 e 11')
    else:
        print(i)
        
