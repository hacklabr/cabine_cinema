var fazendo_contagem_regressiva = false;
var contagem;
var radius = 40;
var intervalo_start = 3;
var fps = 25;
var intervalo_iterator = 1;
var origin = [ 50, 50 ];
var speed = 1;
var intervalo_iterator_max = fps * intervalo_start;

$(document).ready(function() {

	$('.accordion > h3').click(function() {
        var button = $(this).find('div');
        if (button.hasClass('ocultar')) {
            button.removeClass('ocultar').addClass('exibir').parents('h3').next().slideUp();
        } else {
            button.removeClass('exibir').addClass('ocultar').parents('h3').next().slideDown();
        }
    });
    
	$('.adicionar').click(function() {
		
		var clip_id = $(this).data('clipid');
		
		for (var i=1; i<3; i ++) {
		
			if ($('#proximo_'+i).data('clip') == 0) {
				
				coloca_filme_na_caixa('#proximo_'+i, clip_id);
				break;
			}
		
		}
		return false;
	});
	
	$('.em-breve').click(function() {
		var id = $(this).attr('id').replace('proximo_', '');
		
        if ($(this).data('clip') > 0)
            $('#remover_'+id).fadeIn();
		
		return false;
	});
	
	$('.remover a').click(function() {
		$(this).parents('.remover').hide();
		
		if ($(this).hasClass('sim')) {
			var posicao = $(this).parents('.remover').attr('id').replace('remover_', '');
			remover_da_fila(posicao);
		}
		
		
		return false;
	
	});
	
	$('#contador_pause').click(function() {
		clearTimeout(contagem);
		$(this).hide();
		$('#contador_play').show();
	});
	
	$('#contador_play').click(function() {
		contagem_regressiva();
		$(this).hide();
		$('#contador_pause').show();
	});
	
	$('#contador_skip').click(function() {
		fazendo_contagem_regressiva = false;
		clearTimeout(contagem);
		anda_fila_e_toca_video();
	});
	
	$('.openpopup').click(function() {
		
        var pop = $(this).attr('id').replace('-button', '');
        var is_opened = $('#popup-'+pop).is(':visible');
        
        $('.popup').hide();
        $('.openpopup').removeClass('ativo');
        
        if (is_opened)
            return;
        
		$(this).addClass('ativo');
		$('#popup-'+pop).fadeIn('fast');
	});
	
	$('.fechar').click(function() {
		$('.popup').fadeOut('fast', function() {
            $('.openpopup').removeClass('ativo');
        });
		
	});
	
	
	/** scroll **/
	
	$('#cenas').mousedown(function(){
		$('#selecao').hide();
	}).mouseup(function(){
		$('#selecao').fadeIn('fast');
	}).mouseleave(function(){
		$('#selecao').fadeIn('fast');
	});
	
	
	
	$(document.body).disableSelection();
	
	var timeout_delay = 15;
	
	var $sbar = $('#scroll-handler');
	var $cenas = $('#cenas');
	var $fichas = $('#fichas');
	
	var fichas_height, cenas_height;
	var sbar_height = $sbar.parent().height() - $sbar.height();
	
	var snap_ficha = 620;
	var snap_cena = 168;
	
	var last_cenas_top, last_fichas_top, last_sbar_top = 0;
	
	var scrolling = false;
	var in_animate = false;
	var mousedown = false;
	
	$('#cenas-content').data('selected-clip',0);
	
	$(window).load(function(){
		fichas_height = $('#fichas-content').outerHeight() - $('#fichas').height();
		cenas_height = $('#cenas-content').outerHeight() - $('#cenas').height();
	})
	
	
	setInterval(function(){
		var p, new_fichas_top, new_cenas_top, new_sbar_top;
		var cenas_top	= parseInt(document.getElementById('cenas-content').style.top);
		var fichas_top	= parseInt(document.getElementById('fichas-content').style.top);
		var sbar_top	= parseInt(document.getElementById('scroll-handler').style.top);
		
		if(cenas_top != last_cenas_top){
			scrolling = true;
			
			p = cenas_top/cenas_height;
			new_fichas_top = parseInt(fichas_height*p);
			new_sbar_top = -parseInt(sbar_height*p);
			
			document.getElementById('scroll-handler').style.top = new_sbar_top+'px';
			document.getElementById('fichas-content').style.top = new_fichas_top+'px';
			
			last_cenas_top = cenas_top;
			last_fichas_top = new_fichas_top;
			last_sbar_top = new_sbar_top;
			
		}else if(fichas_top != last_fichas_top){
			scrolling = true;
			p = fichas_top/fichas_height;
			new_cenas_top = parseInt(cenas_height*p);
			new_sbar_top = -parseInt(sbar_height*p);
			
			document.getElementById('scroll-handler').style.top = new_sbar_top+'px';
			document.getElementById('cenas-content').style.top = new_cenas_top+'px';
			
			last_cenas_top = new_cenas_top;
			last_fichas_top = fichas_top;
			last_sbar_top = new_sbar_top;
			
			
		}else if(sbar_top != last_sbar_top){
			scrolling = true;
			scrolling = true;
			p = sbar_top/sbar_height;
			new_cenas_top = -parseInt(cenas_height*p);
			new_fichas_top = -parseInt(fichas_height*p);
			
			document.getElementById('fichas-content').style.top = new_fichas_top+'px';
			document.getElementById('cenas-content').style.top = new_cenas_top+'px';
			
			last_cenas_top = new_cenas_top;
			last_fichas_top = new_fichas_top;
			last_sbar_top = sbar_top;
			
		}else if(scrolling && !mousedown){
			
			// on stop scrolling event
			var i = Math.round(cenas_top/snap_cena);
			
			if(!in_animate){
				in_animate = true;
				i = i <= -$('#cenas-content img').length ? -$('#cenas-content img').length + 1 : i;
				i = i > 0 ? 0 : i;				
				$('#cenas-content').animate({top:(i*snap_cena)}, 'slow', function(){
					scrolling = false;
					in_animate = false;
					$('#cenas-content').data('selected-clip',-i);
				});
			}
			
		}
	},timeout_delay);
	
	$('#cenas, #main-section').mousedown(function(){
		mousedown = true;
	}).mouseup(function(){
		mousedown = false;
	});
	
	$('#scroll-handler').draggable({
		axis: 'y', 
		drag: function(){
			scrolling = true;
			in_animate = true;
			
			if(parseInt($(this).css('top')) < 0)
				return false;
			else if(parseInt($(this).css('top')) > sbar_height)
				return false;
		},
		stop: function(){
			in_animate = false;
		}
	});
	
	$('#cenas-content').data('selected-clip',0);
	
	$("#fichas").jScroll({
		hScroll: false,
		vScrollbar: false,
		useTransform: false
		
	});
	$("#cenas").jScroll({
		hScroll: false,
		vScrollbar: false,
		useTransform: false
		
	});
	
	
	
	$('#scroll-up').click(function(){
		var i = $('#cenas-content').data('selected-clip') -1;
		i = i >= 0 ? i : 0;
		
		$('#cenas-content').stop().animate({top:(-i*snap_cena)}, 'slow', function(){
			scrolling = false;
			in_animate = false;
			
		});
		$('#cenas-content').data('selected-clip',i);
	});
	
	$('#scroll-down').click(function(){
		var i = $('#cenas-content').data('selected-clip') +1;
		i = i > $('#cenas-content img').length ? $('#cenas-content img').length : i;
		
		$('#cenas-content').stop().animate({top:(-i*snap_cena)}, 'slow', function(){
			scrolling = false;
			in_animate = false;
			
		});
		$('#cenas-content').data('selected-clip',i);
		
	});
	
	$('#cenas-content img').click(function(){
		var i = $(this).data('clipid')-1;
		var top = (-i*snap_cena);
		$('#cenas-content').stop().animate({top:(-i*snap_cena)}, 'slow', function(){
			scrolling = false;
			in_animate = false;
			
		});
		
		$('#cenas-content').data('selected-clip',i);
	});
});
	


