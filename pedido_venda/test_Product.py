from datetime import datetime

from Entities.Customer import Customer
from Entities.Order import Order
from Entities.OrderProduct import OrderProduct
from Entities.Product import Product
from Repositories.CustomerRepository import CustomerRepository
from Repositories.ProductRepository import ProductRepository

def test_new_process_product_with_down_stock():
    # Arrange
    customer1 = Customer(1, "Jefté")
    customer_repository = CustomerRepository()
    customer_repository.append_customer(customer1)

    product1 = Product(1, "Milk", 50, 10)
    product_repository = ProductRepository()
    product_repository.append_product(product1)

    order = Order(1, customer1, datetime.today)
    order_product1 = OrderProduct()
    order_product1.add_product(product1, 5)
    order.add_order_product(order_product1)

    # Act
    order.update_total_price()

    # Assert
    assert product1.get_stock() == 5
    
    
def test_down_stock():
    product1 = Product(1, "Milk", 50, 20)
    
    # Act
    product1.down_stock(5)

    # Assert
    assert product1.get_stock() == 15
        
        