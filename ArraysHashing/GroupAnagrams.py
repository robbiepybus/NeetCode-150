from collections import defaultdict

class Solution:
    def groupAnagrams(strs: list[str]) -> list[list[str]]:
        # default dict creates a default, in our case an empty list, 
        # if the index/value you are referencing does not exist
        res = defaultdict(list) # mapping charCount to list of Anagrams

        for s in strs:
            count = [0] * 26 # a ... z

            for c in s:
                # clever way of getting the index of the charater in 
                # the alphabet -> ord(c) - ord("a")
                count[ord(c) - ord("a")] += 1
            
            res[tuple(count)].append(s)

        return res.values()


    def MYgroupAnagrams(strs: list[str]) -> list[list[str]]:
        # gave up as solution either wouldnt work or would
        # take a while to code
        
        output = []

        if len(strs) == 1:
            return [strs]
            
        for idx in range(len(strs)):

            words = [strs[idx]]

            countS = {}

            for i in range(len(idx)):
                countS[idx[i]] = 1 + countS.get(idx[i], 0)

            for idx2 in range(idx, len(strs)):

                if len(strs[idx]) != len(strs[idx2]):
                    break

                countT = {}

                for i in range(len(idx2)):
                    countT[idx2[i]] = 1 + countT.get(idx2[i], 0)

                for c in countS:
                    if countS[c] != countT.get(c, 0):
                        return False

                words.append(strs[idx2])

            output.append(words)


if __name__ == "__main__":
    print(Solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))