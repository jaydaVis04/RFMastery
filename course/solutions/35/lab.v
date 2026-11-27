module lab(input wire clk,rst,input wire s_valid,output wire s_ready,input wire signed [15:0] s_data,
output reg m_valid,input wire m_ready,output reg signed [15:0] m_data);
reg signed [15:0] z1,z2;reg signed [63:0] a,b,c,acc,scaled;reg signed [15:0] result;
assign s_ready=!m_valid||m_ready;
always @* begin
 a={{48{s_data[15]}},s_data};b={{48{z1[15]}},z1};c={{48{z2[15]}},z2};
 acc=a*64'sd8192+b*64'sd16384+c*64'sd8192;
 scaled=acc/64'sd32768;
 if(scaled>64'sd32767)result=16'sd32767;
 else if(scaled< -64'sd32768)result=16'sh8000;
 else result=scaled[15:0];
end
always @(posedge clk)begin
 if(rst)begin m_valid<=0;m_data<=0;z1<=0;z2<=0;end
 else if(s_ready)begin m_valid<=s_valid;if(s_valid)begin m_data<=result;z2<=z1;z1<=s_data;end end
end endmodule
