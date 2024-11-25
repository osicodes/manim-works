from manim import *


class VectorInSpace(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(
            x_range=[-6, 6, 1],
            y_range=[-6, 6, 1],
            z_range=[-6, 6, 1],
            x_length=12,
            y_length=12,
            z_length=12,
        )
        labels = axes.get_axis_labels(x_label='x', y_label="y", z_label="z")
        # self.add_fixed_orientation_mobjects(labels)
        self.set_camera_orientation(60*DEGREES, -45*DEGREES, zoom=0.5)

        point = Dot3D([4, 2, 5], color=RED).scale(2)
        originPoint = Dot3D([0, 0, 0], color=DARK_BLUE).scale(2)
        vectorP = Vector(direction=[4, 2, 5])
        p = Tex("P")
        self.add_fixed_orientation_mobjects(p)
        p.next_to(point, RIGHT, buff=0.2)

        '''loc = SVGMobject(
            "assets\images\pin.svg", 
            fill_color=GREEN,
            stroke_color=GREEN,
            ).shift([4, 2, 5.5]).scale(0.2)#.rotate(PI/2, axis=RIGHT)'''
        # self.add_fixed_orientation_mobjects(loc)

        self.play(FadeIn(point))
        self.wait(1)
        self.play(Write(VGroup(axes, labels)))
        self.wait(1)
        '''self.play(Transform(p,loc))
        self.wait(1)'''
        l = Line(originPoint, point, color=YELLOW)
        self.add(VGroup(originPoint, l))
        self.wait(1)

        pointXLine = DashedLine([4, 0, 0], [4, 2, 0], color=GRAY)
        pointYLine = DashedLine([0, 2, 0], [4, 2, 0], color=GRAY)
        pointZLine = DashedLine([4, 2, 0], [4, 2, 5], color=GRAY)

        labelx = MathTex("a_x", font_size=30,
                         color=BLUE).set_shade_in_3d(True)
        # self.add_fixed_in_frame_mobjects(text3d)
        self.add_fixed_orientation_mobjects(labelx)
        labelx.next_to(pointXLine, RIGHT)

        labely = MathTex("b_y", font_size=30,
                         color=RED).set_shade_in_3d(True)
        self.add_fixed_orientation_mobjects(labely)
        labely.next_to(pointYLine, UP)

        labelz = MathTex("c_z", font_size=30,
                         color=GREEN).set_shade_in_3d(True)
        self.add_fixed_orientation_mobjects(labelz)
        labelz.next_to(pointZLine, RIGHT)

        self.play(Create(VGroup(pointXLine, pointYLine,
                                pointZLine, labelx, labely, labelz)))

        self.wait(2)

        vectorX = Arrow(
            [4, 0, 0], [4, 2, 0],
            color=BLUE,
        )
        vectorY = Arrow(
            [0, 2, 0], [4, 2, 0],
            color=RED,
        )
        vectorZ = Arrow(
            [4, 2, 0], [4, 2, 5],
            color=GREEN,
        )
        self.play(Create(VGroup(vectorX, vectorY, vectorZ)))

        self.wait(2)

        pointP = Tex("P")
        self.add_fixed_in_frame_mobjects(pointP)
        pointP.to_corner(UL)

        self.begin_ambient_camera_rotation()
        self.play(Write(pointP))

        
        coordP = MathTex("(", "a_x, ", "b_y, ", "a_x", ")")
        coordP[1].set_color(BLUE)
        coordP[2].set_color(RED)
        coordP[3].set_color(GREEN)
        
        self.add_fixed_in_frame_mobjects(coordP)
        coordP.next_to(pointP)#.arrange(RIGHT)
        self.play(Write(coordP))

        self.wait(2)

        self.play(FadeOut(l))
        self.wait(1)

        self.play(Create(vectorP))
        self.wait(1)

        p2 = pointP.copy()
        self.add_fixed_in_frame_mobjects(p2)
        self.play(ApplyMethod(p2.next_to, pointP, DOWN))

        equal = Tex("=")
        
        m1 = MathTex(r"\begin{bmatrix} a_x \\ b_y \\ c_z \end{bmatrix}")
        self.add_fixed_in_frame_mobjects(VGroup(equal, m1))
        equal.next_to( p2, RIGHT)
        m1.next_to(equal, RIGHT + DOWN * 0.003) 
        self.play(Write(VGroup(equal, m1)))
        self.wait(2)
        
        px=MathTex("P_x", color=BLUE)
        py=MathTex("P_y", color=RED)
        pz=MathTex("P_z", color=GREEN)
        w=MathTex("w", color=YELLOW)
        
        m2 = MobjectMatrix([[px], [py], [pz], [w]])
        self.add_fixed_in_frame_mobjects(m2)
        m2.next_to(p2, DOWN * 8 + RIGHT * 0.003)
        self.play(TransformFromCopy(m1, m2))
        # self.play(ApplyMethod(p2.shift, [4, 2, 3]))
        # self.play(ApplyMethod(p2.next_to, axes))

        self.wait(2)
        
        self.play(FadeOut(VGroup(axes, p, vectorP, vectorX, vectorY, vectorZ,pointXLine, pointYLine,
                                pointZLine, labelx, labely, labelz, labels, point, originPoint)))
        self.wait(2)
        pxcopy = m2[0].copy()
        pycopy = m2[1].copy()
        pzcopy = m2[2].copy()
        wcopy = m2[3].copy()
        self.wait(2)
