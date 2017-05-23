(define (ordered? lst)
	;take a list of numbers as an arg and return True if the list is in 
	;ascending order otherwise False
	(cond 
		((null? (cdr lst)) True) ; means the end of the list
		((> (car lst) (car (cdr lst))) False)
		(else (ordered? (cdr lst)))
	)
)