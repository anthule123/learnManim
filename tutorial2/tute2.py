from manim import *
import numpy as np
class Tute2(Scene):
    def construct(self):
        e = ValueTracker(0.01)
        plane = PolarPlane(radius_max=3).add_coordinates()
        plane.shift(LEFT*2)
        graph1 = always_redraw(lambda: ParametricFunction(
            lambda t: plane.polar_to_point(2*np.sin(8*t), t),
            t_range=[0, e.get_value()],
            
        ))
        dot1 = always_redraw(lambda: Dot(
            fill_color =GREEN, fill_opacity=0.8,
            ).scale(0.5) .move_to(graph1.get_end()))
        axes = Axes(x_range=[0,4,1], x_length=3,
                    y_range=[-3,3,1], y_length=3,)
        axes.shift(RIGHT*4).add_coordinates()
        graph2 = always_redraw(lambda: axes.plot(
            lambda x: 2* np.sin(8*x),
            x_range=[0, e.get_value()],
            #stroke_color=YELLOW,
        ))
        dot2 = always_redraw(lambda: Dot(
            fill_color =YELLOW, fill_opacity=0.8,
            ).scale(0.5) .move_to(graph2.get_end()))
        title = MathTex("r = 2\\sin(8\\theta)").next_to(axes,UP,buff=0.2)
        self.play(LaggedStart(Write(plane), Create(axes),
                              Write(title)), lag_ratio=0.5)
        self.add(graph1, graph2, dot1, dot2)
        self.play(e.animate.set_value(np.pi), run_time=10, rate_func=linear)
        self.wait()