module lab(input wire [3:0] data,input wire [1:0] sel,output wire y);
assign y=data[sel];
endmodule
