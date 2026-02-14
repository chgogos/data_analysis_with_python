import copy

a_list = [1, 2, 3]
new_list = a_list  # Αντιγραφή αναφοράς (alias)
new_list.append(4)
print(a_list)  # [1, 2, 3, 4]  => επηρεάζεται
print(new_list)  # [1, 2, 3, 4]

a_list = [1, 2, 3]
new_list = a_list[:]  # Ρηχή αντιγραφή (slice)
new_list.append(4)
print(a_list)  # [1, 2, 3]     => δεν επηρεάζεται
print(new_list)  # [1, 2, 3, 4]

a_list = [[1, 2], [3, 4]]  # εμφωλευμένη λίστα
new_list = a_list.copy()  # Ρηχή αντιγραφή
new_list[0].append(99)
print(a_list)  # [[1, 2, 99], [3, 4]]  => επηρεάζεται (εσωτερική λίστα)
print(new_list)  # [[1, 2, 99], [3, 4]]

a_list = [[1, 2], [3, 4]]
new_list = copy.deepcopy(a_list)  # Βαθιά αντιγραφή
new_list[0].append(99)
print(a_list)  # [[1, 2], [3, 4]]      => δεν επηρεάζεται
print(new_list)  # [[1, 2, 99], [3, 4]]