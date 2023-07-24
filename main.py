import ast
def notdangeval(expression):
    tree = ast.parse(expression, mode='eval')
    validate_ast(tree)
    code = compile(tree, filename='', mode='eval')
    return eval(code)

#ограничение eval для безопасности
_allowed_nodes = (
    # базовые узлы:
    ast.BinOp, ast.UnaryOp, ast.Constant,

    # основные BinOps:
    ast.Add, ast.Sub, ast.Mult, ast.Div, ast.FloorDiv, ast.Mod, ast.Pow,

    # основные UnaryOps:
    ast.UAdd, ast.USub
)

def validate_ast(tree):
    # валидируем корень дерева
    if not isinstance(tree, ast.Expression):
        raise Exception('Неправильное выражение')
    # валидируем узлы
    def validate_children(node):
        for child in ast.iter_child_nodes(node):
            if not isinstance(child, _allowed_nodes):
                raise Exception('Неправильное выражение')
            validate_children(child)
            if isinstance(child, ast.Constant) and not isinstance(child.value, (int, float, complex)):
                raise Exception('Неправильное выражение')
    validate_children(tree)

while True:
    calc = input("Enter ('quit' to end): ")
    if calc == "quit":
        break
    try:
        result = notdangeval(calc)
        print("Result:", result)
    except:
        print("Error, not vaild input")