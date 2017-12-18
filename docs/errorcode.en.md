# Common error code

The process of transmission error code:

| Parameter Name | Error Code | Description |
| --- | :---: | --- |
| RPCUnavailable | 100 | RPC Not Available |
| TxUnavailable | 101 | Transactional Hash is not available |
| TxConfirmed | 102 | Transaction Hash Confirmed |
| TxDoubleSpent | 103 | Deals Hash is Double Flower |
| TxExists | 104 | Deals Hash has been in an accelerated queue |
| UnconfirmedChainTooLong | 105 | Unconfirmed transaction chain is too long |
| PaymentFailed | 200 | Payment failed |
| InsufficientFunds | 201 | |
| AlipayCreateOrderFailed | 300 | Create Order Failed |
| MerchantAppExists | 10201 | App Exist |
| MerchantAppNoFound | 10202 | Application does not exist |
| MerchantExists | 10203 | Merchant already exists |
| MerchantSettingExists | 10204 | Merchant Configuration already exists |
| MerchantNotFound | 10205 | Did not find it |
| MerchantBalanceInsufficient | 10206 | Insufficient balance |
| MerchantAppSignInvalid | 10207 | Signature Error |

Payment process error code:

```
    PaymentSuccess = 200,
    ParametersInvalid = 400,
    MerchantIdInvalid = 401,
    APISignatureInvalid = 402,
    AppNameInvalid = 403,
    PaymentMethodInvalid = 405,
    CurrencyInvalid = 406,
    AmountInvalid = 407,
    LanguageInvalid = 408,
    URLInvalid = 409,
    SecretKeyInvalid = 411,
    TransactionIdInvalid = 412,
    OrderRepeated = 413,
    CountryInvalid = 414,
    PaymentTypeInvalid = 415,
    RequestMethodInvalid = 420,
    AppInactive = 441,
    PayMethodNotEnabled = 491,
    ServerError = 500,
    ServerBusy = 501,
    ThirdPartyError = 502,
    SeriviceNotFound = 503
```