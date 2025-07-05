class HashTable:
    """ keep length with 6 default"""

    def __init__(self, size=7):
        self.data_map = [None] * size
        print(type(self.data_map))
        print(self.data_map)

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            """use prime number any"""
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, " : ", val)

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if key == self.data_map[index][i][0]:
                    return self.data_map[index][i][1]
        return None

    def get_keys(self):
        all_keys = []
        print(type(range(8)))
        for i in range(len(self.data_map)):

            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys


if __name__ == '__main__':
    hash_table = HashTable()
    hash_table.set_item('bolts', 1400)
    hash_table.set_item('washers', 50)
    hash_table.set_item('lumber', 70)
    hash_table.print_table()
    print(hash_table.get_item('bolts'))
    print(hash_table.get_item('bolts1'))
    print(hash_table.get_keys())
