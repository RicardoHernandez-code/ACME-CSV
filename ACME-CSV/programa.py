import sys
import csv

#Funcion que busca productos y devuelve su valor, como parametro se utiliza el id de producto que se encuentre en otras listas o funciones.
def buscarProducto(x):
    with open('products.csv') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if(x == int(row[0])):
                return float(row[2])
#incrementa el valor total de una orden, guiandose por la funcion anterior que provee el precio de cada producto
def orden(y):
    with open('orders.csv') as file:
        resultado = 0
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if(row[0] == y):
                array=row[2].split()
                for x in array:
                    if(x.isnumeric()):
                        resultado+=buscarProducto(float(x))
    return resultado
                
            
                

                

#Punto 1: funcion para actualizar el documento 'order_prices.csv'
def orders_prices():
    orderPrices = []
    with open('orders.csv') as file:
        order = csv.reader(file)
        next(order)
        for row in order:
            euro = orden(row[0])
            ids = row[0]
            orderPrices.append([ids,euro])
    dataList = orderPrices
    with open('order_prices.csv','w',newline = '') as file2:
        writer = csv.writer(file2,delimiter=',')
        header = ['id','Euros']
        writer.writerow(header)
        writer.writerows(dataList)


#Funcion que prepara un array en donde se podran almacenar las listas que contendran los latos para luego imprimirlos,
# esta lista es proporcional a la cantidad de productos que tengamos
def recolectorProductos():
    productosId = []
    with open('products.csv') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            productosId.append([])
    return productosId

#Funcion en la cual se almacenan los id de los clientes en las listas correspondientes a cada id de producto dentro de la lista principal que las contiene.
def registroDeCompras():
    productos = recolectorProductos()
    with open('orders.csv') as file:
        order = csv.reader(file)
        next(order)
        for row in order:
            array=row[2].split()
            for x in array:
                if(x.isnumeric()):
                    productos[int(x)].append(row[1])
    number=0
    for y in productos:
        productos[number] = list(set(productos[number]))
        productos[number].sort(key=int)
        number+=1
    return productos



#punto 2: funcion para actualizar el documento product_customers.csv
def product_customers():
    data = registroDeCompras()
    arrayFinal = []
    with open('products.csv') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            ids = row[0]           
            clientes = data[int(row[0])]
            dato = ' '.join(map(str,clientes))
            arrayFinal.append([ids,dato])
    dataList = arrayFinal
    with open('product_customers.csv','w',newline = '') as file2:
        writer = csv.writer(file2,delimiter=',')
        header = ['id','customer_id']
        writer.writerow(header)
        writer.writerows(dataList)

    
#Funcion que ensambla una lista que colecciona los datos de la lista customers.
def recolectorCustomers():
    clientesId = []
    with open('customers.csv') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            clientesId.append([row[0],row[1],row[2]])
    return clientesId

#Funcion que realiza la suma de todas las ordenes realizadas por un cliente en particular (usando su id)
def sumaCustomer(y):
    with open('orders.csv') as file:
        resultado = 0
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if(row[1] == y):
                array=row[2].split()
                for x in array:
                    if(x.isnumeric()):
                        resultado+=buscarProducto(float(x))
    return resultado

#Funcion para organizar el ranking de clientes de mayor a menor
def rankearGastos(lis):
    return(sorted(lis, key = lambda x: x[3] , reverse = True)) 
    



#Funcion que realiza el ranking de los clientes.    
def customerRanking():
    customersId = recolectorCustomers()
    with open('customers.csv') as file:
        reader = csv.reader(file)
        next(reader)
        
        for row in reader:
            suma = sumaCustomer(row[0])
            customersId[int(row[0])].append(suma)
    return rankearGastos(customersId)  
    
#punto 3: funcion que rankea los clientes y su consumo total de mayor a menor
def customer_ranking():
    data = customerRanking()
    with open('customer_ranking.csv','w',newline = '') as file2:
        writer = csv.writer(file2,delimiter=',')
        header = ['id','firstname','lastname','total_euros']
        writer.writerow(header)
        writer.writerows(data)
#Funcion para imprimir el menu
def menu():
    print(" ")
    print(" ")
    print("1- Visualizar customer_ranking.")
    print(" ")
    print("2- Visualizar order_prices. ")
    print(" ")
    print("3- Visualizar product_customer")
    print(" ")
    print("4- actualizar ficheros ")
    print(" ")
    print("5- Salir ")
    print(" ")
    print(" ")

#Funcion de mensaje de confirmacion
def display():
    print("--------------------------")
    print(" ")
    print("ficheros actualizados: orders_prices.csv, product_customer.csv y customer_ranking.csv.")
    print(" ")
    print("--------------------------")

#Funcion para actualizar los ficheros 
def actualizarFicheros():
    customer_ranking()
    product_customers()
    orders_prices()
    display()


#Funcion principal del programa
def programa():
    option = 0
    while(option != 5):
        menu()
        print("Seleccione una opcion por favor")
        option = input()
        
        if(int(option) == 1):
            with open('customer_ranking.csv') as file:
                reader = csv.reader(file)
                for row in reader:
                    print(row)
        if(int(option)== 2):
            with open('order_prices.csv') as file:
                reader = csv.reader(file)
                for row in reader:
                    print(row)
        if(int(option) == 3):
            with open('product_customers.csv') as file:
                reader = csv.reader(file)
                for row in reader:
                    print(row)
        if(int(option) == 4):
            actualizarFicheros()
        if(int(option) == 5):
            sys.exit(0)
        if(option.isnumeric() ==  False or int(option) > 5):
            print("Valor incorrecto!")

programa()
            
            
            

