`timescale 1ns/1ns

module sevensegment_CC_TB;
reg [3:0];
reg data;
wire [6:0] data_segment;
sevensegment_CC DUT([3:0], data, data_segment);
initial begin
$dumpfile("sevensegment_CC.vcd");
$dumpvars(0,sevensegment_CC_TB);
{[3:0], data}=2'b00; #1
{[3:0], data}=2'b01; #1
{[3:0], data}=2'b10; #1
{[3:0], data}=2'b11; #1
$finish;
end
endmodule
