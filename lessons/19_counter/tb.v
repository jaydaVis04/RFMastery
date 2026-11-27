`timescale 1ns/1ps
module tb;reg clk=0,rst=1;wire [3:0] q;integer k;reg [3:0] expected=0;
lab dut(clk,rst,q);always #5 clk=~clk;
initial begin $dumpfile("wave.vcd");$dumpvars(0,tb);
for(k=0;k<40;k=k+1)begin @(negedge clk);rst=(k==0||k==21);@(posedge clk);if(rst)expected=0;else expected=expected+1;#1;if(q!==expected)$fatal(1,"counter cycle %d",k);end
$display("PASS");$finish;end
initial begin #10000;$fatal(1,"watchdog");end endmodule
