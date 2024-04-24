"""
- Make sure you are in Lab5A_Tester/tests
- Install pytest with the following terminal command:
        pip install pytest
- Run with the following terminal command:
        pytest tester.py -v --tb=no -s
"""

import pytest
from difflib import SequenceMatcher
from colorama import Fore, Back, Style
import os
import re
from itertools import count

# UPDATE: Replace import with the correct file
import src.axa_Lab5A as student_file


# UPDATE: Ignore whitespace/newline differences
IGNORE_NEWLINE = False
IGNORE_WHITESPACE = True

# Alters actual and expected to replace all patterns with replacement to ignore newline/whitespace
update_output = lambda pattern, replacement, actual, expected:\
    [re.sub(pattern, replacement, text) for text in (actual, expected)]

# DO NOT CHANGE
ptest_input = lambda num: rf"TestCases/ProgramTests/P{num}_Input.txt"
ptest_output = lambda num: rf"TestCases/ProgramTests/P{num}_Expected_Output.txt"
utest_output = lambda num: rf"TestCases/UnitTests/U{num}_Expected_Output.txt"
test_iter = count(start=1)


@pytest.mark.parametrize("case", [("Program Test: Compare Output (1)",),
                                  ("Program Test: Compare Output (2)",)], ids=lambda x: x[0])
def test_main(capsys, monkeypatch, case):
    case_num = next(test_iter)
    
    # Read inputs from file, stripping trailing whitespace
    with open(ptest_input(case_num), 'r') as file:
        user_input = [line.rstrip() for line in file.readlines()]
    input_iter = iter(user_input)
    monkeypatch.setattr('builtins.input', lambda prompt='': (print(prompt), next(input_iter))[1])
    
    # Read expected output from file
    with open(ptest_output(case_num), 'r') as file:
        expected_output = file.read()

    # Run function to test
    # student_file.main_with_errors()
    student_file.main()

    # Capture program output
    actual_output, _ = capsys.readouterr()
    
    # Write actual output to file
    with open(f'ActualOutput/P{case_num}_Actual_Output.txt', 'w') as output_file:
        output_file.write(actual_output)

    # Show differences (does not necessarily mean test case failed)
    if actual_output != expected_output:
        show_print_difference(actual_output, expected_output)

    # Remove newline/whitespace if desired
    if IGNORE_WHITESPACE:
        actual_output, expected_output = update_output(r'\s*', '', actual_output, expected_output)
    elif IGNORE_NEWLINE:
        actual_output, expected_output = update_output(r'\n*', '\n', actual_output, expected_output)

    assert actual_output == expected_output


# case: ("test_name", function_input, expected_return)
@pytest.mark.parametrize("case", [("Unit Test on hex_char_decode (1)", 'f', 15),
                                  ("Unit Test on hex_char_decode (2)", '0', 0)], ids=lambda x: x[0])
def test_hex_char_decode(capsys, case):
    case_num = next(test_iter)
    function_input, expected_return = case[1:3]
    
    # Read expected output from file (if any)
    expected_output = ''
    if os.path.exists(utest_output(case_num)):
        with open(utest_output(case_num), 'r') as file:
            expected_output = file.read()
            
    # Run function
    actual_return = student_file.hex_char_decode(function_input)

    # Capture program output
    actual_output, _ = capsys.readouterr()
    
    # Write actual output to file
    with open(f'ActualOutput/U{case_num}_Actual_Output.txt', 'w') as output_file:
        output_file.write(actual_output)

    # Show differences (does not necessarily mean test case failed)
    if actual_output != expected_output:
        show_print_difference(actual_output, expected_output)
    if actual_return != expected_return:
        show_return_difference(actual_return, expected_return)

    # Remove newline/whitespace if desired
    if IGNORE_WHITESPACE:
        actual_output, expected_output = update_output(r'\s*', '', actual_output, expected_output)
    elif IGNORE_NEWLINE:
        actual_output, expected_output = update_output(r'\n*', '\n', actual_output, expected_output)

    assert actual_output == expected_output
    assert actual_return == expected_return


