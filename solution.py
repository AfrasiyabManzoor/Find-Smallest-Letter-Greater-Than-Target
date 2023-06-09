class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        result = letters[0]
        diff = 25

        for letter in letters:
            if ord(letter) - ord(target) > 0 and ord(letter) - ord(target) < diff:
                result = letter
                diff = ord(letter) - ord(target)
        
        return result


