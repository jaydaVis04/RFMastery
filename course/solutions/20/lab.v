module lab(input wire clk,rst,valid,input wire [7:0] data,output reg done);
localparam IDLE=0,PAYLOAD=1,END=2;reg [1:0] state;
always @(posedge clk)begin if(rst)begin state<=IDLE;done<=0;end else begin done<=0;if(valid)case(state)
IDLE:if(data==8'ha5)state<=PAYLOAD;
PAYLOAD:state<=END;
END:begin if(data==8'h5a)done<=1;state<=IDLE;end
default:state<=IDLE;endcase end end endmodule
