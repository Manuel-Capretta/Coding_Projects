const accountSid = 'ACb00c9743d1cdba56222faae0959f7b27'; 
const authToken = '09508f65bbdb8349dae29a7c7d80ec46'; 
const client = require('twilio')(accountSid, authToken); 
 
client.messages 
      .create({ 
         body: 'Hello Stefan', 
         from: 'whatsapp:+14155238886',       
         to: 'whatsapp:+41792231242' 
       }) 
      .then(message => console.log(message.sid)) 
      .done();