from intbase import InterpreterBase
from brewparse import parse_program

class Interpreter(InterpreterBase):
    def __init__(self, console_output=True, inp=None, trace_output=False):
        super().__init__(console_output, inp)

    def run_func(self, func):
        for statement in func.get('statements'):
            print(statement.get('name'))
        
    
    def run(self, program):
        ast = parse_program(program)
        self.var_dict = dict()
        funcs = ast.dict['functions'] #for proj 1 we only have 1 function?
        main = funcs[0]
        self.run_func(main)
    
    
        


program_source = """func main() {
var x;
x = 5 + 6;
print("The sum is: ", x);
}
"""

inter = Interpreter()
inter.run(program_source)