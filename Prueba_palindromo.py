from array import array
import random
import sys
from termcolor import colored
#Lista enlazada
class Error(Exception):
  def __init__(self,message):
    self.message = message

class Node:
  def __init__(self, value, next = None, color = "sin color", index = None):
    self.value = value
    self.next = next
    self.color = color
  def set_color(self, color):
    self.color = color
  def get_color(self):
    return self.color
  def set_value(self, value):
    self.value = value
  def get_value(self):
    return self.value
  def set_next(self, next):
    self.next = next
  def get_next(self):
    return self.next
  def set_index(self,index):
    self.index = index
  def get_index(self):
    return self.index


class Linked_List:
  def __init__(self):
    self.size = 0
    self.head = None
    self.tail = None

  def get_size(self):
    return self.size

  def append_head(self, e):
    if self.size == 0:
      self.head = Node(e)
      self.size += 1
    elif self.size == 1:
      self.size += 1
      newest = Node(e)
      newest.set_next(self.head)
      self.tail = newest.get_next()
      self.head = newest
    else:
      self.size += 1
      newest = Node(e)
      newest.set_next(self.head)
      self.head = newest

  def append_tail(self, e):
    n = Node(e)
    if self.size == 0:
      self.head = n
      n.set_index(self.size)
      self.size += 1
    elif self.size == 1:
      self.tail = n
      self.head.set_next(self.tail)
      n.set_index(self.size)
      self.size += 1
    else:
      newest = n
      self.tail.set_next(newest)
      self.tail = self.tail.get_next()
      n.set_index(self.size)
      self.size += 1
          
def insercion_en_Linked_list(palabra : str,lista_enlazada : Linked_List):
  for i in range(len(palabra)): #inserto cada caracter en mi variable linked list
    lista_enlazada.append_tail(palabra[i])

def insercion_de_palabra_en_diccionario(palabra : Linked_List,indice_de_palabra : Linked_List,diccionario : dict):
  for i in range(palabra.get_size()):
    if indice_de_palabra.get_value() in diccionario.keys():
      diccionario[indice_de_palabra.get_value()] = diccionario[indice_de_palabra.get_value()] + 1
    else:
      diccionario[indice_de_palabra.get_value()] = 1
    indice_de_palabra = indice_de_palabra.get_next()

def insercion_de_palabra_usuario_en_diccionario(palabra : Linked_List,indice_de_palabra : Linked_List,diccionario : dict):
  for i in range(palabra.get_size()):
    diccionario[indice_de_palabra.get_value()] = 0
    indice_de_palabra = indice_de_palabra.get_next()

def verificacion_de_letras_repetidas(con : int,palabra_usuario_head,palabra_usuario_head2,lista_enlazada_palabra_usuario):
  while palabra_usuario_head is not None:
    if palabra_usuario_head2.get_next() != None:
      if palabra_usuario_head.get_value() == palabra_usuario_head2.get_value() and palabra_usuario_head2.get_value() not in diccionario_palabra_elegida.keys():
        palabra_usuario_head2.set_color("sin color")
      elif palabra_usuario_head.get_value() == palabra_usuario_head2.get_value() and con < diccionario_palabra_elegida[palabra_usuario_head.get_value()]:
        con += 1
      elif palabra_usuario_head.get_value() == palabra_usuario_head2.get_value() and con >= diccionario_palabra_elegida[palabra_usuario_head.get_value()]:
        con += 1
        palabra_usuario_head2.set_color("sin color.")
      if palabra_usuario_head2.get_next() != None:
        palabra_usuario_head2 = palabra_usuario_head2.get_next()
      else:
        continue
    else:
      if palabra_usuario_head.get_value() == palabra_usuario_head2.get_value() and palabra_usuario_head2.get_value() not in diccionario_palabra_elegida.keys():
        palabra_usuario_head2.set_color("sin color")
      elif palabra_usuario_head.get_value() == palabra_usuario_head2.get_value() and con < diccionario_palabra_elegida[palabra_usuario_head.get_value()]:
        con += 1
      elif palabra_usuario_head.get_value() == palabra_usuario_head2.get_value() and con >= diccionario_palabra_elegida[palabra_usuario_head.get_value()]:
        con += 1
        palabra_usuario_head2.set_color("sin color.")
      palabra_usuario_head = palabra_usuario_head.get_next()
      palabra_usuario_head2 = lista_enlazada_palabra_usuario.head
      con = 0

