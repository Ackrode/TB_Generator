from stimulus import stimulus
def convert(s):
    # initialization of string to ""
    new = "" 
    # traverse in the string 
    for x in s:
        if x==s[-1]:
            new+=x
        else:
            new =new+ x +', '  
    # return string 
    return new
def get_n(inputs=[]):
    n=0
    if inputs:
        for i in inputs.get('size'):
            if len(i)==2:
                n=n+int(i[0])-int(i[1])+1
            else:
                n=n+1

    return n
def backbone(inputs=[], outputs=[],inouts=[], module=''): 


    testbench=[]
    '''
    `timescale 1ns/1ns
    module module+"_TB.v";
    reg inputs;
    wire outputs;
    module DUT(inputs, outputs);
    initial begin 
        $dumpfile("design.vcd");
        $dumpvars(0, module+"_TB);
        // addd stimulus

        $finish;
    end
    endmodule
    '''
    #
    with open(module+"_TB.sv",'w') as file:
        testbench=["`timescale 1ns/1ns\n", 'module '+module +'_TB;']
        j=0
        # if inputs is not empty
        if inputs:
            for name in inputs.get('name'):
                # If the inputs.get('name') size is 1, then the input is a single bit
                if len(inputs.get('size')[j])==2:
                    print(len(inputs.get('size')[j]))
                    if len(inputs.get('name'))==1:
                        testbench.append('reg'+' ['+inputs.get('size')[0]+':' +inputs.get('size')[1]+'] '  + name +';')
                    else:
                        testbench.append('reg'+' ['+inputs.get('size')[j][0]+':' +inputs.get('size')[j][1]+'] '  + name +';')
            
                else:
                    testbench.append('reg '+ name +';')
                j=j+1
        j=0
        if outputs:
            for name in outputs.get('name'):
                if len(outputs.get('size')[j])==2:
                    if len(outputs.get('name'))==1:
                        testbench.append('wire'+' ['+outputs.get('size')[0]+':' +outputs.get('size')[1]+'] '  + name +';')
                    else:
                        testbench.append('wire'+' ['+outputs.get('size')[j][0]+':' +outputs.get('size')[j][1]+'] '  + name +';')
                        
                else:
                    testbench.append('wire '+ name +';')
                j=j+1
        j=0
        if inouts:
            for name in inouts.get('name'):
                if len(inouts.get('size')[j])==2:
                    if len(inouts.get('name'))==1:
                        testbench.append('wire'+' ['+inouts.get('size')[0]+':' +inouts.get('size')[1]+'] '  + name +';')
                    else:
                        testbench.append('wire'+' ['+inouts.get('size')[j][0]+':' +inouts.get('size')[j][1]+'] '  + name +';')
                else:
                    testbench.append('wire '+ name +';')
                j=j+1
                '''
            for name in inouts.get('name'):
                if len(inouts.get('size')[j])==2:
                    if len(inouts.get('name'))==1:
                        testbench.append('reg'+' ['+inouts.get('size')[0]+':' +inouts.get('size')[1]+'] '  + name +';')
                    else:
                        testbench.append('reg'+' ['+inouts.get('size')[j][0]+':' +inouts.get('size')[j][1]+'] '  + name +';')
                        j=j+1
                else:
                    testbench.append('reg '+ name +';')
                '''
        j=0
        intputL=convert(inputs.get('name'))
        outputL=convert(outputs.get('name'))
        inoutL=convert(inouts.get('name'))
        testbench.append(module +' DUT('+intputL+','+outputL+','+inoutL+');')
        testbench.append('initial begin')
        testbench.append('$dumpfile("'+module+'.vcd");')
        testbench.append('$dumpvars(0,'+module+'_TB);')
        numeros=get_n(inputs)
        stimulus_list=stimulus(inputs,numeros)
        for i in stimulus_list:
            testbench.append(i)
        testbench.append('$finish;')
        testbench.append('end')
        testbench.append('endmodule')
        for line in testbench:
            file.write(line+'\n')
        #return the sum of the inputs size
