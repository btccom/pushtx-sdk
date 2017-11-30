<?php

require_once(dirname(__FILE__) . '/../vendor/autoload.php');

$pushtx = new \Pushtx\Pushtx('app_id', 'secret_key', 'https://sandbox.pushtx.btc.com/');
$result = $pushtx->createMerchantOrder('txhash', 'description');
var_dump($result);
if ($result['err_no'] !== 0) {
    echo $result['err_msg'];
}