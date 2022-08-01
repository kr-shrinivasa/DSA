# This function should return a function which takes string as input 
# removes all the alphabets which are present in the forbidden_alphabets list
# forbidden_alphabets is a list off alphabets
# Your returned function should take string as input returns a string 
# by removing forbidden alphabets
def word_smith(forbidden_alphabets):
    def chopper(str):
        
        for i in forbidden_alphabets:
            for j in str:
                if i==j:
                    str=str.replace(j,"")
                
        return str
    return chopper
                
### Do not change anything below this line.
if __name__ == "__main__":
    alphabets = [i for i in input().split(' ')]
    input_string = input()
    chopper = word_smith(alphabets)
    print(chopper(input_string))