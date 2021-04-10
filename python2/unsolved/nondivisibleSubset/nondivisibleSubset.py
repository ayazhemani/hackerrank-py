"""Solution for HackerRank challenge: Non-Divisible Subset
"""

def nondivisible_subset(nums, nonfactor):
    """Description
    """

    # removed = []
    # for i in xrange(0, len(nums)):
    #     for j in xrange(i + 1, len(nums)):
    #         if (nums[i] + nums[j]) % nonfactor != 0:
    #             removed.append(nums[i])
    #             removed.append(nums[j])
    #return len(set(removed))
    count = 0
    nums_remainder = [i % nonfactor for i in nums]
    remainder_count = [nums_remainder.count(i) for i in range(nonfactor)]
    print 'nums_remainder', nums_remainder
    print 'remainder_count', remainder_count
    print 'i, nonfactor - i, count, remainder_count[abs(nonfactor - i)]'
    for i in xrange(1, nonfactor):
        print i, nonfactor - i, count, remainder_count[abs(nonfactor - i)]
        count += remainder_count[abs(nonfactor - i)]
    return count/2 + 1


def main():
    """Receives input from stdin, provides output to stdout.
    """
    s, nonfactor = map(int, raw_input().split(' '))
    numset = map(int, raw_input().split(' '))
    print nondivisible_subset(numset, nonfactor)

if __name__ == '__main__':
    main()
