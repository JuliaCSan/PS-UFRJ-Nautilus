class auv: 
    def __init__(self, nome, ano, num_thursters, num_sensores, cores, software):
        self.nome = nome
        self.ano = ano
        self.num_thursters = num_thursters
        self.num_sensores = num_sensores
        self.cores = cores
        self.software = software
        listas = list()
        Nomes = list()
        


lua1 = auv('Nome:  LUA', 'Ano Fabricação: 2016', 'No. Thursters: 8', 'No. Sensores: 5', 
'Cores: Azul e transparente', 'Software: ROS/Gazebo' )

print(lua1.nome, lua1.ano, lua1.num_thursters, lua1.num_sensores, lua1.cores, lua1.software)
print('=='*40)

brhue2 = auv('Nome: BrHUE 2020', 'Ano Fabricação: 2020', 'No. Thursters: 6', 'No. Sensores: 5', 
'Cores: Azul, Verde e transparente', 'Software: ROS')

print(brhue2.nome, brhue2.ano, brhue2.num_thursters, brhue2.num_sensores, brhue2.cores,brhue2.software)
print('=='*40)

lista1=[lua1.nome, lua1.ano, lua1.num_thursters, lua1.num_sensores, lua1.cores,
lua1.software]

lista2=[brhue2.nome, brhue2.ano, brhue2.num_thursters, brhue2.num_sensores,
brhue2.cores, brhue2.software]

print('AUVS: ')
novos = [lista1, lista2]
novos_sorted = sorted(novos, reverse=True)
import pprint; pprint.pprint(novos_sorted)
print('=='*40)

print('DATA DE FABRICAÇÃO: MAIS NOVO/MAIS VELHO\n')
Nomes = ([[lua1.nome], [lua1.ano]], [[brhue2.nome], [brhue2.ano]])
Nomes_sorted = sorted(Nomes, reverse=True)
import pprint; pprint.pprint(Nomes_sorted)
print('=='*40)

class robos:
    def __init__(self, idaderob, idadelua, idadebrhue):
        self.idadelua = idadelua
        self.idadebrhue = idadebrhue
        self.idaderob = idaderob

idaderob = robos('IDADE DO ROBO: ', 'LUA: 7 Anos', 'BrHUE2020: 3 Anos')
print(idaderob.idaderob, [idaderob.idadelua], [idaderob.idadebrhue])
