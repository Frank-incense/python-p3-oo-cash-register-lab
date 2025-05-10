#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0):
    self.discount = discount
    self.total = 0
    self.items = []

  @property
  def discount(self):
    return self._discount
  
  @discount.setter
  def discount(self, discount):
    self._discount = discount

  def add_item(self, title, price, quantity=1):
    for i in range(quantity):
      self.items.append(title)

    self.last_transaction = price * quantity
    self.total += self.last_transaction

  def apply_discount(self):
    if self.discount:
      self.total -= self.total * (self.discount/100)
      print(f"After the discount, the total comes to ${self.total:.0f}.")
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    self.total -= self.last_transaction