from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def response_handler(input_string):
  while True:
    response = input(input_string)
    if response.lower() in COMMANDS:
      return response.lower()
    print("Unknown command")

def turn_off():
  global ON
  ON = False

def print_report():
  coffee_maker.report()
  till.report()

def process_item(item):
  drink = menu.find_drink(item)
  if not coffee_maker.is_resource_sufficient(drink):
    return
  if not till.make_payment(drink.cost):
    return
  coffee_maker.make_coffee(drink)

menu = Menu()
coffee_maker = CoffeeMaker()
till = MoneyMachine()

items = [item for item in menu.get_items().split("/") if item]

COMMANDS = {
  "off": turn_off,
  "report": print_report
}
COMMANDS.update({ item: process_item for item in items })

ON = True

while ON:
  input_question = f"What would you like? ({",".join(items)}): "
  response = response_handler(input_question)
  if response in items:
    COMMANDS[response](response)
  else:
    COMMANDS[response]()