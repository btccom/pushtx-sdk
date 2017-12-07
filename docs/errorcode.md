# 常见的错误码

传的过程的错误码：

| 参数名 | 错误码 | 描述 |
| --- | :---: | --- |
| RPCUnavailable | 100 | RPC不可用 |
| TxUnavailable | 101 | 交易Hash不可用 | 
| TxConfirmed | 102 | 交易Hash被确认 | 
| TxDoubleSpent | 103 | 交易Hash被双花 | 
| TxExists | 104 | 交易Hash已在加速队列 | 
| UnconfirmedChainTooLong | 105 | 未确认交易链过长 | 
| PaymentFailed | 200 | 支付失败 | 
| InsufficientFunds | 201 |  | 
| AlipayCreateOrderFailed | 300 | 创建订单失败 | 
| MerchantAppExists | 10201 | 应用已存在 | 
| MerchantAppNoFound | 10202 | 应用不存在 | 
| MerchantExists | 10203 | 商户已存在 | 
| MerchantSettingExists | 10204 | 商户配置已存在 | 
| MerchantNotFound | 10205 | 没有找到该商户 | 
| MerchantBalanceInsufficient | 10206 | 余额不足 | 
| MerchantAppSignInvalid | 10207 | 签名错误 | 

支付过程的错误码：

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