def letras_iguales(head_palabra_usuario : Node, head_palabra_usuario2 : Node, palabra_usuario : Linked_List):
  contador_letras_repetidas = 0
  todas_iguales = False
  for i in range(palabra_usuario.get_size()):
    if head_palabra_usuario.get_value() == head_palabra_usuario2.get_value():
      contador_letras_repetidas += 1
    head_palabra_usuario2 = head_palabra_usuario2.get_next()
  if contador_letras_repetidas == 5:
    todas_iguales = True
  return todas_iguales

def verificacion_letras_iguales(head_palabra_usuario : Node, head_palabra_elegida : Node, palabra_verificada : array):
  while head_palabra_usuario != None:
    if head_palabra_usuario.get_value() == head_palabra_elegida.get_value() and head_palabra_usuario.index == head_palabra_elegida.index:
      head_palabra_usuario.set_color("verde")
      lista_temporal = []
      lista_temporal.append(head_palabra_usuario.get_value())
      lista_temporal.append(head_palabra_usuario.get_color())
      palabra_verificada.append(lista_temporal)
      head_palabra_usuario = head_palabra_usuario.get_next()
      head_palabra_elegida = palabra_destino.head
    else:
      if head_palabra_elegida.get_next() == None:
        head_palabra_elegida = palabra_destino.head
        lista_temporal = []
        lista_temporal.append(head_palabra_usuario.get_value())
        lista_temporal.append(head_palabra_usuario.get_color())
        palabra_verificada.append(lista_temporal)
        head_palabra_usuario = head_palabra_usuario.get_next()
      else:
        head_palabra_elegida = head_palabra_elegida.get_next()
  return palabra_verificada, 0



def verificacion_de_palabra_usuario(head_palabra_usuario: Node,head_palabra_elegida: Node,contador_checks: int,palabra_verificada: array, diccionario_palabra_elegida : dict, diccionario_palabra_usuario : dict):
  while head_palabra_usuario != None:
    if head_palabra_usuario.get_value() == head_palabra_elegida.get_value() and head_palabra_usuario.index == head_palabra_elegida.index:
      if head_palabra_usuario.get_color() == "sin color.":
        lista_temporal = []
        lista_temporal.append(head_palabra_usuario.get_value())
        lista_temporal.append(head_palabra_usuario.get_color())
        palabra_verificada.append(lista_temporal)
        if head_palabra_usuario.get_value() in diccionario_palabra_usuario.keys():
          diccionario_palabra_usuario[head_palabra_usuario.get_value()] = diccionario_palabra_usuario[head_palabra_usuario.get_value()] + 1
        head_palabra_usuario = head_palabra_usuario.get_next()
        head_palabra_elegida = palabra_destino.head
      else:
        head_palabra_usuario.set_color("verde")
        lista_temporal = []
        lista_temporal.append(head_palabra_usuario.get_value())
        lista_temporal.append(head_palabra_usuario.get_color())
        palabra_verificada.append(lista_temporal)
        if head_palabra_usuario.get_value() in diccionario_palabra_usuario.keys():
          diccionario_palabra_usuario[head_palabra_usuario.get_value()] = diccionario_palabra_usuario[head_palabra_usuario.get_value()] + 1
        contador_checks += 1
        head_palabra_usuario = head_palabra_usuario.get_next()
        head_palabra_elegida = palabra_destino.head
    elif head_palabra_usuario.get_value() == head_palabra_elegida.get_value() and head_palabra_usuario.index != head_palabra_elegida.index:
      if head_palabra_usuario.get_color() == "sin color.":
        lista_temporal = []
        lista_temporal.append(head_palabra_usuario.get_value())
        lista_temporal.append(head_palabra_usuario.get_color())
        palabra_verificada.append(lista_temporal)
        if head_palabra_usuario.get_value() in diccionario_palabra_usuario.keys():
          diccionario_palabra_usuario[head_palabra_usuario.get_value()] = diccionario_palabra_usuario[head_palabra_usuario.get_value()] + 1
        head_palabra_usuario = head_palabra_usuario.get_next()
        head_palabra_elegida = palabra_destino.head
      else:
        if diccionario_palabra_usuario[head_palabra_usuario.get_value()] < diccionario_palabra_elegida[head_palabra_usuario.get_value()]: 
          diccionario_palabra_usuario[head_palabra_usuario.get_value()] = diccionario_palabra_usuario[head_palabra_usuario.get_value()] + 1
          head_palabra_usuario.set_color("amarillo")
          if head_palabra_elegida.get_next() == None:
            continue
          else:
            head_palabra_elegida = head_palabra_elegida.get_next()
        else:
          head_palabra_usuario.set_color("amarillo")
          lista_temporal = []
          lista_temporal.append(head_palabra_usuario.get_value())
          lista_temporal.append(head_palabra_usuario.get_color())
          palabra_verificada.append(lista_temporal)
          if head_palabra_usuario.get_value() in diccionario_palabra_usuario.keys():
            diccionario_palabra_usuario[head_palabra_usuario.get_value()] = diccionario_palabra_usuario[head_palabra_usuario.get_value()] + 1
          head_palabra_usuario = head_palabra_usuario.get_next()
          head_palabra_elegida = palabra_destino.head
    else:
      if head_palabra_elegida.get_next() == None:
        head_palabra_elegida = palabra_destino.head
        lista_temporal = []
        lista_temporal.append(head_palabra_usuario.get_value())
        lista_temporal.append(head_palabra_usuario.get_color())
        palabra_verificada.append(lista_temporal)
        if head_palabra_usuario.get_value() in diccionario_palabra_usuario.keys():
          diccionario_palabra_usuario[head_palabra_usuario.get_value()] = diccionario_palabra_usuario[head_palabra_usuario.get_value()] + 1
        head_palabra_usuario = head_palabra_usuario.get_next()
      else:
        head_palabra_elegida = head_palabra_elegida.get_next() 
  return palabra_verificada,contador_checks

