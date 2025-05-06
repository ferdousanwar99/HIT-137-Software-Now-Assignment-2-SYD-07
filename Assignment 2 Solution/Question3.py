import turtle

def draw_branch(length, left_angle, right_angle, depth, reduction_factor, is_root=False):
    if depth == 0:
        return

    if is_root:
        turtle.color("brown")
    else:
        turtle.color("green")
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


def main():
    
    left_angle = float(input("Enter left branch angle (degrees): "))
    right_angle = float(input("Enter right branch angle (degrees): "))
    start_length = float(input("Enter starting branch length (pixels): "))
    depth = int(input("Enter recursion depth: "))
    reduction_factor = float(input("Enter branch length reduction factor (e.g., 0.7): "))

    
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
