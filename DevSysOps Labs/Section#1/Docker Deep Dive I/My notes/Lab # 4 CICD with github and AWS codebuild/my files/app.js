const express = require('express');
const app = express();
const port = 8880;

app.get('/', (req, res) => {
  res.send('Hello World from Node.js on AWS with ECR + CodeBuild!');
});

app.listen(port, () => {
  console.log(`App running at http://localhost:${port}`);
});
