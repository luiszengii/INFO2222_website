<head>
  <link rel="stylesheet" type="text/css" href="css/temp1.css">
  <script src="js/head.js"></script>
  <br> <br> <br>
</head>

<p>
<ul id="navbar">
  <li><a class="active" href="/home">Home</a></li>
  <li><a href="/login">sLogin</a></li>
  <li><a href="/about">About</a></li>
  <li><a href="/profile">Profile</a></li>
  <li><a href="/tut">Tutorial</a></li>
  <li><a href="/discussion">Discussion</a></li>
</ul>
</p>

<form action="/try_new_post" method="get">
    <button action="/try_new_post">+ New Post</button>
</form>

<body>
  <ul class="tutorial">
    <li class="tutorial"><a class="tutorial" href="#web">Web Basics</a></li>
    <li class="tutorial"><a class="tutorial" href="#html">HTML</a></li>
    <li class="tutorial"><a class="tutorial" href="#css">CSS</a></li>
    <li class="tutorial"><a class="tutorial" href="#js">JavaScript</a></li>
  </ul>

  %
  <div id="web" class="tutorial">
    <h2>Web Basics</h2>
    % if len(dis_list[0]) > 0:
      % for elem in dis_list[0]:
          <p>{{elem[0]}}: {{elem[1]}}</p>
      % end
    % end
  </div>
  %

  %
  <div id="html" class="tutorial">
      <h2>Html</h2>
      % if len(dis_list[1]) > 0:
      % for elem in dis_list[1]:
          <p>{{elem[0]}}: {{elem[1]}}</p>
      % end
    % end
  </div>
  %

  %
  <div id="css" class="tutorial">
    <h2>CSS</h2>
    % if len(dis_list[2]) > 0:
      % for elem in dis_list[2]:
          <p>{{elem[0]}}: {{elem[1]}}</p>
      % end
    % end
  </div>
  %

  %
  <div id="js" class="tutorial">
    <h2>JavaScript</h2>
    % if len(dis_list[3]) > 0:
      % for elem in dis_list[3]:
          <p>{{elem[0]}}: {{elem[1]}}</p>
      % end
    % end
  </div>
  %


</body>
