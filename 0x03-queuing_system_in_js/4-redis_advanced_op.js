#!/usr/bin/node

import {createClient, print} from 'redis'

const client = createClient()
// The key of the hash should be HolbertonSchools
// It should have a value for:
// Portland=50
// Seattle=80
// New York=20
// Bogota=20
// Cali=40
// Paris=2
function callback(_, res) {
  print(`reply: ${res}`);
}

client.hset('HolbertonSchools', 'Portland', 50, callback);
client.hset('HolbertonSchools', 'Seatttle', 80, callback);
client.hset('HolbertonSchools', 'New York', 20, callback);
client.hset('HolbertonSchools', 'Bogota', 20, callback);
client.hset('HolbertonSchools', 'Cali', 40, callback);
client.hset('HolbertonSchools', 'Paris', 2, callback);

client.hgetall('HolbertonSchools', (_, rep) => {
  console.log(rep);
});
