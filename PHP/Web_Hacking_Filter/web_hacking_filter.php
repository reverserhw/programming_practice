<?php
/*
*************************************************************


Web Hacking Prevention Source Code (PHP)

Coded by. ReverserHW
I would welcome your advice and feedback. :)
E-Mail : security_swn@naver.com



*************************************************************
*/


function sqli_filter($param) {
	$param = str_replace("/[\r\n\s\t\’\;\”\=\-\-\#\/*]+/","",$param); // special character replace.
	$param = addslashes($param);

	// SQL injection filter
	if(preg_match("/(union|select|from|where|information_schema|tables|columns|top|\n|\r|\t|substr|subtring|#|-|\||\&|admin|and|or|limit)/i", $param)) {
		die("No Hack");
	} else {
		return $param;
	}
}

function lfi_filter($param) {
	$param = str_replace("/[\r\n\s\t\’\;\”\=\-\-\#\/*]+/","",$param); // special character replace.
	// Local File Inclusion(LFI) filter
	if(preg_match("/(etc|passwd|\/|system|curl|php|jsp|asp|log|access|httpd|apache|\.|user|environ|limits|lib|usr|security|readfile|fread|cat)/i", $param)) {
		die("No Hack");
	} else {
		return $param;
	}
}

function xss_filter($param) {
	$param = str_replace("/[\r\n\s\t\’\;\”\=\-\-\#\/*]+/","",$param); // special character replace.
	// XSS filter
	$param = str_replace("&", "&amp;", $param);
	$param = str_replace("<", "&lt;", $param);
	$param = str_replace(">", "&gt;", $param);
	$param = str_replace("(", "&#40;", $param);
	$param = str_replace("\"", "&#quot;", $param);
	$param = str_replace("'", "&#x27;", $param);
	$param = str_replace("/", "&#x2f;", $param);
	$param = str_replace(")", "&#41;", $param);

	return $param;
}

// php.ini set options, xxe filter
function security_set() {
	libxml_disable_entity_loader(true);
	ini_set("allow_url_include", "off");
	ini_set("allow_url_fopen", "off");
	ini_set("magic_quotes_gpc", "on");
}

// Test Parameter
$param = $_GET['param'];
echo xss_filter(lfi_filter(sqli_filter($param)));
?>
