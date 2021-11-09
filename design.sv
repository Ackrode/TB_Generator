
module and_gate(in_a, b,we,ew, a, c, w, Data);
   input a, c, w;
   input wire [1:0] Data;
    output c,dt;
   output wire [2:0] out_c1;
  inout tc;
  
  assign c= a & b;
  
endmodule