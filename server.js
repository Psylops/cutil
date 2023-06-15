const fs = require('fs');
const path = require('path');
const http = require('http');
const url = require('url');
const express = require('express');
const app = express();

var ver = "1.0.0"

app.get('/', (req, res) => {
    const headerValue = req.headers['user-agent'];
    if (headerValue && headerValue.includes('curl')) {
      res.send(ver+"\n");
    } else {
      res.send('Default text response');
    }
  });
  
app.listen(8080, () => {
  console.log('Example app listening on port 8080!');
});