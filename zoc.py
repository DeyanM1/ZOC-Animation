from manim import *

class FirstScene(Scene):
    def construct(self):
        title = Text("FC", font="Rockwell").scale(1.5)
        title_ext = Text("Future Crafts", font="Rockwell").scale(1.5)
        
        self.play(Write(title))
        
        title_word1 = title_ext[0:6]
        title_word2 = title_ext[6:]
        
        self.play(
            ReplacementTransform(title[0], title_word1),
            ReplacementTransform(title[1], title_word2),
            run_time = 0.75
        )
        
        title2 = Text("ZOC", font="Rockwell").scale(1.5)
        title_underline1 = Underline(title2, color=RED)
        
        title2_group = VGroup(title2, title_underline1)
        
        self.play(
            title_word1.animate.to_edge(UL),
            title_word2.animate.to_edge(DR),
            GrowFromCenter(title2_group),
            Flash(title2, color=RED, line_length=0.8, num_lines=15),
            ShowPassingFlashWithThinningStrokeWidth(title2, color=RED)
        )
        
        self.play(title2_group.animate.shift(LEFT))
        
        title2_ext = Text("v2", font="valorax").scale(1.5)
        
        
        
        for i in range(len(title2_ext)):
            self.play(
                GrowFromCenter(title2_ext[i]),
                title2_ext.animate.shift(RIGHT*0.5),
                run_time = 0.1
            )
    
        title2_ext_underline1 = Underline(title2_ext, color=BLUE)
            
        self.play(
            ReplacementTransform(title_underline1, title2_ext_underline1),
        )
        
        title2_group = VGroup(title2, title2_ext)
        
        title2_group_underline1 = Underline(title2_group, color=PINK)
        
        self.play(ReplacementTransform(title2_ext_underline1, title2_group_underline1),
                  FadeOut(title_ext))
        
        
        
        self.wait(0.4)

        credits = Text("BDY", font="Rockwell").scale(1)
        credits_ext = Text("By Deyan, Louis", font="Rockwell").scale(1)     
        
        
        
        credits_word1 = credits_ext[0:2]
        credits_word2 = credits_ext[2:7]
        credits_word3 = credits_ext[7:]
        
        credits_word_group = VGroup(credits_word1, credits_word2, credits_word3)
        self.play(
            title2_group_underline1.animate.shift(DOWN * 1.2).set_opacity(0),
            title2_group.animate.shift(UP*1.1), 
            Write(credits),
            run_time = 0.5
        )
        self.wait(0.2)
        
        self.play(
            ReplacementTransform(credits[0], credits_word1),
            ReplacementTransform(credits[1], credits_word2),
            ReplacementTransform(credits[2], credits_word3),
        )
        
        
            
        
        self.play(
            title2_group.animate.move_to([-5, 3.5, 0]),
            credits_word_group. animate.move_to([4.3, -3.5, 0]),
        )
        
        credits_flash = Flash(
            [4.3, -3.5, 0],
            color=PINK,
            line_length=1,  # Length of the lines
            num_lines=12,     # Number of lines in the flash
            flash_radius=1.0, # Radius of the flash
            time_width=0.3,    # Duration of each flash
        )
        title2_group_flash = Flash(
            [-5, 3.5, 0],
            color=PINK,
            line_length=1,  # Length of the lines
            num_lines=12,     # Number of lines in the flash
            flash_radius=1.0, # Radius of the flash
            time_width=0.3,    # Duration of each flash
        )

        # Rotate the flash
        self.play(credits_flash,
                  title2_group_flash,
                  FadeOut(credits_word_group),
                  FadeOut(title2_group))
        
        self.wait(2)