function monitorar_fila() {
	//console.log('monitorando');
	// faz um ajax e checa um arquivo de texto pra saber se tem algo tocando

    $.ajax({
        type: 'GET',
        url: '/status/',
        success: function(data){
            playing_status = data;
            if (playing_status == "idle"){
                playing = false;
            }else{
                playing = true;
            }


            console.log(playing,fazendo_contagem_regressiva );
            // se não tem nada tocando
            if (!playing && !fazendo_contagem_regressiva) {

                // se tiver algo na fila
                if ( $('#proximo_1').data('clip') != 0) {

                    // carrega contagem regressiva
                    $('#tocando').hide();
                    $('#intervalo').show();


                    // inicializa contagem regressiva
                    inicia_contagem_regressiva();


                } else {
                    // se não tiver nada na fila
                    //console.log('nada na fila');
                    // carrega interface vazia
                    carrega_caixas_vazias();
                }
            }


        },
    });


}

function carrega_caixas_vazias() {

	
	coloca_filme_na_caixa('#proximo_1', 0);
	coloca_filme_na_caixa('#proximo_2', 0);
	coloca_filme_na_caixa('#tocando', 0);

}

function anda_fila_e_toca_video() {

	// se tiver algo na fila
	if ( $('#proximo_1').data('clip') != 0) {
		
		$('.remover').hide();
		
		// movimenta os videos na fila
		coloca_filme_na_caixa('#tocando', $('#proximo_1').data('clip'));
		coloca_filme_na_caixa('#proximo_1', $('#proximo_2').data('clip'));
		coloca_filme_na_caixa('#proximo_2', 0);
		
		// dá o play no ajax

        $.ajax({
            type: 'GET',
            url: '/enqueue/'+$("#tocando").data('clip'),
        });
		// Não esquecer de no ajax fazer a contagem dos plays! 
		// Temos que fazer uma tabela de log com hora e play de todos os videos
		
		$('#intervalo').hide();
		$('#tocando').show();
	
	
	} else {
	// se não tiver nada na fila
	
		// carrega interface vazia
		carrega_caixas_vazias();
	}

}

