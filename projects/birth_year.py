# write a program that take name and age and return birth year

name = input('what is your name ? ')
age = int(input('how old are you ? '))
birth_year = 2023 - age
print(f'Hi, {name.capitalize()} your birth year is {birth_year}')