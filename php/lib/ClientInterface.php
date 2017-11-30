<?php
namespace Pushtx;

interface ClientInterface
{
    public function get($uri);

    public function delete($uri, $data);
    
    public function post($uri, $data);

    public function request($uri, $method, array $options = array());

    // public function auth();
}