var Pushtx = require('../index.js');
const pushtx = new Pushtx({
    app_id: 'app_id',
    secret_key: 'secret_key',
    base_url: 'https://sandbox.pushtx.btc.com'
});

pushtx.createMerchantOrder('txhash', 'description')
    .then(result => {
        console.log(result);
    }).catch(error => console.error(error));