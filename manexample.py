from manim import *


class SquareToCircleEmbed(Scene):
    def construct(self):
        text = Text("osinachi leanrs maths")
        self.play(Write(text))
        self.wait(3)

class Formula(Scene):
    def construct(self):
        t = MathTex(r"\int_a^b f'(x) dx = f(b)- f(a)")
        self.play(Write(t))
        self.wait(1)
        
        # coordP = Tex("( a_x b_y c_z )")
        coordP = MathTex("(", "a_x, ", "b_y, ", "a_x", ")")
        coordP[1].set_color(BLUE)
        coordP[2].set_color(RED)
        coordP[3].set_color(GREEN)
        
        # self.add_fixed_in_frame_mobjects(coordP)
        coordP.next_to(t)#.arrange(RIGHT)
        self.play(Write(coordP))
        self.wait(3)

class CurvedArrowScene(Scene):
    def construct(self):
        # Define the start and end points
        start_point = [1, 2, 3]
        end_point = [-1, -2, 3]

        # Create a curved arrow
        curved_arrow = CurvedArrow(
            start_point=start_point,
            end_point=end_point,
            color=BLUE
        )

        # Add the arrow to the scene
        self.play(Create(curved_arrow))
        self.wait()

