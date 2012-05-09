#usage: python Q1prep.py [filename] 
#example: python Q1prep.py A-small-practice.in 
#Description: Google code jam Qualification Round 2012 Q1
#           : Preprocess to prepare translation mapping

from sys import argv

#initial translation mapping: "_" -> Never been mapped
mapping = {
" ":" ",
"a":"_",
"b":"_",
"c":"_",
"d":"_",
"e":"_",
"f":"_",
"g":"_",
"h":"_",
"i":"_",
"j":"_",
"k":"_",
"l":"_",
"m":"_",
"n":"_",
"o":"_",
"p":"_",
"q":"_",
"r":"_",
"s":"_",
"t":"_",
"u":"_",
"v":"_",
"w":"_",
"x":"_",
"y":"_",
"z":"_"
}    
     
#print translation mapping for later use   
def printmapping():
    out = "mapping = {"
    for k in sorted(mapping.iterkeys()):
        out +=  '"%s":"%s",' % (k,mapping[k])
    out = out.rstrip(',')
    out += "}"
    print "%s" %out
    
#return mapped word according to translation mapping at the time  
def mapped(str):
    mappedstr = ""
    for i in str :
        mappedstr += mapping[i]
    return mappedstr

#open input file
ifile = open(argv[1])


for i in range(1,int(ifile.readline())) :
    #Get each word in each line
    line = ifile.readline().split(' ')
    
    
    for word in line:
        word = word.rstrip()
        #Display current mapping and ask user what is the correct translation
        cmd = raw_input(word +"="+ mapped(word) + "\n")
        #skip if not sure
        if cmd == "skip" :
            continue
        #break to show translation mapping at the time
        elif cmd == "break" :
            printmapping()
            break
        else :
            #According to user input, update the translation mapping
            for i in range(len(word)) :
                #No change if the translation mapping is already correct
                if mapping[word[i]] == cmd[i] :
                    print "%s = %s correct!" %(mapping[word[i]],cmd[i])
                    continue
                elif mapping[word[i]] == "_" and mapping[word[i]] != cmd[i] :
                    mapping[word[i]] = cmd[i]
                    print "[%s->%s]" % (word[i],cmd[i])
                    
printmapping()


        
    

