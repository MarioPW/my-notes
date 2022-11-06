
# Show the letters of a string three at a time:
"""
letters=["a","b","c","d","e","f","g","h","i"]
por3=[letters.pop(i) for i in range(len(letters))if i%3==0]
print(por3)
"""
# Reverse a string
"""
my_string = "patogeno"
rev_string = my_string[::-1]
print (f"\n{rev_string.upper()}\n")"""

# Find the index where the character first appears with .find():
"""
word = "palabra"
print(word.find("l"))"""

"""
my_string = "asdasdfasdsdfgsdfgsdfg"
rep = my_string.find("fgs")
print(rep)"""

# Count how many times a character is repeated:
"""
my_string = "asdasdfasdsdfgsdfgsdfg"
def rep_times(string,caracter):  
    counter = 0
    for i in string:
        if caracter == i:
            counter += 1
    print(f"The letter {caracter} is repeated {counter} times.")

rep_times(my_string,"d")"""

# Validate if an input is a letter:
"""
letter = input("Fill in a letter: ")

if letter.isalpha():
    print("OK")
else: 
    print("NOP")"""

# Remove not alpha caracters in a string
"""
text = "&%3456Hola, me llamo Juan4334#$$${sings3"
clean_text = filter(lambda x: x.isalpha() or x == " ", text)
clean_text1 = "".join(clean_text)
print(clean_text1)"""



# Create triangles of stars:

# Right Triangle:
"""
def triangle(size):
    for i in range(0,size,1):
        for j in range (0,i+1,1):
            print ("*",end="")
        print ("")

size = int (input ("Fill in the size: "))
triangle(size)"""

# Side Triangle:
"""
size = (int(input("Size: ")))
for i in range(size):
    if i <= size/2:
        star = "*"
        print(star * i)
    elif i>size/210:
        star = "*" * (size-i)
        print(star)"""

# Isosel Triangle:
"""
size=int(input("Size: "))

for i in range(size):
    print(" "*(size-i-1) +"*"*(2*i+1))"""

# Fibonacci series:
"""
a = 1
b = 0
for i in range(20):
    c = a+b
    a=b
    b=c
    print(c,end=",")"""


# Even Numbers
"""
even = [i for i in range(22) if i%2==0]
print (even)"""

# Show the prime numbers within the range of 2 and a given number:
"""
given_num = int(input("Fill in a number: "))
primes = []
for i in range (given_num+1):
    dividers = []
    for j in range(1,i+1):
        if i % j == 0:
            dividers.append(j)
    if len(dividers) == 2:
        primes.append(i)

print("Pimes:", primes)"""
            
# Multiplication tables:
"""
for i in range(1,10):
    print (f"\nTable of {i}")
    for j in range(1,10):        
        print(f"{i} x {j} = {i*j}")
    """
# concatenation with f"" in variables
"""add = "adition"
can = f"word {add}"

print(can)"""

# Capitalize vowels in a string:
"""
string = "parangaricutirimicuaro"
comparador = "aeiou"
for i in string:
    if i in comparador: 
        print(i.upper(),end="")
    else:
        print(i,end="")"""

# Squares with for and while loops

# With for:
"""for i in range(60):
    print(f"Number: {i}  Square: {i**2}")"""

# With while:
"""
limit = 0
while limit <= 60:
    print (limit**2)
    limit+=1"""

# Pedir al usuario dos numeros y mostrar las operaciones de la calculadora por pantalla

"""num1 = int(input("Ingresa un número: "))
num2 = int(input("Ingresa otro número: "))

print (f"Suma: {num1+num2} \nResta: {num1-num2}... etc" )

        # Mostrar todos los numeros entre los que ingrese el usuario

for i in range(num1,num2):
    if num1<num2:
        print (i)
    else:
        print("El primero debe ser menor que el segundo")

        # Mostrar solo los impares

impares=[i for i in range(num1,num2) if i%2!=0]
print(f"Impares: {impares}")"""

