class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        flipped = []
        for row in image:
            flipped.append(row[::-1])
        
        return[[0 if x==1 else 1 for x in x] for x in flipped] 
