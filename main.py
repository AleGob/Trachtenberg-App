from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
import random

import moltiplicazioni
import addizioni
import quadrati
import divisioni
import radici # <-- Ultimo modulo importato!

Window.fullscreen = 'auto'

class MenuScreen(Screen):
    pass

class TrainingScreen(Screen):
    pass

class TrachtenbergApp(App):
    user_input = ""
    answer_str = ""
    input_direction = "Right to Left"

    def build(self):
        return Builder.load_file('grafica.kv')

    def start_training(self):
        menu = self.root.get_screen('menu')
        
        self.rand_op = menu.ids.chk_rand_op.active
        self.rand_rule = menu.ids.chk_rand_rule.active
        self.rand_digits = menu.ids.chk_rand_digits.active
        self.rand_rows = menu.ids.chk_rand_rows.active
        
        self.selected_op = menu.ids.op_spinner.text
        self.selected_rule = menu.ids.rule_spinner.text
        self.selected_digits = menu.ids.digit_input.text
        self.selected_rows = menu.ids.rows_input.text
        self.input_direction = menu.ids.direction_spinner.text 
        
        self.next_problem()
        self.root.current = 'training'

    def next_problem(self):
        training = self.root.get_screen('training')
        self.user_input = "" 
        
        # 1. Operation
        operations = ['Rapid Rules', 'NxN Multiplication', 'Addition', 'Division', 'Square', 'Square Root']
        op = random.choice(operations) if self.rand_op else self.selected_op
        
        # Gestione visibilità tasto "R" (attivo per Division e Square Root)
        btn_resto = training.ids.btn_resto
        if op in ['Division', 'Square Root']:
            btn_resto.opacity = 1
        else:
            btn_resto.opacity = 0
            
        # 2. Parse Digits
        digits_str = self.selected_digits.strip()
        if '-' in digits_str:
            try:
                parts = digits_str.split('-')
                min_d, max_d = int(parts[0]), int(parts[1])
            except ValueError:
                min_d, max_d = 3, 6
        else:
            try:
                val = int(digits_str)
                min_d, max_d = (val, val) if not self.rand_digits else (2, val)
            except ValueError:
                min_d, max_d = 3, 6
                
        # 3. Parse Addition Rows
        rows_str = self.selected_rows.strip()
        if '-' in rows_str:
            try:
                parts = rows_str.split('-')
                righe = random.randint(int(parts[0]), int(parts[1]))
            except ValueError:
                righe = random.randint(3, 6)
        else:
            try:
                val = int(rows_str)
                righe = random.randint(2, val) if self.rand_rows else val
            except ValueError:
                righe = 4

        # 4. Route to Modules
        if op == 'Rapid Rules':
            rules = [2, 3, 4, 5, 6, 7, 8, 9, 11, 12]
            rule = random.choice(rules) if self.rand_rule else int(self.selected_rule.split(' ')[-1])
            testo, risposta = moltiplicazioni.GeneratoreMoltiplicazioni.genera_regola_rapida(rule, min_d, max_d)
            training.ids.title_label.text = f"Rule: x{rule}"
            training.ids.problem_label.text = testo
            self.answer_str = risposta

        elif op == 'NxN Multiplication':
            testo, risposta = moltiplicazioni.GeneratoreMoltiplicazioni.genera_diretta(min_d, max_d)
            training.ids.title_label.text = "Direct Multiplication"
            training.ids.problem_label.text = testo
            self.answer_str = risposta
            
        elif op == 'Addition':
            testo, risposta = addizioni.GeneratoreAddizioni.genera_colonna(min_d, max_d, righe)
            training.ids.title_label.text = "Addition"
            training.ids.problem_label.text = testo
            self.answer_str = risposta
            
        elif op == 'Square':
            testo, risposta = quadrati.GeneratoreQuadrati.genera_quadrato(min_d, max_d)
            training.ids.title_label.text = "Square"
            training.ids.problem_label.text = testo
            self.answer_str = risposta
            
        elif op == 'Division':
            testo, risposta = divisioni.GeneratoreDivisioni.genera_divisione(min_d, max_d)
            training.ids.title_label.text = "Division"
            training.ids.problem_label.text = testo
            self.answer_str = risposta
            
        elif op == 'Square Root':
            testo, risposta = radici.GeneratoreRadici.genera_radice(min_d, max_d)
            training.ids.title_label.text = "Square Root"
            training.ids.problem_label.text = testo
            self.answer_str = risposta

        else:
            training.ids.title_label.text = f"Mode: {op}"
            training.ids.problem_label.text = "Work in progress..."
            self.answer_str = "0"

        training.ids.answer_label.text = ""
        dir_text = "L to R" if self.input_direction == "Left to Right" else "R to L"
        training.ids.feedback_label.text = f"Type the answer ({dir_text})"
        training.ids.feedback_label.color = (0.7, 0.7, 0.7, 1)

    def type_digit(self, digit):
        if ' R ' in self.user_input:
            self.user_input += str(digit)
        else:
            if self.input_direction == "Right to Left":
                self.user_input = str(digit) + self.user_input
            else:
                self.user_input += str(digit)
        self.update_display()

    def toggle_resto(self):
        if ' R ' in self.user_input:
            self.user_input = self.user_input.split(' R ')[0]
        else:
            self.user_input += " R "
        self.update_display()

    def delete_digit(self):
        if not self.user_input: return
        
        if self.user_input.endswith(' R '):
            self.user_input = self.user_input[:-3]
        elif ' R ' in self.user_input:
            self.user_input = self.user_input[:-1]
        else:
            if self.input_direction == "Right to Left":
                self.user_input = self.user_input[1:]
            else:
                self.user_input = self.user_input[:-1]
                
        self.update_display()

    def update_display(self):
        training = self.root.get_screen('training')
        training.ids.answer_label.text = self.user_input

    def check_answer(self):
        training = self.root.get_screen('training')
        if not self.user_input: return
            
        if self.user_input == self.answer_str:
            training.ids.feedback_label.text = "CORRECT!"
            training.ids.feedback_label.color = (0, 1, 0, 1)
        else:
            training.ids.feedback_label.text = f"WRONG! Try again."
            training.ids.feedback_label.color = (1, 0.3, 0.3, 1)
            self.user_input = ""
            self.update_display()

if __name__ == '__main__':
    TrachtenbergApp().run()
