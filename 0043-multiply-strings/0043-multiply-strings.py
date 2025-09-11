class Solution:
    def multiply(self, num1: str, num2: str) -> str:
                        
        binary_str = bin(int(num1))[2:]        
        back_to_int = int(binary_str, 2)
        binary_str2 = bin(int(num2))[2:]        
        back_to_int2 = int(binary_str2, 2)
        sum=back_to_int*back_to_int2

        return str(sum)

        
        
        