# case: ("test_name", function_input, expected_return)
@pytest.mark.parametrize("case", [("Unit Test on binary_string_decode (1)", "0b11000000111001", 12345),
                                  ("Unit Test on binary_string_decode (2)", "0b00011111111", 255),
                                  ("Unit Test on binary_string_decode (3)", "101011111111", 2815)], ids=lambda x: x[0])
def test_binary_string_decode(capsys, case):
    case_num = next(test_iter)
    function_input, expected_return = case[1:3]
    
    # Read expected output from file (if any)
    expected_output = ''
    if os.path.exists(utest_output(case_num)):
        with open(utest_output(case_num), 'r') as file:
            expected_output = file.read()
            
    # Run function
    actual_return = student_file.binary_string_decode(function_input)

    # Capture program output
    actual_output, _ = capsys.readouterr()

    # Write actual output to file
    with open(f'ActualOutput/U{case_num}_Actual_Output.txt', 'w') as output_file:
        output_file.write(actual_output)

    # Show differences (does not necessarily mean test case failed)
    if actual_output != expected_output:
        show_print_difference(actual_output, expected_output)
    if actual_return != expected_return:
        show_return_difference(actual_return, expected_return)

    # Remove newline/whitespace if desired
    if IGNORE_WHITESPACE:
        actual_output, expected_output = update_output(r'\s*', '', actual_output, expected_output)
    elif IGNORE_NEWLINE:
        actual_output, expected_output = update_output(r'\n*', '\n', actual_output, expected_output)

    assert actual_output == expected_output
    assert actual_return == expected_return


# case: ("test_name", function_input, expected_return)
@pytest.mark.parametrize("case", [("Unit Test on hex_string_decode (1)", "4D2", 1234),
                                  ("Unit Test on hex_string_decode (2)", "0xCaBdEfA", 212590330),
                                  ("Unit Test on hex_string_decode (3)", "0x4321ab00", 1126279936)], ids=lambda x: x[0])
def test_hex_string_decode(capsys, case):
    case_num = next(test_iter)
    function_input, expected_return = case[1:3]
    
    # Read expected output from file (if any)
    expected_output = ''
    if os.path.exists(utest_output(case_num)):
        with open(utest_output(case_num), 'r') as file:
            expected_output = file.read()
            
    # Run function
    # actual_return = student_file.hex_string_decode_with_errors(function_input)
    actual_return = student_file.hex_string_decode(function_input)

    # Capture program output
    actual_output, _ = capsys.readouterr()
    
    # Write actual output to file
    with open(f'ActualOutput/U{case_num}_Actual_Output.txt', 'w') as output_file:
        output_file.write(actual_output)

    # Show differences (does not necessarily mean test case failed)
    if actual_output != expected_output:
        show_print_difference(actual_output, expected_output)
    if actual_return != expected_return:
        show_return_difference(actual_return, expected_return)

    # Remove newline/whitespace if desired
    if IGNORE_WHITESPACE:
        actual_output, expected_output = update_output(r'\s*', '', actual_output, expected_output)
    elif IGNORE_NEWLINE:
        actual_output, expected_output = update_output(r'\n*', '\n', actual_output, expected_output)

    assert actual_output == expected_output
    assert actual_return == expected_return


# case: ("test_name", function_input, expected_return)
@pytest.mark.parametrize("case", [("Unit Test on binary_to_hex", "010111111010", "5fa")], ids=lambda x: x[0])
def test_binary_to_hex(capsys, case):
    case_num = next(test_iter)
    function_input, expected_return = case[1:3]
    
    # Read expected print from file (if any)
    expected_output = ''
    if os.path.exists(utest_output(case_num)):
        with open(utest_output(case_num), 'r') as file:
            expected_output = file.read()
            
    # Run function
    actual_return = student_file.binary_to_hex(function_input).lower()

    # Capture program output
    actual_output, _ = capsys.readouterr()
    
    # Write actual output to a file in the 'ActualOutput' folder
    with open(f'ActualOutput/U{case_num}_Actual_Output.txt', 'w') as output_file:
        output_file.write(actual_output)

    # Show differences (does not necessarily mean test case failed)
    if actual_output != expected_output:
        show_print_difference(actual_output, expected_output)
    if actual_return != expected_return:
        show_return_difference(actual_return, expected_return)

    # Remove newline/whitespace if desired
    if IGNORE_WHITESPACE:
        actual_output, expected_output = update_output(r'\s*', '', actual_output, expected_output)
    elif IGNORE_NEWLINE:
        actual_output, expected_output = update_output(r'\n*', '\n', actual_output, expected_output)

    assert actual_output == expected_output
    assert actual_return == expected_return


