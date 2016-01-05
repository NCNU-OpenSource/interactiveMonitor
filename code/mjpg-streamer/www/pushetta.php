<?php
$channel = 'InteractiveMonitor';
$apikey = 'a310b9c29cab605a1397b96f6caf6950a948ff5a';
$expire = 'EXPIRY_DATE'; // In YYYY-MM-DD format

$data = array(
'body' => $message,
'message_type' => 'text/plain',
'expire' => $expire
);

$ch = curl_init("http://api.pushetta.com/api/pushes/$channel/");
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));
curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json', "A$

$response = json_decode(curl_exec($ch));
?>
