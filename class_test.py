class Item : 
    pay_rate = 0.8
    all = []
    def __init__(self , name :str , price : float , quantity =0 ):
        assert price >= 0 , f"price {price} is not greater than zero"
        assert quantity >= 0 ,f"quantity {quantity} is not greater than zero "
        self.name = name 
        self.price = price 
        self.quantity = quantity

        Item.all.append(self)
    
    def calculate_total_price (self):
        return self.price *self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
    
    def __repr__(self) :
        return f"Item('{self.name}','{self.price}','{self.quantity}'"
    
item1 = Item("phone" , 100 , 3)
item2 = Item("laptop" , 500 , 4)


print(Item.all)