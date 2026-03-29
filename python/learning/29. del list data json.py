import json

todo_list = [
    "Balajar Python",
    "Belajar Django",
    "Belajar MongoDB",
    "Belajar Sulap",
    "Belajar Python",
    "Belajar Flask"
]

with open(r"C:\Users\lenovo\Latihan\todolist.json") as file_object:
        todo_list = json.load(file_object)

# Misalkan kita ingin menghapus "Belajar Sulap" & "Belajar Python"
# yang berada di indeks ke-3
del todo_list[3]
# nilai harus string
todo_list.remove("Belajar Python")

with open('todolist.json', 'w') as json_file:
    json.dump(todo_list, json_file)
print(todo_list)