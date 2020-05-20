# Codewars style ranking system
   <p>Write a class called User that is used to calculate the amount that a user will progress through a ranking system similar to the one Codewars uses.  </p>
   <h3>Business Rules:</h3>
   <ul>
      <li>A user starts at rank -8 and can progress all the way to 8.</li>
      <li>There is no 0 (zero) rank. The next rank after -1 is 1.</li>
      <li>Users will complete activities. These activities also have ranks.</li>
      <li>Each time the user completes a ranked activity the users rank progress is updated based off of the activity's rank</li>
      <li>The progress earned from the completed activity is relative to what the user's current rank is compared to the rank of the activity</li>
      <li>A user's rank progress starts off at zero, each time the progress reaches 100 the user's rank is upgraded to the next level</li>
      <li>Any remaining progress earned while in the previous rank will be applied towards the next rank's progress (we don't throw any progress away). The exception is if there is no other rank left to progress towards (Once you reach rank 8 there is no more progression). </li>
      <li>A user cannot progress beyond rank 8. </li>
      <li>The only acceptable range of rank values is -8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8. Any other value should raise an error. </li>
   </ul>
   The progress is scored like so:
   <ul>
      <li>Completing an activity that is ranked the same as that of the user's will be worth 3 points</li>
      <li>Completing an activity that is ranked one ranking lower than the user's will be worth 1 point</li>
      <li>Any activities completed that are ranking 2 levels or more lower than the user's ranking will be ignored</li>
      <li>Completing an activity ranked higher than the current user's rank will accelerate the rank progression. The greater the difference between rankings the more the progression will be increased. The formula is <code>10 * d * d</code> where <code>d</code> equals the difference in ranking between the activity and the user.  </li>
   </ul>
   <h3>Logic Examples:</h3>
   <ul>
      <li>If a user ranked -8 completes an activity ranked -7 they will receive 10 progress</li>
      <li>If a user ranked -8 completes an activity ranked -6 they will receive 40 progress</li>
      <li>If a user ranked -8 completes an activity ranked -5 they will receive 90 progress</li>
      <li>If a user ranked -8 completes an activity ranked -4 they will receive 160 progress, resulting in the user being upgraded to rank -7 and having earned 60 progress towards their next rank</li>
      <li>If a user ranked -1 completes an activity ranked 1 they will receive 10 progress (remember, zero rank is ignored)</li>
   </ul>
<h3>Usage Examples:</h3>
<pre>
<code class="language-python"><span class="cm-variable">user</span> <span class="cm-operator">=</span> <span class="cm-variable">User</span>()
<span class="cm-variable">user</span>.<span class="cm-property">rank</span> <span class="cm-comment"># =&gt; -8</span>
<span class="cm-variable">user</span>.<span class="cm-property">progress</span> <span class="cm-comment"># =&gt; 0</span>
<span class="cm-variable">user</span>.<span class="cm-property">inc_progress</span>(<span class="cm-operator">-</span><span class="cm-number">7</span>)
<span class="cm-variable">user</span>.<span class="cm-property">progress</span> <span class="cm-comment"># =&gt; 10</span>
<span class="cm-variable">user</span>.<span class="cm-property">inc_progress</span>(<span class="cm-operator">-</span><span class="cm-number">5</span>) <span class="cm-comment"># will add 90 progress</span>
<span class="cm-variable">user</span>.<span class="cm-property">progress</span> <span class="cm-comment"># =&gt; 0 # progress is now zero</span>
<span class="cm-variable">user</span>.<span class="cm-property">rank</span> <span class="cm-comment"># =&gt; -7 # rank was upgraded to -7</span></code>
</pre>
