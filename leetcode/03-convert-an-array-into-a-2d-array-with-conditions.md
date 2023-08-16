# PROBLEM
Link: [Convert an Array Into a 2D Array With Conditions](https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/)

You are given an integer array nums. You need to create a 2D array from nums satisfying the following conditions:

- The 2D array should contain only the elements of the array nums.
- Each row in the 2D array contains distinct integers.
- The number of rows in the 2D array should be minimal.
- Return the resulting array. If there are multiple answers, return any of them.

Note that the 2D array can have a different number of elements on each row.

# INPUT AND OUTPUT FORMAT
Example 1:

    Input: nums = [1,3,4,1,2,3,1]
    Output: [[1,3,4,2],[1,3],[1]]
    Explanation: We can create a 2D array that contains the following rows:
    - 1,3,4,2
    - 1,3
    - 1
    All elements of nums were used, and each row of the 2D array contains distinct integers, so it is a valid answer.
    It can be shown that we cannot have less than 3 rows in a valid array.

Example 2:

    Input: nums = [1,2,3,4]
    Output: [[4,3,2,1]]
    Explanation: All elements of the array are distinct, so we can keep all of them in the first row of the 2D array.


# ANALYSIS 
Kalimat kunci yang dapat diambil dari persoalan ini adalah bahwa setiap subarray yang terbentuk harus memiliki **nilai elemen yang unik**.
Dari sini, kita dapat menyimpulkan bahwa banyaknya subarray yang akan dibuat adalah sejumlah frekuensi elemen terbanyak pada nums (max_freq).

Untuk menyimpan informasi mengenai jumlah kemunculan setiap elemen pada nums, kita dapat membuat sebuah hash table. 
Dengan mengetahui informasi frekuensi masing-masing elemen, kita dapat menginisiasi sebuah array 2D sepanjang max_freq yang pada awalnya kita biarkan kosong terlebih dahulu.
Selanjutnya kita dapat melakukan iterasi terhadap setiap elemen pada map, dan mengisikannya pada array 2D yang telah dibuat, sebanyak jumlah frekuensi kemunculannya pada nums.

Perhatikan ilustrasi jalannya kode berikut:

    Input: nums = [1,3,4,1,2,3,1]

    // Dibuat sebuah frequency table
    freq = {
        1: 3
        2: 1
        3: 2
        4: 1
    }

Dapat dilihat pada tabel frekuensi yang terbentuk bahwa jumlah kemunculan elemen terbanyak adalah sejumlah 3 kali, yaitu untuk elemen '1'.
Maka, kita akan menginisiasi sebuah array 2D (matrix) dengan jumlah baris = 3.

    matrix = [[], [], []]

Selanjutnya, kita akan mengisi matrix dengan elemen pada nums sesuai dengan jumlah kemunculannya masing-masing.

    // Iterasi 1: k = 1, v = 3
    matrix = [[1], [1], [1]]

    // Iterasi 2: k = 2, v = 1
    matrix = [[1, 2], [1], [1]]

    // Iterasi 3: k = 3, v = 2
    matrix = [[1, 2, 3], [1, 3], [1]]

    // Iterasi 4: k = 4, v = 1
    matrix = [[1, 2, 3, 4], [1, 3], [1]]

**Time Complexity: O(n^2)**<br>
**Space Complexity: O(n)**

# CODE IMPLEMENTATION
```golang
func findMatrix(nums []int) [][]int {

    freq := make(map[int]int) 
    max_freq := 0

    // Initialize frequency table and get maximum frequency
    for _, v := range nums {
        freq[v]++
        if freq[v] > max_freq {
            max_freq = freq[v]
        }
    }
    
    matrix := make([][]int, max_freq) // Initialize result matric

    // Fill in matrix
    for k, v := range freq {
        for i := 0; i < v; i++ {
            matrix[i] = append(matrix[i], k)
        }
    }

    return matrix

}
```
