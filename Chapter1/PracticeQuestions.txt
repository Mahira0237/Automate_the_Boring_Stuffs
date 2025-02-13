Practice Questions:

1. Which of the following are operators, and which are values?

*        operator
'hello'  value
-88.8    value
-        operator
/        operator
+        operator
5        operator

2. Which of the following is a variable, and which is a string?

spam        variable
'spam'      string

3. Name three data types.
integer, string, float

4. What is an expression made up of? What do all expressions do?

An expression is made up of values and operators. They evaluate and return a single value

5. This chapter introduced assignment statements, like spam = 10. What is the difference between an expression and a statement?

Assignment is used to store values in variables. The result of an expression can be stored used assignment in a variable. i.e. spam=42+1

6. What does the variable bacon contain after the following code runs?

bacon = 20
bacon + 1

Answer: 21

7. What should the following two expressions evaluate to?

'spam' + 'spamspam'
'spam' * 3

both the expressions will evaluate to spamspamspam

8. Why is eggs a valid variable name while 100 is invalid?

variable names can not start with a number

9. What three functions can be used to get the integer, floating-point number, or string version of a value? 

int(), str(), float()

10. Why does this expression cause an error? How can you fix it?

'I have eaten ' + 99 + ' burritos.'

here 99 is not a string value so cannot be concatenated. 
Corrected code: 
'I have eaten ' + '99' + ' burritos.'


round()

x=round(2.3456,2)
print(x) 

round function returns a floating point number rounder to desired decimal points. here x is 2.35 