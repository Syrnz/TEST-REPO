list_makanan = [
    ["Niku", "Ramen", "Mochi"],
    ["Burger", "Pizza", "Pasta"],
    ["Mie", "Rujak", "Sate"]
]

# for menu in list_makanan:
#     for makanan in menu:
for i in range (0, 2):
    for j in range (i, 3):
        print (list_makanan[i*j])
    print()