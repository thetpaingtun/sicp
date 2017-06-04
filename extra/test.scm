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



(define (member? x lst)
   (cond  
   ((null? lst) False)
   ((equal? x (car lst)) True)
   (else (member? x (cdr lst)))
   
   ) 
)


(define (european-time time)
  ;return the european time. the arg passed is in the format '(8 am)
  (cond
      ((equal? (car (cdr time)) 'am) (if (< (car time) 12 ) (car time) (+ 12 (car time))))
      (else (if (< (car time) 12) (+ 12 (car time)) (car time)))
  )  
)



(define (american-time time)
   ;time is in range of 1-24
   (cond 
     ((= time 24) '(12 am))  
     ((< time 12) (list time 'am))
     ((= time 12) '(12 pm))
     (else (list (- time 12) 'pm))
   )
)




(define (teen? age)
  (and (> age 13) (< age 19))
)


(define (is-leap? y)
   (and 
      (zero? (remainder y 4))
      (or 
         (not (zero? (remainder y 100)))
         (zero? (remainder y 400))
      )
   )  
)


(define (valid-date? m d y)
   (cond 
      ((member? m '(4 6 9 11)) (and (< d 31) (> d 0)))  ;in these months should be 30 days
      ((member? m '(1 3 5 7 8 10 12)) (and (< d 32) (> d 0)))
      ((= m 2) (if (is-leap? y) (and (< d 30) (> d 0)) (and (< d 29) (> d 0))))
      (else False)
   )  
)










