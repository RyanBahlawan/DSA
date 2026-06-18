class Solution:
    def isValid(self, s: str) -> bool:
        seen = []
        closedToOpen = {"]":"[", "}":"{", ")":"("}

        for c in s:
            if c in closedToOpen:
                if seen and seen[-1]==closedToOpen[c]:
                    seen.pop()
                else:
                    return False
            else:
                seen.append(c)
        return True if not seen else False