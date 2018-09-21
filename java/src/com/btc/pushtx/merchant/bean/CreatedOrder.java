package com.btc.pushtx.merchant.bean;

import java.math.BigDecimal;

/**
 * Created by zhengyan.gao on 2018/9/20.
 */
public class CreatedOrder {
    private String status;
    private BigDecimal balance;
    private String order_id;

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public BigDecimal getBalance() {
        return balance;
    }

    public void setBalance(BigDecimal balance) {
        this.balance = balance;
    }

    public String getOrder_id() {
        return order_id;
    }

    public void setOrder_id(String order_id) {
        this.order_id = order_id;
    }
}
