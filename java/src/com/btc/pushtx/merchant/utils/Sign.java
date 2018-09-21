package com.btc.pushtx.merchant.utils;

import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import java.util.ArrayList;
import java.util.Map;
import java.util.StringJoiner;

/**
 * Created by zhengyan.gao on 2018/9/20.
 */
public final class Sign {
    public static String createSign(Map<String, Object> param, String nonce) {
        StringJoiner result = new StringJoiner("|");
        for (Object str : param.values()) {
            result.add(str.toString());
        }
        return sign(result.toString(), nonce);
    }

    public static String createSign(String[] param, String nonce) {
        StringJoiner result = new StringJoiner("|");
        for (String str : param) {
            result.add(str);
        }
        return sign(result.toString(), nonce);
    }

    /**
     * @param msg
     * @param key
     * @return
     */
    public static String sign(String msg, String key) {
        try {
            Mac sha256_HMAC = Mac.getInstance("HmacSHA256");
            SecretKeySpec secret_key = new SecretKeySpec(key.getBytes(), "HmacSHA256");
            sha256_HMAC.init(secret_key);
            return bytes2hex(sha256_HMAC.doFinal(msg.getBytes()));
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    /**
     * Byte[] to String
     *
     * @param bytes
     * @return
     */
    public static String bytes2hex(byte[] bytes) {
        StringBuffer hash = new StringBuffer();
        for (int i = 0; i < bytes.length; i++) {
            String hex = Integer.toHexString(0xFF & bytes[i]);
            if (hex.length() == 1) {
                hash.append('0');
            }
            hash.append(hex);
        }
        String digest = hash.toString();
        return digest;
    }
}
