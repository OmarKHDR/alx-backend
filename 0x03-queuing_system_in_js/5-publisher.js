#!/usr/bin/node

import { createClient } from 'redis';

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err);
});



function publishMessage(mess, time) {
  setTimeout(() => {
    console.log('About to send MESSAGE');
    client.publish('holberton school', mess);
  }, time);
}


publishMessage("hello world", 10000);
publishMessage("hello, can anybody hear me", 15000);
publishMessage("are you here", 20000);
publishMessage("oh i guess i havd to kill you then", 25000);
publishMessage("KILL_SERVER", 30000);

