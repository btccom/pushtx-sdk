package com.btc.pushtx.merchant.bean;

import org.json.JSONObject;

/**
 * Created by zhengyan.gao on 2018/9/20.
 */
public class BaseResponse {
    public BaseResponse(int err_no, String err_msg, JSONObject data) {
        this.err_no = err_no;
        this.err_msg = err_msg;
        this.data = data;
    }

    private int err_no;
    private String err_msg;
    private JSONObject data;

    public int getErr_no() {
        return err_no;
    }

    public void setErr_no(int err_no) {
        this.err_no = err_no;
    }

    public String getErr_msg() {
        return err_msg;
    }

    public void setErr_msg(String err_msg) {
        this.err_msg = err_msg;
    }

    public JSONObject getData() {
        return data;
    }

    public void setData(JSONObject data) {
        this.data = data;
    }
}
