# Web Hacking Filter (PHP)
## How to use this function?
```
include "web_hacking_filter.php";
security_set();

$your_param = $_GET['param1'];

$your_param = sqli_filter($your_param);
$your_param = lfi_filter($your_param);
$your_param = xss_filter($your_param);
```

I would welcome your advice and feedback :)
*My english skill is basic! sorry... LOL~*
