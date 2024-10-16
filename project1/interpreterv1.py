from intbase import InterpreterBase
from intbase import ErrorType
from brewparse import parse_program

class Interpreter(InterpreterBase):
    def __init__(self, console_output=True, inp=None, trace_output=False):
        super().__init__(console_output, inp)

    def eval_expr(self, expr):
        return 0 #this is temp
    

    def run_func(self, func):
        for statement in func.get('statements'):
            if statement.elem_type == 'vardef':
                #print(statement.dict['name'])
                self.var_dict[statement.dict['name']] = None
            elif statement.elem_type == '=':
                self.var_dict[statement.dict['name']] = self.eval_expr(statement.dict['expression'])
                #print(self.var_dict[statement.dict['name']])
    
    def run(self, program):
        ast = parse_program(program)
        self.var_dict = dict()
        funcs = ast.dict['functions'] #for proj 1 we only have 1 function?
        main = funcs[0]
        if main.dict['name'] != "main":
            super().error(ErrorType.NAME_ERROR,"No main() function was found",)
        self.run_func(main)
    
    
        


program_source = """func main() {
var x;
x = 5 + 6;
print("The sum is: ", x);
}
"""

inter = Interpreter()
inter.run(program_source)