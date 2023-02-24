#!/usr/bin/python3

#Diogo de Macedo

print("Welcome to this Python program that predicts the probability of a child having cheek dimples based on the genotypes of both parents. Please use 'D' to represent the dominant allele and 'd' to represent the recessive allele when entering the parent genotypes. Only enter genotype combinations consisting of these two letters as arguments, such as 'Dd' or 'dd'. Have fun!"")

while True:
    try:
        mother = str(input("What is the mother's genotype?"))
        father = str(input("What is the father's genotype?"))
        if len(mother) != 2 or len(father) != 2:
            raise ValueError("Please provide two letters to represent each genotype")
        if not all(letter in {'D', 'd'} for letter in mother+father):
            raise ValueError("Please provide valid genotype characters (D' or 'd')")
        break
    except ValueError as e:
        print(f"Error: {e}")
        print("Please try again.\n")

x= "The child may or may not have dimples. Based on the parental genotypes, the probability of the child having dimples is of 25%."
y= "The child may or may not have dimples. Based on the parental genotypes, the probability of the child having dimples is of 50%."
if mother =='DD' or father == 'DD':
    print("The child will not have cheek dimples.")
    
if mother =='Dd' and father == 'Dd':
    print(x)
    
if mother == 'dD' and father == 'Dd':
    print(x)

if mother =='Dd' and father == 'dD':
    print(x)
    
if mother == 'dD' and father == 'dD':
    print(x)
    
if mother == 'Dd' and father =='dd':
    print(y)
if mother == 'dD' and father == 'dd':
    print(y)

elif father =='Dd' and mother =='dd':
    print(y)
elif father=='dD' and mother == 'dd':
    print(y)
elif mother == 'dd' and father == 'dd':
    print("The child will have cheek dimples!")

print("Thanks for playing! :)")
