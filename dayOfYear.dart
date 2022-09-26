// Problem: https://leetcode.com/problems/day-of-the-year/
// Author: Teo Cheng Guan
// Date: 16-09-2022

class Solution:
    def dayOfYear(self, date: str) -> int:
      daysInMonth = [0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
      year  = int(date[0:4])
      month = int(date[5:7])
      day   = int(date[8:10])
      
      if (month > 2):
          if ((year % 4) == 0):
            if not (((year % 100) == 0) & ((year % 400) != 0)):
                day += 1;
      day += daysInMonth[month];
      
      return day;
