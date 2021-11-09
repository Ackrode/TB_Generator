def stimulus(inputs, numero):
    if numero >8:  
        return ValueError("Number of inputs needs to be less than 8")
    else:   
        strings=['']
        for i in range(0,2**numero):
            for name in inputs.get('name'):
                if name==inputs.get('name')[0]:
                    strings[i]='{'+name+','
                elif name==inputs.get('name')[-1]:
                    strings[i]+=' '+name
                else:
                    strings[i]+=name+','   
            strings[i]=strings[i]+'}='+str(numero)+"b'"+str(format(i,'0'+str(numero)+'b')+'; #1')
            strings.append(strings[i])
        return strings  
    #with open('stimulus.txt', 'w') as filehandle:
    #    for listitem in strings[0:-1]:
    #            filehandle.write('%s\n' % listitem)  #write list with every element in a new line
