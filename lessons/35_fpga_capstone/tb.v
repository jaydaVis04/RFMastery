`timescale 1ns/1ps
module tb;reg clk=0,rst=1,sv=0,mr=0;reg signed [15:0] sd=0;wire sr,mv;wire signed [15:0] md;
lab dut(clk,rst,sv,sr,sd,mv,mr,md);always #5 clk=~clk;
reg [15:0] inputs[0:511],expected[0:511];integer count,offered,received,k;reg [31:0] rng=32'habcd;reg held;reg [15:0] held_data;
always @(posedge clk)if(!rst)begin
 if(held&&(mv!==1'b1||md!==held_data))$fatal(1,"unstable stalled output");
 if(mv&&mr)begin if(received>=offered||md!==expected[received])$fatal(1,"FIR mismatch index=%d got=%d expected=%d",received,md,$signed(expected[received]));received=received+1;end
 if(sv&&sr)offered=offered+1;
 held=mv&&!mr;held_data=md;
end else held=0;
initial begin
 $readmemh("inputs.hex",inputs);$readmemh("expected.hex",expected);
 count=512;offered=0;received=0;held=0;
 // Epoch 1: normal full comparison under stalls.
 repeat(2)@(negedge clk);rst=0;
 for(k=0;k<5000&&received<count;k=k+1)begin
   rng=rng*1664525+1013904223;
   sv=offered<count;sd=inputs[offered<count?offered:0];mr=rng[3]||rng[7];@(negedge clk);
 end
 sv=0;mr=1;if(received!=count||offered!=count)$fatal(1,"sample count mismatch");
 // Epoch 2: accept a nonzero sample and discard it/history with reset.
 rst=1;@(negedge clk);rst=0;offered=0;received=0;sv=1;sd=16'sd30000;mr=0;@(negedge clk);
 sv=0;rst=1;@(negedge clk);rst=0;offered=0;received=0;held=0;mr=1;
 // Epoch 3 must again match zero-history reference.
 for(k=0;k<5000&&received<count;k=k+1)begin
   rng=rng*1664525+1013904223;sv=offered<count;sd=inputs[offered<count?offered:0];mr=rng[4];@(negedge clk);
 end
 sv=0;mr=1;repeat(3)@(negedge clk);
 if(received!=count||offered!=count||mv)$fatal(1,"reset epoch mismatch");
 $display("PASS");$finish;
end
initial begin #200000;$fatal(1,"watchdog");end endmodule
