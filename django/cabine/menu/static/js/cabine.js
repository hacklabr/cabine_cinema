// Copyright (C) 2012 Hacklab Ltda

// This software is free software; you can redistribute it and/or
// modify it under the terms of the GNU Affero General Public
// License as published by the Free Software Foundation;  either
// version 3 of the License, or (at your option) any later version.

// This software is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
// Affero General Public License for more details.

// You should have received a copy of the GNU Lesser General Public
// License along with this software; if not, write to the Free Software
// Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA


var fazendo_contagem_regressiva = false;
var count_idle = false;
var stop_update = false;
var contagem;
var radius = 40;
var intervalo_start = 15;
var fps = 25;
var intervalo_iterator = 1;
var origin = [ 50, 50 ];
var speed = 1;
var intervalo_iterator_max = fps * intervalo_start;
var waiting = false;
var timeout_delay = 15;

$(document).ready(function() {

	$('.accordion > h3').click(function() {
        var button = $(this).find('div');
        if (button.hasClass('ocultar')) {
            button.removeClass('ocultar').addClass('exibir').parents('h3').next().slideUp(function(){
				var top = parseInt($(this).parent().css('top'));
				adjustPopupScrollBar($(this).parent().parent().parent().parent().get());
				$(this).parent().parent().jScroll({
					hScroll: false,
					vScrollbar: false,
					useTransform: false,
					y: top
				});
			});
        } else {
            button.removeClass('exibir').addClass('ocultar').parents('h3').next().slideDown(function(){
				var top = parseInt($(this).parent().css('top'));
				adjustPopupScrollBar($(this).parent().parent().parent().parent().get());
				
				$(this).parent().parent().jScroll({
					hScroll: false,
					vScrollbar: false,
					useTransform: false,
					y: top
				});
			});
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

	var popup_interval;
	
	$('.openpopup').click(function() {
		
        var pop = $(this).attr('id').replace('-button', '');
        var is_opened = $('#popup-'+pop).is(':visible');
        
		if(is_opened)
			$('.popup').fadeOut('fast');
		else
			$('.popup').hide();
		
        $('.openpopup').removeClass('ativo');
        
		clearInterval(popup_interval);
        
		if (is_opened)
            return;
        
		$(this).addClass('ativo');
		var popup = $('#popup-'+pop).get();
		var $sbar = $()
		
		$(popup).fadeIn('fast').find('.popup-scroll').jScroll({
			hScroll: false,
			vScrollbar: false,
			useTransform: false
		});
		
		
		
		
		/** scroll dos popups **/
		var last_scroll_top, last_content_top = 0;
		
		popup_interval = setInterval(function(){
			var new_content_top, new_scroll_top, ratio;
			
			var content_top = parseInt($(popup).find('.accordion').css('top'));
			var content_scroll_height = $(popup).find('.accordion').outerHeight() - $(popup).find('.popup-scroll').height();
			
			var scroll_top = parseInt($(popup).find('.scroll-handler').css('top'));
			var scroll_scroll_height = $(popup).find('.scroll-bar').height() - $(popup).find('.scroll-handler').outerHeight();
			
			if(content_top != last_content_top){
				ratio = content_top / content_scroll_height;
				last_scroll_top = new_scroll_top = parseInt(scroll_scroll_height * -ratio);
				last_content_top = parseInt(content_top);
				$(popup).find('.scroll-handler').css('top', new_scroll_top);
				
			}else if(scroll_top != last_scroll_top){
				ratio = scroll_top / scroll_scroll_height;
				last_content_top = new_content_top = parseInt(content_scroll_height * -ratio);
				last_scroll_top = parseInt(scroll_top);
				$(popup).find('.accordion').css('top',new_content_top);
			}
			
			adjustPopupScrollBar(popup);
		}, timeout_delay);
	});
	
	$('.popup li').click(function(){
		var index = $(this).data('movie-index');
		$('.openpopup').removeClass('ativo');
		$('.popup').fadeOut('fast');
		$('#img-'+index).click();
	});
	
	$('.popup').each(function(){
		adjustPopupScrollBar(this);
		
		$(this).find('.scroll-handler').draggable({
			axis: 'y', 
			drag: function(){
				if(parseInt($(this).css('top')) < 0){
					$(this).css('top', 0);
					return false;
				}else if(parseInt($(this).css('top')) > $(this).parent().height() - $(this).height()){
					$(this).css('top', $(this).parent().height() - $(this).height());
					return false;
				}
			}
		});
	});
    
    $('#cenas-content, #playlist, #intervalo, .em-breve, #tocando').mousedown(function() {
		$('.popup').fadeOut('fast');
        $('.openpopup').removeClass('ativo');
    });
	
	$('.fechar').click(function() {
		$('.popup').fadeOut('fast', function() {
            $('.openpopup').removeClass('ativo');
			clearInterval(popup_interval);
        });
		
	});
	
	/** scroll das cenas e fichas**/
	
	$('#cenas').mousedown(function(){
		$('#selecao').hide();
	}).mouseup(function(){
		$('#selecao').fadeIn('fast');
	}).mouseleave(function(){
		$('#selecao').fadeIn('fast');
	});
	
	
	
	$(document).disableSelection();
	
	var $sbar = $('#scroll-handler');
	var $cenas = $('#cenas');
	var $fichas = $('#fichas');
	
	var fichas_height, cenas_height;
	var sbar_height = $sbar.parent().height() - $sbar.height();
	
	var snap_ficha = 620;
	var snap_cena = 168;
	
	var last_cenas_top, last_fichas_top, last_sbar_top = 0;
	
	var scrolling = false;
	var clicked = false;
	var in_animate = false;
	var mousedown = false;
	
	var selected_clip = 0;
	
	var num_cenas = $('#cenas-content img').length;
	
	var stop = false;
	
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
			p = sbar_top/sbar_height;
			new_cenas_top = -parseInt(cenas_height*p);
			new_fichas_top = -parseInt(fichas_height*p);
			
			document.getElementById('fichas-content').style.top = new_fichas_top+'px';
			document.getElementById('cenas-content').style.top = new_cenas_top+'px';
			
			last_cenas_top = new_cenas_top;
			last_fichas_top = new_fichas_top;
			last_sbar_top = sbar_top;
			
		}else if(scrolling && !mousedown || stop){
			stop = false;
			// on stop scrolling event
			if(!in_animate){
				
				var i = Math.round(cenas_top/snap_cena);
				var current_top = parseInt($('#cenas-content').css('top'));
				in_animate = true;
				i = i <= -num_cenas ? -num_cenas + 1 : i;
				i = i > 0 ? 0 : i;
				var top = i*snap_cena;
				if(current_top != top){
					$('#cenas-content').animate({top: top}, 'slow', function(){
						in_animate = false;
						selected_clip = -i;
						scrolling = false;
					});
				}
			}
			
		}else if(scrolling || in_animate){
			scrolling = false;
			in_animate = false;
		}
	},timeout_delay);
	
	
	$('#cenas-content img').click(function(){
		var i = $(this).data('movie-index')-1;
		var top = (-i*snap_cena);
		if(!scrolling || clicked){
			clicked = true;
			in_animate = true;
			
			$('#cenas-content').stop().animate({top:top}, 'slow', function(){
				scrolling = false;
				in_animate = false;
				clicked = false;
			});
		
			selected_clip = i;
		}
	});
	
	$(document).mousedown(function(){
		mousedown = true;
	}).mouseup(function(){
		mousedown = false;
	});
	
	$('#scroll-handler').draggable({
		axis: 'y', 
		drag: function(){
			scrolling = true;
			in_animate = true;
			
			if(parseInt($(this).css('top')) < 0){
				$(this).css('top', 0);
				return false;
			}else if(parseInt($(this).css('top')) > $(this).parent().height() - $(this).height()){
				$(this).css('top', $(this).parent().height() - $(this).height());
				return false;
			}
		},
		stop: function(){
			in_animate = false;
			mousedown = false;
			stop = true;
		}
	});
	
	$(window).load(function(){
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
	});
	
	
	
	
	
	$('#scroll-up').click(function(){
		var i = selected_clip -1;
		i = i >= 0 ? i : 0;
		
		$('#cenas-content').stop().animate({top:(-i*snap_cena)}, 'slow', function(){
			scrolling = false;
			in_animate = false;
			
		});
		selected_clip = i;
	});
	
	$('#scroll-down').click(function(){
		var i = selected_clip +1;
		i = i >= num_cenas - 1 ? num_cenas - 1 : i;
		
		$('#cenas-content').stop().animate({top:(-i*snap_cena)}, 'slow', function(){
			scrolling = false;
			in_animate = false;
			
		});
		selected_clip = i;
		
	});
    
	
});
	