# Tablas de multiplicar con funciones
"""
def tabla (numero):
    print(f"Tabla del {numero}")
    
    for i in range(1,10):
        print(f"{numero} x {i} = {numero*i}")
    print("\n")
for i in range(1,10):
    tabla(i)"""
"""
cad = "progresivamente"
print (cad[:-5])"""

# Create list of 8 random numbers
"""
from random import randint

lista = [randint(1,100) for i in range(8)]
   
    # Sort that list
lista.sort()
print(lista)

    # Show its length
print (len(lista))

    # Search for an element that the user asks for by keyboard
element = int(input("Element: "))

if element in lista:
    print (f"Your number is in the index {lista.index(element)}")
else:
    print ("Not in...") """

# Dictionaries
"""rye_bread = {
    "name": "Rye Bread",
    "ingredients":["Flour","Rye Flour","Whole Flour","Water","Salt","Sour Dougth","Olive Oil"],
    "weights":[1250,1250,900,3000,80,900,64]
}
plus = 12.12
rye_bread["ingredients"] += [plus]

print(rye_bread["ingredients"])"""

# Know if a year is a leap year (From HackerRank.com)
"""
def is_leap(year):
    leap = False
    
    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True
    else:
        leap = False            
    return leap

year = int(input('year: '))

print(is_leap(year))"""

# Hackerrank exercise 
"""
num = int(input("#"))
a = set(input().split(" "))
other = int(input("#"))
for i in range(other):
    b = input().split(" ")
    c = set(input().split(" "))
    if b[0] == 'intersection_update':
        a.intersection_update(c)
    elif b[0] == 'update':
        a.update(c)
    elif b[0] == 'symmetric_difference_update':
        a.symmetric_difference_update(c)
    else:
        a.difference_update(c)
print(len(a))"""

# Find the value that does not repeat (From HackerRank.com)
"""
a = [1,2,3,4,5,6,1,2,3,4,5,7,8,9,7,9,6]
b = []

for n in a:
    if n not in b:
        b.append(n)
print (b)

for i in b:
    c = 0   
    for j in range(len(a)):        
        if i == a[j]:
            c += 1
    if c == 1:
        print(i)"""
    

# Find all possible coordinates that do not add up to n: (From HackerRank.com)
"""
x = 1
y = 1
z = 1
n = 2
lista1 = [i for i in range(x+1)]
lista2 = [i for i in range(y+1)]
lista3 = [i for i in range(z+1)]
lista_f = lista1+lista2+lista3
lista = list(lista_f)
print (lista)
from itertools import permutations
result = []
for p in permutations(lista_f,3):
    l = list(p)
    if l not in result:
        if sum(l) != n:
            result.append(l)
print(result)"""

# Finding the second largest of a list: (From HackerRank.com)
"""
n = 5
arr = map(int, input().split())
s = list(arr)
unrep = []
for i in s:
    if i not in unrep:
         unrep.append(i)

unrep.sort()
print(unrep[-2])"""

#Create nested list and print stuff (From HackerRank.com)
"""
students = []
for _ in range(int(input())):
        name = input()
        score = float(input())
        student = []
        student.append(name)
        student.append(score)
        students.append(student)
    temps = [students[i][1] for i in range(len(students))]
    unrep_temps = []
    for i in temps:
        if i not in unrep_temps:
            unrep_temps.append(i)
    unrep_temps.sort()
    second_lower = unrep_temps[1]
    
    for i in range(len(students)):
        if students[i][1] == second_lower:
            print(students[i][0])    """

"""n = int(input("#"))
student_marks = {}
for _ in range(n):
    name, *line = input("name: ").split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input("query")
print(student_marks)
for i in student_marks:
    if i == query_name:
        prom = (sum(student_marks[i])/len(student_marks[i]))
        print(".%f2"%prom)
        break"""


"""num = {"values":[32.5345,33.45,645.5234], "other": 123}
for i in range(len(num["values"])):
    print(int(round(num["values"][i])))"""

