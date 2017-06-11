;tic tac toe


(define (substitute-letter square position)
   (if (equal? '_ (item square position))
     square 
     (item square position)
   )  
)

(define (substitute-triple comb pos)    
   (accumulate (every (lambda (square) (substitute-letter square pos)) (num->list comb)))
)



;helper functions 
(define (symbol->list symbol) 
  (map char->symbol (string->list (symbol->string symbol)))
  
)


(define (char->symbol char)
   (string->symbol (list->string (list char)))
)

(define (item pos from)
   (define lt (cond
                ((list? from) from)  
                ((symbol? from) (symbol->list from))
                ((number? from) (number->list from))
                )) 

   (define (_item pos lst)
      (if (= 1 pos)
         (car lst)  
         (_item (- pos 1) (cdr lst))
      ) 
   )
   (_item pos lt)
)

(define (num->list num)
   (list (truediv num 100) (truediv (remainder num 100) 10) (remainder num 10))
)

(define (truediv x y)
	;only return the remainder as integer
	(floor (/ x y))

)

(define (every fn lst)
   (if (null? lst)
      lst
      (cons (fn (car lst)) (every fn (cdr lst)))
   )  
)


(define (accumulate lst)
  (define (_acc lst)
      (if (null? lst)
      lst
      (if (number? (car lst))
          (cons (car (string->list (number->string (car lst)))) (_acc (cdr lst)))
          (cons (car (string->list (symbol->string (car lst)))) (_acc (cdr lst)))
      )
      )     
  )
  (list->string (_acc lst))

)

