#  "It is a period of civil war. Rebel programs, striking from a hidden computer, have won their first victory against the evil System Tests."
# 
# You might be aware that the events of the Star Wars saga took place a long time ago, in a galaxy that was rather far away. But just how far away was it? We can try to describe it by repeating the word far a certain number of times in the following sentence format:
# A long time ago in a galaxy far, far away...
# 
# In the above example, the word far is repeated twice. However, we'd instead like to repeat it exactly N ( 1 ≤ N ≤ 5 ) times without changing the rest of the sentence at all. There should be a comma right after each occurrence except for the last one.
# 
# Given N , can you produce the correct sentence?
# Input Specification
# 
# The input consists of a single integer N .
# Output Specification
# 
# Output on a single line the appropriate sentence with far repeated N times. It must match the correct answer exactly!
start = 'A long time ago in a galaxy '
end = 'far away...'
times = int(input()) - 1    
how_far = 'far, '
print(start + how_far * times + end)
