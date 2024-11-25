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
        vectorP = Arrow(
            [0, 0, 0], [4, 2, 5],
            color=GOLD, tip_shape=StealthTip, buff=0.3
        )  # Vector(direction=[4, 2, 5])
        p = Tex("P")
        self.add_fixed_orientation_mobjects(p)
        p.next_to(point, RIGHT, buff=0.2)

        # loc = SVGMobject(
        #     "assets\images\pin.svg",
        #     fill_color=GREEN,
        #     stroke_color=GREEN,
        #     ).shift([4, 2, 5.5]).scale(0.2)#.rotate(PI/2, axis=RIGHT)
        # self.add_fixed_orientation_mobjects(loc)

        self.play(FadeIn(point))
        self.wait(2)
        self.play(Write(VGroup(axes, labels)), run_time=2)
        self.wait(2)
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

        self.wait(3)

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
        self.play(Create(VGroup(vectorX, vectorY, vectorZ)), run_time=4)

        self.wait(3)

        # Point P and cordinates
        pointP = Tex("P")
        self.add_fixed_in_frame_mobjects(pointP)
        pointP.to_corner(UL)

        self.begin_ambient_camera_rotation()
        self.play(Write(pointP), run_time=2)

        coordP = MathTex("(", "a_x, ", "b_y, ", "c_z", ")")
        coordP[1].set_color(BLUE)
        coordP[2].set_color(RED)
        coordP[3].set_color(GREEN)

        self.add_fixed_in_frame_mobjects(coordP)
        coordP.next_to(pointP)
        self.play(Write(coordP))

        self.wait(4)

        self.play(FadeOut(l))
        self.wait(2)

        self.play(Create(vectorP), run_time=3)
        self.wait(1)

        # p2 = pointP.copy()
        p2 = MathTex(r"\overrightarrow{P}")
        self.add_fixed_in_frame_mobjects(p2)
        p2.next_to(pointP, DOWN * 4)
        self.play(TransformFromCopy(pointP,p2))

        equal = Tex("=")

        m1 = MathTex(r"\begin{bmatrix} a_x \\ b_y \\ c_z \end{bmatrix}")[0]
        m1[2:4].set_color(BLUE)
        m1[4:6].set_color(RED)
        m1[6:8].set_color(GREEN)

        self.add_fixed_in_frame_mobjects(VGroup(equal, m1))
        equal.next_to(p2, RIGHT)
        m1.next_to(equal, RIGHT)
        self.play(Write(VGroup(equal, m1)))
        self.wait(5)

        px = MathTex("P_x", color=BLUE)[0]
        py = MathTex("P_y", color=RED)[0]
        pz = MathTex("P_z", color=GREEN)[0]
        w = MathTex("w", color=YELLOW)[0]
        self.add_fixed_in_frame_mobjects(VGroup(px, py, pz, w))

        m2 = MobjectMatrix([[px], [py], [pz], [w]])
        self.add_fixed_in_frame_mobjects(m2)
        m2.next_to(p2, DOWN * 8 + RIGHT * 0.003)
        self.play(Write(m2), run_time=3)

        self.play(FadeOut(VGroup(axes, p, vectorP, vectorX, vectorY, vectorZ,pointXLine, pointYLine,
                                pointZLine, labelx, labely, labelz, labels, point, originPoint)))
        self.wait(1)

        m2x = px[0:2].copy()
        m2y = py[0:2].copy()
        m2z = pz[0:2].copy()
        m2w = w[0:2].copy()

        self.add_fixed_in_frame_mobjects(VGroup(m2x, m2y, m2z, m2w))

        axcopy = coordP[1].copy()
        bycopy = coordP[2].copy()
        czcopy = coordP[3].copy()

        axfrac = MathTex(r"\frac{p_x}{w}")[0]
        byfrac = MathTex(r"\frac{p_y}{w}")[0]
        czfrac = MathTex(r"\frac{p_z}{w}")[0]

        axfrac[0:2].set_color(BLUE)
        axfrac[3].set_color(YELLOW)
        byfrac[0:2].set_color(RED)
        byfrac[3].set_color(YELLOW)
        czfrac[0:2].set_color(GREEN)
        czfrac[3].set_color(YELLOW)

        result = VGroup(axfrac, equal.copy(), axcopy, byfrac,
                        equal.copy(), bycopy, czfrac, equal.copy(), czcopy)
        self.add_fixed_in_frame_mobjects(result)
        result.arrange(RIGHT).next_to(m2, RIGHT * 2)

        self.play(Write(result), run_time=3)
        self.wait(2)
        
        # Curved arrow        
        points = [
            axcopy.get_top(),
            bycopy.get_top(),
            czcopy.get_top(),
            coordP.get_right()
        ]
        
        carrows = VGroup(
            CurvedArrow(points[0], points[3], color=RED, tip_shape=StealthTip),
            CurvedArrow(points[1], points[3], color=RED, tip_shape=StealthTip),
            CurvedArrow(points[2], points[3], color=RED, tip_shape=StealthTip)
        )
        self.add_fixed_in_frame_mobjects(carrows)
        self.play(Create(carrows))
        self.wait(2)
