import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.title("Understanding Pi (π) with Turtle")
screen.bgcolor("white")

# Set up the turtle
pen = turtle.Turtle()
pen.speed(1)
pen.pensize(2)

# Draw a circle
radius = 100
pen.penup()
pen.goto(0, -radius)
pen.pendown()
pen.circle(radius)

# Draw the diameter
pen.penup()
pen.goto(-radius, 0)
pen.pendown()
pen.goto(radius, 0)

# Annotate the diameter
pen.penup()
pen.goto(-radius, -20)
pen.write("Diameter = 2r", align="center", font=("Arial", 12, "normal"))

# Calculate the circumference
circumference = 2 * math.pi * radius

# Move to the start point for circumference demonstration
pen.penup()
pen.goto(0, -radius)
pen.pendown()
pen.pencolor("red")

# Draw the circumference in segments to show it visually
num_segments = 100  # More segments for smoother circle
segment_length = circumference / num_segments

for _ in range(num_segments):
    pen.forward(segment_length)
    pen.left(360 / num_segments)

# Annotate the circumference
pen.penup()
pen.goto(0, radius + 20)
pen.pendown()
pen.pencolor("black")
pen.write(f"Circumference = 2πr ≈ {circumference:.2f}", align="center", font=("Arial", 12, "normal"))

# Keep the window open until it is closed by the user
turtle.done()
