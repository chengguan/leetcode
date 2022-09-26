// Problem: https://leetcode.com/problems/add-binary/
// Author: Teo Cheng Guan
// Dat: 16-09-2022
//

class Solution {
  String addBinary(String a, String b) {
    String SumString = "";
    int Carry = 0;
    int IntermediateSum = 0;
    int index_a = a.length;
    int index_b = b.length;
      
    while (index_a > 0 || index_b > 0)
    {
        if (index_a > 0)
            index_a--;
        if (index_b > 0)
            index_b--;
        IntermediateSum = int.parse(a[index_a]) + int.parse(b[index_b]) + Carry;
        Carry = IntermediateSum >> 1;
        SumString = "${IntermediateSum & 1}" + SumString;
        if (index_a == 0)
            a="0";
        if (index_b == 0)
            b="0";
    }
    if (Carry > 0)
        SumString = "1" + SumString;
      
    return SumString;
  }
}
