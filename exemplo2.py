from abc import ABC, abstractmethod

#Componente
class Notificador(ABC):
  @abstractmethod
  def enviar(self, mensagem):
    pass


#Componente Concreto
class NotificadorEmail(Notificador):
  def enviar(self, mensagem):
    return f"Enviando por Email: {mensagem}"

#Decorator
class DecoradorNotificador(Notificador):
  def __init__(self, notificador):
    self._notificador = notificador
    
  def enviar(self, mensagem):
    return self._notificador.enviar(mensagem)


#Decoradores Concretoss
class NotificadorSMS(DecoradorNotificador):
  def enviar(self, mensagem):
    return self._notificador.enviar(mensagem) + f"\nEnviando por SMS: {mensagem}"


class NotificadorWhatsApp(DecoradorNotificador):
  def enviar(self, mensagem):
    return self._notificador.enviar(mensagem) + \
    f"\nEnviando por WhatsApp: {mensagem}" #define a mensagem que sera enviada pela método enviar da class NotificadorWhatsApp


#utilização
notificador = NotificadorEmail() #cria o objeto base que notifica apenas o email
notificador = NotificadorSMS(notificador)# usa o objeto base como parametro e o coloca em um decorador para pegar a mensagem dentro do enviar e usa-la de outra forma
notificador = NotificadorWhatsApp(notificador)

print(notificador.enviar("Sistema em manutenção"))
