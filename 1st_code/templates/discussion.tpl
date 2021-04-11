<body>

%for i in range(5):
<h1> test </h1>
%end

    <ul class="tutorial">
        <li class="tutorial"><a class="tutorial" href="#web">Web Basics</a></li>
        <li class="tutorial"><a class="tutorial" href="#html">HTML</a></li>
        <li class="tutorial"><a class="tutorial" href="#css">CSS</a></li>
        <li class="tutorial"><a class="tutorial" href="#js">JavaScript</a></li>
        <!-- #仅作为测试 -->
    </ul>

    <form action="/try_new_post" method="get">
        <button type="submit" formaction="/try_new_post">+ New Post</button>
    </form>

    <div id="web" class="tutorial">
        <h2>Web Basics</h2>
    </div>

    <div id="html" class="tutorial">
        <h2>HTML</h2>
    </div>

    <div id="css" class="tutorial">
        <h2>CSS</h2>
    </div>

    <div id="js" class="tutorial">
        <h2>JavaScript</h2>
    </div>


</body>