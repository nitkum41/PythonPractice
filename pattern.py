def pattern(n):
    for i in range(n):
        # print(f'{' '}{'*'*i}{' '}')
        # print("*" * i)
        z=int(n-i/2)
        if i%2!=0:
            i-=1
            print('{}{}{}'.format(' '* z, '*'*i, ' '* z)
        else:
            i+=1
            print('{}{}{}'.format(' ' * z, '*' * i, ' ' * z))


pattern(17)
