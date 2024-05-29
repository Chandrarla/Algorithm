import Foundation

struct Node {
    var left: Character?
    var right: Character?
}

class BinaryTree {
    var nodes: [Character: Node] = [:]
    
    func addNode(parent: Character, left: Character?, right: Character?) {
        nodes[parent] = Node(left: left, right: right)
    }
    
    func preorderTraversal(node: Character?, result: inout String) {
        guard let node = node else { return }
        result.append(node)
        preorderTraversal(node: nodes[node]?.left, result: &result)
        preorderTraversal(node: nodes[node]?.right, result: &result)
    }
    
    func inorderTraversal(node: Character?, result: inout String) {
        guard let node = node else { return }
        inorderTraversal(node: nodes[node]?.left, result: &result)
        result.append(node)
        inorderTraversal(node: nodes[node]?.right, result: &result)
    }
    
    func postorderTraversal(node: Character?, result: inout String) {
        guard let node = node else { return }
        postorderTraversal(node: nodes[node]?.left, result: &result)
        postorderTraversal(node: nodes[node]?.right, result: &result)
        result.append(node)
    }
}

func readInput() -> (Int, [(Character, Character?, Character?)]) {
    let n = Int(readLine()!)!
    var edges = [(Character, Character?, Character?)]()
    
    for _ in 0..<n {
        let line = readLine()!.split(separator: " ").map { String($0) }
        let parent = Character(line[0])
        let left = line[1] == "." ? nil : Character(line[1])
        let right = line[2] == "." ? nil : Character(line[2])
        edges.append((parent, left, right))
    }
    
    return (n, edges)
}

func main() {
    let (_, edges) = readInput()
    let tree = BinaryTree()
    
    for edge in edges {
        tree.addNode(parent: edge.0, left: edge.1, right: edge.2)
    }
    
    var preorderResult = ""
    var inorderResult = ""
    var postorderResult = ""
    
    tree.preorderTraversal(node: "A", result: &preorderResult)
    tree.inorderTraversal(node: "A", result: &inorderResult)
    tree.postorderTraversal(node: "A", result: &postorderResult)
    
    print(preorderResult)
    print(inorderResult)
    print(postorderResult)
}

main()