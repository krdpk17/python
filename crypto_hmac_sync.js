const crypto = require('crypto');                                                                                                                                                                           
const key = crypto.pbkdf2Sync ('secret', 'salt', 100000, 64, 'sha512');
console.log(key.toString('hex'));
