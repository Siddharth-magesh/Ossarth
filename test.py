from Ossarth.tool_manager import CustomFunctionManager

manager = CustomFunctionManager(result_dir="tools")

manager.create_custom_tool(
    func_name="addition_tool",
    description="A tool to add two numbers.",
    params="num1: int, num2: int",
    args_doc="num1 (int): The first number.\nnum2 (int): The second number.",
    return_type="int",
    return_desc="The sum of num1 and num2.",
    body="return num1 + num2",
    filename="math"
)
