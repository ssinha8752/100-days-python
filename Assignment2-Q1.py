import re
class Q1:

    def start_search(self, d):

        ### REPLACE THE BELOW LINE WITH YOUR CODE ###
        ### DO NOT EDIT ANYTHING ELSE IN THIS FUNCTION ###
        self.pattern = r'(?<!00\.)\b(?!00)\d{1,3}\.\d{2}\b'
        next = "00.00+00.00"
        while next:
            p = re.compile(self.pattern)
            print(p)
            m = p.findall(d[next])
            print(m)
            if not m:
                break
            next = "+".join(m)

        return next


# Run this code to get the feedback for question 1
with open('q1.txt', 'w') as f:
    score = 0
    q1 = Q1()
    ### Open test case # 1 ###
    d = {
        "00.00+00.00": "The next treasure is at 12.34 and 23.45",
        "12.34+23.45": "The fake treasure is in 222.11 and 11.11 and 14.56",
        "222.11+11.11+14.56": "Welcome to your infinite loop at 00.00 and 00.00",
        "222.11+11.11": "Welcome to your infinite loop at 12.34 and 23.45",
        "11.11+14.56": "Congrats!",
    }
    if q1.start_search(d) == "11.11+14.56":
        score += 1
        f.write('[1/1] first sample case is matched\n')
    else:
        f.write('[0/1] first sample case is not matched\n')

    ### Open test case # 2 ###
    d = {
        "00.00+00.00": "The next treasure is at 16.88 and 26.84",
        "16.88+26.84": "The fake treasure is in 00.13 and 55.66 and 14.56",
        "00.13+55.66+14.56": "Welcome to your infinite loop at 00.00 and 00.00",
        "00.13+55.66": "Welcome to your infinite loop at 16.88 and 26.84",
        "55.66+14.56": "Seek 12.1 and you shall find24.55and 14.56.",
        "24.55+14.56": "Congrats!",
    }
    if q1.start_search(d) == "24.55+14.56":
        score += 1
        f.write('[1/1] second sample case is matched\n')
    else:
        f.write('[0/1] second sample case is not matched\n')

    ### Test that the length of pattern is less than or equal to 50 characters ###
    if len(q1.pattern) <= 50:
        score += 1
        f.write('[1/1] pattern is less than or equal to 50 characters\n')
    else:
        f.write('[0/1] pattern is longer than 50 characters\n')

# Output the final score
print(f"Final Score: {score}/3")
