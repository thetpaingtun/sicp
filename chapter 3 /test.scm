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


(define (assert_equal a b)

	(define (print_error)
		(display a)
		(display " is not equal to ")
		(display b)
		(newline)
	)

	(if (not (equal? a b))
		(print_error)
		(null)
	)
)


(define (circle_detail r)
  (define pi 3.14)
  (define (area) (* pi r r))
  (define (circum)  (* 2 pi r))
  (list (area) (circum))

)


(define (make_adder x)
	(define (adder y)
		(+ x y)
	)
	adder
) 


(define (fib n)
	(if (or (= n 0) (= n 1))
		n
		(+ (fib (- n 2)) (fib (- n 1)))
	)
)



(define (fact n)
	(if (= n 0)
		1
		(* n (fact (- n 1)))
	)
)


(define (fact_iter n)
	(define (impl acc count)
		(if (= count 0)
			acc
			(impl (* acc count) (- count 1))
		)
	)
	(impl 1 n)
)




(define (fib_iter n)
	(define (impl acc1 acc2 count)
		(if (= count 2)
			acc1
			(impl (+ acc1 acc2) acc1 (- count 1))
		)
	)
	(impl 1 1 n)

)



(define (safe_sum x y)
	(if (and (integer? x) (integer? y))
		(+ x y)
		"Incorrect types"
	)
)



(define (average_of_list lst)
	(define (impl acc count lst)
		(if (null? lst)
			(/ acc count)
			(impl (+ acc (car lst)) (+ count 1) (cdr lst))
		)
	)
	(impl 0 0 lst)
)









