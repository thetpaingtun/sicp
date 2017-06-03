(define (next x)
	(+ x 1)
)


(define (abs x)
	(sqrt (square x))
)

(define (CTOF x)
	(+ 32 (* x (/ 9 5)))
)

;reurun x power to y 
(define (pow x y)
	(if (zero? y)
		1
		(* x (pow x (- y 1)))
	)
)


(define (scientific  x y)
	(if (> y 0)
		(* x (pow 10 (abs y)))
		(/ x (pow 10 (abs y)))
	)
)

(define (discount initial percent)
	(- initial (* initial (/ percent 100)))
)


(define (truediv x y)
	;only return the remainder as integer
	(floor (/ x y))

)

(define (first-digit x)
	(if (< x 10)
		x
		(first-digit (truediv x 10))
	)
)