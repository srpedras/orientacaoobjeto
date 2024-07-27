class Pets (object):
    def __init__(self,nome,idade, especie):
        self.nome = nome
        self.idade = idade
        self.especie = especie
       
        #print (f'parabens sou {self.nome} seu novo cahorro')   
        
        
         
    def setIdade(self,idade):
        self.idade = idade
        
    def getIdade(self):
        return self.idade
    
    
    
    def som(self,especie):
        self.especie = especie
    
    
    #def som(self):
        #print('Woof woof')
        
        
     
        
class Cachorro(Pets):
    def __init__(self,nome,idade,especie):
        super().__init__(nome,idade,especie)#('Cachorro', 10)
        
    """def som(self):
        return  'au au ' """
       
        
        
acerola = Cachorro(f'\nacerola',10,"Woof woof")
print(acerola.nome)   
print(acerola.idade)
print(acerola.especie) 
   

#classe filho (gato) usando a classe pai(pets)
class Gato(Pets):
    def __init__(self,nome,idade,especie):
        super().__init__(nome,idade,especie)
       
        
miguelito = Gato(f'\nmiguelito', 30,'miau miau')
print(miguelito.nome)
print(miguelito.idade)
print(miguelito.especie)


class Peixe(Pets):
    def __init__(self,nome,idade,especie):
        super().__init__(nome,idade,especie)
    '''def sum(self):
        return  'au au' '''
       
Dori = Peixe(f'\nDori',6,'Peixe')
print('Nome: ',Dori.nome)
print('Idadde: ',Dori.idade)
print('Especie: ',Dori.especie)
#ANTONIO CARLOS SANTOS PEDRA
        