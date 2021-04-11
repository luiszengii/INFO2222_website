<body>
    <form action="/post_discussion" method="post">
    <label for="post">Post content</label>
    <input type="text" name="post" placeholder="254 letters max" />
    </br>

    <label for="category">Category</label>
    <select id="category" name="category">
      <option value="web">Web Basics</option>
      <option value="html">HTML</option>
      <option value="css">CSS</option>
      <option value="js">JavaScript</option>
    </select>
  
    <input type="submit" value="Submit" />
  </form>
</body>