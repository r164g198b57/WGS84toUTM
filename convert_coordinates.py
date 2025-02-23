from pyproj import Transformer

# Ствараем трансформер для зоны UTM 35U
transformer = Transformer.from_crs("epsg:4326", "epsg:32635", always_xy=True)

while True:
    try:
        # Запытваем у карыстальніка ўвод каардынат
        longitude = float(input("Увядзіце даўгату (градусы, дзесятковыя хвiлiны): "))
        latitude = float(input("Увядзіце шырыню (градусы, дзесятковыя хвiлiны): "))

        # Пераўтвараем каардынаты ў сістэму UTM
        x, y = transformer.transform(longitude, latitude)

        # Выводзім вынік
        print(f"Каардынаты ў сістэме UTM для AutoCAD: X = {x}, Y = {y}")

        # Запыты на паўтор
        repeat = input("Націсніце 'Прабел' для паўтору, альбо 'Enter' для выхаду: ")

        if repeat == '':
            break  # Закрытие программы при нажатии Enter

    except ValueError:
        print("Невірны ўвод! Пераканайцеся, што ўводзеце толькі лічбы для даўгаты і шырыні.")
    except Exception as e:
        print(f"Адбылася памылка: {e}")
