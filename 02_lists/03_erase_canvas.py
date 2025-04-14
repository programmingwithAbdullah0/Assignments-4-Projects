# Implement an 'eraser' on a canvas.

# The canvas consists of a grid of blue 'cells' which are drawn as rectangles on the screen. We then create an eraser rectangle which, when dragged around the canvas, sets all of the rectangles it is in contact with to white.

from graphics import Canvas  # type: ignore
import time
    
# Dimensions for the canvas
CANVAS_WIDTH : int = 400
CANVAS_HEIGHT : int = 400

# Size of each cell in the grid
CELL_SIZE : int = 40

# Size of the eraser
ERASER_SIZE : int = 20

def erase_objects(canvas, eraser):
    """Erase objects that the eraser is touching"""
    # Get the mouse position to find out which cells need to be erased
    mouse_x = canvas.get_mouse_x()
    mouse_y = canvas.get_mouse_y()
    
    # Calculate the position of the eraser on the canvas
    left_x = mouse_x
    top_y = mouse_y
    right_x = left_x + ERASER_SIZE
    bottom_y = top_y + ERASER_SIZE
    
    # Find all objects that overlap with the eraser's area
    overlapping_objects = canvas.find_overlapping(left_x, top_y, right_x, bottom_y)
    
    # For every object that overlaps with the eraser (except the eraser itself), change the color to white (erase it)
    for overlapping_object in overlapping_objects:
        if overlapping_object != eraser:
            canvas.set_color(overlapping_object, 'white')

# This part handles the main program logic
def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)  # Create the canvas with the given width and height
    
    # Determine how many rows and columns of cells are needed for the canvas size
    num_rows = CANVAS_HEIGHT // CELL_SIZE
    num_cols = CANVAS_WIDTH // CELL_SIZE
    
    # Create a grid of blue cells by iterating through rows and columns
    for row in range(num_rows):
        for col in range(num_cols):
            left_x = col * CELL_SIZE
            top_y = row * CELL_SIZE
            right_x = left_x + CELL_SIZE
            bottom_y = top_y + CELL_SIZE
            
            # Create each individual cell in the grid
            cell = canvas.create_rectangle(left_x, top_y, right_x, bottom_y, 'blue')
    
    canvas.wait_for_click()  # Wait for the user to click to start creating the eraser
    
    last_click_x, last_click_y = canvas.get_last_click()  # Get the position where the user clicked to place the eraser
    
    # Create the eraser rectangle at the clicked position
    eraser = canvas.create_rectangle(
        last_click_x, 
        last_click_y, 
        last_click_x + ERASER_SIZE, 
        last_click_y + ERASER_SIZE, 
        'pink'  # Initial color of the eraser
    )
    
    # Start the eraser movement and erasing process
    while True:
        # Get the current position of the mouse and move the eraser accordingly
        mouse_x = canvas.get_mouse_x()
        mouse_y = canvas.get_mouse_y()
        canvas.moveto(eraser, mouse_x, mouse_y)
        
        # Erase any cells the eraser is touching
        erase_objects(canvas, eraser)
        
        # Add a small delay to make the movement smoother
        time.sleep(0.05)

# Run the main function if this file is executed
if __name__ == '__main__':
    main()



#---------------------- NOT COMPLETE NOW -------------------------#

