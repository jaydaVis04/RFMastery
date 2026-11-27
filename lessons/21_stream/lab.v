module lab(input wire clk,rst,input wire s_valid,output wire s_ready,input wire [15:0] s_data,
output reg m_valid,input wire m_ready,output reg [15:0] m_data);
assign s_ready=1'b0;
always @(posedge clk)begin m_valid<=0;m_data<=0;end // TODO
endmodule
