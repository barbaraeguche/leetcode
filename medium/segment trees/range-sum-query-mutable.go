package segment_trees

// name: 307. range sum query - mutable
// link: https://leetcode.com/problems/range-sum-query-mutable

// SegmentNode solution //
type SegmentNode struct {
	Sum         int
	L, R        int
	Left, Right *SegmentNode
}

func (sn *SegmentNode) Build(nums []int, L, R int) *SegmentNode {
	if L == R {
		return &SegmentNode{Sum: nums[L], L: L, R: R}
	}

	M := (L + R) / 2

	// build the tree
	root := &SegmentNode{L: L, R: R}
	root.Left = sn.Build(nums, L, M)
	root.Right = sn.Build(nums, M+1, R)

	root.Sum = root.Left.Sum + root.Right.Sum
	return root
}

func (sn *SegmentNode) Update(index, val int) {
	if sn.L == sn.R {
		sn.Sum = val
		return
	}

	M := (sn.L + sn.R) / 2

	if index <= M {
		sn.Left.Update(index, val)
	} else {
		sn.Right.Update(index, val)
	}

	sn.Sum = sn.Left.Sum + sn.Right.Sum
}

func (sn *SegmentNode) RangeQuery(L, R int) int {
	if sn.L == L && sn.R == R {
		return sn.Sum
	}

	M := (sn.L + sn.R) / 2

	if L > M {
		return sn.Right.RangeQuery(L, R)
	} else if R <= M {
		return sn.Left.RangeQuery(L, R)
	} else {
		return sn.Left.RangeQuery(L, M) + sn.Right.RangeQuery(M+1, R)
	}
}

type NumArray struct {
	root *SegmentNode
}

func Constructor(nums []int) NumArray {
	dummy := SegmentNode{}
	root := dummy.Build(nums, 0, len(nums)-1)
	return NumArray{root: root}
}

func (na *NumArray) Update(index int, val int) {
	na.root.Update(index, val)
}

func (na *NumArray) SumRange(left int, right int) int {
	return na.root.RangeQuery(left, right)
}

/**
time complexity:
- O(n)

space complexity:
- O(n)
*/
