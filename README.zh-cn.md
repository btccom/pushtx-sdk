## Pushtx 交易加速接入 SDK 指南

### 说明

Pushtx 交易加速商户版 SDK

### 步骤

#### 1.申请商户

与BTC.com联系，并提供BTC.com账户信息(电子邮箱或手机或UID)，提供公司或个人相关信息，BTC.com审核通过以后即可访问商户页面。

#### 2.商户充值

与BTC.com联系，使用银行转账方式或者数字货币进行充值，并与相关人员联系，进行充值。

#### 3.使用sdk或者接口进行消费

使用SDK进行集成。

### SDK 说明

暂时目前有nodejs, php, python版本的sdk，其他语言可按规则进行生成签名调用。

现已提供有沙盒环境(https://sandbox-pushtx.btc.com), 构造函数传入即可。

Node.js:

```
npm install --save pushtx
```

PHP:

```
composer install
```

Python:
实现了多种client，可根据自己实际使用，并且兼容Python2/3。

```
pip install 
```

### TODO

+ 完善测试
+ 重构结构
+ 

### 联系

BTC.com 团队