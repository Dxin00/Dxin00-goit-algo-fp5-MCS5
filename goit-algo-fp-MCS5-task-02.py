import turtle

def draw_pifagoras_tree(t, length, level, colors):
    if level == 0:
        return
    t.pencolor(colors[level % len(colors)])
    t.forward(length * level)
    t.left(45)
    draw_pifagoras_tree(t, length, level-1, colors)
    t.right(90)
    draw_pifagoras_tree(t, length, level-1, colors)
    t.left(45)
    t.backward(length * level)

def main():
    try:
        level = int(input("Введіть рівень рекурсії для фракталу дерева Піфагора: "))
    except ValueError:
        print("Помилка: Введіть ціле число для рівня рекурсії.")
        return
    
    colors = ["brown", "green", "blue", "orange", "purple"]  # Цвета для разных уровней рекурсии

    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.title("Фрактал дерева Піфагора")

    t = turtle.Turtle()
    t.speed(0)

    t.penup()
    t.goto(0, -250)
    t.pendown()
    t.left(90)

    draw_pifagoras_tree(t, 10, level, colors)

    screen.mainloop()

if __name__ == "__main__":
    main()
