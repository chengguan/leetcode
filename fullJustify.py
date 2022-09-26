# Problem: https://leetcode.com/problems/text-justification/
# Author: Teo Cheng Guan
# Date: 23-09-2022

class Solution:
    def getWordsLen(self, words: list[str]) -> int:
        totalLength = 0
        for each in words:
            totalLength += len(each)
            
        return totalLength
    
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        output = []
        
        while len(words) > 0:
            newWordList = []
            while len(words) > 0:
                newWord = words.pop(0)
                #print(f'{newWord=}, {self.getWordsLen(newWordList)=}')
                if (self.getWordsLen(newWordList) + len(newWordList) + len(newWord) <= maxWidth):
                    newWordList += [newWord]
                else:
                    words = [newWord] + words
                    output += [self.packJustified(newWordList, maxWidth)]
                    newWordList = []
                    
            if len(newWordList) != 0:
                output += [self.packLeftJustified(newWordList, maxWidth)]
        
        #print(output)
        return output
    
    def packJustified(self, words: list[str], maxWidth: int) -> list[str]:
        JustifiedText = ""
        totalLength = self.getWordsLen(words)
        numWords = len(words)
        extraSpace = maxWidth - totalLength - numWords + 1

        print(f'{totalLength=}, {numWords=}, {extraSpace=}')

        if numWords > 1:
            justifiedGap = int(extraSpace / (numWords - 1)) + 1
            # To be distribute 1 extra space from left to right
            remainingSpace = int(extraSpace % (numWords - 1))
        else:
            justifiedGap = 0
            remainingSpace = extraSpace

        while len(words) > 0:
            JustifiedText += words.pop(0)
            if (len(words) > 0):
                 JustifiedText += ' ' * justifiedGap
            if remainingSpace > 0:
                remainingSpace -= 1
                JustifiedText += ' '
                if (len(words) == 0):
                    JustifiedText += ' ' * remainingSpace

        return JustifiedText
            
    def packLeftJustified(self, words: list[str], maxWidth: int) -> list[str]:
        JustifiedText = ""
        totalLength = self.getWordsLen(words)
        numWords = len(words)
        extraSpace = maxWidth - totalLength - (numWords - 1)
        
        print(f'{totalLength=}, {numWords=}, {extraSpace=}')

        while len(words) > 0:
            newWord = words.pop(0)
            if (len(words) > 0):
                JustifiedText += newWord + " "
            else:
                JustifiedText += newWord
        if extraSpace > 0: 
            JustifiedText = JustifiedText + ' ' * extraSpace

        return JustifiedText
