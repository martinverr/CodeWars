<h2 id="task">Task</h2>
<p>Create a RomanNumerals class that can convert a roman numeral to and from an integer value.  It should follow the API demonstrated in the examples below. Multiple roman numeral values will be tested for each helper method. </p>
<p>Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.</p>
<h2 id="examples">Examples</h2>
<pre style="display: none;"><code class="language-javascript"><span class="cm-variable">RomanNumerals</span>.<span class="cm-property">toRoman</span>(<span class="cm-number">1000</span>); <span class="cm-comment">// should return 'M'</span>
<span class="cm-variable">RomanNumerals</span>.<span class="cm-property">fromRoman</span>(<span class="cm-string">'M'</span>); <span class="cm-comment">// should return 1000</span></code></pre>

<h2>Help</h2>
<pre>
| Symbol    | Value |
|-------------------|
| I         | 1     |
| V         | 5     |
| X         | 10    |
| L         | 50    |
| C         | 100   |
| D         | 500   |
| M         | 1000  |</p>
</pre>
