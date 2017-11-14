class OrdDic():

    def __init__(self, dict_arg={}, **kvpairs):
        # set the index of the dict to be -1, to iterate from 0
        self.index = -1

        # instanciate keys and values lists
        self._keys_list = []
        self._values_list = []

        # for each k:v pairs...
        for key, value in kvpairs.items():
            # append key to _keys_list
            self._keys_list.append(key)
            # append value to _values_list
            self._values_list.append(value)

        for key in dict_arg:
            self[key] = dict_arg[key]

    def __repr__(self):
        """
        Represents the dict like a built-in dict in Python.
        {k:v, k:v, ...}
        """
        t = []
        if len(self._keys_list) <= 0:
            return '{}'
        else:
            for i_idx, i in enumerate(self._keys_list):
                t.append('{}: {}'.format(self._keys_list[i_idx], self._values_list[i_idx]))
            return '{' + ", ".join(t) + '}'

    def __str__(self):
        """ Using repr to print """
        return repr(self)

    def __getitem__(self, key):
        """
        Returns the value associated with the key passed in arg.
        Can be used like so : dict[key].
        """
        if key not in self._keys_list:
            raise KeyError("{} not in dict.".format(key))
        else:
            # get the index of the passed key
            index = self._keys_list.index(key)
            # return the value at this index in _values_list
            return self._values_list[index]

    def __setitem__(self, key, value):
        """
        Sets new items in the dict.
        If the key exists, replace old value with the new one.
        """
        # if the key is already in the dict
        if key in self._keys_list:
            # get the index of the key
            idx = self._keys_list.index(key)
            # assign the value to the existing key
            self._values_list[idx] = value

        # else, append the key and value in their respective list
        else:
            self._keys_list.append(key)
            self._values_list.append(value)

    def __len__(self):
        """
        Returns the length of the dict.
        """
        return len(self._keys_list)

    def __delitem__(self, key):
        """
        If the specified key is in the dict,
        delete it.
        Else raise a KeyError.
        """
        if key in self._keys_list:
            idx = self._keys_list.index(key)
            del self._keys_list[idx]
            del self._values_list[idx]

        else:
            raise KeyError('Key {} not in dict'.format(key))

    def sort(self):
        """
        Sorts the dict keys.
        """
        sorted_keys = sorted(self._keys_list)

        # new values list
        sorted_values = []

        for key in sorted_keys:
            # get the value for each key
            value = self[key]
            # append the value to the new list
            sorted_values.append(value)

        # set origin keys_list and values_list to the new ones
        self._keys_list = sorted_keys
        self._values_list = sorted_values

    def reverse(self):
        """
        Reverses the index by creating reversed copies of the dict.
        """
        self._keys_list = self._keys_list[::-1]
        self._values_list = self._values_list[::-1]

    def __contains__(self):
        """ Returns True if key in self._keys_list, False otherwise"""
        return key in self._keys_list

    def __iter__(self):
        """ returns self, the iterable """
        return self

    def __next__(self):
        """ Returns each key in the iterable """
        if self.index == len(self) - 1:
            raise StopIteration
        self.index += 1
        return self._keys_list[self.index]

    def __add__(self, other):
        """ Creates a new ord dict. self and other are added to this new dict, in order. """
        new_dict = OrdDic()

        # add self items to the new_dict
        for key, value in self.items():
            new_dict[key] = value

        # add other dict items to the new_dict
        for key, value in other.items():
            new_dict[key] = value

        return new_dict

    def keys(self):
        """ Checks if the dict has keys.
        If it has, returns the list of the keys, in a list
        """
        if self._keys_list == 0:
            print("There is no key in the dictionnary")
        else:
            return self._keys_list

    def values(self):
        """ Checks if the dict has values.
        If it has, returns the list of the values, in a list
        """
        if self._values_list == 0:
            print("There is no value in the dictionnary")
        else:
            return self._values_list

    def items(self):
        """
        Checks if there is at least one k:v pair in the dict.
        If there is, yields each key and value.
        """
        if self._keys_list == 0 and self._values_list == 0:
            print("There is no valid key:value pair in the dictionnary")
        else:
            for k_idx, key in enumerate(self._keys_list):
                # value is equal to the value at the k_idx
                value = self._values_list[k_idx]
                yield(key, value)


d = {1: 2, 3: 4}

new_d = OrdDic(d)
print("From dict:", new_d)

dic = OrdDic(banane=1, poire=0)

dic_two = OrdDic(apple="macOS", microsoft="Windows")

dic["haricot"] = 4
dic["patate"] = 45


print("keys:", dic.keys())
print("values:", dic.values())

for key, value in dic.items():
    print("{} ({})".format(key, value))

for key in dic:
    print(key)

dic.sort()
print("sorted:", dic)

dic.reverse()
print("reversed:", dic)

t = dic + dic_two
print("New dict:", t)

print(dic)

if "banane" in dic.keys():
    print("Yes")
