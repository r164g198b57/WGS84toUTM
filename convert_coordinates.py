from pyproj import Proj, transform

# Ствараем праекцыі
wgs84 = Proj(init="epsg:4326")  # Геаграфічная сістэма WGS84
utm = Proj(init="epsg:32633")   # UTM зона 33N для Беларусі

# Запытваем у карыстальніка ўвод каардынат
longitude = float(input("Увядзіце даўгату: "))
latitude = float(input("Увядзіце шырыню: "))

# Пераўтвараем каардынаты
x, y = transform(wgs84, utm, longitude, latitude)

# Выводзім вынік
print(f"Каардынаты ў сістэме UTM: X = {x}, Y = {y}")

# Дадаем затрымку, каб акно не закрывалася
input("Націсніце Enter для закрыцця праграмы...")
