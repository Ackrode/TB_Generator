`timescale 1ns/1ns

module and_gate_TB;
reg a;
reg  c;
reg  w;
reg [1:0] Data;
wire c;
wire dt;
wire [2:0] out_c1;
wire tc;
and_gate DUT(a,  c,  w, Data, c, dt, out_c1, tc);
initial begin
$dumpfile("and_gate.vcd");
$dumpvars(0,and_gate_TB);
{a c, w, Data}=5'b00000; #1
{a c, w, Data}=5'b00001; #1
{a c, w, Data}=5'b00010; #1
{a c, w, Data}=5'b00011; #1
{a c, w, Data}=5'b00100; #1
{a c, w, Data}=5'b00101; #1
{a c, w, Data}=5'b00110; #1
{a c, w, Data}=5'b00111; #1
{a c, w, Data}=5'b01000; #1
{a c, w, Data}=5'b01001; #1
{a c, w, Data}=5'b01010; #1
{a c, w, Data}=5'b01011; #1
{a c, w, Data}=5'b01100; #1
{a c, w, Data}=5'b01101; #1
{a c, w, Data}=5'b01110; #1
{a c, w, Data}=5'b01111; #1
{a c, w, Data}=5'b10000; #1
{a c, w, Data}=5'b10001; #1
{a c, w, Data}=5'b10010; #1
{a c, w, Data}=5'b10011; #1
{a c, w, Data}=5'b10100; #1
{a c, w, Data}=5'b10101; #1
{a c, w, Data}=5'b10110; #1
{a c, w, Data}=5'b10111; #1
{a c, w, Data}=5'b11000; #1
{a c, w, Data}=5'b11001; #1
{a c, w, Data}=5'b11010; #1
{a c, w, Data}=5'b11011; #1
{a c, w, Data}=5'b11100; #1
{a c, w, Data}=5'b11101; #1
{a c, w, Data}=5'b11110; #1
{a c, w, Data}=5'b11111; #1
$finish;
end
endmodule
