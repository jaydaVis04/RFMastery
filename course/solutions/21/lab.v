module lab(input wire clk,rst,input wire s_valid,output wire s_ready,input wire [15:0] s_data,
output reg m_valid,input wire m_ready,output reg [15:0] m_data);
assign s_ready=!m_valid||m_ready;
always @(posedge clk)if(rst)begin m_valid<=0;m_data<=0;end else if(s_ready)begin m_valid<=s_valid;if(s_valid)m_data<=s_data;end
endmodule
