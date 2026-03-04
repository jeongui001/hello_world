colors = ["red", "blue", "orange", "purple", "green"] # 리스트 선언
print(colors)

colors[1] = "sky blue" # 리스트 요소 변경
print(colors)

colors.append("추가한 값") # 리스트 요소 추가
print(colors)

colors.remove("추가한 값") # 리스트 요소 제거
print(colors)

del colors[0] # 리스트 요소 제거
print(colors)

colors.insert(0,"red") # 리스트 요소 원하는 위치에 추가
print(colors)

colors.extend(["indigo", "yellow", "gray"]) # 리스트 요소 여러개 추가
print(colors)

print(colors[0:3]) # 인덱스 슬라이싱([0],[1],[2])
print(colors[-1])
print(colors[:3])
print(colors[0:])
print(colors[0:-1:2])
print("------------------------------")

# lista = [1, "hi", [10, 20, 30]]
# print(lista[2][1])