(define (sign x)
	(cond 
		((zero? x) 0)
		((> x 0) 1)
		(else -1)
	)
)