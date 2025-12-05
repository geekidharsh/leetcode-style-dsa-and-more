# 2300. Successful Pairs of Spells and Potions

# Input: 
spells = [3,1,2]
potions = [8,5,8]
success = 16

# Output: [2,0,2]
def successfulPairs(spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        result = []
        potions.sort()
        m = len(spells)
        n = len(potions)
        for i in range(m):
            j = 0 
            while j < n and spells[i] * potions[j] < success:
                j += 1
            result.append(n - j)

        return result

print(successfulPairs(spells, potions, success))