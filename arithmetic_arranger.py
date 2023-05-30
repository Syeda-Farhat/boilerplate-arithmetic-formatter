def arithmetic_arranger(problems, show_answers=False):
    # Check the number of problems
    if len(problems) > 5:
        return "Error: Too many problems."

    # Initialize empty lists for each line of arranged problems
    first_lines = []
    second_lines = []
    dashes = []
    answers = []

    for problem in problems:
        # Split the problem into operands and operator
        operand1, operator, operand2 = problem.split()

        # Check the operator
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Check the operands
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."
        
        # Check the number of digits in the operands
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Determine the maximum length of the operands for spacing
        max_length = max(len(operand1), len(operand2))

        # Create the arranged lines for the current problem
        first_line = operand1.rjust(max_length + 2)
        second_line = operator + operand2.rjust(max_length + 1)
        dash_line = '-' * (max_length + 2)
        answer_line = str(eval(problem)).rjust(max_length + 2) if show_answers else ''

        # Add the lines to the respective lists
        first_lines.append(first_line)
        second_lines.append(second_line)
        dashes.append(dash_line)
        answers.append(answer_line)

    # Combine the lines with appropriate spacing
    arranged_problems = '    '.join(first_lines) + '\n'
    arranged_problems += '    '.join(second_lines) + '\n'
    arranged_problems += '    '.join(dashes)
    
    if show_answers:
        arranged_problems += '\n' + '    '.join(answers)

    return arranged_problems
