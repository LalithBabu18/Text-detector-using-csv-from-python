import csv

amount=0
namearray=[]
dataarray=[]
ordersarray=[]




csv.register_dialect('myDialect',
delimiter = ',',
skipinitialspace=True)
with open('data.txt', 'r') as csvFile:
    reader = csv.reader(csvFile, dialect='myDialect')
    for row in reader:
        dataarray.append(row)





for i in range(1,len(dataarray)):
    amount=amount+int(dataarray[i][3])



def singleOrderFinder(arr, n):

    visited = [False for i in range(n)]


    for i in range(n):


        if (visited[i] == True):
            continue


        count = 1
        for j in range(i + 1, n, 1):
            if (arr[i] == arr[j]):
                visited[j] = True
                count += 1


        if(count==1):
            print(arr[i])

        ordersarray.append(count)






for i in range(1,len(dataarray)):
    namearray.append(dataarray[i][2])




def orders(array):
    o1 = 0
    o2 = 0
    o3 = 0
    o4 = 0
    o5 = 0
    for o in range(0, len(array)):
        if (array[o] == 1):
            o1 = o1 + 1

        if (array[o] == 2):
            o2 = o2 + 1

        if (array[o] == 3):
            o3 = o3 + 1

        if (array[o] == 4):
            o4 = o4 + 1

        if (array[o] >= 5):
            o5 = o5 + 1

    print("PEOPLE ORDERED ONCE", o1)
    print("PEOPLE ORDERED TWICE", o2)
    print("PEOPLE ORDERED THRICE", o3)
    print("PEOPLE ORDERED FOUR TIMES", o4)
    print("PEOPLE ORDERED FIVE TIMES", o5)




print("1.Total orders recieved by the site",len(dataarray))
print("------------")
print("2.Total amount recieved from the orders",amount)
print("------------")
print("3.Customers only ordered onece")
singleOrderFinder(namearray, len(namearray))
print("------------")
orders(ordersarray)