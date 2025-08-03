import asyncio
from asyncio import Queue
from random import randrange
from typing import List


class Product:
    def __init__(self, name: str, checkout_time: float):
        self.name = name
        self.checkout_time = checkout_time
    

class Customer:
    def __init__(self, customer_id: int, products: List[Product]):
        self.customer_id = customer_id
        self.products = products
    

async def checkout_customer(queue: Queue, cashier_number: int):
    while not queue.empty():
        customer: Customer = queue.get_nowait()
        print(f'Cashier {cashier_number}')
        print(f"Checking out customer {customer.customer_id}")
        print(f"Estimate time: {sum([i.checkout_time for i in customer.products])}")
    
        for product in customer.products:
            print(f"Cashier {cashier_number} checking out {customer.customer_id}'s {product.name}")
            await asyncio.sleep(product.checkout_time)
        
        print(f'Cashier {cashier_number} finished checking out customer {customer.customer_id}')

        queue.task_done()  # counter will -= 1


async def main():
    customer_queue = Queue()
    all_products = [Product('beer', 0.2), Product('bananas', 0.5), Product('sausage', .2), Product('diapers', .2)]
    for i in range(10):
        products = [all_products[randrange(len(all_products))] for _ in range(randrange(10))]

        customer_queue.put_nowait(Customer(i, products))

        print(f"Customer {i} products: {[p.name for p in products]}")

    cashier = [asyncio.create_task(checkout_customer(customer_queue, i)) for i in range(3)]

    await asyncio.gather(customer_queue.join(), *cashier)


# asyncio.run(main())


# 处理上下限

def generate_customer(customer_id: int) -> Customer:
    all_products = [Product('beer', .2), Product('bananas', .5), Product('sausage', .2), Product('diapers', .2)]
    products = [all_products[randrange(len(all_products))] for _ in range(randrange(10))]
    return Customer(customer_id, products)


async def customer_generator(queue: Queue):
    customer_count = 0
    while True:
        customers = [generate_customer(i) for i in range(customer_count, customer_count + randrange(5))]

        for customer in customers:
            print("Waiting to put customer in line")
            await queue.put(customer)  # blocking
            print("Customer put in line!")
            customer_count = customer_count + len(customers)
            await asyncio.sleep(1)


async def main_with_customer_generator():
    customer_queue = Queue(5)

    customer_producer = asyncio.create_task(customer_generator(customer_queue))

    cashiers = [asyncio.create_task(checkout_customer(customer_queue, i)) for i in range(3)]
    print(f"Cashiers: {cashiers}")
    await asyncio.gather(customer_producer, *cashiers)


asyncio.run(main_with_customer_generator())