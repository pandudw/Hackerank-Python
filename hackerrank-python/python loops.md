### Task
The provided code stub reads and integer, n, from STDIN. For all non-negative integers i<n , print i^2.  
#### Example
The list of non-negative integers that are less than n = 3 is [0,1,3] . Print the square of each number on a separate line.  
> 0  
> 1  
> 4  
#### Input Format
The first and only line contains the integer, n.
#### Constraints
1 <= n <= 20  
#### Sample Input 
> 5  
#### Sample Output 
> 0  
> 1  
> 4  
> 9  
> 16  
### Solution 
```python
n = int(input())
for i in range(n) :
    print(i**2)
  ```
