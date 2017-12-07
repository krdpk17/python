const crypto = require('crypto');                                                                                                                                                                           
crypto.pbkdf2('secret', 'salt', 100000, 64, 'sha512', (err,derivedKey) => {
  if (err) throw err;
  console.log(derivedKey.toString('hex'));// output will be '3745e48...08d59ae' 
});
