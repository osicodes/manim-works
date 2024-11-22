from manim import *

class VectorDisplay(VectorScene):
    def construct(self):

        myaxis = Axes(
            x_range=[-5,5,1],
            y_range=[-5,5,1],
            x_length=10,
            y_length=10,
        )
        self.add(myaxis)
        
        myvec = Vector([3, 2])
        self.add_vector(myvec) # draws the vector on the plane
        self.write_vector_coordinates(myvec) # draws cordinated of the vector
        
        self.label_vector(myvec,"myvector") # draws label of the vector
        self.wait(3)
        self.play(FadeOut(myaxis,myvec))

        plane = NumberPlane().add_coordinates()
        vector_1 = Vector([1,2]) 
        vector_2 = Vector([-5,-2]) 
        self.add(plane, vector_1, vector_2)
        self.wait(3)



class VectorRotation(VectorScene):
    def construct(self):
        myplane = NumberPlane()
        vec = Vector([3,2])
        self.add(myplane, vec)
        self.play(
            Rotate(
                vec, 
                angle=3*PI/4,
                about_point=ORIGIN
            ),
            subcaption_duration=3
        )
        self.wait(3)
        

class Vector3dRotation(ThreeDScene):
    def construct(self):

        axes = ThreeDAxes(
            x_range=[-6,6,1],
            y_range=[-6,6,1],
            z_range=[-6,6,1],
            x_length=12,
            y_length=12,
            z_length=12,
        )
        
        mycurve = CurvedArrow([1, 2, 3],[-1, -2, 3])
        mydot = Dot3D([1, 2, 3],color=RED_A)
        myvec = Vector(direction=[1, 2, 3])
        # self.add(axes,myvec,mydot,mycurve)
        self.play(Create(VGroup(axes,myvec,mydot,mycurve)))
        self.move_camera(60*DEGREES,-45*DEGREES)
        self.wait(2)
        self.play(
            [Rotate(
                myvec, 
                angle=3*PI/2,
                about_point=[0,0,1]
            ),Rotate(
                mydot, 
                angle=3*PI/2,
                about_point=[0,0,1]
            )],
            subcaption_duration=5
        )
        self.wait(3)

        curve = ParametricFunction(
            lambda u: ( 1.2 * np.cos(u), np.sin(u), u * 0.05 ), 
            color=RED, 
            t_range = (-3*TAU, 5*TAU, 0.01) 
        ).set_shade_in_3d(True)
        self.add(curve)