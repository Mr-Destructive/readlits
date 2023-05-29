import { Client } from 'appwrite';
const client = new Client();

client
    .setEndpoint('http://127.0.0.1:8001/v1')
    .setProject('6467a226111048c72b2c');

const account = new Account(client);

account.create(
    ID.unique(),
    'me@example.com',
    'password',
    'Jane Doe'
).then(response => {
    console.log(response);
}, error => {
    console.log(error);
});
