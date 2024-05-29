import Foundation

func readInput() -> (Int, Int, [[Int]]) {
    let n = Int(readLine()!)!
    let m = Int(readLine()!)!
    var edges = [[Int]]()
    
    for _ in 0..<m {
        let edge = readLine()!.split(separator: " ").map { Int($0)! }
        edges.append(edge)
    }
    
    return (n, m, edges)
}

func buildGraph(n: Int, edges: [[Int]]) -> [[Int]] {
    var graph = Array(repeating: [Int](), count: n + 1)
    
    for edge in edges {
        let a = edge[0]
        let b = edge[1]
        graph[a].append(b)
        graph[b].append(a)
    }
    
    return graph
}

func bfs(graph: [[Int]], start: Int) -> Int {
    var visited = Array(repeating: false, count: graph.count)
    var queue = [start]
    var level = 0
    var count = 0
    
    visited[start] = true
    
    while !queue.isEmpty {
        let currentLevelSize = queue.count
        for _ in 0..<currentLevelSize {
            let node = queue.removeFirst()
            for neighbor in graph[node] {
                if !visited[neighbor] {
                    visited[neighbor] = true
                    queue.append(neighbor)
                    if level < 2 {
                        count += 1
                    }
                }
            }
        }
        level += 1
        if level >= 2 {
            break
        }
    }
    
    return count
}

func main() {
    let (n, _, edges) = readInput()
    let graph = buildGraph(n: n, edges: edges)
    
    let inviteCount = bfs(graph: graph, start: 1)
    
    print(inviteCount)
}

main()
