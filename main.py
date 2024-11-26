from cliente import Cliente
from item import Item

cliente = Cliente("Laís", "Alura")
item_um = Item("Pizza", 30.0)
item_dois = Item("Refrigerante", 5.0)
print(f"Item: {item_um.nome}, Preço: {item_um.preco}")