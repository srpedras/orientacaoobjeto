class Cachorro (object):
    def __init__(self,nome):
        self.nome = nome
        print (f'parabens sou {self.nome} seu novo cahorro')
    
        
    def som (self):
        print(f'{self.nome} late')
      
        
caramelo = Cachorro('safadão')
caramelo.som()
caradechinelo = Cachorro('Cara de Chinelo')
caradechinelo.som()

class Gato (object):
    def __init__(self,nome,anoNasc):
        self.nome = nome
        self.anoNasc= anoNasc
        print(f'\nparabens sou seu novo gato {self.nome}')
        
    def som (self):
        print(f'{self.nome} mia')
        
    def getIdade(self):
        return 2022 - self.anoNasc
        
rapido = Gato("Prisma",2000)
idaderapido =rapido.getIdade()
print ('idade gato:',rapido.getIdade())
rapido.som()        


class Jacare(object):
    def __init__(self,nome, anoNasc):
        self.nome = nome
        self.anoNasc = anoNasc
       
        print(f'\nparabens sou seu novo animal de estimação {self.nome}, o jacare')
        
    def som(self):
     print(f'{self.nome} croa')
     
    def getIdade(self):
        return 2024 - self.anoNasc
    
    def setAnoNac(self,ano):
        self.anoNasc = ano
        
   

 
        
     
jacare = Jacare('Pia',1900)
idadejacare = jacare.getIdade()
print('ano do jacaré',jacare.getIdade())
jacare.setAnoNac = 19000
print('idade',jacare.getIdade())
jacare.som()