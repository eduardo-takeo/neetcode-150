import unittest
from collections import defaultdict
   
def groupAnagrams( strs: list[str]) ->list[list[str]]:
    res = defaultdict(list)
    
    for s in strs:
         sortedS = ''.join(sorted(s))
         res[sortedS].append(s)
    return list(res.values())

   
   
#######################################################################################
class Tests(unittest.TestCase):
     def test_solution(self):
        input  = ["act","pots","tops","cat","stop","hat"]
        result = [['act', 'cat'], ['pots', 'tops', 'stop'], ['hat']]
 
        self.assertEqual(groupAnagrams(input), result) # Change function name
   
if __name__ == "__main__":
   unittest.main()
