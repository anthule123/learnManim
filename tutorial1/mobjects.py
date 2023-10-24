from manim import * 

class NameOfAnimation(Scene):
    def construct(self):
        # Code Here
        box = Rectangle(stroke_color=RED,
                        stroke_opacity =0.7,
                        fill_color=RED_C,
                        fill_opacity=0.5,
                        height=1,
                        width=1)
        self.add(box)
        self.play(box.animate.shift(RIGHT*2), run_time=2)
        self.play(box.animate.shift(UP*3), run_time=2)
        self.play(box.animate.shift(LEFT*2 + DOWN), run_time=2)
        self.play(box.animate.shift(UP + RIGHT), run_time=2)
