#Dominando string e fatiamentos

 #A classe String é famosa por ser rica em métodos e possuir uma interface muito fácil de trabalhar.
 #Em algumas linguagens manipular sequências de caracteres
 #não é um trabalho trivial, porém, em Python esse trabalho é muito simples.

 #Métodos úteis

 #Maiúscula, minúscula e título

 curso = "pYtHon"

 print(curso.upper()) #maiúsculo

 print(curso.lower()) #minusculo

 print(curso.title()) #a primeira maiúscula

 #Eliminando espaços em branco

 curso = "      Python"

  print(curso.strip()) #remove espaços da direita e esquerda

  print(curso.lstrip()) #remove espaços da esquerda
  
  print(curso.rstrip()) #remove espaços da direita

  #Junções e centralização

  curso = "Python"

  print(curso.center(10, "#")) #   "##Python##"
 
  print(".".join(curso)) # "P.y.t.h.o.n"

  #Old style %

  nome = "Évelim"
  idade = 27
  profissão = "Programadora"
  linguagem = "Python"
  
  print("Nome: %s Idade %d" % (nome, idade))
  print("Nome: {} Idade: {}".format(nome, idade))
  print("Nome: {1} Idade: {0}".format(nome, idade))
  print("Nome: {1} Idade: {0} Nome: {1} {1}".format(nome, idade))
  print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
  print("Nome: {name} Idade: {age}".format(name=nome, age=idade))


