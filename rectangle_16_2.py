from rectangle_16 import Rectangle, Square, Circle

# Создаем два прямоугольника
rect_1 = Rectangle(3,4)
rect_2 = Rectangle(12,5)

# Вывод площади прямогольников
print("S первого прямоугольника: ", rect_1.get_area(),
      "S второго прямоугольника: ", rect_2.get_area())

# Создаем два квадрата
square_1 = Square(5)
square_2 = Square(10)

# Вывод площади квадратов
print("S первого квадрата: ",square_1.get_area_square(),
      "S второго квадрата: ",square_2.get_area_square())

# Создаем два круга
circle_1 = Circle(2)
circle_2 = Circle(10)

# Вывод площади кругов
print("S первого круга: ",circle_1.get_area_circle(),
      "S второго круга: ",circle_2.get_area_circle())


figures = [rect_1, rect_2, square_1, square_2, circle_1, circle_2]

for figure in figures:
    if isinstance(figure, Circle):
        print(figure.get_area_circle())
    elif isinstance(figure, Square):
        print(figure.get_area_square())
    else:
        print(figure.get_area())