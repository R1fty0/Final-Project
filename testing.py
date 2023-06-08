def execute_if_statement(if_statement):
    if_statement = if_statement.strip()  # Remove leading/trailing whitespace
    if if_statement.endswith(":"):
        if_body = if_statement[:-1]  # Remove the colon at the end
        try:
            exec(if_body)
            print("If statement executed successfully.")
        except Exception as e:
            print("Error occurred while executing the if statement:")
            print(e)
    else:
        print("Invalid if-statement. It should end with a colon.")

# Example usage:
if_statement = "4 < 5:"
execute_if_statement(if_statement)