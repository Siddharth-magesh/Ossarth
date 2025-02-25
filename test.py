from Ossarth.tool_manager import CustomFunctionManager

manager = CustomFunctionManager(result_dir="tests")

manager.create_custom_tool(
    func_name="test_tool",
    description="A test tool function.",
    params="param1: int, param2: str",
    args_doc="param1 (int): An integer.\nparam2 (str): A string.",
    return_type="str",
    return_desc="A formatted string.",
    body="return f'Test tool with {param1} and {param2}'",
    filename="new"
)

manager.create_custom_function(
    func_name="test_function",
    description="A test helper function.",
    params="x: int, y: int",
    args_doc="x (int): First number.\ny (int): Second number.",
    return_type="int",
    return_desc="Sum of x and y.",
    body="return x + y",
    filename="new"
)
