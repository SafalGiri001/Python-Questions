numbers = [4,7,1,9,3]
total = 0
for n in range(len(numbers)):
    total += numbers[n]
print(total)

numbers = [2,3,4,5,6,7,8]
total = 0
for i in range (len(numbers)):
    total += numbers[i]
print(total)

number = [2,3,4,5,6,7,8]
for i in range (len(number)):
    if number[i]%2 == 0:
        print(f'{number[i]} is even')

print(total)



number = [2,3,4,5,6,7,8]
total = 0
for i in range (len(number)): #7  0 1 2 3 4 5 6
    if number[i]%2 == 0: #this is for even but for odd use !=0.
        total = total + number[i] #0+2=2 2+2=4 2+4=5
print(total)

number = [2,3,4,5,6,7,8]
even_number =  [3,4,6,8]
odd_number = [3,5,7]
total = 0
for i in range (len(number)): #7  0 1 2 3 4 5 6
    if number[i]%2 != 0:#this is for even but for odd use !=0
        odd_number.append(number[i])
        total = total + number[i] #0+2=2 2+2=4 2+4=5
print(total)
print(f'odd number: {odd_number}')
print(f'even number: {even_number}')



number =[2,3,4,5,6,7,8]
even_number = []
odd_number = []
for i in numbers:
    if i%2 == 0:
        even_number.append(i)
    else:
        odd_number.append(i)
print(f'even number: {even_number}')
print(f'odd number: {odd_number}')





