"""def listas (lista1, lista2, lista3=0, lista4=0):
    listas = [lista1, lista2, lista3, lista4]
    largo = len(lista1)
    for i in range(largo):
        if len(listas[i]) == largo:
            for j in range(largo):
                print(listas[i][j],end=" ")

one = ["fa", "fe", "sd", "fr", "gdm"]
two = [23,43,65,87,76]
three= [234,6546,876,324,675]

listas(one, two, three)
    
"""
"""N = int(input())
lis = []
for i in range (N):
    var = input()
    task = var.split()

    if task[0] == ['insert']:
        a = int(task[1])
        b = int(task[2])
        lis.insert(a,b)
    elif task[0] == ['print']:
        print(lis)
    elif task[0] == 'remove':
        a = int(task[1])
        lis.remove(a)
    elif task[0]== ['append']:
        a = int(task[1])
        lis.append(a)
    elif task[0]== 'sort':
        lis.sort
    elif task[0]== 'pop':
        lis.pop()
    elif task[0]== 'reverse':
        lis.reverse()"""

# Create PDF File:
"""
import pdfkit
pdfkit.from_string("Hello world!!!", "Hello.pdf")"""

# Create HTML list from a dictionary with bread recipe:
"""
recipe ={
    "ingredients":["Flour","Whole Flour","Rye Flour","Water","Salt","Olive Oil","Sour Dought"],
    "values":    [11100.23425,5700.654,750.84647,13500,345,300,4200],
    "prices":     [4000,4000,8000,1,3600,16000,1100]
    }

#recipe_str = str([f'{recipe["ingredients"][i]:20}{recipe["values"][i]}' for i in range(len(recipe["ingredients"]))])
recipe_str1 = str([f'<tr><td>{recipe["ingredients"][i]}</td><td>{recipe["values"][i]}</td><td>{recipe["prices"][i]}</td></tr>' for i in range(len(recipe["ingredients"]))])
cleaner={
    ord("[",):None,
    ord("]",):None,
    ord("'",):None,
    ord(",",):None}
html_format = recipe_str1.translate(cleaner)
print(html_format)"""


# Separate a number with decimals by the point and place them in a list:
"""
division = 2354/45
print(division)

dollar_cent_sep = lambda number: f'{number:.2f}'.split(".")
sep_div = dollar_cent_sep(division)
print(sep_div)"""

# Loop to validate if an input is of type integer with 4 tries and error messages:
"""
attempts = 0
 
while True:
    attempts += 1
    print(attempts)
    if attempts < 5:
        try:   
            validated_entry = int(input("entry"))   
            break            
        except:
            print("error_message\n")
    else:             
        print("Sorry, you have exceeded the valid number of attempts...")
        exit()

"""
"""
a = 12534.5345
b = a.split()
print(b)
"""

"""
a = "1990 Nov primer pagina en servidor del CERN"
b = "Abr 30 1993 el CERN puso www. de dominio publico"
c = "Oct 1994 T. E. Lee abandona el CERN y funda W3C"
d = "DIC 1991 T. E. Lee presenta www"""

"""
print("1 to save: \n2 to get")
save = Actions.menu_options_validator("Save: ")
        
if save == 1:
    Recipes.save_recipe(recipe)
elif save == 2:
    recipe1 = Recipes.get_user_recipe()
    Actions.show_recipe(recipe1, "g")"""


"""print("Invertir un a cadena en una linea"[::-1])"""

# Get html content from URL:
"""
import requests
from bs4 import BeautifulSoup
users_url = "https://www.eltiempo.com/opinion/columnistas/gustavo-duncan/columna-de-gustavo-duncan-educacion-a-cambio-de-coca-712620"
page = requests.get(users_url)
data = BeautifulSoup(page.content, "html.parser")

print (page.status_code)
#print(data.prettify())
print(page.encoding)"""

# Validate URL.txt:
"""
import os
cad = "C:/Users/mario/Escritorio/cota.tt"
print(os.path.isfile(cad) )"""

# Find .txt extension:
"""
url = "Hangmantexto.txt"
print(url[-4:len(url)])"""

