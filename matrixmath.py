# https://www.youtube.com/watch?v=_IM9Eb4m7hY

from manim import *

class MatrixMath(Scene):
    def construct(self):
        t = Tex("Kernel Matrix", font_size=45, color=BLUE)
        self.play(Write(t))
        self.wait(1)
        self.play(t.animate.shift(UP * 3))
        self.wait(1)
        
        m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.play(Write(m1))
        self.wait(1)
        sr = SurroundingRectangle(m1.get_columns()[1])
        self.play(Write(sr))
        self.play(sr.animate.to_edge(),m1.get_columns()[1].animate.to_edge())
        self.wait(1)