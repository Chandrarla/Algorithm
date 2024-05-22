import Foundation

let n = Int(readLine()!)!

var score = [Int](repeating: 0, count: n + 1)

for i in 1...n {
    score[i] = Int(readLine()!)!
}

var dp = [Int](repeating: 0, count: n + 1)

dp[1] = score[1]

if n > 1 {
    dp[2] = score[1] + score[2]
}

if n > 2 {
    for i in 3...n {
        dp[i] = max(dp[i-2] + score[i], dp[i-3] + score[i-1] + score[i])
    }
}

print(dp[n])