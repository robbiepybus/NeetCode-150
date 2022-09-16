s = "hello"
t = "elloh"

def isAnagram(s: str, t: str) -> bool:

    # return sorted(s) == sorted(t)

    # return Counter(s) == Counter(t)

    if len(s) != len(t):
        return False

    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)

    for c in countS:
        if countS[c] != countT.get(c, 0):
            return False

    return True

if __name__ == "__main__":
    print(isAnagram(s, t))