from collections import OrderedDict
class Solution(object):
   def longestPalindrome(self, s):
      dp = [[False for i in range(len(s))] for i in range(len(s))]
      for i in range(len(s)):
         dp[i][i] = True
      max_length = 1
      start = 0
      for l in range(2,len(s)+1):
         for i in range(len(s)-l+1):
            end = i+l
            if l==2:
               if s[i] == s[end-1]:
                  dp[i][end-1]=True
                  max_length = l
                  start = i
            else:
               if s[i] == s[end-1] and dp[i+1][end-2]:
                  dp[i][end-1]=True
                  max_length = l
                  start = i
      return s[start:start+max_length]

def remove_duplicate(s): 
    return "".join(OrderedDict.fromkeys(s))
        
x = ["Helloworld","HoChiMinhCity","Theresnohope","Thisisanormalthingtodo","Istilldontknowwhatamidoing",
     "secret ","senones","two","evilive","man",
     "#1wAnT0D0s0m3th1ng#","Istilldontknowwhatamidoing","Pantoneisacolourbutalsothesingularversionofpants.Ifyouwakeupwithagiantzit,youarereallyfacingyourfearswhenyoulookinthemirror.",
     "HEll0w0rld","!@MAOKA123681AS41","FUgo NTitanElSbeGudhfr","12368497Helowrd",
     "sensedev1llivedesnes","sugarredividerragus","stabdevilsteeltimefeedsecretstotslivemeetteetdebedsomesellesemosdebedteetteemevilstotstercesdeefemitleetslivedbats"]

y = ["world","i M","Hope","normalz","doing","students","FF","128","rrior.","carbs","w0rld","1AS","ab","aa","aa"," light ","d0","Pantone","HEll0","81A"]

ob1 = Solution()

for i in range(20):
    print(len(ob1.longestPalindrome(x[i])))
