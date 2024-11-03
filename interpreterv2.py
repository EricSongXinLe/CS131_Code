from intbase import InterpreterBase
from intbase import ErrorType
from brewparse import parse_program

class Interpreter(InterpreterBase):
    class Nil:
        def __eq__(self, other):
            return isinstance(other,Interpreter.Nil)
    def __init__(self, console_output=True, inp=None, trace_output=False):
        super().__init__(console_output, inp)

    def eval_expr(self, expr):
        if expr.elem_type == '+':
            op1 = self.eval_expr(expr.dict['op1'])
            op2 = self.eval_expr(expr.dict['op2'])
            if isinstance(op1, bool) or isinstance(op2, bool):
                super().error(
                ErrorType.TYPE_ERROR,
                "Incompatible types for arithmetic operation",
            )
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
            if isinstance(op1, bool) or isinstance(op2, bool):
                super().error(
                ErrorType.TYPE_ERROR,
                "Incompatible types for arithmetic operation",
            )
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
            if isinstance(op1, bool) or isinstance(op2, bool):
                super().error(
                ErrorType.TYPE_ERROR,
                "Incompatible types for arithmetic operation",
            )
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
            if isinstance(op1, bool) or isinstance(op2, bool):
                super().error(
                ErrorType.TYPE_ERROR,
                "Incompatible types for arithmetic operation",
            )
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
            if isinstance(op1, bool) or isinstance(op2, bool):
                super().error(
                ErrorType.TYPE_ERROR,
                "Incompatible types for arithmetic operation",
            )
            if isinstance(op1, int) and isinstance(op2, int):
                return (op1 < op2)
            else:
                super().error(
                ErrorType.TYPE_ERROR,
                "Incompatible types for < operation",
            )
        elif expr.elem_type == '<=':
            op1 = self.eval_expr(expr.dict['op1'])
            op2 = self.eval_expr(expr.dict['op2'])
            if isinstance(op1, bool) or isinstance(op2, bool):
                super().error(
                ErrorType.TYPE_ERROR,
                "Incompatible types for arithmetic operation",
            )
            if isinstance(op1, int) and isinstance(op2, int):
                return (op1 <= op2)
            else:
                super().error(
                ErrorType.TYPE_ERROR,
                "Incompatible types for <= operation",
            )
        elif expr.elem_type == '>':
            op1 = self.eval_expr(expr.dict['op1'])
            op2 = self.eval_expr(expr.dict['op2'])
            if isinstance(op1, bool) or isinstance(op2, bool):
                super().error(
                ErrorType.TYPE_ERROR,
                "Incompatible types for arithmetic operation",
            )
            if isinstance(op1, int) and isinstance(op2, int):
                return (op1 > op2)
            else:
                super().error(
                ErrorType.TYPE_ERROR,
                "Incompatible types for > operation",
            )
        elif expr.elem_type == '>=':
            op1 = self.eval_expr(expr.dict['op1'])
            op2 = self.eval_expr(expr.dict['op2'])
            if isinstance(op1, bool) or isinstance(op2, bool):
                super().error(
                ErrorType.TYPE_ERROR,
                "Incompatible types for arithmetic operation",
            )
            if isinstance(op1, int) and isinstance(op2, int):
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
            stack_depth = len(self.env_stack[-1])
            found = False
            for i in range(1,stack_depth+1):
                if var in self.env_stack[-1][-i]:
                    found = True
                    return self.env_stack[-1][-i][var] #var found in current scope
                #not found, go to previous stack.
            if(not found):
                super().error(
                    ErrorType.NAME_ERROR,
                    f"Variable {var} has not been defined",
                ) 
        elif expr.elem_type == 'neg':
            op1 = self.eval_expr(expr.dict['op1'])
            if isinstance(op1,bool):
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
            return self.Nil()
        elif expr.elem_type == 'fcall':
            func = expr.dict['name']
            return self.func_call(func,expr.dict['args'] )
    
    def func_call(self, funcName, args):
        if funcName == 'print':
            outstr = ''
            for arg in args:
                outstr += str(self.eval_expr(arg))
            if outstr == 'True':
                outstr = 'true'
            elif outstr == 'False':
                outstr = 'false'
            super().output(outstr)
            return self.Nil()
        elif funcName == 'inputi':
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
        elif funcName == 'inputs':
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
            found = False
            callerArgs = args
            for func in self.funcs:
                currFuncName = func.dict['name']
                currFuncArgs = func.dict['args']
                if currFuncName == funcName:
                    if len(currFuncArgs) == len(args):
                        found = True
                        calleeArgs = currFuncArgs
                        ##var copy starts
                        if callerArgs == []:
                            self.env_stack.append([])
                            self.env_stack[-1].append(dict())
                        else:
                            callerVals = []
                            for callerArg in callerArgs:
                                callerVals.append(self.eval_expr(callerArg))
                            self.env_stack.append([])
                            self.env_stack[-1].append(dict())
                            for calleeArg,callerVal in zip(calleeArgs,callerVals):
                                self.env_stack[-1][-1][calleeArg.dict['name']] = callerVal ##Finds the caller arg from prev stack, and copies it to the new stack.
                        # execution
                        for statement in func.dict['statements']:
                            exec_result = self.exec_statment(statement)
                            if(exec_result!= None):
                                self.env_stack.pop()
                                return exec_result
                        self.env_stack.pop()
                        return self.Nil()
            if not found:
                super().error(
                    ErrorType.NAME_ERROR,
                    f"No corrsponding function: {funcName} found",
                )
    def exec_statment(self, statement):
        if statement.elem_type == 'vardef':
            #print(statement.dict['name'])
            var = statement.dict['name']
            if var in self.env_stack[-1][-1]: #looks at current scope.
                super().error(
                ErrorType.NAME_ERROR,
                f"Variable {var} defined more than once",
            )
            self.env_stack[-1][-1][var] = None 

        elif statement.elem_type == '=':
            var = statement.dict['name']
            stack_depth = len(self.env_stack[-1])
            found = False
            for i in range(1,stack_depth+1):
                if var in self.env_stack[-1][-i] and not found:
                    found = True
                    self.env_stack[-1][-i][var] = self.eval_expr(statement.dict['expression'])
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
                    self.env_stack[-1].append(dict())
                    for statement in statement.dict['statements']:
                        result = self.exec_statment(statement)
                        if result != None:
                            return result
                    self.env_stack[-1].pop()
                else:
                    if statement.dict['else_statements'] != None:
                        self.env_stack[-1].append(dict())
                        for statement in statement.dict['else_statements']:
                            #self.exec_statment(statement)
                            result = self.exec_statment(statement)
                            if result != None:
                                return result
                        self.env_stack[-1].pop()
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
            while(status := self.eval_expr(cond)):
                if not isinstance(status, bool):
                    super().error(
                    ErrorType.TYPE_ERROR,
                    "Condition must eval to bool",
                )
                self.env_stack[-1].append(dict())
                for statement in statements:
                    result = self.exec_statment(statement)
                    if result != None:
                        return result
                self.env_stack[-1].pop()
                self.exec_statment(update)
        elif statement.elem_type == 'return':
            expr = statement.dict['expression']
            if expr == None:
                return self.Nil()
            else:
                return self.eval_expr(expr)
        else:
            pass


    def run_func(self, func): ##this is legacy code that just takes about main.
        for statement in func.get('statements'):
            result = self.exec_statment(statement)
            if result != None:
                return result
    
    def run(self, program):
        ast = parse_program(program)
        self.env_stack = []
        self.env_stack.append([]) ##[[func1: {scope1,},{scope2}],[func2: {scope1},{scope2}]]
        self.env_stack[-1].append(dict())
        self.funcs = ast.dict['functions']
        main = None
        for func in self.funcs:
            if func.dict['name'] == "main":
                main = func
        if main == None:
            super().error(ErrorType.NAME_ERROR,"No main() function was found",)
        self.run_func(main)
    
    
'''
program_source = """
func main() {
    var x;
    x = 5;
    if (x == 5) {
        print("Inside if pre return");
        return;
        print("Inside if post return");
    }
    print("Outside if");
}
"""

inter = Interpreter()
inter.run(program_source)
'''