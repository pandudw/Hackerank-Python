# PROBLEM
Link: [Can Convert String in K Moves](https://leetcode.com/problems/can-convert-string-in-k-moves/)

Given two strings `s` and `t`, your goal is to convert `s` into `t` in `k` moves or less.

During the `ith` (`1 <= i <= k`) move you can:

- Choose any index `j` (1-indexed) from `s`, such that `1 <= j <= s`.length and `j` has not been chosen in any previous move, and shift the character at that index `i` times.
Do nothing.
- Shifting a character means replacing it by the next letter in the alphabet (wrapping around so that 'z' becomes 'a'). Shifting a character by `i` means applying the shift operations `i` times.

Remember that any index j can be picked at most once.

Return `true` if it's possible to convert `s` into `t` in no more than `k` moves, otherwise return `false`.

# INPUT AND OUTPUT FORMAT
Example 1:

    Input: s = "input", t = "ouput", k = 9
    Output: true
    Explanation: In the 6th move, we shift 'i' 6 times to get 'o'. And in the 7th move we shift 'n' to get 'u'.

Example 2:

    Input: s = "abc", t = "bcd", k = 10
    Output: false
    Explanation: We need to shift each character in s one time to convert it into t. We can shift 'a' to 'b' during the 1st move. However, there is no way to shift the other characters in the remaining moves to obtain t from s.

Example 3:

    Input: s = "aab", t = "bbb", k = 27
    Output: true
    Explanation: In the 1st move, we shift the first 'a' 1 time to get 'b'. In the 27th move, we shift the second 'a' 27 times to get 'b'.


# ANALYSIS 
Pendekatan yang diambil adalah untuk menghitung apakah perbedaan antar karakter pada setiap posisi pada string s dan t melebihi k atau tidak.
Akan tetapi, hanya memeriksa perbedaannya saja tidak cukup, karena jika terdapat dua karakter yang memiliki perbedaan yang sama, maka perbedaan aktualnya merupakan angka tersebut ditambah dengan `26 * jumlah kemunculan perbedaan tersebut sebelumnya` (Digunakan 26, karena tertulis pada soal bahwa s dan t hanya dapat terdiri atas huruf kecil alfabet).

Maka dari itu, perlu sebuah struktur data untuk menyimpan jumlah kemunculan sebuah perbedaan antar dua karakter (`diff`). Dipilih untuk digunakan sebuah array statik 1D (`freq`) dengan panjang 26, dengan indeks `i` merepresentasikan `diff` dan `freq[i]` merepresentasikan jumlah kemunculannya.

Selanjutnya akan dilakukan iterasi sebanyak panjang s kali, dan pada setiap iterasinya, akan dilakukan beberapa langkah berikut:
1. Perhitungan perbedaan `diff`
2. Perhitungan perbedaan aktual `multDiff = diff + 26 * freq[diff]`
3. Pengecekan apakah `multDiff < k`
4. Inkrementasi nilai `freq[diff]`

Perhatikan ilustrasi jalannya kode berikut:

    Input: s = "abc", t = "bcd", k = 10

    // Jika direpresentasikan dalam kode ASCII, maka didapatkan
    s = [97 98 99]
    t = [98 99 100]

Diinisiasikan sebuah array 1D dengan panjang 26, yang awalnya seluruhnya berisi 0.

    freq = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

Selanjutnya, kita akan mengisi freq dengan jumlah perbedaan antar karakter pada s dan t bersifat round robin (sirkular), dengan memanfaatkan modulo 26.

    // Iterasi 1: 
    t[1] = 98 
    s[1] = 97
    diff = 98 - 97 = 1
    multDiff = 1 + 26 * 0 = 1
    freq = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    multDiff <= k -> Lanjut

    // Iterasi 2: 
    t[1] = 99 
    s[1] = 98
    diff = 99 - 98 = 1
    multDiff = 1 + 26 * 1 = 27
    freq = [0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    multDiff > k -> Berhenti

**Time Complexity: O(n)**<br>
**Space Complexity: O(1)**

# CODE IMPLEMENTATION
```golang
func canConvertString(s string, t string, k int) bool {

    if len(s) != len(t) {return false} // Default false

    freq := make([]int, 26) // Array to hold frequency of circular difference

    for i := range s {

        if t[i] != s[i] {
            diff := ((int(t[i]) - int(s[i])) + 26) % 26 // Modulo to get distance from the two letters
            multDiff := freq[diff] * 26 + int(diff) // Diff multiplied by number of prev occurence
            if multDiff > k { // Actual difference exceeds k
                return false
            }

            freq[diff]++ // Increase occurrence of diff
        }
        
    }

    return true

}
```
