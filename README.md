# LeetCode-128.-Longest-Consecutive-Sequence

We sort the input nums, then we loop through the array and if current element is one larger than previous, we up the current counter by one.
If the previous is equal to the current we continue.
If the chain is broken, we update the longest if current is larger, then we reset the counter to 1 and continue.
Return the largest.
Stats:

Runtime: Beats %91.55
Memory: Beats %95.43