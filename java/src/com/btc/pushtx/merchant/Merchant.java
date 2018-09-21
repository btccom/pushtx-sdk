package com.btc.pushtx.merchant;

import com.alibaba.fastjson.JSON;
import com.btc.pushtx.merchant.bean.Balance;
import com.btc.pushtx.merchant.bean.BaseResponse;
import com.btc.pushtx.merchant.bean.CreatedOrder;
import com.btc.pushtx.merchant.http.Client;
import com.btc.pushtx.merchant.utils.Nonce;
import com.btc.pushtx.merchant.utils.Sign;

import java.math.BigDecimal;
import java.util.Map;
import java.util.TreeMap;

/**
 * Created by zhengyan.gao on 2018/9/20.
 */
public class Merchant {

    private String appId = "";
    private String secretKey = "";
    private String endpoint = "https://pushtx.btc.com/";

    public void init(String appId, String secretKey, String endpoint) {
        this.secretKey = secretKey;
        this.appId = appId;
        this.endpoint = endpoint;
    }

    public void init(String accessKey, String secretKey) {
        this.secretKey = secretKey;
        this.appId = accessKey;
    }

    public CreatedOrder createOrder(String txhash, String description) throws Exception {
        Map<String, Object> params = new TreeMap<>();
        String nonce = Nonce.createNonce(15);
        params.put("nonce", nonce);
        params.put("app_id", appId);
        params.put("description", description);
        params.put("txhash", txhash);
        String sign = Sign.createSign(new String[]{txhash, description, appId, nonce, secretKey}, nonce);
        params.put("sign", sign);
        BaseResponse result = Client.sendPost(this.endpoint + Config.API_URL_CREATE_ORDER_URL, params);
        if (result != null && result.getErr_no() == 0) {
            CreatedOrder order = JSON.parseObject(result.getData().toString(), CreatedOrder.class);
            return order;
        } else {
            throw new Exception(result.getErr_msg());
        }
    }

    public BigDecimal getBalance() {
        Map<String, Object> params = new TreeMap<>();
        String nonce = Nonce.createNonce(15);
        params.put("secret_key", secretKey);
        params.put("nonce", nonce);
        params.put("app_id", appId);
        String sign = Sign.createSign(params, nonce);
        params.put("sign", sign);
        params.remove("secret_key");
        BaseResponse result = Client.sendPost(this.endpoint + Config.API_URL_GET_BALANCE, params);
        if (result != null && result.getErr_no() == 0) {
            Balance balance = JSON.parseObject(result.getData().toString(), Balance.class);
            return balance.getBalance();
        }
        return null;
    }
}
