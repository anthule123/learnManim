
from manim import *

class Tute3(Scene):
    def construct(self):
        plane = NumberPlane(x_range=[-5, 5, 1], y_range=[-4, 4, 1],
                            x_length=10, y_length=7)
        plane.add_coordinates()
        plane.shift(RIGHT*2)
        
        vect1 = Line(start = plane.coords_to_point(0,0),
                     end = plane.coords_to_point(3,2), color = YELLOW).add_tip()
        vect1_name = MathTex(r"\vec{v}").next_to(
            vect1, RIGHT,buff=0.1).set_color(YELLOW)
        vect2 = Line(start = plane.coords_to_point(0,0),
                     end = plane.coords_to_point(-2,1), color = RED).add_tip()
        vect2_name = MathTex(r"\vec{u}").next_to(
            vect2, LEFT,buff=0.1).set_color(RED)
        vect3 = Line(start = plane.coords_to_point(3,2),
                     end = plane.coords_to_point(1,3), color = RED).add_tip()
        vect4 = Line(start = plane.coords_to_point(0,0),
                     end = plane.coords_to_point(1,3), color = YELLOW).add_tip()
        vect4_name = MathTex(r"\vec{v}+\vec{u}").next_to(
            vect4, RIGHT,buff=0.1).set_color(YELLOW)
        stuff = VGroup(plane,vect1, vect1_name, vect2, 
                       vect2_name, vect3, vect4, vect4_name)
        box = RoundedRectangle(height=2, width=3, color=BLUE).shift(LEFT*2+UP)
        self.play(DrawBorderThenFill(plane), run_time=2)
        self.wait(0.5)
        self.play(GrowFromPoint(vect1,point= vect1.get_start()),
                  Write(vect1_name),
                  run_time=2)
        #vect2 tương tự
        self.wait(0.5)
        self.play(GrowFromPoint(vect2,point= vect2.get_start()),
                  Write(vect2_name),
                  run_time=2)
        self.play(Transform(vect2, vect3), run_time=2)
        self.play(LaggedStart(GrowFromPoint(vect4,point= vect4.get_start()),
                              Write(vect4_name), run_time=2))
        self.wait(0.5)
        self.add(box)
        self.wait(2)
        self.play(stuff.animate.move_to(box.get_center()).set_width(4), 
                  run_time=2)
        
        
        