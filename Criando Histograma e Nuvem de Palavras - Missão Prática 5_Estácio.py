#Programa Principal

#Gerando Dados de Teste
from faker import Faker

nomes = Faker('pt_BR')
notas = Faker()

lista_mestra = []
for i in range(10):
    lista = [nomes.name(), notas.random_int(0,10)]
    lista_mestra.append(lista)

#Gravando Dados
my_file = open('lista.txt', 'w+')
for item in lista_mestra:
    my_file.write(str(item) + '\n')
my_file.close()

#Recuperando Dados
lista_recuperada = []
my_file = open('lista.txt')
for line in my_file:
    lista_recuperada.append(line)

#Separando Dados
notas = []
for item in lista_recuperada:
    nome, nota = eval(item)
    notas.append(nota)
    
#Criando Histograma
import matplotlib.pyplot as plt

num_bins = 10
plt.hist(notas, num_bins, density=True, facecolor = 'green', 
         alpha = 0.75)

plt.xlabel('Pontuações')
plt.ylabel('Probabilidade')
plt.title('Histograma de Pontuações')
plt.grid(True)
plt.show()

#Convertendo Números
from num2words import num2words
lista_convertida = []
for item in notas:
    lista_convertida.append(num2words(item, lang='pt-br'))

#Criando Nuvem de Palavras
from wordcloud import WordCloud

texto = ','.join(lista_convertida)

nuvem_palavras = WordCloud(background_color='grey',
                           width=800,height=400).generate(texto)
plt.imshow(nuvem_palavras, interpolation='bilinear')
plt.axis("off")
nuvem_palavras.to_file("Nuvem de palavras.png")
plt.show()