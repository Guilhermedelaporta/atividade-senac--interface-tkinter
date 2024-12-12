import tkinter as tk

class CombinedApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Interface Combinada")
        
        # Frame para a interface de teclas
        self.key_frame = tk.Frame(root)
        self.key_frame.pack(pady=10)
        
        # Componentes da interface de teclas
        tk.Label(self.key_frame, text="Pressione qualquer tecla ou clique no botão").pack(pady=5)
        tk.Button(self.key_frame, text="Clique Aqui", command=self.button_click).pack(pady=5)
        self.key_label = tk.Label(self.key_frame, text="")
        self.key_label.pack(pady=5)
        
        # Canvas para desenho
        self.canvas = tk.Canvas(root, width=800, height=400, bg='white')
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH, padx=10, pady=10)
        
        # Variáveis para o desenho
        self.old_x = None
        self.old_y = None
        
        # Botão para limpar o canvas
        self.clear_button = tk.Button(root, text="Limpar Desenho", command=self.clear_canvas)
        self.clear_button.pack(pady=5)
        
        # Binds de eventos
        self.root.bind('<Key>', self.key_press)
        self.canvas.bind('<B1-Motion>', self.paint)
        self.canvas.bind('<ButtonRelease-1>', self.reset)
    
    def button_click(self):
        self.key_label.config(text="Botão foi clicado!")
    
    def key_press(self, event):
        self.key_label.config(text=f"Tecla pressionada: {event.char}")
    
    def paint(self, event):
        if self.old_x and self.old_y:
            self.canvas.create_line(
                self.old_x, self.old_y, event.x, event.y,
                width=2, fill='black',
                capstyle=tk.ROUND, smooth=tk.TRUE
            )
        self.old_x = event.x
        self.old_y = event.y
    
    def reset(self, event):
        self.old_x = None
        self.old_y = None
    
    def clear_canvas(self):
        self.canvas.delete("all")

if __name__ == "__main__":
    root = tk.Tk()
    app = CombinedApp(root)
    root.mainloop()
