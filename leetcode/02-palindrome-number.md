# PROBLEM
Given an integer x, return true if x is a palindrome.  

# INPUT AND OUTPUT FORMAT
Example 1:

    Input: x = 121
    Output: true
    Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:

    Input: x = -121
    Output: false
    Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

    Input: x = 10
    Output: false
    Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

    -231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?

# ANALYSIS 
Bilangan alindrome adalah kondisi dimana jika bilangan memiliki urutan yang sama apabila dibaca dari kanan ke kiri atau sebaliknya kiri ke kanan. 
Di awal kita akan mengeliminasi yang bukan bilangan palindrome yaitu bilangan negatif tidak bisa menjadi bilangan palindrome sehingga x < 0 akan menghasilkan value false.
Untuk menentukan sebuah bilangan apakah palindrome dengan cara menbandingkan digit pertama dengan digit terakhir, kemudian digit kedua dengan digit kedua dari belakang.  

# CODE IMPLEMENTATION
```golang
func isPalindrome(x int) bool {
    if x < 0 {
        return false
    }

    str := strconv.Itoa(x)
    for i, j := 0, len(str)-1; i <= j; i, j = i+1, j-1 {
        if str[i] != str[j] {
            return false
        }
    }
    return true
}
```
