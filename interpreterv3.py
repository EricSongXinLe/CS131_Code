from intbase import InterpreterBase
from intbase import ErrorType
from brewparse import parse_program

class Interpreter(InterpreterBase):
    class Nil:
        def __eq__(self, other):
            return isinstance(other,Interpreter.Nil)
        def __str__(self):
            return "nil"
    class Void:
        def __eq__(self, other):
            return isinstance(other,Interpreter.Void)

    def __init__(self, console_output=True, inp=None, trace_output=False):
        super().__init__(console_output, inp)

    def determine_type(self,var):
        if isinstance(var,int):
            if var is True or var is False:
                return "bool"
            else:
                return "int"
        elif isinstance(var,bool):
            return "bool"
        elif isinstance(var, str):
            return "string"
        elif isinstance(var, list):
            return var[1]
        else:
            return self.Nil ##Nil Type
        
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
            if isinstance(op1, bool) or isinstance(op2, bool):
                if isinstance(op1,int):
                    if op1 == 0:
                        op1 = False
                    else:
                        op1 = True
                if isinstance(op2,int):
                    if op2 == 0:
                        op2 = False
                    else:
                        op2 = True                    
            if type(op1) == type(op2):
                return (op1 == op2)
            else:
                super().error(
                ErrorType.TYPE_ERROR,
                "Incompatible types for == operation",
            )
        elif expr.elem_type == '!=':
            op1 = self.eval_expr(expr.dict['op1'])
            op2 = self.eval_expr(expr.dict['op2'])
            if isinstance(op1, bool) or isinstance(op2, bool):
                if isinstance(op1,int):
                    if op1 == 0:
                        op1 = False
                    else:
                        op1 = True
                if isinstance(op2,int):
                    if op2 == 0:
                        op2 = False
                    else:
                        op2 = True        
            if type(op1) == type(op2):
                return (op1 != op2)
            else:
                super().error(
                ErrorType.TYPE_ERROR,
                "Incompatible types for == operation",
            )
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
            if isinstance(op1,int):
                if op1 == 0:
                    op1 = False
                else:
                    op1 = True
            if isinstance(op2,int):
                if op2 == 0:
                    op2 = False
                else:
                    op2 = True     
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
            if isinstance(op1,int):
                if op1 == 0:
                    op1 = False
                else:
                    op1 = True
            if isinstance(op2,int):
                if op2 == 0:
                    op2 = False
                else:
                    op2 = True        
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
                if "." in var: #STRUCT
                    var_name, field_name = var.split('.')
                    if var_name in self.env_stack[-1][-i] and not found:
                        found = True
                        ptr = self.env_stack[-1][-i][var_name][0]
                        #print(ptr)
                        if isinstance(ptr, int) or isinstance(ptr, str) or isinstance(ptr, bool):
                            super().error(
                                ErrorType.TYPE_ERROR,
                                f"NOT A Struct!: {var_name}",
                            )
                        if isinstance(ptr,self.Nil):
                            super().error(
                                ErrorType.FAULT_ERROR,
                                f"Nullptr access: {var_name}",
                            )
                        return ptr[0][field_name][0]
                else:
                    if var in self.env_stack[-1][-i]:
                        found = True
                        return self.env_stack[-1][-i][var][0] #var found in current scope
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
            elif isinstance(op1, int):
                if op1 == 0:
                    return True
                else:
                    return False
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
            ret = self.func_call(func,expr.dict['args'] )
            if isinstance(ret,self.Void):
                super().error(
                    ErrorType.TYPE_ERROR,
                    "Must not use void func in expression",
                ) 
            return ret
        elif expr.elem_type == 'new':
            var_type = expr.dict['var_type']
            if var_type in self.valid_types:
                structure = self.struct_LUT[var_type] #a dict of how the struct should look like
                #print(structure)
                struct_dict = {}
                for field in structure:
                    field_type = structure[field]
                    if field_type == "int":
                        struct_dict[field] = [0,field_type]
                    elif field_type == "string":
                        struct_dict[field] = ["",field_type]
                    elif field_type =="bool":
                        struct_dict[field] = [False,field_type]
                    elif field_type in self.valid_types:
                        struct_dict[field] = [self.Nil(),field_type]
                return [struct_dict,var_type]
            else:
                super().error(
                    ErrorType.TYPE_ERROR,
                    f"Invalid type {var_type} for new operation",
                )
    
    def func_call(self, funcName, args):
        if funcName == 'print':
            outstr = ''
            for arg in args:
                #print(arg)
                eval_result = self.eval_expr(arg)
                if isinstance(eval_result,list) and eval_result[0] == self.Nil():
                    eval_result = self.Nil()
                #print(type(eval_result))
                if eval_result != self.Void():
                    curr = str(eval_result)
                    if curr == 'True':
                        curr = 'true'
                    elif curr == 'False':
                        curr = 'false'
                    outstr += curr
                else:
                    super().error(
                ErrorType.TYPE_ERROR,
                f"void not allows as parameter",
                )
            super().output(outstr)
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
                                callervarType = self.determine_type(callerVal)
                                calleevarType = calleeArg.dict['var_type']
                                if callervarType == calleevarType:
                                    self.env_stack[-1][-1][calleeArg.dict['name']] = [callerVal,calleevarType] ##Finds the caller arg from prev stack, and copies it to the new stack.
                                elif callervarType == "int" and calleevarType == "bool":
                                    if callerVal == 0:
                                        callerVal = False
                                    else:
                                        callerVal = True
                                    self.env_stack[-1][-1][calleeArg.dict['name']] = [callerVal,calleevarType] ##Finds the caller arg from prev stack, and copies it to the new stack.
                                else:
                                    super().error(
                                    ErrorType.TYPE_ERROR,
                                    f"fcall Var Type not match",
                                )
                                    
                        # execution
                        funcRetType = func.dict['return_type']
                        for statement in func.dict['statements']:
                            exec_result = self.exec_statment(statement,funcRetType)
                            if(exec_result!= None):
                                if funcRetType != "void":
                                    #self.env_stack.pop()
                                    actualRetType = self.determine_type(exec_result)
                                    #print(funcRetType)
                                    #print(actualRetType)
                                    if exec_result != self.Nil():
                                        if funcRetType == actualRetType:
                                            self.env_stack.pop()
                                            return exec_result
                                        elif funcRetType == 'bool' and actualRetType == 'int':
                                            self.env_stack.pop()
                                            if exec_result == 0:
                                                return False
                                            else:
                                                return True
                                        else:
                                            super().error(
                                            ErrorType.TYPE_ERROR,
                                            f"fcall return type wrong!",
                                        )
                                elif exec_result != self.Void():
                                    super().error(
                                        ErrorType.TYPE_ERROR,
                                        f"void function should not return!",
                                    )                                                                                                 
                        self.env_stack.pop()
                        if funcRetType == "int":
                            return 0
                        elif funcRetType == "bool":
                            return False
                        elif funcRetType == "string":
                            return ""
                        elif funcRetType == "void":
                            return self.Void()
                        else:
                            return [self.Nil(),funcRetType] ##Returns nullptr for struct
            if not found:
                super().error(
                    ErrorType.NAME_ERROR,
                    f"No corrsponding function: {funcName} found",
                )
    def exec_statment(self, statement, funcRetType = None):
        if statement.elem_type == 'vardef':
            #print(statement.dict['name'])
            var = statement.dict['name']
            varType = statement.dict['var_type']
            if var in self.env_stack[-1][-1]: #looks at current scope.
                super().error(
                ErrorType.NAME_ERROR,
                f"Variable {var} defined more than once",
            )
            if varType == "int":
                self.env_stack[-1][-1][var] = [0,varType]
            elif varType == "string":
                self.env_stack[-1][-1][var] = ["",varType]
            elif varType =="bool":
                self.env_stack[-1][-1][var] = [False,varType]
            elif varType in self.valid_types:
                self.env_stack[-1][-1][var] = [self.Nil(),varType]
            else:
                super().error(
                ErrorType.TYPE_ERROR,
                f"Unknown/invalid type specified {varType}",
            )
            #self.env_stack[-1][-1][var] = None 

        elif statement.elem_type == '=':
            var = statement.dict['name']
            stack_depth = len(self.env_stack[-1])
            found = False
            for i in range(1,stack_depth+1):
                if "." in var:
                    var_name, field_name = var.split('.')
                    #print(var_name,field_name)
                    if var_name in self.env_stack[-1][-i] and not found:
                        found = True
                        val = self.eval_expr(statement.dict['expression'])
                        valType = self.determine_type(val)
                        #print(self.env_stack[-1][-i][var_name][0][0])
                        varType = self.env_stack[-1][-i][var_name][0][0][field_name][1]
                        if valType ==varType:
                            self.env_stack[-1][-i][var_name][0][0][field_name] = [val,valType]
                        elif valType == "int" and varType == "bool":
                            if val == 0:
                                val = False
                            else:
                                val = True
                            self.env_stack[-1][-i][var_name][0][0][field_name] = [val,valType]
                        
                        else:
                            super().error(
                                ErrorType.TYPE_ERROR,
                                f"var assignment Type not match",
                            )
                        #print(self.env_stack[-1][-i][var_name][0][0])
                else:
                    if var in self.env_stack[-1][-i] and not found:
                        found = True
                        val = self.eval_expr(statement.dict['expression'])
                        valType = self.determine_type(val)
                        varType = self.env_stack[-1][-i][var][1]
                        if valType == self.Nil:
                            valType = varType
                        if valType ==varType:
                            self.env_stack[-1][-i][var] = [val,valType]
                        elif valType == "int" and varType == "bool":
                            if val == 0:
                                val = False
                            else:
                                val = True
                            self.env_stack[-1][-i][var] = [val,valType]
                        else:
                            super().error(
                                ErrorType.TYPE_ERROR,
                                f"var assignment Type not match",
                            )
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
                        result = self.exec_statment(statement,funcRetType)
                        if result != None:
                            return result
                    self.env_stack[-1].pop()
                else:
                    if statement.dict['else_statements'] != None:
                        self.env_stack[-1].append(dict())
                        for statement in statement.dict['else_statements']:
                            #self.exec_statment(statement)
                            result = self.exec_statment(statement,funcRetType)
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
            self.exec_statment(init,funcRetType)
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
                    result = self.exec_statment(statement,funcRetType)
                    if result != None:
                        return result
                self.env_stack[-1].pop()
                self.exec_statment(update,funcRetType)
        elif statement.elem_type == 'return':
            expr = statement.dict['expression']
            if expr == None:
                if funcRetType == "int":
                    return 0
                elif funcRetType == "bool":
                    return False
                elif funcRetType == "string":
                    return ""
                elif funcRetType == "void":
                    return self.Void()
                else:
                    return [self.Nil(),funcRetType]
            else:
                retVal = self.eval_expr(expr)
                return retVal
        else:
            pass

    def process_structs(self,structs):
        for struct in structs:
            struct_name = struct.dict['name']
            self.struct_LUT[struct_name] = {} #
            self.valid_types.add(struct_name)
            fields = struct.dict['fields']
            for field in fields:
                field_name = field.dict['name']
                field_type = field.dict['var_type']
                if field_type in self.valid_types:
                    self.struct_LUT[struct_name][field_name] = field_type
                else:
                    super().error(
                        ErrorType.TYPE_ERROR,
                        f"invalid fieldType {field_type} in {field_name}",
                    )
        #print(self.struct_LUT)
        #print(self.valid_types)
    def run(self, program):
        ast = parse_program(program)
        self.env_stack = []
        self.env_stack.append([]) ##[[func1: {scope1,},{scope2}],[func2: {scope1},{scope2}]]
        self.env_stack[-1].append(dict())
        self.valid_types = {"int","bool","string"} #Set
        self.struct_LUT = {} #Look Up Table for the struct structures. 
        structs = ast.dict['structs']
        self.process_structs(structs)
        self.funcs = ast.dict['functions']

        self.func_call("main",[])
    
    
if __name__ == '__main__':
    program_source = """
    

struct s {
  a:int;
}

func main() : int {
  var x: s;
  x = new s;
  x = nil;
  print(x.a);
}   
    

    """

    inter = Interpreter()
    inter.run(program_source)