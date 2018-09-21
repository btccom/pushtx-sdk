package com.btc.pushtx.merchant;

import com.btc.pushtx.merchant.bean.CreatedOrder;

import java.math.BigDecimal;

public class Main {

    public static void main(String[] args) {
        Merchant merchant = new Merchant();
        merchant.init("app_id", "secret_key", "https://pushtx.btc.com");
        try {
            CreatedOrder order = merchant.createOrder("txhash", "test");
            System.out.println(order.getStatus());
            System.out.println(order.getOrder_id());
            System.out.println(order.getBalance());
        } catch (Exception e) {
            e.printStackTrace();
        }
        BigDecimal balance = merchant.getBalance();
        System.out.println(balance);
    }
}
