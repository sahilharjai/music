var Search=(function(){

	function update(response){
		console.log("%%%%%%%%%");
		list=response.data;

		var i=0;
		if(list.length===0){
			$('.collection-header').html('No Results Found');}
		else{
			$('.collection-header').html(list.length+' Questions Found');
		}

		$('.collection-item').remove();
		for(i=0;i<list.length;i++)
		{  console.log(list[i].id)
			$('.collection').append('<li class="collection-item"><a href="/tracks/detail/'+list[i].id+'">'+list[i].track+"</a></li>");
		}
       
		
	}


	function perform_search(e){
		
		$.ajax({
			url:'/tracks/search',
			type:'GET',
			data:{'term':$('#id_search').val()},
			success:update,
			error:function(error){
				console.log("$$$$$$$$$$$$$$$$")
				console.log(error);
			}
		})
	}

	function clear_all(e){
		console.log("clear")
		$('.collection-header').html('Type Something On the Top!!');
		$('.collection-item').remove();
		$('#id_search').val('')
	}


	function init(){

		$('#id_search').keyup(perform_search);
		$('#id_search').focusout(clear_all);

	}
		return {
		init:init
	};

})();
