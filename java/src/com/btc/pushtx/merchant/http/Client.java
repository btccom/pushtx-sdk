package com.btc.pushtx.merchant.http;

import com.btc.pushtx.merchant.bean.BaseResponse;
import com.mashape.unirest.http.Unirest;
import org.json.JSONObject;

import java.util.Map;

/**
 * Created by zhengyan.gao on 2018/9/20.
 */
public class Client {
    public static BaseResponse sendPost(String url, Map<String, Object> param) {
        try {
            System.out.println(JSONObject.valueToString(param));
            JSONObject jsonObject = Unirest.post(url)
                    .header("Content-Type", "application/json")
                    .header("accept", "application/json")
                    .body(JSONObject.valueToString(param))
                    .asJson().getBody().getObject();
            int err_no = jsonObject.getInt("err_no");
            String err_msg = jsonObject.has("err_msg") ? jsonObject.getString("err_msg") : "";
            JSONObject data = jsonObject.has("data") ? jsonObject.getJSONObject("data") : null;
            return new BaseResponse(err_no, err_msg, data);
        } catch (Exception e) {
            e.printStackTrace();
        }
        return null;
    }
}
