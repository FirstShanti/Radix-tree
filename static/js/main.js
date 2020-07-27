$(function(){
	let resource;
	$('#btn_submit').on('click', function() {
		console.log(this)
		// resource = $(this).children("option:selected").val();
		resource = $('#select_resource').children("option:selected").val()
		code = $('#form_to_api').find($('#params')).val()
		console.log('resource: ', resource)
		console.log('elements: ', code)
		if (code || resource == 'all') {
			$('#form_to_api').find($('#params')).removeClass('invalid')
			renderHtml('')
			sendRequest(resource, {code})
		} else {
			$('#form_to_api').find($('#params')).addClass('invalid')
			renderHtml('')
		}
	})
})

getParams = function (elements) {
	[code] = elements.map(function(i,element){return element.value;})
	return {code}
}

sendRequest = function (url, data) {
	$.ajax({
		cache: false,
		url,
		type: 'GET',
		data,
		dataType: 'json',
		success: function(response) {
			console.log(response)
			renderHtml(response.data)
		}
	})
}


parseListItemsToHtml = function (key, data) {
	listItems = `<li id=${key} href='' class="list-group-item d-flex justify-content-between align-items-center with_items">${key.replace('_', ' ').toUpperCase()}:<span class="badge badge-primary badge-pill">${data[key].length}</span></li>`
	for (var i in data[key]) {
		listItems += `<li class="list-group-item detail_none font-italic ${key}" style="text-align: center;">${data[key][i]}</li>`
	}
	return listItems
}

responseToHtml = function (response) {
	
	// let data = ['specification', 'info', 'data']
	var htmlPartOfResponse = '<ul class="list-group">'
	if ( Array.isArray(response) ) {
		for (i=0; i<=response.length; i++) {
			if (response[i]) {
				htmlPartOfResponse += `<li class="list-group-item">${response[i]}</li>`
			}
		}
	} else if (response != 'undefined') {
		htmlPartOfResponse += response
	}

	// for (var i in data) {
	// 	var field = data[i]
	// 	if (response[field]) {
	// 		for (var key in response[field]) {
	// 			if ( !response[field][key] ) {
	// 			} else {
	// 					listPart = parseListItemsToHtml(key, response[field])
	// 					htmlPartOfResponse += listPart
	// 				} else {
	// 					htmlPartOfResponse += `<li class="list-group-item">${key.replace('_', ' ').toUpperCase()}: ${response[field][key]}</li>`
	// 				}
	// 			}
	// 		}
	// 	}
	// } 
	htmlPartOfResponse += '</ul>'
	return htmlPartOfResponse
}

renderHtml = function(response) {
	$('#response').hide()
	$('#response').empty().append(responseToHtml(response))
	$('#response').show()
}
