from manim import *
import random

class Matrix(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            show_basis_vectors=True,
            basis_vector_stroke_width=3,
            leave_ghost_vectors=True,
        )
    def construct(self):
        matrix = [[1,2],[2,1]]
        matrix_tex = MathTex(r"\begin{bmatrix} 1 & 2 \\ 2 & 1 \end{bmatrix}")
        matrix_tex.to_edge(UL).add_background_rectangle()
        
        unit_square = self.get_unit_square()
        text = always_redraw(
            lambda : Tex("Det(A)").set(width=0.7).move_to(unit_square.get_center())
        )
        vector = self.get_vector([1,-2], color=PURPLE)
        rectangle1 = Rectangle(height=2, width=1, color=RED).shift(LEFT*2+UP)
        circle1 = Circle(radius=1, color=BLUE).shift(RIGHT*2+UP)
        self.add_transformable_mobject(vector, unit_square,rectangle1,circle1)
        self.add_background_mobject(matrix_tex, text)
        self.apply_matrix(matrix)
        self.wait(2)
        