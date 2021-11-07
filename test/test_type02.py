import importlib

import type02 as main 

#Create a test to check if the variable 'var_int' is defined
def test_int_defined():
    assert hasattr(main, 'var_int'), "The variable var_int is not defined"
#Create a test to check if the variable 'var_float' is defined.
def test_float_defined():
    assert hasattr(main, 'var_float'), "The variable var_float is not defined"

#Create a test to check if the varable 'answer' is equal of the sum of the 'var_float' and 'var_str'
def test_answer():
    #Check if the varable 'answer' is defined.
    # assert hasattr(main, 'answer'), "The variable answer is not defined"
    output = main.answer
    #Check if the output is equal to the sum of the 'var_float' and 'var_str'
    #find the sum of the 'var_float' and 'var_str' and assign it the variable expected.
    expected = main.var_float + main.var_int
    assert output == expected, "The value of the variable answer is not equal to the sum of the variable var_float and var_str"

#Create test to check if the variable 'answer''s type is float.
def test_answer_type():
    #Create a variable 'answer'.
    answer = main.answer
    #Check if the variable 'answer' is of type float.
    assert type(answer) == float, "The type of the variable answer is not float"
