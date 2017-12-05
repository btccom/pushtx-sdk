<?php

namespace Pushtx;

if (!function_exists('generate_hmac_sha256_sign')) {
    /**
     *
     * @param $array
     * @param $nonce
     * @return string
     */
    function generate_hmac_sha256_sign($array, $nonce)
    {
        $encrypt = implode('|', $array);
        $sign = hash_hmac('sha256', $encrypt, $nonce);
        return $sign;
    }
}

if (!function_exists('create_nonce')) {
    /**
     *
     * @return string
     */
    function create_nonce()
    {
        $chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
        $result = '';
        $max = strlen($chars) - 1;
        for ($i = 0; $i < 20; $i++) {
            $result .= $chars[rand(0, $max)];
        }
        return $result;
    }
}
