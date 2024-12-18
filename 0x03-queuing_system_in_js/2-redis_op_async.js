#!/usr/bin/node

import { createClient, print } from 'redis';
import {promisify} from 'util'

const client = createClient();
const async_set = promisify(client.set.bind(client));
const async_get = promisify(client.get.bind(client));

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err);
});

async function setNewSchool(schoolName, value) {
  const ret = await async_set(schoolName, value);
  print('reply:', ret);
}

async function displaySchoolValue(schoolName) {
  const res = await async_get(schoolName);
  console.log(res)
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
