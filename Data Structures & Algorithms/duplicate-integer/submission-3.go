func hasDuplicate(nums []int) bool {
    visitedNumsSet := make(map[int]bool)

    for _, value := range nums {
        if visitedNumsSet[value] { return true }
        visitedNumsSet[value] = true
    }

    return false
}
