# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
print("hi")
print("""this
is 
great""")
print('3' + 'a')

print('x' + str(42))
print('hello\nworld')

x = 4
if x > 8:
    print('more than eight')
elif x < 100:
    print('less than 100')
print('all done')

astr = '123'
istr = int(astr)
print('Second', istr)

"""
score = input("Enter Score: ")
if float(score) < float(0.0) or float(score) > float(1.0) :
     print('score is out of range!')
elif float(score) >= float(0.9):
    print('A')
elif float(score) >= float(0.8) and float(score) < float(0.9):
    print('B')
elif float(score) >= float(0.7) and float(score) < float(0.8):
    print('C')
elif float(score) >= float(0.6) and float(score) < float(0.7):
    print('D')
else:
    print('F')
""
largest_so_far = 0
print('Before',largest_so_far)
for the_num in [5,6,10,40,78,100]:

    if the_num > largest_so_far:
        largest_so_far = the_num
        print(largest_so_far,the_num)
print('After',largest_so_far)
"""
found = False
print('Before', found)
for value in [9, 8, 7, 5, 4, 6, 10, 12, 18]:
    if value == 6:
        found = True
        print(found, value)
print('After', found)

smallest = None
for value in [9, 41, 12, 3, 74, 15]:
    if smallest is None or value < smallest:
        smallest = value
        print(smallest)

"""
def slice_1():
    email_address = input("Enter your email addres :").strip()
    strip_username = email_address.split('@')[0]
    strip_ending = email_address.split('@')[-1]
    print('Username:', strip_username)
    print('Provider:', strip_ending)


slice()
""""""
def slice_1(x,y):
    email_address = input("Enter your email addres :").strip()
    strip_username = email_address.split('@')[0]
    strip_ending = email_address.split('@')[-1]

    if strip_username == x:
        return x
    if strip_ending == y:
        return y
print('Username:',slice_1(x,y))
print('Provider:',slice_1(x,y))
"""


def slice_mail(email_address):
    parts = email_address.split('@')
    strip_username = parts[0]
    strip_ending = parts[-1]
    return 'Username:' + strip_username + '\n' + 'Provider:' + strip_ending


email_from_input = input("Enter your email address : ").strip()
print(slice_mail(email_address=email_from_input))
