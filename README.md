# git_ui

Python UI shell to simplify generic tasks with GIT

<h1>Git UI Script</h1>
<p><img src="https://www.vladonai.com/images/favicon-32x32.png" alt="JediCoder"/></p>
<h2>Welcome, Young Padawan!</h2>
<p>This is the Git UI Script, a powerful tool for managing your Git repositories with ease. Developed by the legendary JediCoder, Volodymyr Frytskyy, this script has been a trusted companion since 2009.</p>
<h2>About the Author</h2>
<p>Volodymyr Frytskyy is a seasoned software developer and a true JediCoder. You can learn more about him and his adventures on his <a href="https://www.vladonai.com/about-resume">personal website</a>.</p>
<h2>Features</h2>
<ul>
<li><strong>Easy Configuration</strong>: Manage your Git repositories with a user-friendly interface.</li>
<li><strong>Remote Management</strong>: Add, remove, and switch between remote repositories effortlessly.</li>
<li><strong>Global Settings</strong>: Set your global user name and email directly from the script.</li>
<li><strong>Clone Repositories</strong>: Clone new repositories and assign them names with a single command.</li>
</ul>
<h2>Getting Started</h2>
<h3>Prerequisites</h3>
<ul>
<li><strong>Python</strong>: Make sure you have Python installed on your system. You can download it from <a href="https://www.python.org/">python.org</a>.</li>
<li><strong>Git</strong>: Ensure that Git is installed and configured on your machine. You can download it from <a href="https://git-scm.com/">git-scm.com</a>.</li>
</ul>
<h3>Installation</h3>
<ol>
<li>
<p><strong>Clone the Repository</strong>:</p>
<pre><div class="relative rounded-md"><button class="inline-flex items-center justify-center whitespace-nowrap text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-auto disabled:opacity-50 hover:text-accent-foreground absolute right-2 top-2 h-6 w-6 rounded-full p-0 text-muted-foreground hover:bg-accent" aria-label="Copy code to clipboard"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-copy h-4 w-4"><rect width="14" height="14" x="8" y="8" rx="2" ry="2"></rect><path d="M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2"></path></svg></button><div node="[object Object]" class="rounded-md" style="color:#d4d4d4;font-size:13px;text-shadow:none;font-family:Menlo, Monaco, Consolas, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;, &quot;Courier New&quot;, monospace;direction:ltr;text-align:left;white-space:pre;word-spacing:normal;word-break:normal;line-height:1.5;-moz-tab-size:4;-o-tab-size:4;tab-size:4;-webkit-hyphens:none;-moz-hyphens:none;-ms-hyphens:none;hyphens:none;padding:1em;margin:.5em 0;overflow:auto;background:#1e1e1e"><code class="language-sh" style="color:#d4d4d4;font-size:13px;text-shadow:none;font-family:Menlo, Monaco, Consolas, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;, &quot;Courier New&quot;, monospace;direction:ltr;text-align:left;white-space:pre;word-spacing:normal;word-break:normal;line-height:1.5;-moz-tab-size:4;-o-tab-size:4;tab-size:4;-webkit-hyphens:none;-moz-hyphens:none;-ms-hyphens:none;hyphens:none"><span>git clone https://github.com/your-username/git-ui-script.git</span></code></div></div></pre>
</li>
<li>
<p><strong>Navigate to the Project Directory</strong>:</p>
<pre><div class="relative rounded-md"><button class="inline-flex items-center justify-center whitespace-nowrap text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-auto disabled:opacity-50 hover:text-accent-foreground absolute right-2 top-2 h-6 w-6 rounded-full p-0 text-muted-foreground hover:bg-accent" aria-label="Copy code to clipboard"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-copy h-4 w-4"><rect width="14" height="14" x="8" y="8" rx="2" ry="2"></rect><path d="M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2"></path></svg></button><div node="[object Object]" class="rounded-md" style="color:#d4d4d4;font-size:13px;text-shadow:none;font-family:Menlo, Monaco, Consolas, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;, &quot;Courier New&quot;, monospace;direction:ltr;text-align:left;white-space:pre;word-spacing:normal;word-break:normal;line-height:1.5;-moz-tab-size:4;-o-tab-size:4;tab-size:4;-webkit-hyphens:none;-moz-hyphens:none;-ms-hyphens:none;hyphens:none;padding:1em;margin:.5em 0;overflow:auto;background:#1e1e1e"><code class="language-sh" style="color:#d4d4d4;font-size:13px;text-shadow:none;font-family:Menlo, Monaco, Consolas, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;, &quot;Courier New&quot;, monospace;direction:ltr;text-align:left;white-space:pre;word-spacing:normal;word-break:normal;line-height:1.5;-moz-tab-size:4;-o-tab-size:4;tab-size:4;-webkit-hyphens:none;-moz-hyphens:none;-ms-hyphens:none;hyphens:none"><span>cd git-ui-script</span></code></div></div></pre>
</li>
<li>
<p><strong>Install Dependencies</strong>:</p>
<pre><div class="relative rounded-md"><button class="inline-flex items-center justify-center whitespace-nowrap text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-auto disabled:opacity-50 hover:text-accent-foreground absolute right-2 top-2 h-6 w-6 rounded-full p-0 text-muted-foreground hover:bg-accent" aria-label="Copy code to clipboard"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-copy h-4 w-4"><rect width="14" height="14" x="8" y="8" rx="2" ry="2"></rect><path d="M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2"></path></svg></button><div node="[object Object]" class="rounded-md" style="color:#d4d4d4;font-size:13px;text-shadow:none;font-family:Menlo, Monaco, Consolas, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;, &quot;Courier New&quot;, monospace;direction:ltr;text-align:left;white-space:pre;word-spacing:normal;word-break:normal;line-height:1.5;-moz-tab-size:4;-o-tab-size:4;tab-size:4;-webkit-hyphens:none;-moz-hyphens:none;-ms-hyphens:none;hyphens:none;padding:1em;margin:.5em 0;overflow:auto;background:#1e1e1e"><code class="language-sh" style="color:#d4d4d4;font-size:13px;text-shadow:none;font-family:Menlo, Monaco, Consolas, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;, &quot;Courier New&quot;, monospace;direction:ltr;text-align:left;white-space:pre;word-spacing:normal;word-break:normal;line-height:1.5;-moz-tab-size:4;-o-tab-size:4;tab-size:4;-webkit-hyphens:none;-moz-hyphens:none;-ms-hyphens:none;hyphens:none"><span>pip install colorama</span></code></div></div></pre>
</li>
</ol>
<h3>Usage</h3>
<ol>
<li>
<p><strong>Run the Script</strong>:</p>
<pre><div class="relative rounded-md"><button class="inline-flex items-center justify-center whitespace-nowrap text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-auto disabled:opacity-50 hover:text-accent-foreground absolute right-2 top-2 h-6 w-6 rounded-full p-0 text-muted-foreground hover:bg-accent" aria-label="Copy code to clipboard"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-copy h-4 w-4"><rect width="14" height="14" x="8" y="8" rx="2" ry="2"></rect><path d="M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2"></path></svg></button><div node="[object Object]" class="rounded-md" style="color:#d4d4d4;font-size:13px;text-shadow:none;font-family:Menlo, Monaco, Consolas, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;, &quot;Courier New&quot;, monospace;direction:ltr;text-align:left;white-space:pre;word-spacing:normal;word-break:normal;line-height:1.5;-moz-tab-size:4;-o-tab-size:4;tab-size:4;-webkit-hyphens:none;-moz-hyphens:none;-ms-hyphens:none;hyphens:none;padding:1em;margin:.5em 0;overflow:auto;background:#1e1e1e"><code class="language-sh" style="color:#d4d4d4;font-size:13px;text-shadow:none;font-family:Menlo, Monaco, Consolas, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;, &quot;Courier New&quot;, monospace;direction:ltr;text-align:left;white-space:pre;word-spacing:normal;word-break:normal;line-height:1.5;-moz-tab-size:4;-o-tab-size:4;tab-size:4;-webkit-hyphens:none;-moz-hyphens:none;-ms-hyphens:none;hyphens:none"><span>python main.py</span></code></div></div></pre>
</li>
<li>
<p><strong>Follow the Prompts</strong>:</p>
<ul>
<li><strong>Main Menu</strong>: Choose from various options like Checkout, Commit/Push, Local Repository, Branch, Tag, and Configure.</li>
<li><strong>Configuration Menu</strong>: Add, remove, and switch between remote repositories. Set your global user name and email.</li>
</ul>
</li>
</ol>
<h2>Examples</h2>
<h3>Adding a New Remote Repository</h3>
<ol>
<li>Select option <code class="" node="[object Object]">3</code> from the configuration menu.</li>
<li>Enter the remote repository name (e.g., <code class="" node="[object Object]">repo1</code>).</li>
<li>Enter the remote repository URL (e.g., <code class="" node="[object Object]">https://github.com/spialert-michael/SpiAlert_CV_Client.git</code>).</li>
<li>Enter the local directory to clone the repository to (e.g., <code class="" node="[object Object]">./repo1</code>).</li>
</ol>
<h3>Switching to a Different Remote Repository</h3>
<ol>
<li>Select option <code class="" node="[object Object]">5</code> from the configuration menu.</li>
<li>Enter the remote repository name to switch to (e.g., <code class="" node="[object Object]">repo1</code>).</li>
</ol>
<h2>License</h2>
<p>This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for details.</p>
<h2>Contributing</h2>
<p>Feel free to contribute to this project by opening issues or submitting pull requests. May the Force be with you!</p>
<h2>Contact</h2>
<p>For more information, visit Volodymyr Frytskyy&#x27;s <a href="https://www.vladonai.com/about-resume">personal website</a> or reach out to him directly.</p>
<hr/>
<p>May the Force be with you, young Padawan! Happy coding!</p>
<p><img src="https://www.vladonai.com/images/favicon-32x32.png" alt="JediCoder"/></p>
<hr/>
