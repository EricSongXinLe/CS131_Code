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
            stack_depth = len(self.env_stack)
            found = False
            for i in range(1,stack_depth+1):
                if var in self.env_stack[-i]:
                    found = True
                    return self.env_stack[-i][var] #var found in current scope
                #not found, go to previous stack.
            if(not found):
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
            if var in self.env_stack[-1]: #looks at current scope.
                super().error(
                ErrorType.NAME_ERROR,
                f"Variable {var} defined more than once",
            )
            self.env_stack[-1][var] = None 

        elif statement.elem_type == '=':
            var = statement.dict['name']
            stack_depth = len(self.env_stack)
            found = False
            for i in range(1,stack_depth+1):
                if var in self.env_stack[-i] and not found:
                    found = True
                    self.env_stack[-i][var] = self.eval_expr(statement.dict['expression'])
            if(not found): #still not found??
                super().error(
                ErrorType.NAME_ERROR,
                f"Variable {var} has not been defined",
            )
        elif statement.elem_type == 'fcall':
            self.func_call(statement.dict['name'],statement.dict['args'])
        elif statement.elem_type == 'if':
            cond = statement.dict['condition']
            cond = self.eval_expr(cond)
            if isinstance(cond,bool):
                if cond:
                    self.env_stack.append(dict())
                    for statement in statement.dict['statements']:
                        self.exec_statment(statement)
                    self.env_stack.pop()
                else:
                    if statement.dict['else_statements'] != None:
                        self.env_stack.append(dict())
                        for statement in statement.dict['else_statements']:
                            self.exec_statment(statement)
                        self.env_stack.pop()
            else:
                super().error(
                    ErrorType.TYPE_ERROR,
                    "Condition must eval to bool",
                )
        elif statement.elem_type == 'for':
            init=statement.dict['init']
            self.exec_statment(init)
            cond = statement.dict['condition']
            update =statement.dict['update']
            statements = statement.dict['statements']
            while(self.eval_expr(cond)):
                self.env_stack.append(dict())
                for statement in statements:
                        self.exec_statment(statement)
                self.env_stack.pop()
                self.exec_statment(update)
        elif statement.elem_type == 'return':
            expr = statement.dict['expression']
            return self.eval_expr(expr)
        else:
            pass


    def run_func(self, func):
        for statement in func.get('statements'):
            self.exec_statment(statement)
    
    def run(self, program):
        ast = parse_program(program)
        self.env_stack = []
        self.env_stack.append(dict())
        funcs = ast.dict['functions']
        main = None
        for func in funcs:
            if func.dict['name'] == "main":
                main = func
        if main == None:
            super().error(ErrorType.NAME_ERROR,"No main() function was found",)
        self.run_func(main)
    
    
        


program_source = """
func foo(){
    print("fuck!!");
}
func main() {
  var i;
  i = true;
  if(i){
    var i;
    i = "shit!!";
    print(i);
  }
  print(i);
}
"""

inter = Interpreter()
inter.run(program_source)
