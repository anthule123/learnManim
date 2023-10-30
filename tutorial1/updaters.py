from manim import * 

class Updaters(Scene):
    def construct(self):
        rectangle = Rectangle(height=2, width=3).shift(LEFT*3+UP*2)
        mathtext = MathTex("\\frac{3}{4}=0.75").set_color_by_gradient
        (RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)
        mathtext.move_to(rectangle.get_center())
        mathtext.add_updater(lambda x: x.move_to(rectangle.get_center()))
        self.play(FadeIn(rectangle), Write(mathtext))
        self.play(rectangle.animate.shift(RIGHT*6), run_time=3)
        self.wait(1)
        mathtext.clear_updaters()
        self.play(rectangle.animate.shift(LEFT*6+UP*2), run_time=3)
        