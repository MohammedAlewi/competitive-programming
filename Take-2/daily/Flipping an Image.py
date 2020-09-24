import math
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for pixel in A:
            for i in range( math.ceil(len(pixel)/2) ):
                pixel[i], pixel[len(pixel) -1 -i] = int ( not pixel[len(pixel) -1 -i] ) ,  int ( not pixel[i] )
                
        return A
