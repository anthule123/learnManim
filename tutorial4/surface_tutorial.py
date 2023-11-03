
from manim import*
import numpy as np
class SurfaceTutorial(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES,
                                    theta=-45 * DEGREES)
        axes = ThreeDAxes()
        graph = axes.plot(
            lambda x:x**2,
            x_range=[-2, 2],
            color=YELLOW
        )
        surface =  Surface(
            func= lambda u, v: np.array([
                v*np.cos(u),
                v*np.sin(u),
                0.5*v**2
            ]),
            u_range=[0,2*np.pi],
            v_range=[0,3],
            resolution=(10, 32),
            checkerboard_colors=[GREEN,RED]
        )
        three_d_stuff = VGroup(axes, graph,surface)
        self.add(axes,graph)
        self.begin_ambient_camera_rotation(rate=np.pi/20)
        self.play(Create(surface))
        self.play(three_d_stuff.animate.shift(LEFT*5))