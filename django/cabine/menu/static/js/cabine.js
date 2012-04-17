var fazendo_contagem_regressiva = false;
var algo_tocando = false; // variável para testes, será substituído pelo ajax da monitorar_fila()
var contagem;
var radius = 50;
var intervalo_start = 10;
var fps = 25;
var intervalo_iterator = 1;
var origin = [ 50, 50 ];
var speed = 1;
var intervalo_iterator_max = fps * intervalo_start;

$(document).ready(function() {
	
	// Simula o fim do filme que está tocando
	// Funçao só para testes! remover!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	$('#tocando').click(function() {
		algo_tocando = false;
	});
	
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
		$('#remover_'+id).fadeIn();
		//console.log('embreve');
		return false;
	});
	
	$('.remover a').click(function() {
		$(this).parents('.remover').hide();
		
		if ($(this).hasClass('sim')) {
			var posicao = $(this).parents('.remover').attr('id').replace('remover_', '');
			remover_da_fila(posicao);
		}
		//console.log('remover');
		
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
		$('.popup').hide();
		$('.openpopup').removeClass('ativo');
		$(this).addClass('ativo');
		var pop = $(this).attr('id').replace('-button', '');
		$('#popup-'+pop).fadeIn('fast');
	});
	
	$('.fechar').click(function() {
		$('.popup').fadeOut('fast', function() {
            $('.openpopup').removeClass('ativo');
        });
		
	});
	
	
});
	


function monitorar_fila() {
	//console.log('monitorando');
	// faz um ajax e checa um arquivo de texto pra saber se tem algo tocando
	var playing = algo_tocando;
	//console.log(playing);
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
		algo_tocando = true;
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

    var or = origin.join(' ')
    start = start.join(' ')
    end = end.join(' ')

    var flag = secs < intervalo_iterator_max/2 ? 0 : 1
    
    $('#clock').attr('d', 'M ' + or + ' L ' + start + ' A ' + or + ' 0 ' + flag + ' 1 ' + end + ' Z')
}

function position(angle) {
    return [ origin[0] + Math.cos(angle) * radius,
	     origin[1] + Math.sin(angle) * radius ]
}

// pasando 0 como clip_id vc vai deixar a caixa vazia
function coloca_filme_na_caixa(caixa, clip_id) {
	
	$(caixa).data('clip', clip_id );
	
	if (clip_id > 0) {
	
		var imgsrc = '/static/thumbs/'+clip_id+'-medio.jpg';
		
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
