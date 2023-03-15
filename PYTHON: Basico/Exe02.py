
notas = list()
notas1 = list()
notas2 = list()
notas3 = list()
nomes = list()
situacao_ap = 'APROVADO'
situacao_rp = 'REPROVADO'

while True:
    print('=='*40)
    nome = str(input('Insira o nome do aluno: '))
    n1 = float(input('Insira a primeira nota: '))
    n2 = float(input('Insira a segunda nota: '))
    n3 = float(input('Insira a terceira nota: '))
    
    
    media = (n1 + n2 + n3)/3
    print('MÉDIA: ', media)

    nomes.append([{nome}])
    notas1.append([{n1}]), notas2.append([{n2}]),  notas3.append([{n3}])

   
    
    if media >=7:
        print('Situação: ', situacao_ap)
    else: print('Situação: ', situacao_rp)
  
    print('=='*40)
    
    proximo = str(input('Registrar próximo aluno? [S/N]'))
    if proximo in "Nn":
        print('==' * 40)
        
    n = str(input('Deseja ver as notas? [S/N]'))
    if n in 'Ss':
        print('=='* 40)
        print('NOMES: ', nomes)
        print('NOTAS 1: ', notas1)
        print('NOTAS 2: ', notas2)
        print('NOTAS 3 :', notas3)
        print('=='* 40)
    else: ('=='*40)
        
    finalizar = str(input('Deseja finalizar? [S/N]'))
    if finalizar in 'Ss':
        break
