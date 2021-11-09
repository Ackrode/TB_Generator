import re

# Get the design module python code

def GetModule(SVFilePath):
    f = open(SVFilePath, 'r')
    Pattern1 = re.compile(r'^\s*module\s+(\w+).*')
    for line in f:
        ModuleMatch = Pattern1.match(line)
        if ModuleMatch != None:
            Module = ModuleMatch.group(1)
    try:
        Module
    except:
        print("\nNo module found") 
        Module = "-------"
    f.close()
    return Module