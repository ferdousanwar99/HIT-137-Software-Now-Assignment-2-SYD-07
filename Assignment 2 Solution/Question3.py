import turtle

def draw_tree(length, depth, left_angle, right_angle, reduction):
    if depth == 0 or length < 2:
        return
    turtle.forward(length)
    turtle.left(left_angle)
    draw_tree(length * reduction, depth - 1, left_angle, right_angle, reduction)
    turtle.right(left_angle + right_angle)
    draw_tree(length * reduction, depth - 1, left_angle, right_angle, reduction)
    turtle.left(right_angle)
    turtle.backward(length)

def main():
    try:
        left_angle = float(input("Left branch angle: "))
        right_angle = float(input("Right branch angle: "))
        length = float(input("Starting branch length: "))
        depth = int(input("Recursion depth: "))
        reduction = float(input("Branch length reduction factor (e.g., 0.7): "))
    except ValueError:
        print("Error: Invalid input. Expected numbers.")
        return

    screen = turtle.Screen()
    screen.reset()
    turtle.left(90)
    turtle.speed('fastest')
    turtle.delay(0)
    draw_tree(length, depth, left_angle, right_angle, reduction)
    turtle.hideturtle()
    turtle.done()


if __name__ == "__main__":
    main()
