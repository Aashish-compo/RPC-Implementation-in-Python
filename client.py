import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8000')

while(1):
    n = int(input("Enter the number for factorial "))
    print("The factorial of the number is {}".format(s.fact(n)))