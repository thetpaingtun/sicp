(define (pow1 b n)
	;return b power to the n 
	;O(n2)
	(if (zero? n)
		1
		(* b (pow1 b (- n 1)))
	)
)


(define (pow2 b n)
	;return b power to the n
	;O(logn)
	(cond 
		((zero? n) 1)
		((even? n) (square (pow2 b (/ n 2))))
		(else (* b (pow2 b (- n 1))))
	)
)