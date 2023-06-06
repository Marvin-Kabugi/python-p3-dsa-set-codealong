class MySet:
    def __init__(self, list=[]) -> None:
        self.dictionary = {}
        for value in list:
            self.dictionary[value] = True

    def has(self, value):
        return value in self.dictionary
    
    def add(self, value):
        if not self.has(value):
            self.dictionary[value] = True
        return self
    
    def delete(self, value):
        self.dictionary.pop(value, None)
        return self
    
    def size(self):
        len(self.dictionary)

    def clear(self):
        self.dictionary.clear()
        return self
    
    def __str__(self) -> str:
        set_list = []
        for key, value in self.dictionary.items():
            set_list.append(str(key))
        return f'MySet: {{{",".join(set_list)}}}'