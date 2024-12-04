#!/usr/bin/node

import { createClient } from 'redis';

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err);
});

client.subscribe('holberton school');

client.on('message', (ch, mess) => {
  if (mess === 'KILL_SERVER') {
		client.unsubscribe('holberton school channel', () => {
		  client.quit()
		})
	  }
	console.log(mess);
})