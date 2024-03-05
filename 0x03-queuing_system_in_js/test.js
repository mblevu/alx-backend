const express = require('express');
const redis = require('redis');
const app = express();
const client = redis.createClient();


app.get('/get/:key', (req, res) => {
    const key = req.params.key;
    client.get(key, (error, reply) => {
        if (err) {
            res.status(500).send('Error');
        } else {
            res.send(reply);
        }
    });
});


app.listen(3000, () => {
    console.log('Server is running on port 3000');
});
