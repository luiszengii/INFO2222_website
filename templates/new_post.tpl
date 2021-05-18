<style>
input[type=text]{
  width: 100%;
  height: 200px;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

select {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

input[type=submit] {
  width: 100%;
  background-color: #4CAF50;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

input[type=submit]:hover {
  background-color: #45a049;
}

div {
  border-radius: 5px;
  background-color: #f2f2f2;
  padding: 20px;
}
</style>

<body>
    <div>
      <form action="/post_discussion" method="post">
      <label for="post">Post content</label>
      <input type="text" name="post" placeholder="254 letters max" />
    </div>
    </br>


    <div>
      <label for="category">Category</label>
      <select id="category" name="category">
        <option value="web">Web Basics</option>
        <option value="html">HTML</option>
        <option value="css">CSS</option>
        <option value="js">JavaScript</option>
      </select>
    </div>
  
    <input type="submit" value="Submit" />
  </form>
</body>