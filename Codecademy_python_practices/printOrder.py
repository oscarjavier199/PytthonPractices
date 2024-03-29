# Program displays tables from a restaurant,
# names and orders, program used to practice functions in python

# nested dict for tables and person who orders
tables = {
    1: {
        'name': 'Jiho',
        'vip_status': False,
        'order': 'Orange Juice, Apple Juice'
    },
    2: {},
    3: {},
    4: {},
    5: {},
    6: {},
    7: {},
}


# assigns tables
def assign_table(table_number, name, vip_status=False):
    tables[table_number]['name'] = name
    tables[table_number]['vip_status'] = vip_status
    tables[table_number]['order'] = ''


# takes order
def assign_and_print_order(table_number, *order_items):
    tables[table_number]['order'] = order_items
    for order_item in order_items:
        pass


assign_table(2, 'Arwa', True)
assign_and_print_order(2, 'Steak', 'Seabass', 'Wine Bottle')
print(tables)
