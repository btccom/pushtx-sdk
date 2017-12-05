<?php

namespace Pushtx;

use Exception;
use GuzzleHttp\Exception\RequestException;

class Client implements ClientInterface
{
    const VERSION = '1.0.0';
    public $base_url = 'https://pushtx.btc.com/';
    protected $client;

    public function __construct($base_url = 'https://pushtx.btc.com/')
    {
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
            'json' => $data,
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
}
