<html>
<head>
<title>Task_1.py</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style type="text/css">
.s0 { color: #cc7832;}
.s1 { color: #a9b7c6;}
.s2 { color: #808080;}
.s3 { color: #6897bb;}
.s4 { color: #6a8759;}
</style>
</head>
<body bgcolor="#2b2b2b">
<table CELLSPACING=0 CELLPADDING=5 COLS=1 WIDTH="100%" BGCOLOR="#606060" >
<tr><td><center>
<font face="Arial, Helvetica" color="#000000">
Task_1.py</font>
</center></td></tr></table>
<pre><span class="s0">import </span><span class="s1">random</span>

<span class="s2"># create objects for further work</span>

<span class="s1">random_list = []    </span><span class="s2"># create empty list for random values</span>
<span class="s1">sorted_list = []    </span><span class="s2"># create empty list for sorted values</span>

<span class="s1">sum_even = </span><span class="s3">0         </span><span class="s2"># create object to store the values of the sum of even numbers</span>
<span class="s1">sum_odd = </span><span class="s3">0          </span><span class="s2"># create object to store the values of the sum of odd numbers</span>

<span class="s1">count_even = </span><span class="s3">0       </span><span class="s2"># create object to store count of even numbers into list</span>
<span class="s1">count_odd = </span><span class="s3">0        </span><span class="s2"># create object to store count of odd numbers into list</span>


<span class="s0">for </span><span class="s1">i </span><span class="s0">in </span><span class="s1">range(</span><span class="s3">100</span><span class="s1">):                              </span><span class="s2"># start loop for creation 100 values into list ( till value &lt;=1000 do )</span>
    <span class="s1">random_list.append(random.randint(</span><span class="s3">0</span><span class="s0">, </span><span class="s3">1000</span><span class="s1">))    </span><span class="s2"># add random int values from 0 to 1000 to the empty list</span>

<span class="s1">print(</span><span class="s4">'Random list is : %s' </span><span class="s1">% (random_list))     </span><span class="s2"># show updated random_list</span>

<span class="s0">while </span><span class="s1">random_list:                                </span><span class="s2"># while list is true (has any values in it) do loop (after each time list decrease)</span>
    <span class="s1">min_value = random_list[</span><span class="s3">0</span><span class="s1">]                    </span><span class="s2"># assign the first value from the list like minimum</span>
    <span class="s0">for </span><span class="s1">i </span><span class="s0">in </span><span class="s1">random_list:                         </span><span class="s2"># for each element into list do loop</span>
        <span class="s0">if </span><span class="s1">i &lt; min_value:                         </span><span class="s2"># if current element &lt; then our minimum</span>
            <span class="s1">min_value = i                         </span><span class="s2"># replace our minimum with current element</span>

    <span class="s1">sorted_list.append(min_value)                 </span><span class="s2"># add to the empty list out minimum element from each iteration of the loop</span>
    <span class="s1">random_list.remove(min_value)                 </span><span class="s2"># delete from random_list our updated minimum element</span>


<span class="s0">for </span><span class="s1">i </span><span class="s0">in </span><span class="s1">sorted_list:                             </span><span class="s2"># for each element from sorted list do</span>
    <span class="s0">if </span><span class="s1">i % </span><span class="s3">2 </span><span class="s1">== </span><span class="s3">0</span><span class="s1">:                                </span><span class="s2"># if the remainder of dividing an element by 2 is 0 (then even)</span>
        <span class="s1">sum_even = sum_even + i                   </span><span class="s2"># update sum_even as sum_even + this element</span>
        <span class="s1">count_even = count_even + </span><span class="s3">1               </span><span class="s2"># update count_even as count_even + 1</span>
    <span class="s0">elif </span><span class="s1">i % </span><span class="s3">2 </span><span class="s1">!= </span><span class="s3">0</span><span class="s1">:                              </span><span class="s2"># if the remainder of dividing an element by 2 is NOT 0 (then odd)</span>
        <span class="s1">sum_odd = sum_odd + i                     </span><span class="s2"># update sum_odd as sum_odd + this element</span>
        <span class="s1">count_odd = count_odd + </span><span class="s3">1                 </span><span class="s2"># update count_odd as count_odd + 1</span>

<span class="s1">avg_even = sum_even / count_even                  </span><span class="s2"># create object for average for even numbers from sorted list like sum_even/count_even</span>
<span class="s1">avg_odd = sum_odd / count_odd                     </span><span class="s2"># create object for average for odd numbers from sorted list like sum_odd/count_odd</span>

<span class="s1">print(</span><span class="s4">'Sorted list is : %s' </span><span class="s1">% (sorted_list))</span>
<span class="s1">print(</span><span class="s4">'Average for even numbers is : %s' </span><span class="s1">% (avg_even))</span>
<span class="s1">print(</span><span class="s4">'Average for odd numbers is : %s' </span><span class="s1">% (avg_odd))</span>




</pre>
</body>
</html>