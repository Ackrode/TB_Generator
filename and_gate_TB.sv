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
and_gate DUT(a,  c,  w, Data,c, dt, out_c1,tc);
initial begin
$dumpfile("and_gate.vcd");
$dumpvars(0,and_gate_TB);
{a, c, w, Data}=5b'00000; #1
{a, c, w, Data}=5b'00001; #1
{a, c, w, Data}=5b'00010; #1
{a, c, w, Data}=5b'00011; #1
{a, c, w, Data}=5b'00100; #1
{a, c, w, Data}=5b'00101; #1
{a, c, w, Data}=5b'00110; #1
{a, c, w, Data}=5b'00111; #1
{a, c, w, Data}=5b'01000; #1
{a, c, w, Data}=5b'01001; #1
{a, c, w, Data}=5b'01010; #1
{a, c, w, Data}=5b'01011; #1
{a, c, w, Data}=5b'01100; #1
{a, c, w, Data}=5b'01101; #1
{a, c, w, Data}=5b'01110; #1
{a, c, w, Data}=5b'01111; #1
{a, c, w, Data}=5b'10000; #1
{a, c, w, Data}=5b'10001; #1
{a, c, w, Data}=5b'10010; #1
{a, c, w, Data}=5b'10011; #1
{a, c, w, Data}=5b'10100; #1
{a, c, w, Data}=5b'10101; #1
{a, c, w, Data}=5b'10110; #1
{a, c, w, Data}=5b'10111; #1
{a, c, w, Data}=5b'11000; #1
{a, c, w, Data}=5b'11001; #1
{a, c, w, Data}=5b'11010; #1
{a, c, w, Data}=5b'11011; #1
{a, c, w, Data}=5b'11100; #1
{a, c, w, Data}=5b'11101; #1
{a, c, w, Data}=5b'11110; #1
{a, c, w, Data}=5b'11111; #1
{a, c, w, Data}=5b'11111; #1
$finish;
end
endmodule
