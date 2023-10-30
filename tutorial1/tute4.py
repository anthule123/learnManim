
from manim import * 

class Tute4(Scene):
    def construct(self):
        r = ValueTracker(0.5)
        circle = always_redraw(lambda: Circle(radius=r.get_value(),
                                                stroke_color=YELLOW,
                                                stroke_width = 5
                                                )
                                )
        line_radius = always_redraw(lambda:
            Line(start=circle.get_center(),
                 end = circle.get_bottom(),
                 stroke_color=RED,
                 stroke_width=10
                 ))
        line_circumference = always_redraw(lambda:
            Line(stroke_color = YELLOW,
                 stroke_width = 5).set_length(2*PI*r.get_value())
            .next_to(circle, DOWN, buff=0)
                 )
        polygon = always_redraw(lambda:
            Polygon(circle.get_center(),
                    circle.get_right(),
                    circle.get_top(),
                    stroke_color=BLUE,
                    stroke_width=5,
                    fill_color=BLUE,
                    fill_opacity=0.5
                    )
            )
        self.play(LaggedStart(Create(circle),
                              DrawBorderThenFill(line_radius),
                              DrawBorderThenFill(polygon),
                              ),
                              run_time=3, lag_ratio=0.5)
        self.play(ReplacementTransform(circle.copy(), line_circumference),
                  run_time=3)
        self.play(r.animate.set_value(2), run_time=3)
        
        