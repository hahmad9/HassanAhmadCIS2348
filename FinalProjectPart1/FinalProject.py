'''
Hassan Ahmad
ID: 1865003
'''


import csv

from datetime import datetime


class OutputInventory:

    def __init__(self, item_list):

        #This is used for the items

        self.item_list = item_list

    def full(self):

        #In alphabetical order the inventory will be created and include specifics into a csv file

        with open('./output/FullInventory.csv', 'w') as file:

            items = self.item_list
            # get order of keys to write to file based on manufacturer
            keys = sorted(items.keys(), key=lambda x: items[x]['manufacturer'])

            for item in keys:

                id = item
                man_name = items[item]['manufacturer']
                item_type = items[item]['item_type']
                price = items[item]['price']
                service_date = items[item]['service_date']
                damaged = items[item]['damaged']
                file.write('{},{},{},{},{},{}\n'.format(id, man_name, item_type, price, service_date, damaged))

    def damaged(self):

        #This function will create output files according to damaged items in a decending order

        items = self.item_list
        # get order of keys to write to file based on price
        keys = sorted(items.keys(), key=lambda x: items[x]['price'], reverse=True)

        with open('./output/DamagedInventory.csv', 'w') as file:

            for item in keys:

                id = item
                man_name = items[item]['manufacturer']
                item_type = items[item]['item_type']
                price = items[item]['price']
                service_date = items[item]['service_date']
                damaged = items[item]['damaged']

                if damaged:

                    file.write('{},{},{},{},{}\n'.format(id, man_name, item_type, price, service_date))

    def by_type(self):

        # the item ID will sort the contents of this function into rows in the csv file

        items = self.item_list
        types = []
        keys = sorted(items.keys())

        for item in items:
            item_type = items[item]['item_type']

            if item_type not in types:
                types.append(item_type)

        for type in types:

            file_name = type.capitalize() + 'Inventory.csv'
            with open('./output/' + file_name, 'w') as file:

                for item in keys:

                    id = item
                    man_name = items[item]['manufacturer']
                    price = items[item]['price']
                    service_date = items[item]['service_date']
                    damaged = items[item]['damaged']
                    item_type = items[item]['item_type']

                    if type == item_type:
                        file.write('{},{},{},{},{}\n'.format(id, man_name, price, service_date, damaged))

    def past_service(self):

        # In this function, output files will be created according to expired items from oldest to recent

        items = self.item_list
        keys = sorted(items.keys(), key=lambda x: datetime.strptime(items[x]['service_date'], "%m/%d/%Y").date(),
                      reverse=True)
        with open('./output/PastServiceDateInventory.csv', 'w') as file:

            for item in keys:

                id = item
                man_name = items[item]['manufacturer']
                item_type = items[item]['item_type']
                price = items[item]['price']
                service_date = items[item]['service_date']
                damaged = items[item]['damaged']
                today = datetime.now().date()
                service_expiration = datetime.strptime(service_date, "%m/%d/%Y").date()
                expired = service_expiration < today

                if expired:
                    file.write('{},{},{},{},{},{}\n'.format(id, man_name, item_type, price, service_date, damaged))



if __name__ == '__main__':
    items = {}
    files = ['ManufacturerList.csv', 'PriceList.csv', 'ServiceDatesList.csv']

    for file in files:
        with open(file, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            for line in csv_reader:
                item_id = line[0]

                if file == files[0]:

                    items[item_id] = {}
                    man_name = line[1]
                    item_type = line[2]
                    damaged = line[3]
                    items[item_id]['manufacturer'] = man_name.strip()
                    items[item_id]['item_type'] = item_type.strip()
                    items[item_id]['damaged'] = damaged

                elif file == files[1]:

                    price = line[1]
                    items[item_id]['price'] = price

                elif file == files[2]:

                    service_date = line[1]
                    items[item_id]['service_date'] = service_date

    inventory = OutputInventory(items)

    inventory.full()

    inventory.by_type()

    inventory.past_service()

    inventory.damaged()

    types = []

    manufacturers = []

    for item in items:

        checked_manufacturer = items[item]['manufacturer']

        checked_type = items[item]['item_type']

        if checked_manufacturer not in types:
            manufacturers.append(checked_manufacturer)

        if checked_type not in types:
            types.append(checked_type)

    
