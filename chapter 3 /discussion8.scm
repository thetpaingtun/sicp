(define (insert ele lst pos)
	(if (zero? pos) 
		(cons ele lst)
		(cons (car lst) (insert ele (cdr lst) (- pos 1)))
	)
)



(define (duplicate lst) 
	(if (null? lst) 
		'()
		(cons (list  (car lst) (car lst)) (duplicate (cdr lst)))

	)
	
)