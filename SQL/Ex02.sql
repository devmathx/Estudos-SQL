/* Mostrar uma lista com os dados de todos aqueles que nasceram entre 1/jan/2000 e 31/dez/2015 */

select nome, nascimento from pessoas 
where nascimento between '2000/01/01' and '2015/12/31';