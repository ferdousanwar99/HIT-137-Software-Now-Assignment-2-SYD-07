import turtle


def draw_branch(length, left_angle, right_angle, depth, reduction_factor, is_root=False):
    if depth == 0:
        return

    
    turtle.color("brown" if is_root else "green")

    turtle.pensize(depth + 2 if is_root else depth + 1)

    turtle.forward(length)

   
    current_pos = turtle.position()
    current_heading = turtle.heading()

    
    turtle.left(left_angle)
    draw_branch(length * reduction_factor, left_angle, right_angle, depth - 1, reduction_factor)

    
    turtle.setposition(current_pos)
    turtle.setheading(current_heading)

    
    turtle.right(right_angle)
    draw_branch(length * reduction_factor, left_angle, right_angle, depth - 1, reduction_factor)

    
    turtle.setposition(current_pos)
    turtle.setheading(current_heading)


def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Degrees must be numeric values (e.g., 30, 31.5). Please try again.")

def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Degrees must be numeric values (e.g., 30, 31.5). Please try again.")


def main():
    
    left_angle = get_float_input("Left branch angle (degrees): ")
    right_angle = get_float_input("Right branch angle (degrees): ")
    start_length = get_float_input("Starting branch length (pixels): ")
    depth = get_int_input("Recursion depth: ")
    reduction_factor = get_float_input("Branch length reduction factor: ")

   
    turtle.speed("fastest")
    turtle.left(90)
    turtle.penup()
    turtle.goto(0, -250)
    turtle.pendown()
    turtle.pensize(depth + 3)  

    
    draw_branch(start_length, left_angle, right_angle, depth, reduction_factor, is_root=True)

    turtle.hideturtle()
    turtle.done()


if __name__ == "__main__":
    main()
