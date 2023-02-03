import fractions
import sys
from fractions import Fraction
input = sys.stdin.readline

#분자,분모
def solution(top,bot):
    if top == 1:
        return bot
    
    new = bot//top + 1 
    rslt = Fraction(top,bot) - Fraction(1,new)
    #print(rslt.toString())
    return solution(rslt.numerator, rslt.denominator)
    print(rslt.numerator + '/' + rslt.denominator)
    
T = int(input())

for _ in range(T):
    top,bot = map(int,input().split())
    print(solution(top,bot))
    

    





"""
3
4 23
5 7
8 11
"""