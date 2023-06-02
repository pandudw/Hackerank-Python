### Task
The provided code stub reads two integers from STDIN, a and b. Add code to print three lines where:

- The first line contains the sum of the two numbers.
- The second line contains the difference of the two numbers (first - second).
- The third line contains the product of the two numbers.

#### Example
a = 3 and b = 5
#### Input format
- The first line contains the first integer, a.
- The second line contains the second integer, b.
#### Constraints
1 <= n <= 10^10  
1 <= n <= 10^10 
#### Sample Input 
> 3  
> 2
#### Sample Ouput 
> 5  
> 1  
> 6
#### Explanation 
Line 1 : 3 + 2 = 5  
Line 2 : 3 - 1 = 1    
Line 3 : 3 * 2 = 6
### Solution
```python
a = int(input())
b = int(input())

print((a + b), (a - b), (a * b), sep='\n')
```
or you can use 
```python
a = int(input())
b = int(input())
print("{0}\n{1}\n{2}".format((a + b), (a - b), (a * b)))
```


