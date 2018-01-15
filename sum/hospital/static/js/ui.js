//ui-search 定义
$.fn.UiSearch = function(){
	var ui = $(this);

	$('.ui-search-selected',ui).on('click',function(){
		$('.ui-search-selected-list').slideDown(500);
		return false;/*防止事件冒泡*/
	});

	$('.ui-search-selected-list a',ui).on('click',function(){
		$('.ui-search-selected').text($(this).text());
		$('.ui-search-selected-list').slideUp(500);
		return false;
	});

	$('body').on('click',function(){
		$('.ui-search-selected-list').hide();
	});
}
//轮播
//左右控制翻页
//翻页是进度条联动focus
//三至一 循环
//进度点点击切换对应图
//自动滚动
//滚动过程中 屏蔽其他操作（自动滚动 左右翻页 进度点点击）
$.fn.UiSlider = function(){
	var ui = $(this);

	var wrap = $('.ui-slider-wrap');

	var btn_prev = $('.ui-slider-arrow .left',ui);
	var btn_next = $('.ui-slider-arrow .right',ui);

	var items = $('.ui-slider-wrap .item',ui);
	var tips = $('.ui-slider-process .item',ui);

	/*var firstItem = items.first().clone();
	$('.ui-slider-wrap').append(firstItem);*/
	//预定义
	var current = 0;
	var length = items.length;
	var width = items.eq(0).width();
	var enableAuto = true;
	//设置自动滚动状态
	ui.hover(function(){
		enableAuto = false;
		$('.ui-slider-arrow').show();
	},function(){
		enableAuto = true;
		$('.ui-slider-arrow').hide();
	});

	
	//具体操作
	wrap
	.on('move_prev',function(){
		if(current <= 0){
			current = length;
		}
		current = current - 1;

		wrap.triggerHandler('move_to',current);
	})
	.on('move_next',function(){
		if(current >= length-1){
			current = -1;
		}
		current = current + 1;

		wrap.triggerHandler('move_to',current);
	})
	.on('move_to',function(evt,index){
		/*wrap.css('left',index*width*-1);*/
		wrap.animate({left:index*width*-1});
		tips.removeClass('item_focus').eq(index).addClass('item_focus');
	})
	.on('auto_move',function(){
		setInterval(function(){
			enableAuto && wrap.triggerHandler('move_next');
		},2000);
	})
	.triggerHandler('auto_move');

	//事件
	btn_prev.on('click',function(){
		wrap.triggerHandler('move_prev');
		
	});
	btn_next.on('click',function(){
		wrap.triggerHandler('move_next');
	});
	tips.on('click',function(){
		var index = $(this).index();
		wrap.triggerHandler('move_to',index);
	});

}
/*$('.ui-tab-header-item').on('click',function(){
	var index = $(this).index();
	$('.ui-tab-header-item').removeClass('active').eq(index).addClass('active');
	$('.ui-tab-content-item').hide().eq(index).show();
	return false;
});*/

//ui-tab 定义
$.fn.UiTab = function(tabs,cons){
	var ui = $(this);
	var tabs = $(tabs,ui);	
	var cons = $(cons,ui);
	
	tabs.on('click',function(){
		var index =$(this).index();
		tabs.removeClass('active').eq(index).addClass('active');
		cons.hide().eq(index).show();
		return false;
	});
}

//回到顶部 UiBackTop
$.fn.UiBackTop = function(){
	var ui = $(this);

	var el = $('<a href="#" class="ui-backTop"></a>');
	ui.append( el );

	var windowHeight = $(window).height();

	$(window).on('scroll',function(){
		var top = $('body').scrollTop();
	
		if(top > windowHeight){
			el.show();
		}else{
			el.hide();
		}
	});

	el.on('click',function(){
		$('body,html').animate({scrollTop:0},500);
	});
}
//页面的脚本逻辑
$( function () {
	$('.ui-search').UiSearch();

	$('.content-tab').UiTab('.ui-tab-header-item','.ui-tab-content-item');
	$('.ui-tab-content-item').UiTab('.ui-tab-content-header-item','.ui-tab-content-bd');

	$('body').UiBackTop();

	$('.ui-slider').UiSlider();
}); 
