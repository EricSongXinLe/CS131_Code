from intbase import InterpreterBase
from intbase import ErrorType
from brewparse import parse_program

class Interpreter(InterpreterBase):
    class Nil:
        def __eq__(self, other):
            return isinstance(other,Interpreter.Nil)
        
    class Exception:
        def __init__(self,exception_type):
            self.exception_type = exception_type

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
                if op2 == 0:
                    raise Exception("div0")
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
            if isinstance(op1, bool):
                if op1 == False:
                    return False
            else:
                super().error(
                ErrorType.TYPE_ERROR,
                "Incompatible types for && operation",
            )
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
            if isinstance(op1, bool):
                if op1 == True:
                    return True
            else:
                super().error(
                ErrorType.TYPE_ERROR,
                "Incompatible types for && operation",
            )
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
                curr = str(self.eval_expr(arg))
                if curr == 'True':
                    curr = 'true'
                elif curr == 'False':
                    curr = 'false'
                outstr += curr
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
        elif statement.elem_type == 'raise':
            self.raise_exception(self.eval_expr(statement.dict['exception_type']))
        elif statement.elem_type == 'try':
            try_statements = statement.dict['statements']
            self.env_stack[-1].append(dict())
            try:
                for try_statement in try_statements:
                    try_res = self.exec_statment(try_statement)
                    if try_res != None:
                        self.env_stack[-1].pop()
                        return try_res
                self.env_stack[-1].pop()
                return None
            except Exception as exc:
                catchers = statement.dict['catchers']
                self.env_stack[-1].append(dict())
                caught = False
                for catcher in catchers:
                    if str(exc) == catcher.dict['exception_type']:
                        caught = True
                        catch_statements = catcher.dict['statements']
                        for catch_statement in catch_statements:
                            catch_res = self.exec_statment(catch_statement)
                            if catch_res != None:
                                self.env_stack[-1].pop()
                                self.env_stack[-1].pop()
                                return catch_res
                        
                if not caught:
                    raise
                self.env_stack[-1].pop()
                self.env_stack[-1].pop()
                return None
                            
        else:
            pass


    def raise_exception(self, type):
        if not isinstance(type, str):
            super().error(
            ErrorType.TYPE_ERROR,
            "Exception type must be string!",
        )
        raise Exception(type)

    
    def run(self, program):
        ast = parse_program(program)
        self.catch_stack = []
        self.env_stack = []
        #self.env_stack.append([]) ##[[func1: {scope1,},{scope2}],[func2: {scope1},{scope2}]]
        #self.env_stack[-1].append(dict())
        self.funcs = ast.dict['functions']
        try:
            self.func_call("main",[])
        except Exception as err:
            errorType = err.args[0][10:20]
            if len(err.args[0]) > 23:
                errorMsg = err.args[0][22:]
            else:
                errorMsg = ""
            #print(errorType)
            #print(errorMsg)
            if errorType == "TYPE_ERROR":
                    super().error(
                ErrorType.TYPE_ERROR,
                errorMsg
                )
            elif errorType == "NAME_ERROR":
                super().error(
                ErrorType.NAME_ERROR,
                errorMsg
                )
            elif errorType == "FAULT_ERROR":
                super().error(
                ErrorType.FAULT_ERROR,
                errorMsg
                )
            else:
                super().error(
                ErrorType.FAULT_ERROR,
                "Uncaught error!"
                )

    
    
if __name__ == '__main__':
    program_source = """
func foo() {
  print("F0");
  raise "a";
  print("F1");
}


func main() {
 print("0");
 try {
   print("1");
   foo();
   print("2");
 }
 catch "b" {
   print("5");
 }
 catch "a" {
   print("3");
 }
 catch "c" {
   print("6");
 }
 print("4");
}






    """

    inter = Interpreter()
    inter.run(program_source)