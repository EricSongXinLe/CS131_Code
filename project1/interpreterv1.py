from intbase import InterpreterBase
from intbase import ErrorType
from brewparse import parse_program

class Interpreter(InterpreterBase):
    def __init__(self, console_output=True, inp=None, trace_output=False):
        super().__init__(console_output, inp)

    def eval_expr(self, expr):
        if expr.elem_type == '+':
            op1 = self.eval_expr(expr.dict['op1'])
            op2 = self.eval_expr(expr.dict['op2'])
            if isinstance(op1, int) and isinstance(op2, int):
                return op1 + op2
            else:
                super().error(
                ErrorType.TYPE_ERROR,
                "Incompatible types for arithmetic operation",
            )
        elif expr.elem_type == '-':
            op1 = self.eval_expr(expr.dict['op1'])
            op2 = self.eval_expr(expr.dict['op2'])
            if isinstance(op1, int) and isinstance(op2, int):
                return op1 - op2
            else:
                super().error(
                ErrorType.TYPE_ERROR,
                "Incompatible types for arithmetic operation",
            )
        elif expr.elem_type == 'var':
            var = expr.dict['name']
            if var in self.var_dict and self.var_dict[var] != None:
                return self.var_dict[var]
            else:
                super().error(
                    ErrorType.NAME_ERROR,
                    f"Variable {var} has not been defined",
                ) 
        elif expr.elem_type == 'int' or expr.elem_type == 'string':
            return expr.dict['val']
        elif expr.elem_type == 'fcall':
            func = expr.dict['name']
            if func == 'inputi':
                args = expr.dict['args']
                if len(args) > 1:
                    super().error(
                    ErrorType.NAME_ERROR,
                    f"No inputi() function found that takes > 1 parameter",
                )
                if args != []:
                    out_string = self.eval_expr(args[0])
                    super().output(out_string)
                user_input = int(super().get_input())
                return user_input
            else:
                super().error(
                ErrorType.NAME_ERROR,
                f"Function {func} has not been defined",
            )
    
    def func_call(self, func, args):
        if func == 'print':
            str = self.eval_expr(args[0])
            super().output(str)
            return None

    def run_func(self, func):
        for statement in func.get('statements'):
            if statement.elem_type == 'vardef':
                #print(statement.dict['name'])
                var = statement.dict['name']
                if var in self.var_dict:
                    super().error(
                    ErrorType.NAME_ERROR,
                    f"Variable {var} defined more than once",
                )
                self.var_dict[var] = None

            elif statement.elem_type == '=':
                var = statement.dict['name']
                if var in self.var_dict:
                    self.var_dict[var] = self.eval_expr(statement.dict['expression'])
                else:
                    super().error(
                    ErrorType.NAME_ERROR,
                    f"Variable {var} has not been defined",
                )
                #print(self.var_dict[statement.dict['name']])
            elif statement.elem_type == 'fcall':
                self.func_call(statement.dict['name'],statement.dict['args'])
            else:
                pass
    
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
x = inputi("Please input your fav number: ");
print(x+1-(3+5));
}
"""

inter = Interpreter()
inter.run(program_source)