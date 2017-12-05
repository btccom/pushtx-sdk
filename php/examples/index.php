<?php

require_once(dirname(__FILE__) . '/../vendor/autoload.php');
use \Pushtx\PushtxMerchant;

$pushtx = new PushtxMerchant('app_id', 'app_id', 'https://sandbox-pushtx.btc.com/');
$result = $pushtx->createOrder('txhash', 'scription');
var_dump($result);
if ($result['err_no'] !== 0) {
    echo 'txhash:' . $result['err_msg'];
}
echo "\n";

$result = $pushtx->getBalance();
var_dump($result);
if ($result['err_no'] !== 0) {
    echo $result['err_msg'];
}