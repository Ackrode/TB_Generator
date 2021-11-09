import re
from backbone import *
def text_match(pattern,text):
        if re.search(pattern,text):
                return 1 
        else:
                return 0



def get_inouts(text):
     filed=open(text,'r')
     f=filed.read()

# encontrar entradas
     patron=r'(input|output|inout)[\s]+([^;)]+)*'
     m=re.findall(patron,f)
# print(m[1])


     list_entrada=[]
     for i in m:
          list_entrada.append(i)

     type_name = ['input','output','inout','reg', 'wire', 'wire', "ERROR"]
     inputs=[]
     outputs=[]
     inoutputs=[]
     insize=[]
     outsize=[]
     inoutsize=[]

     type=[]

     patron1=r'([a-zA-Z_a-zA-Z])([^,\s])*'
     patron2=r'(reg|wire)'
     patron3=r'([^:\s\[\]\n])\b'
     patron4=r'([\[\]])'
     for i in range(0,len(list_entrada)):
          if list_entrada[i][0]==type_name[0]:
               modep=1
          elif list_entrada[i][0]==type_name[1]: 
               modep=2
          elif list_entrada[i][0]==type_name[2]: 
               modep=3
          else:
               modep=4
          s=[]
          c=[]
          n=[]
          m1=[]
          m=[]
          n1=[]
          input=[]
          nameport=[]
          n=list_entrada[i][1].split(',')
          n1=n[0].split(' ')
          for i in range(0,len(n1)):
               c.append(n1[i])
          for i in range(1,len(n)):
               c.append(n[i]) 
       
          k=text_match(patron2,c[0])
          if k==1:
               b=1        
          else:
               for i in range(0,len(c)):
                    nameport.append(c[i])
                    s.append('0')
                    b=0
          if b==1:
               k1=text_match(patron4,c[1])
        
               if k1==1:
                    m1=re.findall(patron3,c[1])
         
                    for i in range(2,len(c)):
                         nameport.append(c[i])
                         s.append(tuple(m1))
               else:
                    for i in range(1,len(c)):
                         nameport.append(c[i])
                         s.append('0') 
      
          if modep==1:
               for i in range(0,len(nameport)):
                    inputs.append(nameport[i]) 
               for i in range(0,len(s)):
                    insize.append(s[i]) 
          elif modep==2:
               for i in range(0,len(nameport)):
                    outputs.append(nameport[i]) 
               for i in range(0,len(s)):
                    outsize.append(s[i]) 
          elif modep==3:
               for i in range(0,len(nameport)):
                    inoutputs.append(nameport[i]) 
               for i in range(0,len(s)):
                    inoutsize.append(s[i]) 
          else:  
               0
     inputS = []
     for item in inputs:
          if item not in inputS:
               inputS.append(item)
     outputS = []
     for item in outputs:
          if item not in outputS:
               outputS.append(item)
     inoutputS = []
     for item in inoutputs:
          if item not in outputS:
               inoutputS.append(item)
     dict_from_inputs={'name':inputS,'size':insize}    
     dict_from_outputs={'name':outputS,'size':outsize}
     dict_from_inoutputs={'name':inoutputS,'size':inoutsize}
     return dict_from_inputs, dict_from_outputs, dict_from_inoutputs
#print(get_inouts('design.sv'))