def show_print_difference(actual_output, expected_output):
    """
    Highlight differences between actual and expected output
    :param actual_output:
    :param expected_output:
    :return:
    """

    # Display Color Coding
    print(f"\n\n{Style.BRIGHT}{Fore.LIGHTYELLOW_EX}========== COLOR CODES =========={Style.NORMAL}")
    print(f"{Fore.LIGHTRED_EX}{Back.RED} Delete ", end='')
    print(f"{Fore.LIGHTGREEN_EX}{Back.GREEN} Insert ", end='')
    print(f"{Back.MAGENTA}{Fore.LIGHTMAGENTA_EX} Extra ", end='')
    print(f"{Back.BLUE}{Fore.LIGHTBLUE_EX} Missing {Back.RESET}")

    # Display Output Difference
    print(f"{Style.BRIGHT}{Fore.LIGHTYELLOW_EX}========== OUTPUT DIFF ==========")
    print(Style.NORMAL, end='')
    matcher = SequenceMatcher(None, actual_output, expected_output)

    # Iterate through matcher tokens
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        text = None
        if tag == 'equal':
            text = Fore.WHITE + actual_output[i1:i2]

        elif tag == 'replace':
            # Replace tokens containing multiple whitespace characters with a single '\\s' for readabiltiy
            text = Back.RED + Fore.LIGHTRED_EX + actual_output[i1:i2] + Back.GREEN + Fore.LIGHTGREEN_EX + expected_output[j1:j2]
            if re.match(rf"^[\s]*$", actual_output[i1:i2]):
                text = Back.RED + Fore.LIGHTRED_EX + '\\s' + Back.GREEN + Fore.LIGHTGREEN_EX + expected_output[j1:j2]

        elif tag == 'delete':
            # Replace tokens containing multiple whitespace characters with a single '\\s' for readabiltiy
            text = Back.MAGENTA + Fore.LIGHTMAGENTA_EX + actual_output[i1:i2]
            if re.match(rf"^\s*$", actual_output[i1:i2]):
                text = Back.MAGENTA + Fore.LIGHTMAGENTA_EX + '\\s'

        elif tag == 'insert':
            text = Back.BLUE + Fore.LIGHTBLUE_EX + expected_output[j1:j2]
        print(f"{text}{Back.RESET}{Fore.RESET}", end='')

    print(f"{Back.RESET}{Style.BRIGHT}{Fore.LIGHTYELLOW_EX}\n================================={Style.RESET_ALL}{Fore.RESET}\n")


def show_return_difference(actual_return, expected_return):
    """
    Highlight differences between actual and expected return values
    :param actual_return:
    :param expected_return:
    :return:
    """
    print(f"{Style.BRIGHT}{Fore.LIGHTYELLOW_EX}\n\n========== RETURN DIFF =========={Style.NORMAL}")
    print(f"{Fore.LIGHTCYAN_EX}Actual:\t  {Fore.LIGHTWHITE_EX}(value: {actual_return}, type: {type(actual_return)})")
    print(f"{Fore.LIGHTCYAN_EX}Expected: {Fore.LIGHTWHITE_EX}(value: {expected_return}, type: {type(expected_return)})")
    print(f"{Style.BRIGHT}{Fore.LIGHTYELLOW_EX}================================={Style.RESET_ALL}")