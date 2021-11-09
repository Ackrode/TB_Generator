from backbone import *
from GetModule import GetModule
from get_inouts import *

design='design.sv'
inputs, outputs, inouts = get_inouts(design)
print(inputs)
module= GetModule(design)
backbone(inputs, outputs, inouts, module)