function monitorar_fila() {
	//console.log('monitorando');
	// faz um ajax e checa um arquivo de texto pra saber se tem algo tocando
    
    if (stop_update)
        return;
    
    
    $.ajax({
        type: 'GET',
        url: '/status/',
        success: function(data){
            playing_status = data;
            if (playing_status == "idle"){
                //console.log('retornou idle');
                //console.log('idle é: ' + count_idle);
                if (count_idle === false) {
                    count_idle = 1;
                    //console.log('count_idle colocado pra 1: ' + count_idle);
                    playing = true;
                } else {
                    //console.log('count_idle não é falso');
                    count_idle ++;
                    //console.log('idle é: ' + count_idle);
                    playing = true;
                    if (count_idle > 3) {
                        //console.log('idle é maior q 3: ' + count_idle);
                        count_idle = false;
                        playing = false;
                    }
                }
                
            } else if (playing_status == 'waiting') {
                //console.log('retornou waitng');
                //console.log('waiting é: ' + waiting);
                if (waiting === false) {
                    waiting = 1;
                    //console.log('waiting é: ' + waiting);
                } else {
                    // Se está retornando waiting há muito tempo, vamos em frente...
                    waiting ++;
                    //console.log('waiting é: ' + waiting);
                    if (waiting > 8) {
                        //console.log('waiting é maior q 8');
                        waiting = false;
                        
                        $.ajax({
                            type: 'GET',
                            url: '/clear_waiting/',
                            complete: function() {
                                anda_fila_e_toca_video();
                            }
                        });
                        
                    }
                }
                playing = true;
            }else{
                playing = true;
            }


            //console.log(playing,fazendo_contagem_regressiva );
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
    count_idle = false;
	// se tiver algo na fila
	if ( $('#proximo_1').data('clip') != 0) {
		
		$('.remover').hide();
		
		// movimenta os videos na fila
		coloca_filme_na_caixa('#tocando', $('#proximo_1').data('clip'));
		coloca_filme_na_caixa('#proximo_1', $('#proximo_2').data('clip'));
		coloca_filme_na_caixa('#proximo_2', 0);
		
		// dá o play no ajax
	//$.ajax({
	//    type: 'GET',
	//    url: '/countdown/',
            	
        stop_update = true;
        $.ajax({
            type: 'GET',
            url: '/enqueue/'+$("#tocando").data('clip'),
            complete: function() {
                stop_update = false;
            }
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
        //g('chegou a zero');
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
	
		var imgsrc = $('#adicionar-clip-'+clip_id).data('thumb_path');
		
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


function adjustPopupScrollBar(popup){
	var inner_height = $(popup).find('.accordion').outerHeight();
	var outer_height = $(popup).find('.popup-scroll').height();
	var sbar_height = $(popup).find('.scroll-bar').height();

	var ratio = (outer_height/inner_height);
	ratio = ratio > 1 ? 1 : ratio;

	$(popup).find('.scroll-handler div').css('height',sbar_height*ratio);
}

window.setInterval('monitorar_fila()', 1000);
