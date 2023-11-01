from manim import *
class Vectors(VectorScene):
    def construct(self):
        plane = self.add_plane(animate=True).add_coordinates()
        vector = self.add_vector([-3, -2], color=YELLOW)
        #basis vector 2 d
        self.add_vector([1, 0], color=BLUE)
        self.add_vector([0, 1], color=BLUE)
        self.vector_to_coords(vector = vector)
        vector2 = self.add_vector([2, 2], color=RED)
        self.write_vector_coordinates(vector = vector2)