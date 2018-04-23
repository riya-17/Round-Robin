# Round-Robin
Distribute the numbers present in the input file into 3 output files in a round robin manner.
Program which reads a single input file - InputFile1.txt and distributes the numbers present in the file into 3 output files in a round robin manner. <br>

If the program is run again with another Input file (InputFile2.txt), it should start the distribution from the next file to be distributed in the loop. <br>

![robin](https://user-images.githubusercontent.com/25060937/39123901-112eb9fa-4717-11e8-836f-b6f862810cb7.PNG)


First Run (with InputFile1.txt) <br>
---------------------------------------

InputFile1.txt <br>
12 34 56 23 9 1 16 <br>

Output after first run with input as InputFile1.txt - <br>

OutputFile1.txt <br>
12 23 16 <br>

OutputFile2.txt <br>
34 9 <br>

OutputFile3.txt <br>
56 1 <br>

Second run (with InputFile2.txt) <br>
------------------------------------------
Output after second run with input as InputFile2.txt. Please note that the first distribution starts from OutputFile2.txt (since the last distributed file was OutputFile1.txt.) <br>

InputFile2.txt <br>
11 3 55 30 33 9 <br>

Output of this program should be: <br>

OutputFile1.txt <br>
12 23 16 55 9 <br>

OutputFile2.txt <br>
34 9 11 30 <br>

OutputFile3.txt <br>
56 1 3 33 <br>
