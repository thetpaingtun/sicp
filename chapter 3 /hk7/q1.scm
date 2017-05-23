(define (cadr lst)
	;this function return the 2nd element of the list
	(car (cdr lst))
)


(define (caddr lst)
	;return the 3rd element of the list
	(car (cdr (cdr lst)))
)


(define (list-at lst n)
	(if (= n 0)
		(car lst)
		(list-at (cdr lst) (- n 1))
	)
)