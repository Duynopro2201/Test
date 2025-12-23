class Product:
    def __init__(self, product_id, name, price):
        self.id = product_id
        self.name = name
        self.price = price
        
class CartItem:
    def __init__(self, product, quantity):
        self.product = product  
        self.quantity = quantity

    def subtotal(self):
        return self.product.price * self.quantity

    def __str__(self):
        return (
            f"{self.product.name:<15} | "
            f"{self.quantity:^5} | "
            f"{self.product.price:>10,.0f} | "
            f"{self.subtotal():>12,.0f}"
        )

class Cart:
    def __init__(self):
        self.items = {}

    def add(self, product, qty):
        if product.id in self.items:
            self.items[product.id].quantity += qty
        else:
            self.items[product.id] = CartItem(product, qty)

    def remove(self, product_id):
        if product_id in self.items:
            del self.items[product_id]

    def update(self, product_id, qty):
        if product_id in self.items:
            if qty <= 0:
                self.remove(product_id)
            else:
                self.items[product_id].quantity = qty

    def total(self):
        return sum(item.subtotal() for item in self.items.values())

    def apply_discount(self, percent):
        discount = self.total() * percent / 100
        return discount

    def print_invoice(self, discount_percent=0):
        print("========== HOÁ ĐƠN ==========")
        print(f"{'Sản phẩm':<15} | {'SL':^5} | {'Giá':>10} | {'Thành tiền':>12}")
        print("-" * 50)

        for item in self.items.values():
            print(item)

        print("-" * 50)
        total = self.total()
        discount = self.apply_discount(discount_percent)
        payable = total - discount

        print(f"{'Tổng cộng:':<30}{total:>20,.0f}")
        print(f"{'Giảm giá:':<30}{discount:>20,.0f}")
        print(f"{'Phải trả:':<30}{payable:>20,.0f}")
        print("=============================")


p1 = Product(1, "Bút", 5000)
p2 = Product(2, "Vở", 12000)
p3 = Product(3, "Thước", 8000)


cart = Cart()


cart.add(p1, 10)
cart.add(p2, 5)
cart.add(p3, 2)


cart.update(1, 12)


cart.print_invoice(discount_percent=10)



