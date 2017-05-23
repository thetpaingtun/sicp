;if a is represented as sorted lists
(define (contains s v)
	(cond 
		((empty? s) False)
		((> (car s) v) False)
		((= (car s) v) True)
		(else (contains (cdr s) v))
	)
)



(define (empty? s) (null? s))


(define (add s v)
	(cond 
		((empty? s) (list v))
		((> (car s) v) (cons v s))
		((< (car s) v) (cons (car s) (add (cdr s) v)))
		((= (car s) v) s)
	)
)

(define (intersect s1 s2)
	(cond 
		((or (empty? s1) (empty? s2)) '()) ; end of set 1 or set 2
		((= (car s1) (car s2)) (cons (car s1) (intersect (cdr s1) (cdr s2))))
		((> (car s1) (car s2)) (intersect s1 (cdr s2)))
		((< (car s1) (car s2)) (intersect (cdr s1) s2))
		(else nil)
	)
)


(define (union s1 s2)
	(cond 
		((empty? s1) s2)
		((empty? s2) s1)
		((< (car s1) (car s2)) (cons (car s1) (union (cdr s1) s2)))
		((> (car s1) (car s2)) (cons (car s2) (union s1 (cdr s2))))
		((= (car s1) (car s2)) (cons (car s1) (union (cdr s1) (cdr s2))))
	)
)