function inicia_contagem_regressiva() {
	
	fazendo_contagem_regressiva = true;
	$('#contador_pause').show();
	$('#contador_play').hide();
	
	//reseta o contador
    intervalo_iterator = 0;
	$('#contador').html(intervalo_start);
    
	drawCircle(0);
	// seta o timeout
	contagem = setTimeout('contagem_regressiva()', 1000/(fps*speed));
	
}

function contagem_regressiva() {

	
    intervalo_iterator = (intervalo_iterator + 1) % intervalo_iterator_max;
    
    drawCircle(intervalo_iterator);
    
    var c = parseInt($('#contador').html());
    
    if (intervalo_iterator % fps == 0) {
        
	    c --;
        $('#contador').html(c);
    }
    
    
	
	// se for zero
	if (c == 0) {
		fazendo_contagem_regressiva = false;
		anda_fila_e_toca_video();
		clearTimeout(contagem);
	} else {
		contagem = setTimeout('contagem_regressiva()', 1000/(speed*fps));
	}

}

function drawCircle(secs) {
    
    var start = position(-Math.PI/2)
    var angle = 2 * Math.PI * secs / intervalo_iterator_max - Math.PI/2
    var end = position(angle)

    var orig = origin.join(' ')
    var rad = radius + ' ' + radius
    start = start.join(' ')
    end = end.join(' ')

    var flag = secs < intervalo_iterator_max/2 ? 0 : 1

    $('#clock').attr('d', 'M ' + orig + ' L ' + start + ' A ' + rad + ' 0 ' + flag + ' 1 ' + end + ' Z')
}

function position(angle) {
    return [ origin[0] + Math.cos(angle) * radius,
	     origin[1] + Math.sin(angle) * radius
	   ]
}

// pasando 0 como clip_id vc vai deixar a caixa vazia
function coloca_filme_na_caixa(caixa, clip_id) {
	
	$(caixa).data('clip', clip_id );
	
	if (clip_id > 0) {
	
		var imgsrc = '/static/thumbs/'+clip_id+'-media.jpg';
		
		// se nao existir imagem, cria
		if ( $(caixa + ' > img').length == 0)
			$(caixa + ' > h2').after('<img />');
		
		$(caixa + ' > img').attr('src', imgsrc);
		
		if ( $(caixa + ' > p').length == 1)
			$(caixa + ' > p').remove(); //Selecione uma cena ao lado
		
		$(caixa).removeClass('vazio').addClass('ocupado');
		
	} else {
		if ( $(caixa + ' > img').length == 1)
			$(caixa + ' > img').remove();
		
		if ( $(caixa + ' > p').length == 0)	
			$(caixa + ' > h2').after('<p>Selecione uma cena ao lado</p>');
		
		$(caixa).removeClass('ocupado').addClass('vazio');

        $('.adicionar').removeClass('adicionar-inativo');
	}
    
    if (caixa == '#proximo_2' && clip_id > 0) {
        $('.adicionar').addClass('adicionar-inativo');
    }
	
}



function remover_da_fila(posicao) {

	coloca_filme_na_caixa('#proximo_'+posicao, 0);
	
	if (posicao == 1) {
		coloca_filme_na_caixa('#proximo_1', $('#proximo_2').data('clip'));
		coloca_filme_na_caixa('#proximo_2', 0);
	}
	
}


window.setInterval('monitorar_fila()', 1000);
