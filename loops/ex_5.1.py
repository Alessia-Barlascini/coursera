# repeat asking for a number until the word done is entered
# print done
# print the total
# print the count
# print the average at the end


somma=0
num=0

while True:
    val=input('Enter a number: ')
    if val == 'done':
        break
    fval=float(val)
    print (fval)
    num=num+1
    somma=somma+fval

print('all done')
print(somma,num,somma/num)