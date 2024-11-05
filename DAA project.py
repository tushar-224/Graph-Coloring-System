class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def greedy_coloring(self):
        result = [-1] * self.V
        result[0] = 0
        available = [True] * self.V

        for u in range(1, self.V):
            for i in self.graph[u]:
                if result[i] != -1:
                    available[result[i]] = False

            cr = 0
            while cr < self.V:
                if available[cr]:
                    break
                cr += 1

            result[u] = cr
            available = [True] * self.V

        return result

import tkinter as tk
from tkinter import simpledialog

class GraphVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Graph Coloring Visualizer")
        self.canvas = tk.Canvas(root, width=600, height=400, bg="white")
        self.canvas.pack()

        self.graph = Graph(0)
        self.vertices = {}
        self.vertex_count = 0

        self.create_widgets()

    def create_widgets(self):
        control_frame = tk.Frame(self.root)
        control_frame.pack()

        add_vertex_button = tk.Button(control_frame, text="Add Vertex", command=self.add_vertex)
        add_vertex_button.pack(side=tk.LEFT)

        add_edge_button = tk.Button(control_frame, text="Add Edge", command=self.add_edge)
        add_edge_button.pack(side=tk.LEFT)

        color_button = tk.Button(control_frame, text="Color Graph", command=self.color_graph)
        color_button.pack(side=tk.LEFT)

    def add_vertex(self):
        x, y = simpledialog.askinteger("Input", "X-coordinate:"), simpledialog.askinteger("Input", "Y-coordinate:")
        if x is not None and y is not None:
            self.graph.V += 1
            self.graph.graph.append([])
            self.vertices[self.vertex_count] = (x, y)
            self.canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="white")
            self.canvas.create_text(x, y, text=str(self.vertex_count))
            self.vertex_count += 1

    def add_edge(self):
        u, v = simpledialog.askinteger("Input", "First vertex:"), simpledialog.askinteger("Input", "Second vertex:")
        if u is not None and v is not None and u in self.vertices and v in self.vertices:
            self.graph.add_edge(u, v)
            x1, y1 = self.vertices[u]
            x2, y2 = self.vertices[v]
            self.canvas.create_line(x1, y1, x2, y2)

    def color_graph(self):
        colors = ["red", "blue", "green", "yellow", "orange", "purple", "brown", "pink"]
        result = self.graph.greedy_coloring()
        for u, color in enumerate(result):
            x, y = self.vertices[u]
            self.canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill=colors[color])
            self.canvas.create_text(x, y, text=str(u), fill="black")

if __name__ == "__main__":
    root = tk.Tk()
    app = GraphVisualizer(root)
    root.mainloop()

