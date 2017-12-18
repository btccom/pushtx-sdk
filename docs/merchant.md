# 商户创建订单
>维护人员：**xxx**
>创建时间：2017-11-29

## 接口简介
商户使用创建好的应用及构建好的签名进行消费，加速未确认的交易。

## 接口详情

### 请求地址
/api/order/merchant

### 请求类型
POST

### 请求参数
| 参数名 | 类型 | 必填 | 描述 | 默认值 | 参考值 |
| --- | :---: | :---: | --- | --- | --- |
| txhash | string | 是 | 交易hash | 无 | ff602f8d64b9188f6831f62486e1391c8281ed6abc71c8862f59a7195d591328 |
| description | string | 是 | 交易描述 | 无 | 可填空字符串 |
| app_id | string | 是 | 应用ID | 无 | 281ed6abc71c8862f59a7195d591328 |
| nonce | string | 是 | 随机字符串，不得少于10位 | 无 | sfsdfsvxcvwfw2esfsaf |
| sign | string | 是 | 签名 | 无 | 生成规则：`hmac256(txhash+ '\|' + description + '\|' + app_id + '\|' + nonce + '\|' + secret_key)`, 以nonce为hmac sha256的key|

### 返回正确JSON示例
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

### 返回错误JSON示例
```javascript
{
	"err_no": 102,
	"err_msg": "TxConfirmed"
}
```

具体参考[错误代码](./errorcode.md)

# 商户获取余额
>维护人员：**xxx**
>创建时间：2017-12-01

## 接口简介
商户通过此接口获取该商户的余额

## 接口详情

### 请求地址
/api/balance/merchant

### 请求类型
POST

### 请求参数
| 参数名 | 类型 | 必填 | 描述 | 默认值 | 参考值 |
| --- | :---: | :---: | --- | --- | --- |
| app_id | string | 是 | 应用ID | 无 | 281ed6abc71c8862f59a7195d591328 |
| nonce | string | 是 | 随机字符串，不得少于10位 | 无 | sfsdfsvxcvwfw2esfsaf |
| sign | string | 是 | 签名 | 无 | 生成规则：`hmac256(app_id + '\|' + nonce + '\|' + secret_key)`, 以nonce为hmac sha256的key|

### 返回正确JSON示例
```javascript
{
    "err_no": 0,
    "data": {
        "balance": 121356.51,
    }
}
```

### 返回错误JSON示例
```javascript
{
	"err_no": 102,
	"err_msg": "TxConfirmed"
}
```

具体参考[错误代码](./errorcode.md)