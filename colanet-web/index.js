// index.js

const path = require("path");
const express = require("express");

const app = express();
const port = process.env.PORT || "8000";

app.use(express.static(path.join(__dirname, "public")));


app.set("views", path.join(__dirname, "views"));
app.set("view engine", "pug");

app.get("/", (req, res) => {
  res.render("index", { title: "Home" });
});

app.get('/download_dataset', function(req, res){
  const file = `${__dirname}/public/colanet.zip`;
  res.download(file); // Set disposition and send it.
});

app.get('/download', function(req, res){
  const file = `${__dirname}/public/${req.query.file}`;
  res.download(file); // Set disposition and send it.
});


app.listen(port, () => {
  console.log(`Listening to requests on http://localhost:${port}`);
});
