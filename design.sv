
module  sevensegment_CC(data, data_segment);
  input wire [3:0] data,data1;
  output reg [6:0] data_segment;
  
   always @*
    begin 
      case (data) 
        4'b0000:  data_segment=7'b1111110;
        4'b0001:  data_segment=7'b0110000;
        4'b0010:  data_segment=7'b1101101;
        4'b0011:  data_segment=7'b1111001;
        4'b0100:  data_segment=7'b0110011;
        4'b0101:  data_segment=7'b1011011;
        4'b0110:  data_segment=7'b1011111;
        4'b0111:  data_segment=7'b1110000;
        4'b1000:  data_segment=7'b1111111;
        4'b1001:  data_segment=7'b1111011;
        default:  data_segment=7'b1110111;
             endcase
        end
 
endmodule