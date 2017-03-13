<?php

if (!isset($_GET['url']) || !isset($_GET['_xfResponseType']) || $_GET['_xfResponseType'] != 'json')
{
    header('HTTP/1.1 404 Not Found');
    echo 'Invalid parameters.';
}
else
{
    $url = $_GET['url'];
    $data = array(
        'templateHtml' => '<form id="DemoOverlay" class="xenForm formOverlay"><div class="DemoContainer" style="background-color: #fff;"><iframe style="border-width: 0; border-style: none;" src="' . htmlspecialchars($url) . '"></iframe></div></form>',
        'css' => '',
        'js' => '',
        'title' => isset($_GET['title']) ? $_GET['title'] : 'Style Demo',
    );
    echo json_encode($data);
}
?>
