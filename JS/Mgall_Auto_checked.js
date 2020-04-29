// Article

var filter_text = ['keyword1', 'keyword2', 'keyword3', 'keyword4'];

for(var i in filter_text) {
	var result = $("tr:contains('"+ filter_text[i] +"')");
	$(result).find("input[type='checkbox']").attr("checked", true);
}

// Reply

var filter_text = ['keyword1', 'keyword2', 'keyword3', 'keyword4'];

for(var i in filter_text) {
	var result = $("li:contains('"+ filter_text[i] +"')");
	$(result).find("input[type='checkbox']").attr("checked", true);
}
