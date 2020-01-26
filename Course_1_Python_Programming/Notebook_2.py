import turtle

'''
forward(X) 	Пройти вперёд X пикселей
backward(X) 	Пройти назад X пикселей
left(X) 	Повернуться налево на X градусов
right(X) 	Повернуться направо на X градусов
penup() 	Не оставлять след при движении
pendown() 	Оставлять след при движении
shape(X) 	Изменить значок черепахи (“arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”)
stamp() 	Нарисовать копию черепахи в текущем месте
color() 	Установить цвет
begin_fill() 	Необходимо вызвать перед рисованием фигуры, которую надо закрасить
end_fill() 	Вызвать после окончания рисования фигуры
width() 	Установить толщину линии
goto(x, y) 	Переместить черепашку в точку (x, y)
'''

turtle.penup()  # Не оставлять след при движении
turtle.goto(-100, 5)  # Переместить черепашку в точку (x, y)
turtle.pendown()  # Не оставлять след при движении

# Рисуем окружность с положительным значением радиуса
turtle.circle(150)

turtle.penup()
turtle.goto(-100, -5)
turtle.pendown()

# Рисуем окружность с отрицательным значением радиуса
turtle.circle(-50)

turtle.penup()
turtle.goto(5, 5)
turtle.pendown()

# Рисуем дугу в 180 градусов с положительным значением
turtle.circle(50, 180)

turtle.penup()
turtle.goto(5, -105)
turtle.pendown()
turtle.seth(0)

# Рисуем дугу в 270 градусов с отрицательным значением
turtle.circle(50, -270)

turtle.penup()
turtle.goto(120, 5)
turtle.pendown()
turtle.seth(0)

# Рисуем пятиугольник
turtle.circle(50, 360, 5)

turtle.penup()
turtle.goto(120, -105)
turtle.pendown()

# Рисуем восьмиугольник
turtle.circle(50, 360, 12)

turtle.mainloop()
