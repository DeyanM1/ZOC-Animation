from manim import *


class shrek(Scene):
    def construct(self):
        t1 = Text("SIL", font="Sentient").scale(1.5)
        t2 = Text("Shrek Is love", font="Sentient").scale(1.5)
        
        self.play(Write(t1))
        
        w1 = t2[0:5]
        w2 = t2[5:7]
        w3 = t2[7:]
        
        self.play(ReplacementTransform(t1[0], w1), run_time = 0.75)
        self.play(ReplacementTransform(t1[1], w2), t1[2].animate.shift(RIGHT*0.75), run_time = 0.75)
        self.play(ReplacementTransform(t1[2], w3), run_time = 0.75)

        w1 = t2[0:5]
        w2 = t2[5:7]
        w3 = t2[7:]
        
        self.play(
            w1.animate.to_edge(UL),
            w3.animate.to_edge(DR),
            w2.animate.move_to(ORIGIN) 
        )
        
        u1 = Underline(w1, color = RED)
        u2 = Underline(w2, color = RED)
        u3 = Underline(w3, color = RED)
        
        self.play(GrowFromCenter(u1), ShowPassingFlashWithThinningStrokeWidth(w1))
        
        for i in range(len(w1)):
            self.play(ShrinkToCenter(w1[i]), run_time = 0.15)
        
        self.play(ReplacementTransform(u1, u2), ShowPassingFlashWithThinningStrokeWidth(w2))
        
        for i in range(len(w2)):
            self.play(ShrinkToCenter(w2[i]), run_time = 0.15)
        
        self.play(ReplacementTransform(u2, u3), ShowPassingFlashWithThinningStrokeWidth(w3))
        
        for i in range(len(w3)):
            self.play(ShrinkToCenter(w3[i]), run_time = 0.15)
        
        
        shrek = Text("Shrek is love", font="Sentient").scale(2)
        u4 = Underline(shrek, color=GREEN, sheen_factor = -0.5)
        
        self.play(ReplacementTransform(u3, u4))
        
        
        for i in range(len(shrek)):
            self.play(GrowFromCenter(shrek[i]), run_time = 0.1)
            
        self.play(Flash(shrek[10].get_top(), color=GREEN, line_length=0.8, num_lines=15))
        
        
        
        self.wait(3)