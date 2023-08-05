# guess game


secret_number = 10
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input('Guess my fav number : '))
    guess_count += 1
    if guess == secret_number:
        print('wow, you win !')
        break
else:
    print('please try agian')   