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

    def total_busket(self):
        '''retorna el valor total de los productos en la canasta'''
        pass

    def add_food(self, product_id: str, quantity: int):
        '''añade el producto a la canasta'''
        pass

    def remove_food(self, Food_basket):
        '''elimina el producto de la canasta'''
        pass




