package com.btc.pushtx.merchant.utils;

import java.util.Random;

/**
 * Created by zhengyan.gao on 2018/9/21.
 */
public final class Nonce {
    public static String createNonce(int length) {
        String str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
        Random random = new Random();
        StringBuffer sb = new StringBuffer();
        for (int i = 0; i < length; i++) {
            int number = random.nextInt(62);
            sb.append(str.charAt(number));
        }
        return sb.toString();
    }
}
