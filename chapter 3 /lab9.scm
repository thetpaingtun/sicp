(define (cube x)
	(* x x x)
)



(define (over_or_under x y)
	(if (= x y)
		0
		(if (> x y)
			1
			-1
		)
	)
)


(define (make-adder num)
	(lambda (x) (+ x num))
)



(define (remove item lst)
  (cond 
  	((null? lst) '())
  	((equal? item (car lst)) (remove item (cdr lst)))
  	(else (cons (car lst) (remove item (cdr lst))))
  )

)


(define (composed f g)
	(lambda (x) (f (g x)))
)


(define (gcd x y)
	(if (= 0 (modulo (max x y) (min x y )))
		(min x y)
		(gcd (min x y) (modulo (max x y) (min x y)))
	))


(define (filter-lst fn lst)
	(cond 
		((null? lst) '())
		((fn (car lst)) (cons (car lst) (filter-lst fn (cdr lst))))
		(else (filter-lst fn (cdr lst)))
	)
)



(define (all-satisfies lst pred)
	(= (length (filter-lst pred lst)) (length lst))
)


;some helper procedures
(define (add-2 x)
	(+ x 2)
)

(define (square x)
	(* x x)
)


(define (min x y) (if (< x y) x y))

(define (max x y) (if (> x y) x y))


(define (is-even? x) (= 0 (modulo x 2)))

(define (is-odd? x) (not (= 0 (modulo x 2))))




























