class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        flipped = []
        for row in image:
            flipped.append(row[::-1])
        
        resultImage = []
        for row in flipped:
            curr = []
            for element in row:
                if element == 1:
                    curr.append(0)
                else:
                    curr.append(1)
            resultImage.append(curr)
        return resultImage
        
