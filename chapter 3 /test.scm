(define (square x) (* x x))

(define (average x y) 
	(/(+ x y)2))


(define (sum list) 
	(if (= 1 (length list))
		(car list)
		(+ (car list) 
			(sum (cdr list))
		)
	)
)


;return the item at index n of the list
(define (list_ref list n)
  (if (equal? n 0)
  	(car list)
  	(list_ref (cdr list) (- n 1))
  )
  )

(define (map fn l)
	(if (null? l)
		nil
		(cons (fn (car l)) (map fn (cdr l)))
	)
)



(define (foldr fn start_val l)
	(if (null? l)
		start_val
		(fn (car l) (foldr fn start_val (cdr l)))
	)
)




(define (sum_of_square x y)
	(define (square x)
		(* x x)
	)

	(define (sum x y)
		(+ x y)
	)

	(sum (square x) (square y))
)













