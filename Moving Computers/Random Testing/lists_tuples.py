camping_list = ["water bottle", "laptop", "phone", "sleeping bag", "tent", "bug spray", "coffee"]

camp_site = ("The Arctic", 404, -34, True)

(location, address, temperature, danger) = camp_site

camping_list.append("charger")

camping_list.extend(["camera", "pencil", "power bank"])

camping_list = camping_list + ["snacks", "books", "warm clothes"]

camping_list.insert(0, "notebook")

camping_list.remove("laptop")

print(camping_list)
print(temperature)
