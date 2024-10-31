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
            elif isinstance(op1, str) and isinstance(op2, str):
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
        elif expr.elem_type == '*':
            op1 = self.eval_expr(expr.dict['op1'])
            op2 = self.eval_expr(expr.dict['op2'])
            if isinstance(op1, int) and isinstance(op2, int):
                return op1 * op2
            else:
                super().error(
                ErrorType.TYPE_ERROR,
                "Incompatible types for arithmetic operation",
            )
        elif expr.elem_type == '/':
            op1 = self.eval_expr(expr.dict['op1'])
            op2 = self.eval_expr(expr.dict['op2'])
            if isinstance(op1, int) and isinstance(op2, int):
                return op1 // op2
            else:
                super().error(
                ErrorType.TYPE_ERROR,
                "Incompatible types for arithmetic operation",
            )
        elif expr.elem_type == '==':
            op1 = self.eval_expr(expr.dict['op1'])
            op2 = self.eval_expr(expr.dict['op2'])
            if type(op1) == type(op2):
                return (op1 == op2)
            else:
                return False
        elif expr.elem_type == '!=':
            op1 = self.eval_expr(expr.dict['op1'])
            op2 = self.eval_expr(expr.dict['op2'])
            if type(op1) == type(op2):
                return (op1 != op2)
            else:
                return True
        elif expr.elem_type == '<':
            op1 = self.eval_expr(expr.dict['op1'])
            op2 = self.eval_expr(expr.dict['op2'])
            if type(op1) == type(op2):
                return (op1 < op2)
            else:
                super().error(
                ErrorType.TYPE_ERROR,
                "Incompatible types for < operation",
            )
        elif expr.elem_type == '<=':
            op1 = self.eval_expr(expr.dict['op1'])
            op2 = self.eval_expr(expr.dict['op2'])
            if type(op1) == type(op2):
                return (op1 <= op2)
            else:
                super().error(
                ErrorType.TYPE_ERROR,
                "Incompatible types for <= operation",
            )
        elif expr.elem_type == '>':
            op1 = self.eval_expr(expr.dict['op1'])
            op2 = self.eval_expr(expr.dict['op2'])
            if type(op1) == type(op2):
                return (op1 > op2)
            else:
                super().error(
                ErrorType.TYPE_ERROR,
                "Incompatible types for > operation",
            )
        elif expr.elem_type == '>=':
            op1 = self.eval_expr(expr.dict['op1'])
            op2 = self.eval_expr(expr.dict['op2'])
            if type(op1) == type(op2):
                return (op1 >= op2)
            else:
                super().error(
                ErrorType.TYPE_ERROR,
                "Incompatible types for >= operation",
            )
        elif expr.elem_type == '&&':
            op1 = self.eval_expr(expr.dict['op1'])
            op2 = self.eval_expr(expr.dict['op2'])
            if isinstance(op1, bool) and isinstance(op2, bool):
                return op1 and op2
            else:
                super().error(
                ErrorType.TYPE_ERROR,
                "Incompatible types for && operation",
            )
        elif expr.elem_type == '||':
            op1 = self.eval_expr(expr.dict['op1'])
            op2 = self.eval_expr(expr.dict['op2'])
            if isinstance(op1, bool) and isinstance(op2, bool):
                return op1 or op2
            else:
                super().error(
                ErrorType.TYPE_ERROR,
                "Incompatible types for or operation",
            )
        elif expr.elem_type == 'var':
            var = expr.dict['name']
            if var in self.var_dict:
                return self.var_dict[var]
            else:
                super().error(
                    ErrorType.NAME_ERROR,
                    f"Variable {var} has not been defined",
                ) 
        elif expr.elem_type == 'neg':
            op1 = self.eval_expr(expr.dict['op1'])
            if op1 == True or op1 == False:
                super().error(
                    ErrorType.TYPE_ERROR,
                    "Incompatible types for neg operation",
                ) 
            elif isinstance(op1, int):
                return 0-op1
            else:
                super().error(
                    ErrorType.TYPE_ERROR,
                    "Incompatible types for neg operation",
                ) 
        elif expr.elem_type == '!':
            op1 = self.eval_expr(expr.dict['op1'])
            if isinstance(op1, bool):
                return not op1
            else:
                super().error(
                    ErrorType.TYPE_ERROR,
                    "Incompatible types for ! operation",
                ) 
        elif expr.elem_type == 'int' or expr.elem_type == 'string' or expr.elem_type == 'bool':
            return expr.dict['val']
        elif expr.elem_type == 'nil':
            return None
        elif expr.elem_type == 'fcall':
            func = expr.dict['name']
            return self.func_call(func,expr.dict['args'] )
    
    def func_call(self, func, args):
        if func == 'print':
            outstr = ''
            for arg in args:
                outstr += str(self.eval_expr(arg))
            if outstr == 'True':
                outstr = 'true'
            elif outstr == 'False':
                outstr = 'false'
            super().output(outstr)
            return None
        elif func == 'inputi':
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
        elif func == 'inputs':
            if len(args) > 1:
                super().error(
                ErrorType.NAME_ERROR,
                f"No inputs() function found that takes > 1 parameter",
            )
            if args != []:
                out_string = self.eval_expr(args[0])
                super().output(out_string)
            user_input = str(super().get_input())
            return user_input
        else:
            super().error(
                ErrorType.NAME_ERROR,
                f"Function {func} has not been defined",
            )
    def exec_statment(self, statement):
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
        elif statement.elem_type == 'if':
            cond = statement.dict['condition']
            cond = self.eval_expr(cond)
            if isinstance(cond,bool):
                if cond:
                    for statement in statement.dict['statements']:
                        self.exec_statment(statement)
                else:
                    if statement.dict['else_statements'] != None:
                        for statement in statement.dict['else_statements']:
                            self.exec_statment(statement)
            else:
                super().error(
                    ErrorType.TYPE_ERROR,
                    "Condition must eval to bool",
                )
        else:
            pass


    def run_func(self, func):
        for statement in func.get('statements'):
            self.exec_statment(statement)
    
    def run(self, program):
        ast = parse_program(program)
        self.var_dict = dict()
        funcs = ast.dict['functions'] #for proj 1 we only have 1 function?
        main = funcs[0]
        if main.dict['name'] != "main":
            super().error(ErrorType.NAME_ERROR,"No main() function was found",)
        self.run_func(main)
    
    
        


program_source = """func main() {
  var val;
  val = 0;
  
  if (nil != nil){
    print("Ugh");
  }
  print(val);
}
"""

inter = Interpreter()
inter.run(program_source)
