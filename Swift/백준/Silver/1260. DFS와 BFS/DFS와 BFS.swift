import Foundation

let firstLine = readLine()!.split(separator: " ").map { Int($0)! }
let N = firstLine[0]
let M = firstLine[1]
let V = firstLine[2]

var graph = Array(repeating: Array(repeating: 0, count: N + 1), count: N + 1)

for _ in 0..<M {
    let edge = readLine()!.split(separator: " ").map { Int($0)! }
    let a = edge[0]
    let b = edge[1]
    graph[a][b] = 1
    graph[b][a] = 1
}

var visited1 = Array(repeating: false, count: N + 1)
var visited2 = Array(repeating: false, count: N + 1)

func dfs(_ V: Int) {
    visited1[V] = true
    print(V, terminator: " ")
    for i in 1...N {
        if graph[V][i] == 1 && !visited1[i] {
            dfs(i)
        }
    }
}

func bfs(_ V: Int) {
    var queue = [V]
    visited2[V] = true
    
    while !queue.isEmpty {
        let node = queue.removeFirst()
        print(node, terminator: " ")
        for i in 1...N {
            if graph[node][i] == 1 && !visited2[i] {
                queue.append(i)
                visited2[i] = true
            }
        }
    }
}

dfs(V)
print()
bfs(V)
print()