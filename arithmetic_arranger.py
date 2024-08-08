def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    for problem in problems:
        if problem.find('*') != -1 or problem.find('/') != -1:
            return "Error: Operator must be '+' or '-'."

        if not problem.translate(str.maketrans({'+': '', '-': '', ' ': ''})).isdigit():
            return 'Error: Numbers must only contain digits.'

        digits = 0
        for char in problem:
            digits = digits + 1 if char.isdigit() else 0
            if digits > 4:
                return 'Error: Numbers cannot be more than four digits.'
        
    problems_divided = []
    for problem in problems:
        problems_divided.append(problem.split(' '))
    
    top = ''
    middle = ''
    dashes = ''
    bottom = ''
    for problem in problems_divided:
        max_length = max(len(problem[0]), len(problem[2]))
        line_length = max_length + 2

        if problems_divided.index(problem) == 0:
            top += ' '*(line_length - len(problem[0])) + problem[0]
            middle += problem[1] + ' '*(line_length - len(problem[2]) - 1) + problem[2]
            dashes += '-'*line_length

            result = str(int(problem[0]) + int(problem[2])) if problem[1] == '+' else str(int(problem[0]) - int(problem[2]))

            bottom += ' '*(line_length - len(result)) + result
        else:
            top += ' '*4 + ' '*(line_length - len(problem[0])) + problem[0]
            middle += ' '*4 + problem[1] + ' '*(line_length - len(problem[2]) - 1) + problem[2]
            dashes += ' '*4 + '-'*line_length

            result = str(int(problem[0]) + int(problem[2])) if problem[1] == '+' else str(int(problem[0]) - int(problem[2]))

            bottom += ' '*4 + ' '*(line_length - len(result)) + result
        
    if show_answers:
        output_string = f'{top}\n{middle}\n{dashes}\n{bottom}'
    else:
        output_string = f'{top}\n{middle}\n{dashes}'
    
    return output_string 

print(f'{arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)}')