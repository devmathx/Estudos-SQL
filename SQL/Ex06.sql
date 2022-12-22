/* Mostrar a maior altura entre os homens que moram no Brasil */

select max(altura) from pessoas 
where sexo = 'M' and nacionalidade = 'Brasil';