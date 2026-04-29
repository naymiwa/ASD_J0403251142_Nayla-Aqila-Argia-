# Implementasi Dasar Graph
#Nama: Nayla Aqila Argia
#NIM: J0403251142

graph = {
    'A':['B','C'],
    'B':['A','D'],
    'C':['A','D'],
    'D':['B','C']
}
for node in graph:
    print(node,"->",graph[node])
# Penjelasan:
# Graph disimpan dalam dictionary:
# - Key = vertex
# - Value = list tetangga
