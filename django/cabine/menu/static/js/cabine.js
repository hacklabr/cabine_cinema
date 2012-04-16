var fazendo_contagem_regressiva = false;
var algo_tocando = false; // variável para testes, será substituído pelo ajax da monitorar_fila()
var contagem;

$(document).ready(function() {
	
	// Simula o fim do filme que está tocando
	// Funçao só para testes! remover!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	$('#tocando').click(function() {
		algo_tocando = false;
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
		console.log('embreve');
		return false;
	});
	
	$('.remover a').click(function() {
		$(this).parents('.remover').hide();
		
		if ($(this).hasClass('sim')) {
			var posicao = $(this).parents('.remover').attr('id').replace('remover_', '');
			remover_da_fila(posicao);
		}
		console.log('remover');
		
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
		$('.popup').fadeOut('fast');
		$('.openpopup').removeClass('ativo');
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
	var c = 10;
	$('#contador').html(c);
	
	// seta o timeout
	contagem = setTimeout('contagem_regressiva()', 1000);
	
}

function contagem_regressiva() {

	// subtrai 1
	var c = parseInt($('#contador').html());
	c --;
	//console.log(c);
	$('#contador').html(c);
	
	// se for zero
	if (c == 0) {
		fazendo_contagem_regressiva = false;
		anda_fila_e_toca_video();
		clearTimeout(contagem);
	} else {
		contagem = setTimeout('contagem_regressiva()', 1000);
	}

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
