# Primitive-Calculator

You are given a primitive calculator that can perform the following three operations with the current number 𝑥: multiply 𝑥 by 2, multiply 𝑥 by 3, or add 1 to 𝑥. Your goal is given a positive integer 𝑛, find the minimum number of operations needed to obtain the number 𝑛 starting from the number 1.

Task. Given an integer 𝑛, compute the minimum number of operations needed to obtain the number 𝑛 starting from the number 1.

Input Format. The input consists of a single integer 1 ≤ 𝑛 ≤ 10 6 .

Output Format. In the first line, output the minimum number 𝑘 of operations needed to get 𝑛 from 1. In the second line output a sequence of intermediate numbers. That is, the second line should contain positive integers 𝑎 0 , 𝑎 2 , . . . , 𝑎 𝑘−1 such that 𝑎 0 = 1, 𝑎 𝑘−1 = 𝑛 and for all 0 ≤ 𝑖 < 𝑘 − 1, 𝑎 𝑖+1 is equal to either 𝑎 𝑖 + 1, 2𝑎 𝑖 , or 3𝑎 𝑖 . If there are many such sequences, output any one of them.