from manim import *

class FittingObjects(Scene):
    def construct(self):
        axes = Axes(x_range=[-3, 3, 1], y_range=[-3, 3, 1],
                    x_length=10, y_length=6)
        axes.to_edge(LEFT, buff=0.5)
        circle = Circle ( stroke_width = 6,
                         stroke_color = YELLOW,
                         fill_color = BLUE,
                         fill_opacity = 0.8,
        )
        circle.set_width(2).to_edge(DR, buff=0.5)
        triangle = Triangle ( stroke_width =10,
                             stroke_color = RED,
                                fill_color = GREEN, 
                                
        ).set_height(2).shift(DOWN*2 + RIGHT*3)
        self.play(Write(axes))
        self.play(DrawBorderThenFill(circle))
        #self.play(DrawBorderThenFill(triangle))
        self.play(Transform(circle, triangle), run_time=3)
                        
                        