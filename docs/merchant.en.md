# Create order on business account

> Created: 2017-11-29

## Interface Introduction
Business account user can consume by created App and signed signature, accelerate unconfirmed transaction.

## interface details

### request address

/api/order/merchant

### request type
POST

### request parameters
| Parameter Name | Type | Required | Description | Default | Reference |
| --- | :---: | :---: | --- | --- | --- |
| txhash | string | yes | transaction hash | no | ff602f8d64b9188f6831f62486e1391c8281ed6abc71c8862f59a7195d591328 |
| description | string | Yes | Transaction Description | None | Can fill in blank string |
| app_id | string | yes | application ID | no | 281ed6abc71c8862f59a7195d591328 |
| nonce | string | yes | a random string of no less than 10 bits | no | sfsdfsvxcvwfw2esfsaf |
| sign | string | yes | Signature | no | Generate Rule: `hmac256 (txhash + '\' '+ description +' \ | '+ app_id +' \ + nonce + '\ |' + secret_key) Key for hmac sha256

### returns the correct JSON example
```javascript
{
    "err_no": 0,
    "data": {
        "status": "succeed",
        "balance": 121356.51,
        "order_id": "ffa419d3625d6839_1511939576962"
    }
}
```

### returns the wrong JSON example
```javascript
{
"err_no": 102,
"err_msg": "TxConfirmed"
}
```

Specific reference [error code](./Errorcode.en.md)

# Check account balance for business account 

> Created: 2017-12-01

## Interface Introduction
Users can check account balance through this interface

## interface details

### request address
/api/balance/merchant

### request type
POST

### request parameters
| Parameter Name | Type | Required | Description | Default | Reference |
| --- | :---: | :---: | --- | --- | --- |
| app_id | string | yes | application ID | no | 281ed6abc71c8862f59a7195d591328 |
| nonce | string | yes | a random string of no less than 10 bits | no | sfsdfsvxcvwfw2esfsaf |
| sign | string | yes | Signature | no | Generate Rule: `hmac256 (app_id + '\ |' + nonce + '\ |' + secret_key)`, key with nonce as hmac sha256 |

### returns the correct JSON example
```javascript
{
    "err_no": 0,
    "data": {
        "balance": 121356.51,
    }
}
```

### returns the wrong JSON example

```javascript
{
"err_no": 102,
"err_msg": "TxConfirmed"
}
```

Specific reference [error code](./Errorcode.en.md)