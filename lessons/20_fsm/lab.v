module lab(input wire clk,rst,valid,input wire [7:0] data,output reg done);
always @(posedge clk) done <= 0; // TODO
endmodule
