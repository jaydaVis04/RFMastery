`timescale 1ns/1ps
module tb;reg [3:0] data;reg [1:0] sel;wire y;lab dut(data,sel,y);integer d,s;initial begin for(d=0;d<16;d=d+1)for(s=0;s<4;s=s+1)begin data=d;sel=s;#1;if(y!==data[s])$fatal(1,"mux mismatch data=%d sel=%d",d,s);end $display("PASS");$finish;end endmodule
