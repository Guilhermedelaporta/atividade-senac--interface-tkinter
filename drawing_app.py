import tkinter as tk

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Drawing App")
        
        # Create canvas
        self.canvas = tk.Canvas(root, width=800, height=600, bg='white')
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)
        
        # Variables to store previous coordinates
        self.old_x = None
        self.old_y = None
        
        # Bind mouse events
        self.canvas.bind('<B1-Motion>', self.paint)  # Left mouse button motion
        self.canvas.bind('<ButtonRelease-1>', self.reset)
        
        # Create clear button
        self.clear_button = tk.Button(root, text="Clear Canvas", command=self.clear_canvas)
        self.clear_button.pack()

    def paint(self, event):
        if self.old_x and self.old_y:
            self.canvas.create_line(self.old_x, self.old_y, event.x, event.y,
                                  width=2, fill='black',
                                  capstyle=tk.ROUND, smooth=tk.TRUE)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x = None
        self.old_y = None

    def clear_canvas(self):
        self.canvas.delete("all")

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()
