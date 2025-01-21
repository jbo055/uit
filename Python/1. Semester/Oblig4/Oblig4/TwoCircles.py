import tkinter as tk
import math

# Set up the main window
window = tk.Tk()
window.title("Draggable Circles")
window.geometry("400x300")  # Fixed window size
window.resizable(False, False)

class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.id = None  # This will hold the circle's canvas ID for movement

    def is_inside(self, x, y):
        # Check if the point (x, y) is within this circle
        return math.sqrt((self.x - x)**2 + (self.y - y)**2) <= self.radius

    def draw(self, canvas):
        # Draw the circle on the canvas and store the ID for future updates
        self.id = canvas.create_oval(
            self.x - self.radius, self.y - self.radius,
            self.x + self.radius, self.y + self.radius,
            fill = "#F49F0A", outline = "#F08700"
        )

def draw_line_and_distance(canvas, circle1, circle2, line_id, text_id):
    # Calculate distance
    distance = math.sqrt((circle1.x - circle2.x)**2 + (circle1.y - circle2.y)**2)
    
    # Update line between circles
    canvas.coords(line_id, circle1.x, circle1.y, circle2.x, circle2.y)
    
    # Update text label for distance
    canvas.coords(text_id, (circle1.x + circle2.x) / 2, (circle1.y + circle2.y) / 2)
    canvas.itemconfig(text_id, text=f"{int(distance)} px")

def mouse_moved(event):
    # Set canvas boundaries
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()
    
    # Check if the click is within a circle
    if circle1.is_inside(event.x, event.y):
        new_x = min(max(event.x, circle1.radius), canvas_width - circle1.radius)
        new_y = min(max(event.y, circle1.radius), canvas_height - circle1.radius)
        
        # Check if the distance constraint is met
        if math.sqrt((new_x - circle2.x)**2 + (new_y - circle2.y)**2) >= 70:
            circle1.x, circle1.y = new_x, new_y
            canvas.coords(circle1.id, new_x - 20, new_y - 20, new_x + 20, new_y + 20)
            draw_line_and_distance(canvas, circle1, circle2, line_id, text_id)

    elif circle2.is_inside(event.x, event.y):
        new_x = min(max(event.x, circle2.radius), canvas_width - circle2.radius)
        new_y = min(max(event.y, circle2.radius), canvas_height - circle2.radius)

        if math.sqrt((circle1.x - new_x)**2 + (circle1.y - new_y)**2) >= 70:
            circle2.x, circle2.y = new_x, new_y
            canvas.coords(circle2.id, new_x - 20, new_y - 20, new_x + 20, new_y + 20)
            draw_line_and_distance(canvas, circle1, circle2, line_id, text_id)

# Create canvas
canvas = tk.Canvas(window, width=400, height=300)
canvas.pack()

# Create circles
circle1 = Circle(20, 20, 20)
circle2 = Circle(120, 50, 20)
circle1.draw(canvas)
circle2.draw(canvas)

# Draw initial line and distance label
line_id = canvas.create_line(circle1.x, circle1.y, circle2.x, circle2.y, fill="black")
text_id = canvas.create_text((circle1.x + circle2.x) / 2, (circle1.y + circle2.y) / 2, text="0 px")

# Initial distance display
draw_line_and_distance(canvas, circle1, circle2, line_id, text_id)

canvas.bind("<B1-Motion>", mouse_moved)

window.mainloop()


