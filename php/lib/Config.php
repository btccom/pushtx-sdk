<?php

namespace Pushtx;

class Config
{
    protected static $ins = null;
    protected static $data = array(
        "merchant_create_order" => "/api/order/merchant",
    );
    public static function getIns()
    {
        if (self::$ins instanceof self) {
            return self::$ins;
        } else {
            self::$ins = new self();
            return self::$ins;
        }
    }
    
    public function __get($key)
    {
        if (array_key_exists($key, self::$data)) {
            return self::$data[$key];
        } else {
            return null;
        }
    }
}