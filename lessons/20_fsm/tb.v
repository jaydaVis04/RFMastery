`timescale 1ns/1ps
module tb;reg clk=0,rst=1,valid=0;reg [7:0] data=0;wire done;lab dut(clk,rst,valid,data,done);always #5 clk=~clk;
task send;input r,v;input [7:0] d;input expect_done;begin @(negedge clk);rst=r;valid=v;data=d;@(posedge clk);#1;if(done!==expect_done)$fatal(1,"FSM got %b expected %b byte %h",done,expect_done,d);end endtask
initial begin send(1,0,0,0);send(0,1,8'h44,0);send(0,1,8'ha5,0);send(0,0,0,0);send(0,1,8'h12,0);send(0,1,8'h5a,1);send(0,0,0,0);
send(0,1,8'ha5,0);send(0,1,0,0);send(0,1,8'ha5,0);send(0,1,8'h5a,0);
send(0,1,8'ha5,0);send(1,1,8'h12,0);send(0,1,8'h5a,0);
send(0,1,8'ha5,0);send(0,1,8'hff,0);send(0,1,8'h5a,1);$display("PASS");$finish;end
initial begin #10000;$fatal(1,"watchdog");end endmodule
