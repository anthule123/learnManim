from manim import *
class GraphingMovement(Scene):
    def construct(self):
        axes = Axes(x_range=[0,5,1],
                    y_range=[0,3,1],
                    x_length=5,
                    y_length=3,
                    axis_config= {"include_tip": True,
                                 "numbers_to_include": [0],}
                    ).add_coordinates()
        axes.to_edge(UR)
        axis_labels = axes.get_axis_labels(x_label="x", y_label="y")
        graph = axes.plot(
            lambda x: x**0.5,
            x_range=[0, 4],
            color=BLUE,
        )
        graphing_stuff = VGroup(axes, axis_labels, graph)
        
        self.play(DrawBorderThenFill(axes), Write(axis_labels))
        self.play
        self.play(graphing_stuff.animate.shift(DOWN*4))
        self.play(axes.animate.shift(LEFT*3), run_time=3)
        
        