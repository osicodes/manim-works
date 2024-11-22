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
        self.wait(3)
