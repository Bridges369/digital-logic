import sys
sys.path.append('./../')
sys.path.append('./')
from manim import *
from config import *

class notaca_posicional_descricao(Scene):
    def construct(self):
        title = Title(
            "Notação Posicional",
            color = WHITE
        ).to_edge(UP+ORIGIN)

        description = Paragraph(
            "\tModo de representação numérica na qual cada", 
            "algarismo depende de sua posição relativa na",
                     "composição do número.",
            color = WHITE,
            slant = ITALIC,
            t2c = {
                'representação numérica' : NORD10,
                'posição relativa'       : NORD10
            }
        )._set_all_lines_alignments("center").scale(0.735).to_edge(ORIGIN)
        
        # OPENING
        self.next_section("OPENING")
        self.play(Write(title))
        self.wait()
        self.play(Write(description))
        self.wait(1)
            
        # CLOSING
        self.next_section("CLOSING")
        self.play(Unwrite(title), Unwrite(description))
        self.wait()




class lista_de_numeros_e_variacao(Scene):
    def construct(self):

        # LIST
        self.next_section("LIST OPENING")

        for i in range(10):
            self.play( Write (
                Integer(
                    number = i,
                    color = WHITE,
                ).scale(1).move_to(i * RIGHT - [4.5,0.0,0.0]).to_edge(UP),
                run_time = 0.3,
                rate_func = linear
            ), run_time = 0.3, rate_func = linear)
        self.wait()
        

        # CHANGE NUMBER ON CENTER
        self.next_section("NUMBER ON CENTER")

        n = Integer(
            number = 0,
            color = WHITE
        ).scale(3)

        for i in [8, 2, 7, 3, 1, 9]:
            self.play(n.animate.set_value(i), run_time = 0.5, rate_func = linear)
            self.wait()


        
        # 9 + 1 = ?
        self.next_section("NOVE MAIS UM")

        expression = MathTex(
            r"9 + 1 = ?",
            color = WHITE
        ).scale(3)

        self.play(Transform(n, expression))
        self.wait()




class primeira_contagem_decimal(Scene):
    def construct(self):
        # DEPOIS DO NOVE
        self.next_section("depois do nove")

        number = Integer(
            number = 9
        ).scale(3)


