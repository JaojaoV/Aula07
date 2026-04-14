from abc import ABC, abstractmethod

#Componente
class Bebida(ABC):
  @abstractmethod
  def custo(self): #define custo como método abstrato, passando self como parametro.
    pass #o pass serve apenas para o método não ser vazio.

  @abstractmethod
  def descricao(self):
    pass


#Componene Concreto
class CafeSimples(Bebida):
  def custo(self):
    return 5.0 #na classe Café define o método abstrato, retornando 5.

  def descricao(self):
    return "Café Simples"


#Decorator 
class DecoradorBebida(Bebida):
  def __init__(self, bebida):
    self._bebida = bebida #guarda os valores da bebida escolhida anteriormente dentro de self._bebida


#Decoradores Concretos
class Leite(DecoradorBebida):
  def custo(self):
    return self._bebida.custo() + 2.0

  def descricao(self):
    return self._bebida.descricao() + ", Leite"


class Chocolate(DecoradorBebida):
  def custo(self):
    return self._bebida.custo() + 3.0

  def descricao(self):
    return self._bebida.descricao() + ", Chocolate"


#Utilização
bebida = CafeSimples()
bebida = Leite(bebida)
bebida = Chocolate(bebida)

print("Descrição:", bebida.descricao())
print("Custo: R$", bebida.custo())
