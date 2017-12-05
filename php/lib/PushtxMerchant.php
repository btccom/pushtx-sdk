<?php

namespace Pushtx;

class PushtxMerchant extends Client
{
    protected $app_id = '';
    protected $secret_key = '';

    /**
     * PushtxMerchant constructor.
     * @param string $app_id
     * @param $secret_key
     * @param string $base_url
     */
    public function __construct($app_id, $secret_key, $base_url = 'https://pushtx.btc.com/')
    {
        parent::__construct($base_url);
        $this->app_id = $app_id;
        $this->secret_key = $secret_key;
    }

    /**
     * @param $txhash
     * @param $description
     * @return mixed
     */
    public function createOrder($txhash, $description)
    {
        $nonce = create_nonce();
        $sign = generate_hmac_sha256_sign([$txhash, $description, $this->app_id, $nonce, $this->secret_key], $nonce);
        return $this->post(Config::getIns()->merchant_create_order, [
            'app_id' => $this->app_id,
            'nonce' => $nonce,
            'txhash' => $txhash,
            'description' => $description,
            'sign' => $sign,
        ]);
    }

    /**
     * @return mixed
     */
    public function getBalance()
    {
        $nonce = create_nonce();
        $sign = generate_hmac_sha256_sign([$this->app_id, $nonce, $this->secret_key], $nonce);
        return $this->post(Config::getIns()->merchant_get_balance, [
            'app_id' => $this->app_id,
            'nonce' => $nonce,
            'sign' => $sign,
        ]);
    }
}
