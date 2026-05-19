func hasDuplicate(nums []int) bool {
    visitedNumsSet := make(map[int]struct{})

    for _, value := range nums {
        _, exists := visitedNumsSet[value]
        if exists { return true }
        visitedNumsSet[value] = struct{}{}
    }

    return false
}
