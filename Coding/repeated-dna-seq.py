# hashmap and set
# once you know how to walk through the iteration, this is quite simple
# also can be solved by using two sets: one to keep track of unique and another to keep track of repeated dna seq

def findRepeatedDNASeq(s):
        dna_seq = {}
        n = len(s)

        for i in range(n - 9): #end n9 steps early cos we have i+10
            if s[i: i + 10] in dna_seq:
                dna_seq[s[i:i+10]] += 1
            else:
                dna_seq[s[i:i+10]] = 1
        result = []
        for key in dna_seq:
            if dna_seq[key] > 1:
                result.append(key)
        return result

# Input:
s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# Output: ["AAAAACCCCC","CCCCCAAAAA"]

print(findRepeatedDNASeq(s))