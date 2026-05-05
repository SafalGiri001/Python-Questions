a = int(input("Enter a number: "))
if a%2==0:
    print("The number is even")
else:
    print("The number is odd")

#2
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
if a>=b and a>=c:
    print("a is greatest number")
elif b>=c:
    print("b is greatest number")
else:
    print("c is greatest number")


#q3
movie =[]
mov1 = input("enter first movie: ")
mov2 = input("enter second movie: ")
mov3 = input("enter third movie: ")
movie.append(mov1)
movie.append(mov2)
movie.append(mov3)
print(movie)


#q4
list1= [1,2,1]
list2= [1,2,3]
copy_list1 = list1.copy()
copy_list1.reverse()
if copy_list1==list1:
    print("palindrome")
else:
    print("not palindrome")

