from manim import * 
import numpy as np
class Tute1(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(
            x_range=[-6, 6, 1],
            y_range=[-6, 6, 1],
            z_range=[-6, 6, 1],
            x_length=8,
            y_length=6,
            z_length=6,
        )
        graph = axes.plot(lambda x: x**2, x_range=[-2, 2,1], color=YELLOW)
        rects = axes.get_riemann_rectangles(
            graph=graph, x_range=[-2, 2],
            dx=0.1, 
            stroke_color=WHITE,
        )
        graph2 = axes.plot_parametric_curve(
            lambda t: [np.cos(t), np.sin(t), t],
            t_range=[-2*np.pi, 2*np.pi],
            color = RED,
        )
        self.add(axes, graph)
        self.wait()
        #cho camera quay
        self.move_camera(phi=60 * DEGREES)
        self.wait()
        self.move_camera(theta=45 * DEGREES)
        self.begin_ambient_camera_rotation(
            rate=np.pi/10, about="theta"
        )
        self.wait(2)
        self.play(Create(rects), run_time=2)
        self.wait(2)
        self.play(Create(graph2), run_time=2)
        self.wait(2)
        self.stop_ambient_camera_rotation(
        )
        self.wait()
        self.begin_ambient_camera_rotation(
            rate= np.pi/10, about="phi"
        )        
        self.wait(2)
        self.stop_ambient_camera_rotation(
        )
        
        
        
        
        
        
        
        
        
        