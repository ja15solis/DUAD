# range function: start, stop, and step arguments

string = "I like listening to music in my spare time"

#start with len -1 because the index starts in 0
#end in -1 because the range function does not ent at the specific end, it ends at the previous value before the end
# step is -1 because we want to print the text in reverse 
for index in range(len(string) -1,-1,-1):  
    print( string[index])