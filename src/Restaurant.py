<<<<<<< HEAD
from sqlite3 import connect


=======
>>>>>>> 7ee4f90036c4d7ce76c59d5fa6bcb55c6550948d
class Product:  # Es una clase para la base de datos
    def __init__(self, food_id: str, name: str,
                 price: float, food_description: str) -> None:
        self.food_id = food_id
        self.name = name
        self.price = price
        self.food_description = food_description

    def delete_product(self):
        '''borra las comidas almacenadas en una base de datos'''
        pass

    def add_product(self):
        '''crea y almacena las comidas en la base de datos'''
        pass



class Food:
    def __init__(self, food_id: str, quantity: int) -> None:
        self.food_id = food_id
        self.quantity = quantity
    
    def checkFood(self):
        '''busca la disponibilidad de la comida en la base de datos'''
        pass



class comission:
    def __init__(self, food_id: str, Total_buy: float, User_name: str,
                buyer_mail: str, buyer_phone: str, commission_id: str ) -> None:
        self.food_id = food_id
        self.Total_buy = Total_buy
        self.User_name = User_name
        self.buyer_mail = buyer_mail
        self.buyer_phone = buyer_phone
        self.commission_id = commission_id

    def Status(self):
        '''Modifica el estado del orden en la base datos, si esta enviado o no'''
        pass

    

class Food_basket:
    def total_food(self):
        '''retorna el valor del producto'''
        pass



class Basket():
    def __init__(self) -> None:
        self.Food_basket = []
        self.product_name = ""
        self.quantity = 0

    def total_busket(self):
        '''retorna el valor total de los productos en la canasta'''
        pass

    # def add_food(self, product_id: str, quantity: int):
    def add_food(self):
        '''añade el producto a la canasta'''
        print("Introducir nombre de la comida")
        self.product_name = str(input())
        print("Cantidad")
        self.quantity = int(input())
        self.Food_basket.append(self.product_name)
        

    def remove_food(self, Food_basket):
        '''elimina el producto de la canasta'''
        pass


class User():
    User_number = 0
    def __init__(self, email: str, password: str) -> None:
        self.email = email
        self.password = password

        self.connected = False
        self.attemps = 3
        User.User_number += 1

    def connect(self):
        mypassword = input("ingresa la contraseña: ")
        if mypassword == self.password:
            print("conectado exitosamente!")
            self.coneccted = True
        else:
            self.attemps -= 1
            if self.attemps > 0:
                print("contraseña incorrecta, intentelo de nuevo ")
                print("te quedan " , self.attemps , " intentos")
                self.connect()
            else:
                print("superaste los maximos intentos, intentalo mas tarde.")

    def disconnect(self):
        if self.connect:
            print("secion cerrado exitosamente.")
            self.connected = False
        else:
            print("Error, secion no iniciada")

    def __repr__(self):
        if self.connect:
            conect = "conectado"
        else:
            conect = "no conectado, verifique sus valores"
        return conect