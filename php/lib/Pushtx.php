<?php

namespace Pushtx;

class Pushtx implements ClientInterface
{
    public $base_url = 'https://pushtx.btc.com/';    
    const VERSION = '1.0.0';
    protected $app_id = '';
    protected $secret_key = '';
    protected $client;

    function __construct($app_id, $secret_key, $base_url = 'https://pushtx.btc.com/') {
        $this->app_id = $app_id;
        $this->secret_key = $secret_key;
        $this->base_url = $base_url;
        try {
            $this->client = new \GuzzleHttp\Client(['base_uri' => $this->base_url]);
        } catch (Exception $e) {
            echo 'Caught exception: ', $e->getMessage(), "\n";
        }
    }

    public function post($uri, $data)
    {
        return json_decode($this->request($uri, 'POST', $options = [
            'headers' => [
                'Accept' => 'application/json',
            ],
            'json' => $data
        ])->getBody(), true);
    }

    public function get($uri)
    {
        return json_decode($this->request($uri, 'GET')->getBody(), true);
    }

    public function delete($uri, $data)
    {
        return json_decode($this->request($uri, 'DELETE', $data)->getBody(), true);
    }

    public function request($uri, $method, array $options = array())
    {
        try {
            $response = $this->client->request($method, $uri, $options);
            return $response;
        } catch (RequestException $e) {
            echo $e->getMessage();
            return null;
        }
    }

    public function createMerchantOrder($txhash, $description) {
        $nonce = $this->createNonce();
        $sign = $this->createSign([$txhash, $description, $this->app_id, $nonce, $this->secret_key], $nonce);
        return $this->post(Config::getIns()->merchant_create_order, [
            'app_id' => $this->app_id,
            'nonce' => $nonce,
            'txhash' => $txhash,
            'description' => $description,
            'sign' => $sign
        ]);
    }

    public function getBalance() {
        $nonce = $this->createNonce();
        $sign = $this->createSign([$this->app_id, $nonce, $this->secret_key], $nonce);
        return $this->post(Config::getIns()->merchant_get_balance, [
            'app_id' => $this->app_id,
            'nonce' => $nonce,
            'sign' => $sign
        ]);
    }

    /**
     * Create Nonce.
     */
    protected function createNonce() {
        $chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
        $result = '';
        $max = strlen($chars) - 1;
        for ($i = 0; $i < 20; $i++) {
            $result .= $chars[rand(0, $max)];
        }
        return $result;
    }

    /**
     * Create Sign
     */
    protected function createSign($array, $nonce) {
        $encrypt = implode('|', $array);
        $sign = hash_hmac('sha256', $encrypt, $nonce);
        return $sign;
    }
}