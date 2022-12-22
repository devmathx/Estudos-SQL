/* Mostrar uma lista de todos os homems que trabalham como programadores */

select nome, profissao from pessoas 
where sexo = 'M' and profissao = 'Programador';