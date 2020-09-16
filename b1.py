ten = "Diệp Thanh Nguyên"
print(ten)

list = [
    {"ten": "Hoc vien A", "tuoi": 100, "donvi": "Viettel"},
    {"ten": "Hoc vien B", "tuoi": 101, "donvi": "Viettel"},
    {"ten": "Hoc vien C", "tuoi": 102, "donvi": "Viettel"},
    {"ten": "Hoc vien D", "tuoi": 103, "donvi": "Viettel"},
    {"ten": "Hoc vien E", "tuoi": 104, "donvi": "Viettel"}
]
for x in list:
    print("-------")
    print("Ten: ", x["ten"])
    print("Tuoi: ", x["tuoi"])
    print("Don vi: ", x["donvi"])
