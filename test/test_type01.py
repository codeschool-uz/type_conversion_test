import importlib

import type01 as main 

#Create a test to check if the variable 'var' is defined
def test_defined():
    assert hasattr(main, 'var'), "The variable var is not defined"

#Create a test to check if the variable 'var_float' is defined
def test_float_defined():
    assert hasattr(main, 'var_float'), "The variable var_float is not defined"

#Create a test to check if the variable 'var_str' is defined
def test_str_defined():
    assert hasattr(main, 'var_str'), "The variable var_str is not defined"

#Create a test to check if the variable 'var_float' is equal to the float value of the 'var'
def test_float_value():
    output = main.var_float
    #Check if the output is equal to the float value of the 'var'
    #find the float value of the 'var' and assign it the variable expected.
    expected = float(main.var)
    assert output == expected, "The value of the variable var_float is not equal to the float value of the variable var"

#Create a test to check if the variable 'var_str' is equal to the string value of the 'var'
def test_str_value():
    output = main.var_str
    #Check if the output is equal to the string value of the 'var'
    #find the string value of the 'var' and assign it the variable expected.
    expected = str(main.var)
    assert output == expected, "The value of the variable var_str is not equal to the string value of the variable var"
#Create a test to check print value.
def test_print_answer(capsys):
    #Reload the module main
    importlib.reload(main)
    #Catche the output of the print function
    out, err = capsys.readouterr()
    #Split the output of the print function

    output = out.split()
    #Create varable var_float and var_str
    var_float = main.var_float
    var_str = main.var_str

    #Check if the number and answer are equal to the output.
    assert output == [str(var_float), str(var_str)], "The value of the variable number is not equal to the value of the variable answer"

