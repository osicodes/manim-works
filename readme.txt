
# -p = play, -ql = low quality, scene.py = script, SquareToCircle = Scene in script
manim -pql scene.py SquareToCircle

-ql -> low (854x480 15FPS)
-qm -> medium (1280x720 30FPS)
-qh -> high (1920x1080 60FPS)
-qp -> 2k (2560x1440 60FPS)
-qk -> 4k (3840x2160 60FPS)

For videos to be created for each section you have to add the --save_sections flag to the Manim call like this:
manim --save_sections scene.py
**example**
manim --save_sections -pql squareToCircle.py AnimatedSquareToCircle

If your file contains multiple Scene classes, and you want to render them all, you can use the -a flag
manim -pqh -a squareToCircle.py