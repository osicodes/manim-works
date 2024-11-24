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

        # Define a parametric curve for the arrow's path
        def parametric_curve(t):
            # Parametric function that creates a curve
            return np.array([np.cos(t), np.sin(t), 3])

        # Create the curve using ParametricFunction
        mycurve = ParametricFunction(
            parametric_curve,
            t_range=np.array([0, 3*PI/2, PI/180]),  # Parameter range for the curve
            color=BLUE,
            stroke_width=4,
        )
        mydot = Dot3D([1, 0, 3],color=RED_A)
        myvec = Vector(direction=[1, 0, 3])
        # self.add(axes,myvec,mydot,mycurve)
        self.play(Create(VGroup(axes,myvec,mydot)))
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
            ),Create(mycurve)],
            run_time=5
        )
        self.wait(3)

        # curve = ParametricFunction(
        #     lambda u: ( 1.2 * np.cos(u), np.sin(u), u * 0.05 ), 
        #     color=RED, 
        #     t_range = (-3*TAU, 5*TAU, 0.01) 
        # )
        # self.add(curve)
        
        
        
class CurvedArrow3DScene(ThreeDScene):
    def construct(self):
        # Set up the 3D camera
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)

        # Define start and end points in 3D
        start_point = [1, 2, 3]
        end_point = [-1, -2, 3]

        # Create a 3D curved arrow using a bezier curve and an arrowhead
        curve = CubicBezier(
            start_point,
            [1, 3, 4],  # Control point 1 for the curve
            [-1, -3, 4],  # Control point 2 for the curve
            end_point,
            color=BLUE,
        )
        # arrow_head = Arrow(end_point - 0.3 * normalize(end_point - start_point), end_point, color=BLUE)

        # Group the curve and arrowhead together
        # curved_arrow = VGroup(curve, arrow_head)

        # Add the curved arrow to the scene
        # self.add(curved_arrow)
        self.play(Create(curve))
        self.wait(2)
        


class Curved2Arrow3DScene(ThreeDScene):
    def construct(self):
        # Set up the 3D camera
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)

        # Define start and end points
        start_point = np.array([1, 2, 3])
        end_point = np.array([-1, -2, 3])

        # Define a parametric curve for the arrow's path
        def parametric_curve(t):
            # Parametric function that creates a curve
            return (1 - t) * start_point + t * end_point + np.array([0, 0, 2 * np.sin(PI * t)])

        # Create the curve using ParametricFunction
        curve = ParametricFunction(
            parametric_curve,
            t_range=np.array([0, 1]),  # Parameter range for the curve
            color=BLUE,
            stroke_width=4,
        )

        # Create the arrowhead at the end of the curve
        arrow_head = Arrow(
            start=parametric_curve(0.95),  # A point slightly before the end
            end=parametric_curve(1),
            buff=0,
            color=BLUE,
        )

        # Group the curve and arrowhead together
        curved_arrow = VGroup(curve, arrow_head)

        # Add the curved arrow to the scene
        self.play(Create(curved_arrow))
        self.wait(2)

