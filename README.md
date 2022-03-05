# How the Algorithm Works:

main_string = "Qtecs" <br/>
sub_string = "Qtec" <br/>
main_length = 5 <br/>
sub_length = 4 <br/>
result = 0  <br/><br/>

outer loop will run from 0 to (main_length - sub_length)<br/>
while i = 0 , j = 0 , then main_string[0+0] = Q  and  sub_string[0] = Q <br/>
while i = 0 , j = 1 , then main_string[0+1] = t  and  sub_string[1] = t <br/>
while i = 0 , j = 2 , then main_string[0+2] = e  and  sub_string[2] = e <br/>
while i = 0 , j = 3 , then main_string[0+3] = c  and  sub_string[3] = c <br/><br/>

Now, j has to be smaller then main_length.Now j is 4 and main_length is 5. So, inner loop will end.<br/>
So, now we will increment result by 1. So, result = 1. <br/>
Now, value of i will increment. So, <br/><br/>

while i = 1 , j = 0 , then main_string[1+0] = t  and  sub_string[0] = Q <br/>
inner loop will break as main_string[1] and sub_string[0] doesn't match. <br/><br/>

while i = 1 , j = 1 , then main_string[1+1] = e  and  sub_string[1] = t <br/>
inner loop will break as main_string[2] and sub_string[1] doesn't match. <br/><br/>

while i = 1 , j = 2 , then main_string[1+2] = c  and  sub_string[2] = e <br/>
inner loop will break as main_string[3] and sub_string[2] doesn't match. <br/><br/>

while i = 1 , j = 3 , then main_string[1+3] = s  and  sub_string[3] = c <br/>
inner loop will break as main_string[4] and sub_string[3] doesn't match. <br/><br/>

And, this way whole outer loop will be executed and result value remains 1. <br/>
