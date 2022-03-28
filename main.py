from Tkfull import Janela

class Calculadora:
 titulo = [['Calculadora']]
 visor  = [[input]]
 botoes = [
           ['*CE','*%','*M+','*M-','*/'],
           ['*7','*8','*9','*+','*.'],
           ['*4','*5','*6','*-','*,'],
           ['*1','*2','*3','**','*=']]

 estilo = {'width':3}
 
 def __init__(self):
        self.classe = Janela()
       

        self.classe.gerar(self.titulo)
        self.classe.gerar(self.visor)
        self.classe.gerar(self.botoes)

        for i in range(3,len(self.classe.getObjetos())):
         self.classe.setEstilo(i,self.estilo)
  
         
         def funcao(self,x):
          texto = self.classe.getTexto(i)
          self.classe.setEvento(i,lambda x= texto:self.funcao(x))

          if (x in ".123456789"):
            self.classe.setTexto(2,x)
            
          elif (x in "/-x"):
            global num1
            global op
            num1 = float (self.classe.getTexto(2))
            op = x
            self.classe.apagarTexto(2,1)
          elif (x == "="):
               num2 = self.classe.getTexto(2)
          if op == "+":
                soma = num1+num2
                self.classe.mensagem(f'Soma é {soma:}')
           
     
Calculadora()
