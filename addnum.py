class Solution(object):
    def addTwoNumbers(self, l1, l2):
        def reverse_and_combine(nums):
            reversed_nums = nums[::-1]                 
            combined_number = int("".join(map(str, reversed_nums)))  
            return combined_number
        
        a=reverse_and_combine(l1)
        b=reverse_and_combine(l2)

        s=a+b

        result = [int(d) for d in str(s)]
        reversed_result = result[::-1]    
        return reversed_result

        

sol=Solution()

print(sol.addTwoNumbers([2,4,3],[5,6,4]))
print(sol.addTwoNumbers([0],[0]))
print(sol.addTwoNumbers([9,9,9,9,9,9,9],[9,9,9,9]))




    

    

        
        