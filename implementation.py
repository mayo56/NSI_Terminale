# Exo 1

class Tableau:
    def __init__(self, data = []) -> None:
        self.data = data

    def __repr__(self):
        return "Tableau(" + str(self.data) + ")"

    def push(self, index: int, element: any) -> None:
        if self.is_empty():
            self.data.append(element)
        else:
            new_data = []
            if len(self.data) <= index:
                new_data = self.data
                new_data.append(element)
            else:
                for i in range(len(self.data)):
                    if index == i:
                        new_data.append(element)
                    new_data.append(self.data[i])
            self.data = new_data

    def delete(self, index:int) -> None:
        new_data = []
        for i in range(len(self.data)):
            if i != index:
                new_data.append(self.data[i])
        self.data = new_data

    def is_empty(self) -> bool:
        return self.data == []

    def len(self) -> int:
        return len(self.data)

print("---- TAB ----")
tab = Tableau()

print(tab.len())
print(tab.is_empty())
tab.push(0, "pomme")
print(tab.data)
tab.push(1, "poire")
print("non", tab.data)
tab.push(0, "peche")
print("oui", tab.data)
print(tab.is_empty())
tab.delete(2)
tab.delete(0)
print(tab.data)

print()
print("---- TABl ----")
tabl = Tableau([2,6,5])

print(tabl.len())
print(tabl.is_empty())
tabl.push(0, 12)
tabl.delete(2)
print(tabl)