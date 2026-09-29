import math
# 1. Ввод радиуса с клавиатуры
radius_cm = float(input("Введите радиус круга в сантиметрах: "))
pi = 3.14
radius_m = radius_cm / 100

# 2. Вычисление длины окружности и площади круга
circumference_cm = 2 * pi * radius_cm
circumference_m = 2 * pi * radius_m
area_cm2 = pi * (radius_cm ** 2)
area_m2 = pi * (radius_m ** 2)

# 3. Стороны вписанных фигур
#Для квадрата: a = R * sqrt(2)
in_square_cm = radius_cm * math.sqrt(2)
in_square_m = radius_m * math.sqrt(2)

#3.1 Для равностороннего треугольника: a = R * sqrt(3)
in_triangle_cm = radius_cm * math.sqrt(3)
in_triangle_m = radius_m * math.sqrt(3)

# 4. Стороны описанных фигур
#Для квадрата: a = 2 * R
out_square_cm = 2 * radius_cm
out_square_m = 2 * radius_m

#4.1 Для равностороннего треугольника: a = 2 * R * sqrt(3)
out_triangle_cm = 2 * radius_cm * math.sqrt(3)
out_triangle_m = 2 * radius_m * math.sqrt(3)

#4.2 Для правильного восьмиугольника: a = 2 * R * tg(180/8) = 2 * R * (sqrt(2) - 1)
octagon_cm = 2 * radius_cm * math.tan(math.pi / 8)
octagon_m = 2 * radius_m * math.tan(math.pi / 8)


#5. Вывод результатов
print("\n--- Результаты расчетов ---")
print(f"3. Длина окружности: {circumference_cm:.2f} см | {circumference_m:.2f} м")
print(f"   Площадь круга:    {area_cm2:.2f} кв. см | {area_m2:.4f} кв. м")

print(f"\n4. Стороны вписанных фигур:")
print(f"   Квадрат:          {in_square_cm:.2f} см | {in_square_m:.4f} м")
print(f"   Треугольник:      {in_triangle_cm:.2f} см | {in_triangle_m:.4f} м")

print(f"\n5. Стороны описанных фигур:")
print(f"   Квадрат:          {out_square_cm:.2f} см | {out_square_m:.4f} м")
print(f"   Треугольник:      {out_triangle_cm:.2f} см | {out_triangle_m:.4f} м")
print(f"   Восьмиугольник:   {octagon_cm:.2f} см | {octagon_m:.4f} м")
