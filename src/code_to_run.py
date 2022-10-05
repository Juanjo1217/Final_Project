#%%
from Restaurant import Basket
from Restaurant import User
#%%
basket1 = Basket()
#%%
basket1.add_food()
basket1.add_food()
basket1.add_food()
basket1.Food_basket
#%%
#%%
user1 = User(input("Ingrese un email porfavor: "), input("ingrese una contraseña: "))
user1.connect()