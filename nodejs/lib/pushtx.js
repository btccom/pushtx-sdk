"use strict";
const request = require("request");

module.exports = class Pushtx {
    constructor(config) {
        this._config = {};
        this._config['app_id'] = config['app_id'];
        this._config['secret_key'] = config['secret_key'];
        this._config['base_url'] = config['base_url'] || 'https://pushtx.btc.com';
    }

    createMerchantOrder(txhash, description) {
        return new Promise((resolve, reject) => {
            const nonce = Math.random().toString(36).substr(2);
            let sign = this.createSign([txhash, description, this._config['app_id'], nonce, this._config['secret_key']]);
            request.post(this._config['base_url'] + '/api/order/merchant', {
                form: {
                    sign: sign,
                    nonce: nonce,
                    app_id: this._config['app_id'],
                    txhash: txhash,
                    description: description
                }, json: true
            }, function (err, res, body) {
                if (err) {
                    return reject({ message: "请求发生错误", info: err });
                }
                if (body.err_no !== 0) {
                    return reject({ message: body.err_msg, info: body.err_msg });                    
                }
                return resolve(body.data);
            });
        });
    }

    getBalance() {
        return new Promise((resolve, reject) => {
            const nonce = Math.random().toString(36).substr(2);
            let sign = this.createSign([this._config['app_id'], nonce, this._config['secret_key']]);
            request.post(this._config['base_url'] + '/api/balance/merchant', {
                form: {
                    sign: sign,
                    nonce: nonce,
                    app_id: this._config['app_id'],
                }, json: true
            }, function (err, res, body) {
                if (err) {
                    return reject({ message: "请求发生错误", info: err });
                }
                if (body.err_no !== 0) {
                    return reject({ message: body.err_msg, info: body.err_msg });                    
                }
                return resolve(body.data);
            });
        }); 
    }

    createSign(param) {
        const crypto = require('crypto');
        const real_sign = crypto.createHmac('sha256', nonce).update(param.join('|')).digest('hex');
        return real_sign;
    }
}