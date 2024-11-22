from manim import *

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.rotate(PI / 4)  # rotate a certain amount

        self.play(Create(square))  # animate the creation of the square
        self.wait(3)
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.wait(6)
        self.play(FadeOut(square))  # fade out animation

class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency

        square = Square()  # create a square
        square.set_fill(BLUE, opacity=0.5)  # set the color and transparency

        square.next_to(circle, UP, buff=0.5)  # set the position
        self.play(Create(circle), Create(square))  # show the shapes on screen. Creates both at the same time
        self.wait(6)
        self.play(FadeOut(square))  # fade out animation

class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_color(BLUE) # sets the circle's outline colour
        square = Square()  # create a square
        square.set_color(YELLOW) # sets the square's outline colour
        triangle = Triangle()  # create a triangle
        triangle.set_color(RED_A) # sets the triangle's outline colour
        triangle.shift(2 * RIGHT) # position the triangle twice to the right of the origin
        rectangle = Rectangle(PURPLE)

        self.play(Create(square))  # show the square on screen
        self.play(square.animate.rotate(PI / 4))  # rotate the square. The original square and the new square are interpolated, so during the animation, the original square contracts slightly.
        self.play(Rotate(square, angle=PI / 4))  # rotate the square. The original square rotates without contracting.
        self.play(square.animate.flip())  # rotate the square
        self.play(Transform(square, circle))  # transform the square into a circle
        self.play(square.animate.set_fill(GREEN, opacity=0.5))  # color the circle on screen
        self.play(square.animate.shift(LEFT)) # shifts the circle to the left
        self.wait(3)
        self.play(Transform(circle,triangle))
        self.play(FadeOut(square),FadeOut(circle))  # fade out animation at same time
        
        self.next_section("Rectangle section") # a separate video for the new section is created
        self.play(Create(rectangle)) # draws the rectangle on the screen
        self.wait(2)
        self.play(FadeOut(rectangle))
        self.add(rectangle) # pops/shows the rectangle on the screen
        self.wait(2)