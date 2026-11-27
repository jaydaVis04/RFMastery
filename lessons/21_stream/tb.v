`timescale 1ns/1ps
module tb;reg clk=0,rst=1,sv=0,mr=0;reg [15:0] sd=0;wire sr,mv;wire [15:0] md;
lab dut(clk,rst,sv,sr,sd,mv,mr,md);always #5 clk=~clk;
reg [15:0] queue[0:4095];integer head=0,tail=0,k,received=0;reg [31:0] rng=32'h12345678;reg held=0;reg [15:0] held_data;reg accepted=0;
always @(posedge clk)begin
if(rst)begin head=0;tail=0;held=0;accepted=0;end else begin
if(held&&(mv!==1'b1||md!==held_data))$fatal(1,"data/valid changed while stalled");
if(mv&&mr)begin if(head>=tail||md!==queue[head])$fatal(1,"loss/order/duplicate");head=head+1;received=received+1;end
if(sv&&sr)begin queue[tail]=sd;tail=tail+1;end
held=mv&&!mr;held_data=md;accepted=sv&&sr;
end end
initial begin repeat(2)@(negedge clk);rst=0;
for(k=0;k<600;k=k+1)begin @(negedge clk);rng=rng*1664525+1013904223;
if(!sv||accepted)begin sv=rng[0]||rng[5];sd=rng[31:16];end mr=rng[3];end
// Finish any input already asserted, then stop producing.
@(negedge clk);mr=1;while(sv&&!accepted)@(negedge clk);sv=0;repeat(5)@(negedge clk);
if(head!=tail||mv||received<30)$fatal(1,"did not drain");
// Fill one pending item, then reset while blocked; the old item must be flushed.
sv=1;sd=16'hdead;mr=0;@(negedge clk);sv=0;rst=1;@(negedge clk);rst=0;mr=1;repeat(3)@(negedge clk);if(mv)$fatal(1,"reset did not flush");
$display("PASS");$finish;end
initial begin #30000;$fatal(1,"watchdog");end endmodule
