# PROBLEM
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.  
You may assume that each input would have exactly one solution, and you may not use the same element twice.  
You can return the answer in any order.  

# INPUT AND OUTPUT FORMAT
Example 1:

    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


Example 2:

    Input: nums = [3,2,4], target = 6
    Output: [1,2]


Example 3:

    Input: nums = [3,3], target = 6
    Output: [0,1]

Constraints:

    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

# ANALYSIS  
Pada soal ini, goalnya adalah mencari dua angka bilangan bulat (nums) dalam sebuah array yang jika dijumlahkan menghasilkan nilai sama dengan target. Untuk menyelesaikan soal ini mari gunakan metode brute force dengan mencoba kemungkinan solusi. 
Saya akan membuat nested loop untuk memeriksa kemungkinan solusi dari pasangan angka.
- Loop pertama akan mengiterai array nums dan mendapatkan indeks i yang merupakan angka pertama dari pasangan.  
- Loop kedua akan mengiterasi array nums dan mendapatkan indeks j yang merupakan angka kedua dari pasangan. 
- Kemudian membuat kondisi, apakah angka pertama dan kedua ketika dijumlahkan sama dengan target. Apabila kondisi ini memenuhi, maka akan mengembalikan nilai slice i dan j, namun apabila tidak akan mengembalikan nilai nil.  


Contoh array nums = [2, 4, 1] dengan target = 3  
- Iterasi 1 untuk loop pertama (i = 0; left = 2)
    - Iterasi 2 untuk loop kedua (j = 1; right = 4) -> 2 + 2 != 3
    - Iterasi 3 untuk loop ketiga (j = 2; right = 1) -> 2 + 1 = 3 (memenuhi)  

- Iterasi 2 untuk loop pertama (i = 1 ; left = 4)
    - Iterasi 2 untuk loop kedua (j = 0; right = 2) -> 4 + 2 != 3
    - Iterasi 3 untuk loop ketiga (j = 3; right = 1) -> 4 + 1 != 3

- Iterasi 3 untuk loop pertama (i = 2; left = 1)
    - Iterasi 2 untuk loop kedua (j = 0; right = 2) -> 1 + 2 = 3 (memenuhi)
    - Iterasi 3 untuk loop ketiga (j = 1; right = 4) -> 1 + 4 != 3  

Apabila sampai akhir looping tidak memenuhi, maka akan mengembalikan nilai nil. 

# CODE IMPLEMENTATION
```golang
func twoSum(nums []int, target int, []int) {
    for i, left = range(nums) {
        for j, right = range(nums) {
            if left + right == target && i != j {
                return []int {i, j}
            }
        }
    }
    return nil
}
```