def colorear(palabra_verificada : array):
  h = 0
  while h < 5:
    if palabra_verificada[h][1] == "verde":
      text = colored(palabra_verificada[h][0], 'green')
      print(text,end="")
    elif palabra_verificada[h][1] == "amarillo":
      text = colored(palabra_verificada[h][0], 'yellow')
      print(text,end="")
    else:
      print(palabra_verificada[h][0],end="")
    h += 1

print("Bienvenid@ Jugador")
q = str(input("Deseas comenzar una nueva partida? y/n: "))
palabras = ["busto", "gorra", "chulo", "costa", "ostra","poste","carro","avion","peste"]
if q == "n" or q == "N":
  print("Si abueno")
elif q == "y" or q == "Y":
  palabra_elegida = random.choice(palabras) #defino mi palabra aleatoria
  palabra_destino = Linked_List()
  insercion_en_Linked_list(palabra_elegida,palabra_destino)
  print("¡COMIENZA LA RONDA DE INTENTOS! RECUERDA: SOLO TIENES 6 INTENTOS PARA ADIVINAR LA PALABRA")
  intentos_usuario = 6
  n = palabra_destino.head
  diccionario_palabra_elegida = {}
  insercion_de_palabra_en_diccionario(palabra_destino,n,diccionario_palabra_elegida)
  while intentos_usuario != 0:
    print("te quedan ",intentos_usuario," intentos, buena suerte")
    palabra_intento = str(input("Ingrese una palabra: "))
    palabra_usuario = Linked_List()
    if len(palabra_intento) != 5:
      print("tu palabra debe contener 5 caracteres")
      continue
    else:
      insercion_en_Linked_list(palabra_intento,palabra_usuario)
      o = palabra_usuario.head
      diccionario_palabra_usuario = {} 
      insercion_de_palabra_usuario_en_diccionario(palabra_usuario,o,diccionario_palabra_usuario)
      a = palabra_usuario.head
      c = palabra_usuario.head
      b = palabra_destino.head
      contador_checks = 0
      palabra_verificada = []
      con = 0
      conf = letras_iguales(a,c,palabra_usuario)
      if conf == True:
        x,y = verificacion_letras_iguales(a,b,palabra_verificada)
      else:
        verificacion_de_letras_repetidas(con,a,c,palabra_usuario)
        x,y = verificacion_de_palabra_usuario(a,b,contador_checks,palabra_verificada,diccionario_palabra_elegida,diccionario_palabra_usuario)
      if y == 5:
        break
      else:
        colorear(palabra_verificada)
        print(" ")
        intentos_usuario -= 1
        if intentos_usuario == 0:
          continue
        else:
          palabra_verificada = []
    if y == 5:
        break
  if y == 5:
        t = 0
        while t < 5:
          text = colored(palabra_verificada[t][0], 'green')
          print(text,end="")
          t += 1
        print(" ")
        print("FELICIDADES, GANASTE LA PARTIDA")
  else:
    z = 0
    while z < 5:
      text = colored(palabra_verificada[z][0], 'red')
      print(text,end="")
      z += 1
    print(" ")
    print("HAZ PERDIDO")
else:
  print("por favor ingrese un valor valido no sea imbecil")